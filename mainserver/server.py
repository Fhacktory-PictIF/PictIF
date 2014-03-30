#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, jsonify, Blueprint, current_app
import json

from core.component import Component

app = Flask(__name__)
app.debug = True

#contient les component ajoutés, liés ou non à d'autres
class ComponentGestion(object) :
    def __init__(self):
        self.map_of_component = {}
        self.iteratorId = 0

componentGestioner = ComponentGestion()


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/block/list", methods = ['GET'])
def getBlocksList():
    resp = dict(ok=True, components=Component.components)
    return json.dumps(resp)

@app.route("/block/execute/<blockId>", methods = ['POST'])
def executeBlock(blockId):
    resp = dict(ok=True)

    return json.dumps(resp)

@app.route("/block/reset/<blockId>", methods = ['POST'])
def resetBlock(blockId):
    resp = dict(ok=True)
    return json.dumps(resp)

@app.route("/block/add/<blockType>", methods = ['POST'])
def getBlockFromType(blockId):
    resp = dict(ok=True)
    return json.dumps(resp)

@app.route("/save", methods = ['POST'])
def saveWorkFlow():
    resp = dict(ok=True)
    return json.dumps(resp)

@app.route("/block/addConnection", methods = ['POST'])
def addConnection() :
    if request.method == 'POST' :
        parentId, currentId = request.json['parentId'], request.json['currentId']
        current_component = componentGestioner.map_of_component.get(currentId)
        parent_component = componentGestioner.map_of_component.get(parentId)
        #Addcomponent to parent
        if (current_component != None and parent_component != None and current_component.parent == None) :
            componentGestioner.map_of_component[currentId].parent = componentGestioner.map_of_component[parentId]
            resp = {'ok': True}
            return json.dump(resp)
        elif(current_component != None and parent_component != None and current_component.parent != None) :
            current_component.setParent2(parent_component)
            resp = {'ok': True}
            return json.dump(resp)
    resp={'ok':False}
    return json.dump(resp)

@app.route("/block/removeConnection", methods = ['POST'])
def removeConnection() :
    if request.method == 'POST' :
        #warning, the currentId is the one whose parent have to be suppressed.
        parentId, currentId = request.json['parentId'], request.json['currentId']
        current_component = componentGestioner.map_of_component.get(currentId)
        parent_component = componentGestioner.map_of_component.get(parentId)
        #Addcomponent to parent
        if (current_component != None and parent_component != None) :
            if current_component.id == parentId :
                current_component.parent = None
            resp = {'ok': True}
            return json.dump(resp)
        #TODO gestion du parent 2 elif(current_component != None and current_component.parent != None) :
            # current_component.setParent2(parent_component)
            # resp = {'ok': True}
            # return json.dump(resp)
    resp={'ok':False}



@app.route("/removeComponent", methods = ['POST'])
def removeComponent() :
    if request.method == 'POST' :
        currentId = request.json['currentId']
        current_component = componentGestioner.map_of_component.get(currentId)
        if current_component != None :
            componentGestioner.map_of_component.pop(currentId)
            resp = {'ok': True}
            return json.dump(resp) 
    resp = {'ok': False}
    return json.dump(resp)

    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
