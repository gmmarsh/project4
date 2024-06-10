from flask import Flask, request, render_template, send_file
from top2vec import Top2Vec
import matplotlib.pyplot as plt



app = Flask(__name__)

# Flask routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/home')
def home1():
    return render_template('home.html')

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

@app.route('/Prediction', methods=['GET', 'POST'])
def prediction():
    results = None
    if request.method == 'POST':
        # Get the input from the user
        text = request.form['text']
        return render_template('prediction.html', results=results)
    elif request.method == 'GET':
        # Handle GET request here
        return render_template('prediction.html')
    
@app.route('/Get_Topics', methods=['POST'])
def get_topics():
    if request.method == 'POST':
        # Load the model
        model = Top2Vec.load("top2vec_model")
        # Get the topics
        topics = model.get_topics()
        return render_template('topics.html', topics=topics)
    elif request.method == 'GET':
        # Handle GET request here
        return render_template('topics.html')

if __name__ == '__main__':
    app.run(debug=True)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404