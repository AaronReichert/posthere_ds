'''Import all necessary modules.'''
import pickle
from flask import Flask, request, jsonify
from .pred import upvote_predictor, subreddit_prediction
from pathlib import Path


def create_app():
    '''Create and configure an instance of the Flask application'''

    app = Flask(__name__)

    @app.route('/')
    def root():
        return 'Where should you post that on reddit?'

    @app.route('/suggestions', methods=['POST'])
    '''Route set up to take in json inputs to be run through model based on
    title and text to first return a subreddit followed by a upvote'''
    def suggestions():
        # Takes json requests from web.
        title_input = request.json['title']
        text_input = request.json['text']
        results_input = request.json['results']

        # Funnels the user inputs into the function and through the model.
        sample_results = subreddit_prediction(title_input,
                                              text_input,
                                              results_input)
        sample_results = sample_results.reset_index()

        sug_sub = (sample_results[0])

        # Funnels the results of the first model into the funciton for upvotes.
        upvote_path = Path(r"Models/up_vote_model.pickle")
        with open(upvote_path, "rb") as f:
            model_uv = pickle.load(f)
        predictor_uv = upvote_predictor(model_uv)

        # Creates the array from the results of the models.
        results = []
        for sub in sample_results[0]:
            results.append({
                'suggested_subreddit': sub,
                'pred_upvotes': predictor_uv.predict(title_input,
                                                     text_input, sub)})

        # Returns results in json format.
        return jsonify(results)

    return app
