from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        data = request.get_json()
        a = data.get('a', 0)
        b = data.get('b', 0)
    else:
        a = float(request.args.get('a', 0))
        b = float(request.args.get('b', 0))
    
    result = a + b
    return jsonify({'result': result})

@app.route('/multiply', methods=['GET', 'POST'])
def multiply():
    if request.method == 'POST':
        data = request.get_json()
        a = data.get('a', 1)
        b = data.get('b', 1)
    else:
        a = float(request.args.get('a', 1))
        b = float(request.args.get('b', 1))
    
    result = a * b
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
