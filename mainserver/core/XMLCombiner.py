#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from xml.etree import ElementTree as et

def main():
    XMLCombiner(('params.xml', 'stage0.xml', 'stage1.xml')).combine("2")

class XMLCombiner(object):
    def __init__(self, filenames):
        assert len(filenames) > 0, 'No filenames!'
        self.roots = [et.parse(f).getroot() for f in filenames]

    def combine(self, idComposant):
        for r in self.roots[1:]:
            self.combine_element(self.roots[0], r)
        f = open("classifier"+str(idComposant)+".xml", "w+")
        print(et.tostring(self.roots[0]), file=f)

    def combine_element(self, one, other):
        mapping = {el.tag: el for el in one}
        for el in other:
            if len(el) == 0:
                try:
                    mapping[el.tag].text = el.text
                except KeyError:
                    mapping[el.tag] = el
                    one.append(el)
            else:
                try:
                    self.combine_element(mapping[el.tag], el)
                except KeyError:
                    mapping[el.tag] = el
                    one.append(el)

if __name__ == '__main__':
    main()