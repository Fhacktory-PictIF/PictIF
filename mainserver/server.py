#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template
import json

from core.component import Component

app = Flask(__name__)
app.debug = True

#contient les component ajoutés, liés ou non à d'autres
class ComponentGestion(object) :
    def __init__(self):
        self.map_of_component = {}

componentGestioner = ComponentGestion()

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/block/list", methods = ['GET'])
def getBlocksList():
    resp = dict(ok=True, io=Component.ioComponents, processors=Component.processors, selectors=Component.selectors, statistics=Component.statistics)
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
def getBlockFromType(blockType):
    subclasses = Component.__subclasses__()
    for subclass in subclasses:
        if subclass == blockType:
            comp = subclass()
            componentGestioner.map_of_component[comp.id] = comp
            resp = {'ok': False, 'id': comp.id}
        return json.dump(resp)


    resp = {'ok': False}
    return json.dump(resp)

@app.route("/save", methods = ['POST'])
def saveWorkFlow():
    resp = dict(ok=True)
    return json.dumps(resp)

@app.route("/addConnection", methods = ['POST'])
def addConnection() :
    resp={'ok':True, 'result':''}
    return json.dump(resp)

@app.route("/removeConnection", methods = ['POST'])
def removeConnection() :
    pass

@app.route("/removeComponent", methods = ['POST'])
def removeComponent() :
    pass

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
