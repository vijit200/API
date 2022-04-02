from flask import Flask,request,jsonify
from sql import my_con
from mongodb import mongo
app = Flask(__name__)
@app.route('/xyz',methods = ['GET','POST'])
def test():
    if request.method == 'POST':
        a = request.json['num1']
        b = request.json['num2']
        result = a + b
        return jsonify(str(result))
@app.route('/XYZ',methods = ['POST'])
def test1():
    if request.method == 'POST':
        a = request.json['num7']
        b = request.json['num8']
        result = a + b
        return jsonify(str(result))

@app.route('/abc',methods = ['POST'])
def test2():
    if request.method == 'POST':
        a = request.json['num3']
        b = request.json['num4']
        result = a + b
        return jsonify(str(result))
@app.route('/ABC',methods = ['POST'])
def test3():
    if request.method == 'POST':
        a = request.json['num5']
        b = request.json['num6']
        result = a + b
        return jsonify(str(result))

@app.route('/mysql',methods = ['POST'])
def sql():
    if request.method == 'POST':
        a = request.json['Host']
        b = request.json['User']
        c = request.json['Passwd']
        d = request.json['Database']
        e = request.json['Table']
        s = my_con(a,b,c,d,e)
        return jsonify(str(s.connection()))
@app.route('/mongo',methods = ['POST'])
def mong():
    if request.method == 'POST':
        a = request.json['Link']
        b = request.json['Database']
        c = request.json['Table']
        s = mongo(a,b,c)
        return jsonify(str(s.mong_con()))

if __name__ == '__main__':
    app.run(port=8000)
# 1. write a function to fetch data from sql table via api
#2  write a function to fetch a data from mongodb table