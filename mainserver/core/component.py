#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time, os, tempfile
from SimpleCV import Image, Color
import cv2

nbComponents = 0
dir_tmp = "../test/treated/"

def generateId():
    global nbComponents
    nbComponents += 1
    return nbComponents

class Component(object):
    ioComponents = dict(Reader='Picture Reader', Writer='Picture Writer')
    processors = dict(Cropper='Cropper', GrayScale='Gray Scale', ChromaKey='Chromakey')
    dir_tmp = tempfile.gettempdir()
    selectors = dict(FileFilter='File Filter', Joiner='Joiner', Splitter='Splitter')
    statistics = []
    #classmere.__subclasses__() return list

    attr_description = "parent:Component:previous component which this object is related to,\
    id:int:component identifiant,images:list:images' list,executed:bool:flag for knowing if the component has to be executed or not"

    def __init__(self) :
    	self.parent = None
    	self.id = generateId()
    	self.images = []
    	self.executed = False

    def setParent(self,parent):
    	self.parent = parent
    	if parent is None :
    		self.executed = False

    def isSafelyExecuted(self):
    	return False if (self.parent is None) else True if isinstance(self.parent, Reader) and self.parent.executed and self.executed else self.parent.isSafelyExecuted() and self.executed

    def executeParent(self):
    	if not self.parent.executed:
    		self.parent.process()

    def process():
    	print 'Abstract class'

    def showOutput():
    	print 'print treated images'


class Splitter(Component):
    """Splits one stream into two based on one criteria"""
    description = "Splits one data stream into two data streams depending whether they match some specific criteria"
    attr_description = Component.attr_description + "images2:list(imageData):second output"

    def __init__(self):
        Component.__init__(self)
        self.criteria = None
        self.images2 = None

    def process(self):
        if not self.executed and self.parent is not None:
            self.executeParent()
            self.images = []
            self.images2 = []

            for image in self.parent.images:
                # TODO define split criteria
                pass

            self.executed = True


class FileFilter(Component):
    """Filters some rows based on certains criteria
    such as date, time, extension"""
    description = "Excludes from data stream files matching any of user's criteria"
    attr_description = Component.attr_description + "time_relative:int:-1 before is default value \
            0 is equal and 1 is after,time_reference:time:reference time,extensions:list(string):\
            list of file extensions,extension_keep:Boolean:Whether we ought to keep specified extensions"

    def __init__(self):
        Component.__init__(self)
        self.criteria = None
        self.time_relative = -1 # (-1) before is default value, 0 is equal and 1 is after
        self.time_reference = None
        self.extensions = None
        self.extension_keep = True

    def set_time_reference(self, time_reference):
        self.time_reference = time_reference
        self.extensions = None

    def set_extensions(self, extensions):
        self.time_reference = None
        self.extensions = extensions

    def process(self):
        if not self.executed and self.parent is not None:
            self.executeParent()

            tempI = set(self.parent.images)
            tempO = set()
            if self.time_reference is not None:
                for image in tempI:
                    if self.time_relative == 1:
                        if self.time_reference < image.date:
                            tempO.add(image)
                    elif self.time_relative == -1:
                        if self.time_reference > image.date:
                            tempO.add(image)
                    elif self.time_relative == 0:
                        if self.time_reference == image.date:
                            tempO.add(image)
            elif self.extensions is not None:
                if not self.extension_keep:
                    tempO = tempO.union(set([im for im in self.parent.images if im.extension in self.extensions]))
                else:
                    tempO = tempO.union(set([im for im in self.parent.images if im.extension not in self.extensions]))
            self.images = list(tempO)

class Joiner(Component):
    """Joins two streams into one"""
    description = "Joins two data streams into one avoiding duplicates."
    attr_description = Component.attr_description + "parent2:component:second parent"

    def __init__(self):
        Component.__init__(self)
        self.parent2 = None

    def setParent2(self, parent):
        self.parent2 = parent
        if parent is None :
            self.executed = False

    def delParent2(self):
        self.parent2 = None
        self.executed = False

    def process(self):
        if not self.executed and self.parent is not None:
            self.executeParent()
            self.images = list(set(self.parent.images + self.parent2.images))
            self.executed = True

class O():
    """Output mechanism"""
    def __init__(self):
        pass

    @classmethod
    def write(cls, images, path, ComponentId):
        for image in images:
            image.path = path + image.name + str(ComponentId) + image.extension
            image.image.save(image.path)
            image.date = time.ctime(os.path.getctime(image.path))

class ImageData():
    """Image object"""
    def __init__(self, path):
        self.path = path
        self.date = time.ctime(os.path.getctime(path))
        self.name = os.path.splitext(os.path.basename(path))[0]
        self.extension = os.path.splitext(path)[1]
        self.image = None

    def load(self):
        self.image = Image(self.path)

    def unload(self):
        del self.image

class Cropper(Component):

    attr_description = Component.attr_description + "output:O:output writer,x:int:top left point's abscisse of cropping rectangle,\
        y:int:top left point's ordonate of cropping rectangle,width:int:width of cropping rectangle,\
        height:int:height of cropping rectangle"

    description = "Component for cropping images. It takes as input a list of images and returns the list of cropped images"

    def __init__(self):
        Component.__init__(self)
        self.output = O()
        self.x = 0
        self.y = 0
        self.width = 100
        self.height = 100

    def process(self):

        if not self.executed and (self.parent is not None):
            self.executeParent()

            self.images = self.parent.images
            for image in self.images:
                image.load()

            for im in self.images:
                im.image = im.image.crop(self.x,self.y,self.width,self.height)

            self.output.write(self.images,dir_tmp,self.id)

            O.write(self.images, dir_tmp, self.id)
            for image in self.images:
                image.unload()

            self.executed = True

class GrayScale(Component):

    attr_description = Component.attr_description + "output:O:output writer,degree:int:output images darkness"

    description = "Component for turning the images into gray scale. It takes as input a list of images and returns the list of gray images"

    def __init__(self):
        Component.__init__(self)
        self.degree = 1

    def process(self):

        if not self.executed and (self.parent is not None):
            self.executeParent()

            self.images = self.parent.images
            for image in self.images:
                image.load()

            for im in self.images:
                (red, green, blue) = im.image.splitChannels(False)
                im.image = (red.toGray() + green.toGray() + blue.toGray()) / self.degree

            self.executed = True

            O.write(self.images,dir_tmp,self.id)
            for image in self.images:
                image.unload()

class ChromaKey(Component):

    description = "Composes all the images in input1 with the background image defined in input2"
    attr_description = Component.attr_description + "output:O:output writer,background:ImageData:the image applied as background,parent2:component:second parent"

    def __init__(self):
        Component.__init__(self)
        self.background = None
        self.parent2 = None
        self.output = O()

    def setParent2(self, parent):
        self.parent2 = parent
        if parent is None :
            self.executed = False

    def delParent2(self):
        self.parent2 = None
        self.executed = False

    def process(self):

        if not self.executed and self.parent is not None:
            self.executeParent()

            self.images = self.parent.images
            self.background = self.parent2.images[0]
            for image in self.images:
                image.load()

            for i in self.images:
                background = self.background.image.scale(i.image.width, i.image.height)
                mask = background.hueDistance(color=Color.GREEN).binarize()

                i.image = (background - mask) + (background - mask.invert())

            self.executed = True
            O.write(self.images,dir_tmp,self.id)
            for image in self.images:
                image.unload()


class FacesDetector(Component):
    cascade = cv2.CascadeClassifier('../../XML/haarcascade_frontalface_default.xml')

    def __init__(self):
        Component.__init__(self)

    def process(self):

        if not self.executed and self.parent is not None:
            self.executeParent()

            self.images = self.parent.images
            for i in self.images:
                img = cv2.imread(i.path)
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                ret,thresh = cv2.threshold(gray,127,255,0)
                faces = FacesDetector.cascade.detectMultiScale(gray, 1.3, 5)
                #contours, _ = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
                for (x,y,w,h),k in zip(faces,range(len(faces))):
                    #cv2.ellipse(img, (x + w / 2,y + h / 2),(w / 2,h / 2), 0, 0, 360,(255,0,0),2)
                    o = img[y: y + h, x: x + w]
                    cv2.imwrite(dir_tmp + i.name + str(self.id) + str(k) + '.jpg', o)
                    #for c,k in zip(contours,range(len(contours))):
                    #   if cv2.pointPolygonTest(c,(x,y),False) > -1:
                    #       cv2.drawContours(img, contours, k, (0,255,0), 3)

                #cv2.imshow('img',img)
                #cv2.waitKey(0)
                #cv2.destroyAllWindows()

class Recognizer(Component):

    def __init__(self):
        Component.__init__(self)
        self.patterns = []
        self.parent2 = None

    def setParent2(self, parent):
        self.parent2 = parent
        if parent is None :
            self.executed = False

    def delParent2(self):
        self.parent2 = None
        self.executed = False

    def process(self):

        if not self.executed and self.parent is not None:
            self.executeParent()

            self.images = self.parent.images

            self.patterns = self.parent2.images

            #f = open('../test/positives.dat', 'w')
            for i in self.images:
                print dir_tmp + i.name + str(self.parent.id) + i.extension

            #retvalue = os.system("ps -p 2993 -o time --no-headers")

            #O.write(self.images,dir_tmp,self.id)

class Reader(Component):
    attr_description = Component.attr_description + "pathes:list(string):lists of file or folder pathes,\
            length:int:images count,key_points:list:osef,mean_colors:list:osef2"
    description = "Creates a data stream from a file or a folder and its subfolders."

    def __init__(self):
        Component.__init__(self)
        self.pathes = None
        self.length = None
        self.key_points = []
        self.mean_colors = []

    def setPathes(self, pathes):
        self.pathes = pathes

    def process(self):
        self.read(self.pathes)
        self.length = len(self.images)
        for image in self.images:
            image.load()
            # image.image.show()
            # time.sleep(1)
        # self.key_points = [i.image.findKeypoints() for i in self.images]
        self.mean_colors = [k.meanColor() for k in self.key_points]
        
        O.write(self.images,dir_tmp,self.id)
        for image in self.images:
            image.unload()
        self.executed = True

    def read(self, pathes):
        for path in pathes:
            images = []
            if os.path.isfile(path):
                # print "Considering file1 ", path
                images.append(ImageData(path))
            elif os.path.isdir(path):
                # print "Considering directory ", path
                for dirname, dirnames, filenames in os.walk(path):
                    # print "Directory ", dirname," has subfolders ", dirnames
                    # print "Directory ", dirname," has subfiles ", filenames
                    for filename in filenames:
                        # print "Considering file2 ", filename, " of ", dirname
                        img = ImageData(os.path.join(dirname, filename))
                        images.append(img)
        self.images = list(set(images))

class Writer(Component):
    """Writes pics on disc"""
    attr_description = Component.attr_description + "path:string:File path"
    description = "Writes the content of the data stream's content in a specified path."

    def __init__(self):
        Component.__init__(self)
        self.path = "" #TODO

    def process(self):
        O.write(self.images, self.path, "Lol")
        self.executed = True

if __name__ == "__main__" :

    import string
    suffixes = string.letters + string.digits
    """binarizer = GrayScale(suffixes[0])
    suffixes = suffixes[1:]
    binarizer.process()
    chroma = ChromaKey(suffixes[0])
    suffixes = suffixes[1:]
    chroma.process()"""
    detector = FacesDetector()
    suffixes = suffixes[1:]
    detector.process()