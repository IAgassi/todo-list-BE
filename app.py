from flask import *
from flask_cors import *
import Functions

app = Flask(__name__)
CORS(app)


# returns all todos
@app.route('/api/todos', methods=['GET'])
def get_todos():
    response = jsonify(Functions.get_all_todos())
    return make_response(response, 200)


# receives ID
# inserts an item into DB
@app.route('/api/todos', methods=['POST'])
def insert_todo():
    content = request.get_json()
    print(content)
    id = content['id']
    task = content['task']
    if (Functions.insert_todo(id, task)):
        return make_response("Insertion Successful", 200)
    else:
        return make_response("Couldn't insert")


# receives ID and String
# deletes from DB
@app.route('/api/todos/<int:todo_item>', methods=['DELETE'])
def remove_todo():
    response = jsonify(Functions.get_all_todos())
    return make_response(response, 200)

##############################
###   ROUTES WITHOUT DB!   ###
##############################

@app.route('/test/todos', methods=['GET'])
def get_fake_todos():
    response = jsonify(Functions.get_fakes())
    return make_response(response, 200)


@app.route('/test/todos', methods=['POST'])
def insert_fake_todo():
    content = request.get_json()
    print(content)
    task = content['task']
    response = jsonify(Functions.insert_fake(task))
    return make_response(response, 200)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, threaded=True)
