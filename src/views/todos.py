from flask import request
from flask_restful import Resource
from models import todo

todo = todo.Todo()


class TodoCollection(Resource):
    def get(self):
        if request.method == "GET":
            return todo.find({})

    def post(self):
        title = request.form['title']
        body = request.form['body']
        response = todo.create({'title': title, 'body': body})
        return response, 201


class Todo(Resource):

    def get(self, todo_id):
        return todo.find_by_id(todo_id)

    def put(self, todo_id):
        title = request.form['title']
        body = request.form['body']
        response = todo.update(todo_id, {'title': title, 'body': body})
        return response, 201

    def delete(self, todo_id):
        todo.delete(todo_id)
        return "Record Deleted", 204
