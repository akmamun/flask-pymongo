from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from views.todos import TodoCollection, Todo

app = Flask(__name__)
CORS(app)
api = Api(app, prefix="/api/v1")


# all routes
api.add_resource(TodoCollection, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')

if __name__ == '__main__':
    app.run(debug=True)
