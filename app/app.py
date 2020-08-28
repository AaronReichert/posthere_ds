from flask import Flask, request, jsonify
import json
from .pred import upvote_predictor, subreddit_prediction, decompress_pickle
import pickle
import numpy
from pathlib import Path
import basilica
import en_core_web_sm

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
        # results_counter = results_input

        # --------Haley's model---------
        clf_model = decompress_pickle(r'Models\post_here_model.pbz2') 
        nlp = en_core_web_sm.load()
        sample_results = subreddit_prediction(title_input, text_input, results_input)
        sample_results = sample_results.reset_index()

        sug_sub = (sample_results[0])              

        upvote_path = Path(r"C:\Users\Aaron\Desktop\posthere_ds\Models\up_vote_model.pickle")
        with open(upvote_path, "rb") as f:
            model_uv = pickle.load(f)
        predictor_uv = upvote_predictor(model_uv)

        results = []
        for sub in sample_results[0]:
            results.append({
                'suggested_subreddit':sub,
                'pred_upvotes':predictor_uv.predict(title_input, text_input, sub)})
        # if results_input > 1:
        #     return jsonify(sample_results[0][:results_input])
        # else:
        #     return jsonify(sample_results[0][:1])
        # sug_sub = (sample_results[0][0])              
        # print(sample_results[0][-1])    
        # sug_sub_list = []
        # while results_counter > 0:
        #     results_counter += -1
        #     sug_sub = (sample_results[results_counter][0])  
        #     sug_sub_list += sug_sub
        # print(sug_sub_list)
        # ---------Eric's model-------

        # pred_upvotes = predictor_uv.predict(title_input, text_input, sug_sub)


        return jsonify(results)
        # return results_input

    return app
