from flask import Flask,jsonify,request,render_template

app = Flask(__name__)



Mul=[]
Sum=[]

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/product',methods=['POST'])
def productOfNum():
    request_data=request.get_json()
    newMul={
        'num1':request_data['num1'],
        'num2':request_data['num2'],
        'output':float(request_data['num1'])* float (request_data['num2'])
            }



    Mul.append(newMul)
    return jsonify(newMul)

@app.route('/sum',methods=['POST'])
def sumOfNum():
    request_data=request.get_json()
    fn=request_data['num1']
    sn=request_data['num2']
    add={
         'num1':fn,
        'num2':sn,
        'output': float(fn) + float (sn)
        }
    Sum.append(add)
    return jsonify(add)




app.run(port=5001)
