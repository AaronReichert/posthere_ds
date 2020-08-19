from flask import Flask


def create_app():
    '''create and configure the flask application'''

    app = Flask(__name__)

    @app.route('/')
    def root():
        message = 'Where should you post that on redit?'
        return message

    @app.route('/submit', methods=['POST'])
        message = 'enter your post here'
        return message

    @app.route('/suggestions', methods=['GET'])
        message = 'here are suggested posts'
        return message

    return app