''' Executing this function initiates the application of emotion
    prediction to be executed over the Flask channel and deployed on
    localhost:5000.
'''

# Import Flask, render_template, request from the flask framework package:
from flask import Flask, render_template, request

# Import the emotion_detector function from the package created:
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the flask app:
app = Flask("Emotion Prediction")

@app.route("/emotionDetector")
def sent_emotion():
    ''' This code receives the text from the HTML interface and 
        runs emotion detector over it using emotion_detector()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''

    text_to_analyze = request.args.get('textToAnalyze')
    if text_to_analyze is None:
        return "Invalid text! Please try again!."
    result = emotion_detector(text_to_analyze)
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!."
    return f"""
        For the given statement, the system response is 
        'anger': {result['anger']},
        'disgust': {result['disgust']},
        'fear': {result['fear']},
        'joy': {result['joy']},
        'sadness': {result['sadness']}.
        The dominant emotion is {result['dominant_emotion']}
    """

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
