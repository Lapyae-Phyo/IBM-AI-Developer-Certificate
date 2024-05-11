""" This function sent text to model and return the result"""
import json
import requests


def sentiment_analyzer(text_to_analyse):
    """This function takes one parameter text to analyse and return the analyzed result"""
    url = """https://sn-watson-sentiment-bert.labs.skills.network/v1/
             watson.runtime.nlp.v1/NlpService/SentimentPredict"""
    header = {
        "grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    myobj = {"raw_document": {"text": text_to_analyse}}
    response = requests.post(url, json=myobj, headers=header, timeout=10)
    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
        return {"label": label, "score": score}
    return {"label": None, "score": None}
