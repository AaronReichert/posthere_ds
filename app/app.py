from flask import Flask, request, jsonify
import json
from .pred import upvote_predictor
# , predict_subreddit, decompress_pickle
import pickle
import numpy
from pathlib import Path
# import basilica


def create_app():
    '''Create and configure an instance of the Flask application'''

    app = Flask(__name__)
    # app.config["SQLALCHEMY_DATABASE_URI"] = 
    # app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    # db.init_app(app)

    @app.route('/')
    def root():
        return 'Where should you post that on reddit?'

    @app.route('/submit', methods=['GET'])
    def submit():

        return 'Enter your post here'

    @app.route('/suggestions', methods=['POST'])
    def suggestions():
        title_input = request.json['title']
        text_input = request.json['text']
        results_input = request.json['results']

        # pred_results = predict_subreddit(text_input, results_input)
        
        # filename = 'Models\post_here_model.pkl'
        # load_model = pickle.load(open(filename, 'rb'))
        # predict_subreddit(text_input, results_input)
                
        # with open('Models\post_here_model.pkl', 'rb') as g:
        #     model_ph = pickle.load(g)
        # predictor_ph = predict_subreddit(load_model)
        # predictor_ph.predict(text_input, results_input)

        
        # upvote_path = Path(r"C:\Users\Aaron\Desktop\posthere_ds\Models\up_vote_model.pickle")
        # with open(upvote_path, "rb") as f:
        #     model_uv = pickle.load(f)
        # predictor_uv = upvote_predictor(model_uv)
        # pred_upvotes = predictor_uv.predict(title_input, text_input, "r/AskReddit")

        # with open("model.pickle", "rb") as f:
        #     model = pickle.load(f)
        # predictor = upvote_predictor(model)
        # pred_upvotes = predictor.predict(title_input, text_input, "r/AskReddit")

        # -----testing purposes only-----
        if results_input == 1:
            sample_results = {'suggested_reddit':'r/sample', 'pred_upvotes':74556}

        return jsonify(sample_results)
        # return results_input

    return app
