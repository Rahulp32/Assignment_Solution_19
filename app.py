from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = "John Doe"
    hobbies = ["Reading", "Hiking", "Coding"]
    return render_template('index.html', name=name, hobbies=hobbies)

if __name__ == '__main__':
    app.run(debug=True)