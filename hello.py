from flask import Flask, escape, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route('/api/messages', methods=['GET'])
def api_messages_get():
    data = [
        {
            "user": "Jon",
            "message": "Hello!",
            "created_at": "2020-01-01 00:00:00"
        }
    ]
    return jsonify(data)