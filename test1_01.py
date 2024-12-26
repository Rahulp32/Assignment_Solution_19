from flask import Flask, request

app = Flask(__name__)

@app.route('/get_example', methods=['GET'])
def get_example():
    # Get data from the URL query parameter 'param'
    param = request.args.get('param', 'No parameter provided')
    return f"GET Request: You sent: {param}"

if __name__ == "__main__":
    app.run(debug=True)

### TO Check URL: http://127.0.0.1:5000/get_example?param=hello