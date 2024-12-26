from flask import Flask, request

app = Flask(__name__)

@app.route('/example', methods=['GET', 'POST'])
def example():
    if request.method == 'GET':
        data = request.args.get('data', 'No data sent')
        return f"GET: You sent {data}"
    elif request.method == 'POST':
        data = request.form.get('data', 'No data sent')
        return f"POST: You sent {data}"

if __name__ == "__main__":
    app.run(debug=True)

## Url to Check 
# Get Method: http://127.0.0.1:5000/example?data=hello
# Post Method : http://127.0.0.1:5000/example