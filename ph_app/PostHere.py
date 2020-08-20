from flask import Flask


def create_app():
    '''create and configure the flask application'''
    APP = Flask(__name__) 
        
    @APP.route('/')
    def root():
        message = 'Where should you post that on redit?'
        return message

    @APP.route('/submit')
    def submit():
        message = 'enter your post here'
        return message

    @APP.route('/suggestions')
    def suggestions():
        message = 'here are suggested posts'
        return message

    return APP