from flask import Flask

def create_app():
    '''Create and configure an instance of the Flask application'''

    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] =
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    
    @app.route('/')
    def root():
        return 'Where should you post that on redit?'

    @app.route('/submit')
    def submit():
        return 'Enter your post here'

    @app.route('/suggestions')
    def suggestions():
        return 'Here are suggested posts'
    
    return app