from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome!'

@app.route('/greet/<username>')
def greet(username):
    return 'Hello, {}!'.format(username)

@app.route('/farewell/<username>')
def farewell(username):
    return 'Goodbye, {}!'.format(username)

if __name__ == '__main__':
    app.run()