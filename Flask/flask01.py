from flask import Flask, jsonify
#app.config['DEBUG'] esto no funciona, para activar el modo debug hay que ponerlo en el run como se indica mas abajo

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World'

@app.route('/json')
def json():
    age = 2*5
    retJson = {
        'Name': "Pedro",
        'Age': age
    }
    return jsonify(array1)

if __name__ =="__main__":
        app.run(debug=True, host="127.0.0.1")
