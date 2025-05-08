from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import os

app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv("MONGO_URI", "mongodb://mongo:27017/todo_db")
mongo = PyMongo(app)
todos = mongo.db.todos

@app.route("/todos", methods=["POST"])
def add_todo():
    data = request.get_json()
    task = data.get("task")
    if not task:
        return jsonify({"error": "Task content is required"}), 400
    todo_id = todos.insert_one({"task": task}).inserted_id
    return jsonify({"id": str(todo_id), "task": task}), 201

@app.route("/todos", methods=["GET"])
def get_todos():
    all_todos = [{"id": str(todo["_id"]), "task": todo["task"]} for todo in todos.find()]
    return jsonify(all_todos)

@app.route("/todos/<id>", methods=["PUT"])
def update_todo(id):
    data = request.get_json()
    task = data.get("task")
    if not task:
        return jsonify({"error": "Task content is required"}), 400
    result = todos.update_one({"_id": ObjectId(id)}, {"$set": {"task": task}})
    if result.matched_count == 0:
        return jsonify({"error": "Todo not found"}), 404
    return jsonify({"id": id, "task": task})

@app.route("/todos/<id>", methods=["DELETE"])
def delete_todo(id):
    result = todos.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        return jsonify({"error": "Todo not found"}), 404
    return jsonify({"result": "Deleted"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
