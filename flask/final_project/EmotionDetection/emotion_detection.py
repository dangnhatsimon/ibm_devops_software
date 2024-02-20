''' NLP sentiment analysis is the practice of using computers 
    to recognize sentiment or emotion expressed in a text.
    Sentiment analysis is often performed on textual data 
    to help businesses monitor brand and product sentiment in customer feedback, 
    and understanding customer needs. It helps attain the attitude 
    and mood of the wider public which can then help gather insightful information.
    We'll be making use of the Watson Embedded AI Libraries.
'''
import json
import requests


def emotion_detector(text_to_analyse: str) -> dict:
    """Function for running Emotion Predict using the Watson NLP libraries
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": {"text": text_to_analyse}}
    response = requests.post(url, json=myobj, headers=header, timeout=10)
    formatted_response = json.loads(response.text)
    if response.status_code == 200:
        anger_score = float(
            formatted_response["emotionPredictions"][0]["emotion"]["anger"])
        disgust_score = float(
            formatted_response["emotionPredictions"][0]["emotion"]["disgust"])
        fear_score = float(
            formatted_response["emotionPredictions"][0]["emotion"]["fear"])
        joy_score = float(
            formatted_response["emotionPredictions"][0]["emotion"]["joy"])
        sadness_score = float(
            formatted_response["emotionPredictions"][0]["emotion"]["sadness"])
        dominant_emotion = max(
            formatted_response["emotionPredictions"][0]["emotion"],
            key=lambda emo: formatted_response["emotionPredictions"][0]["emotion"][emo]
        )
    elif response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion = None
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
