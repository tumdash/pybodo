from flask import Flask, request
app = Flask(__name__)

@app.route('/pybodo/', methods=['GET', 'POST', 'DELETE', 'PUT'])
def hello():
    if request.method == 'GET':
        return handle_get()
    elif request.method == 'POST':
        return handle_post()
    elif request.method == 'DELETE':
        return handle_delete()
    elif request.method == 'PUT':
        return handle_put()

def handle_get():
    return 'GET Successfull'

def handle_post():
    return 'POST Successfull'

def handle_delete():
    return 'DELETE Successfull'

def handle_put():
    return 'PUT Successfull'

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=8080)

