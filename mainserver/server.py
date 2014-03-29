from flask import Flask, render_template, request
import json

app = Flask(__name__)
app.debug = True


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/mapPoint", methods = ['POST','GET'])
def mafonction():
    pass

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)