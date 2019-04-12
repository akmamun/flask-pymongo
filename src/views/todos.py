from flask import request,jsonify
from flask_restful import Resource
from flask_restful.reqparse import RequestParser
import json

from models import todo

todo = todo.Todo()


parser = RequestParser()

parser.add_argument("title")
parser.add_argument("body")



class TodoCollection(Resource):
    def get(self):
     	return jsonify(todo.find({}))  

    def post(self):
        args = parser.parse_args()
        response = todo.create({"title": args["title"], "body":args["body"]})
        return response, 201


class Todo(Resource):

    def get(self, todo_id):
        return jsonify(todo.find_by_id(todo_id))

    def put(self, todo_id):
        args = parser.parse_args()
        response = todo.update(todo_id, {"title": args["title"], "body":args["body"]})
        return response, 201

    def delete(self, todo_id):
        todo.delete(todo_id)
        return "Record Deleted", 204
