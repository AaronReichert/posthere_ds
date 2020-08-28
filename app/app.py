from flask import Flask, request, jsonify
from .pred import upvote_predictor, subreddit_prediction
import pickle
from pathlib import Path


def create_app():
    '''Create and configure an instance of the Flask application'''

    app = Flask(__name__)

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
        # results_counter = results_input

        # --------Haley's model---------
        sample_results = subreddit_prediction(title_input,
                                              text_input,
                                              results_input)
        sample_results = sample_results.reset_index()

        sug_sub = (sample_results[0])

        upvote_path = Path(r"Models/up_vote_model.pickle")
        with open(upvote_path, "rb") as f:
            model_uv = pickle.load(f)
        predictor_uv = upvote_predictor(model_uv)

        results = []
        for sub in sample_results[0]:
            results.append({
                'suggested_subreddit': sub,
                'pred_upvotes': predictor_uv.predict(title_input,
                                                     text_input, sub)})

        return jsonify(results)

    return app
