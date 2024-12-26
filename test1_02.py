from flask import Flask, request

app = Flask(__name__)

@app.route('/post_example', methods=['POST'])
def post_example():
    # Get data from the request body (form data)
    data = request.form.get('data', 'No data provided')
    return f"POST Request: You sent: {data}"

if __name__ == "__main__":
    app.run(debug=True)


### To Check URL: http://127.0.0.1:5000/post_example