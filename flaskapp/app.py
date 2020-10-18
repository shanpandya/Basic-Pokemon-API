from flask import Flask, jsonify, request
import aws_controller
import boto3

app = Flask(__name__)

@app.route('/')
def index():
    return "This is the main page."


@app.route('/pokemon', methods=['GET'])
def get_items():
    return jsonify(aws_controller.get_items())

@app.route('/pokemon', methods=['POST'])
def post_items():
    name = request.json.get('name')
    type = request.json.get('type')

    if not name or not type:
        return jsonify({'error': 'Please provide name and type'}), 400

    return aws_controller.post_items(name, type)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)