import flask
from flask import render_template
app = flask.Flask(__name__)
@app.route('/')
@app.route('/index')
@app.route('/greet/<name>')
def index():
    return render_template('index.html',
                           title='Home',
                           name='name')
if __name__=='__main__':
    app.run()