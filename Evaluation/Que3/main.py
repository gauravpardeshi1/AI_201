from flask import Flask
app=Flask(__name__)

app.route('/')
def Home():
    return "Welcome to Home Page"

app.route('/about')
def About():
    return "Welcom to About Page"

app.route('/id')
def SinglePage():
    return "Redirect particular Page using id"

if __name__ =='__main__':
# app.run()
