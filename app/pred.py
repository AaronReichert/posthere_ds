import basilica
import pandas as pd
import category_encoders

def decompress_pickle(file):
    import bz2
    import pickle
    import _pickle as cPickle
    data = bz2.BZ2File(file)
    data = cPickle.load(data)
    return data


# def predict_subreddit(title, text, num_pred):
#     # data = decompress_pickle('post_here_model.pbz2')
#     proba = pd.Series(decompress_pickle(r'..\Models\post_here_model.pbz2').predict_proba(text)[0])
#     proba = subreddit_df['Subreddit'].unique()
#     prediction = (pd.Series(proba).sort_values(ascending=False)).reset_index(drop=True)
#     if num_pred > 1:
#         return prediction[:num_pred]
#     else:
#         return prediction[:1]

def predict_subreddit(title, text, num_pred):
    title = pd.Series(title)
    text = pd.Series(text)
    df = pd.concat([title, text])
    data = decompress_pickle(r'Models\post_here_model.pbz2')
    proba = pd.Series(data.predict_proba(df)[0])
    proba = subreddit_df['Subreddit'].unique()
    prediction = (pd.Series(proba).sort_values(ascending=False)).reset_index(drop=True)
    if num_pred > 1:
        return prediction[:num_pred] 
    else:
        return prediction[:1]

class upvote_predictor:
    def __init__(self, model,):
        self.model = model
    def prepare_string(self, string):
        embedding = None
        with basilica.Connection('370a60d1-2938-b1bf-d813-0cb6954f5a0e') as c:
            embedding = c.embed_sentence(
                string,
                model='reddit',
                timeout=120
                )
        df = pd.Series(embedding)
        df = pd.DataFrame(df).T
        return df
    def predict(self, title, text, subreddit):
        title = self.prepare_string(title)
        text = self.prepare_string(text)
        sub = pd.DataFrame(pd.Series([subreddit]))
        sub.columns = ['subreddit']
        embeddings = pd.concat([title, text], axis = 1)
        embeddings.columns = [i for i in range(1536)]
        df = pd.concat([sub, embeddings], axis =1)
        # print(df)
        return int(self.model.predict(df)[0])
