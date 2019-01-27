from flask import Flask, render_template, request, jsonify
import pickle
from build_model import TextClassifier

app = Flask(__name__)


with open('static/model.pkl', 'rb') as f:
    model = pickle.load(f)

# missing decorators and content 

def index():
    """Render a simple splash page."""


def submit():
    """Render a page containing a textarea input where the user can paste an
    article to be classified.  """


def predict():
    """Recieve the article to be classified from an input form and use the
    model to classify.
    """



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
