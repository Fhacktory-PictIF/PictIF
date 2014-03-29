#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template
import json

from core.component import Component

app = Flask(__name__)
app.debug = True

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
def getBlockFromType(blockId):
    resp = dict(ok=True)
    return json.dumps(resp)

@app.route("/save", methods = ['POST'])
def saveWorkFlow():
    resp = dict(ok=True)
    return json.dumps(resp)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
