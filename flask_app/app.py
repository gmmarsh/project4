from flask import Flask, request, render_template, send_file
from top2vec import Top2Vec
import matplotlib.pyplot as plt



app = Flask(__name__)

# Flask routes
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/what')
def what():
    return render_template('what.html')

@app.route('/Why')
def why():
    return render_template('why.html')

@app.route('/how')
def how():
    return render_template('how.html')

@app.route('/20NewsGroups')
def news():
    return render_template('20NewsGroups.html')

if __name__ == '__main__':
    app.run(debug=True)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404