from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return jsonify({'message': 'Hello from Flask!'})

if __name__ == '__main__':
    app.run(debug=True)


## URL to Check : http://127.0.0.1:5000/hello