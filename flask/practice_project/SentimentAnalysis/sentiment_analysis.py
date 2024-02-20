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

def sentiment_analyzer(text_to_analyse: str) -> dict:
    """Function for running sentiment analysis using the Watson NLP BERT Seniment Analysis function
    """
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    myobj = {"raw_document": { "text": text_to_analyse }}
    response = requests.post(url, json = myobj, headers = header, timeout = 10)
    formatted_response = json.loads(response.text)
    if response.status_code == 200:
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    elif response.status_code == 500:
        label = None
        score = None
    return {"label": label, "score": score}
    