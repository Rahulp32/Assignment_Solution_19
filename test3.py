from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the homepage!'

@app.route('/login')
def login():
    # Logic for logging in the user
    return 'Please log in!'

@app.route('/secret')
def secret():
    logged_in = False  # Example condition
    if not logged_in:
        return redirect(url_for('login'))
    return 'This is a secret page!'

if __name__ == '__main__':
    app.run(debug=True)
