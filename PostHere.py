from flask import Flask


app = Flask(__name__) 

def create_app():
    '''create and configure the flask application'''

@app.route('/')
def root():
    message = 'Where should you post that on redit?'
    return message

@app.route('/submit')
def submit():
    message = 'enter your post here'
    return message

@app.route('/suggestions')
def suggestions():
    message = 'here are suggested posts'
    return message