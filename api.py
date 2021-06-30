import modules
import flask
import requests

app = flask.Flask(__name__)


"""
================================================================
[ Create Entry ]

Method: GET | POST 
Requirements: 
    NONE
Returns:
    server Ip: STRING
================================================================
"""  
@app.route("/", methods=["GET", "POST"])
def index():
    return "Flask Ip Saver" + flask.request.environ.get('HTTP_X_REAL_IP', flask.request.remote_addr)

"""
================================================================
[ Create Entry ]

Method: GET 
Requirements: 
    name: STRING
    ip: STRING 
Returns:
    result: STRING
================================================================
"""   
@app.route("/save", methods=["GET"])
def save():
    if 'name' in flask.request.args:
        name = str(flask.request.args['name'])
    else:
        return "Name field cant be NONE"

    if 'ip' in flask.request.args:
        ip = str(flask.request.args['ip'])
    else:
        return "Ip field cant be NONE"
    
    if modules.db.table().validate(name):
        return "Table Already Exists"
    elif modules.db.table().validate(name) == False:
        modules.db.table().create(name)
        return modules.db.table().add(name,ip)
"""
================================================================
[ Get Ip ]

Method: GET 
Requirements: 
    name: STRING 
Returns:
    ip: STRING
================================================================
"""    
@app.route("/get", methods=["GET"])
def get():
    if 'name' in flask.request.args:
        name = str(flask.request.args['name'])
    else:
        return "Name field cant be NONE" 
    
    if modules.db.table().validate(name) == False:
        return "Table " + name + " does not exist"
    elif modules.db.table().validate(name) == True:
        return modules.db.table().get(name)

"""
================================================================
[ Delete Entry ]

Method: GET 
Requirements: 
    name: STRING 
Returns:
    result: STRING
================================================================
"""   
@app.route("/delete", methods=["GET"])
def delete():
    if 'name' in flask.request.args:
        name = str(flask.request.args['name'])
    else:
        return "Name field cant be NONE" 
    
    if modules.db.table().validate(name) == False:
        return "Table " + name + " does not exist"
    elif modules.db.table().validate(name) == True:
        return modules.db.table().delete(name)

# Run command.
app.run()