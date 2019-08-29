import pandas
from sklearn import datasets
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
import pickle


def predict(X):
    '''
    Evaluate a prediction and hand over the result
    '''
    # load the model from disk
    filename = 'model.pkl'
    loaded_model = pickle.load(open(filename, 'rb'))
    return loaded_model.predict(X)
 
 
