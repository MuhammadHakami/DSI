"""
Module containing model fitting code for a web application that implements a
text classification model.

When run as a module, this will load a csv dataset, train a classification
model, and then pickle the resulting model object to disk.

USE:

python build_model.py --data path_to_input_data --out path_to_save_pickled_model

FOR EXAMPLE:

python build_model.py --data ./data/articles_small.csv --out ./static/model.pkl


"""
import argparse
import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB


class TextClassifier(object):
    """A text classifier model:
        - Vectorize the raw text into features.
        - Fit a naive bayes model to the resulting features.

    The work done by this class could also be done with a sklean.pipeline
    object.  Since the author cannot guarentee that Pipelines have been
    introduced, he opted to write his own class implementing the model.

    This class is an example of coding to an interface, it implements the
    standard sklearn fit, predict, score interface.
    """

    def __init__(self):
        self._vectorizer = TfidfVectorizer()
        self._classifier = MultinomialNB()

    def fit(self, X, y):
        """Fit a text classifier model.

        Parameters
        ----------
        X: A numpy array or list of text fragments, to be used as predictors.
        y: A numpy array or python list of labels, to be used as responses.

        Returns
        -------
        self: The fit model object.
        """


    def predict_proba(self, X):
        """Make probability predictions on new data.

        Parameters
        ----------
        X: A numpy array or list of text fragments, to be used as predictors.

        Returns
        -------
        probs: A (n_obs, n_classes) numpy array of predicted class probabilities.
        """


    def predict(self, X):
        """Make class predictions on new data.

        Parameters
        ----------
        X: A numpy array or list of text fragments, to be used as predictors.

        Returns
        -------
        preds: A (n_obs,) numpy array containing the predicted class for each
        observation (i.e. the class with the maximal predicted class probabilitiy.
        """
        X = self._vectorizer.transform(X)
        return self._classifier.predict(X)

    def score(self, X, y):
        """Return a classification accuracy score on new data.

        Parameters
        ----------
        X: A numpy array or list of text fragments.
        y: A numpy array or python list of true class labels.
        """
    


def get_data(filename):
    """Load raw data from a file and return training data and responses.

    Parameters
    ----------
    filename: The path to a csv file containing the raw text data and response.

    Returns
    -------
    X: A numpy array containing the text fragments used for training.
    y: A numpy array containing labels, used for model response.
    """



if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Fit a Text Classifier model and save the results.')
    parser.add_argument('--data', help='A csv file with input data.')
    parser.add_argument(
        '--out', help='A file to save the pickled model object to.')
    args = parser.parse_args()

    X, y = get_data(args.data)
    tc = TextClassifier()
    tc.fit(X, y)
    with open(args.out, 'wb') as f:
        pickle.dump(tc, f)
