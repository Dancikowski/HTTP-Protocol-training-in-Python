from flask import Flask, request, jsonify
import jsonschema
from jsonschema import validate
import  json
from werkzeug.exceptions import BadRequest
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False




@app.route('/product', methods=['POST'])
def hello():

   print("A")
   data = request.get_json()

   if validation(json.loads(json.dumps(data))):
        return jsonify({"token": data['token'], "product": (data['a']*data['b']) })

   else:
        return "Error"


    
def validation(obj):

    schema = dict({
        "type" : "object", "minProperties": 3, "maxProperties": 3,
        "required": ["token", "a", "b"],
        "properties": {
            "token": {"type": "number", "minimum" : 1},
            "a": {"type": "number", "minimum" : 1},
            "b": {"type": "number", "minimum" : 1}
        }

    })
    try:
        validate(obj, schema)
        return  True
    except jsonschema.exceptions.ValidationError as ve:

        raise BadRequest('My custom message')




if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    server = make_server('', 8080, app)
    server.serve_forever()

