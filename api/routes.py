from flask import jsonify, request
from .config import API_KEY
from .models import news_list


def get_news():

    news_data = [
        {
            "title": news.tit, 
            "description": news.des,
            "image": news.img
        }
        for news in news_list
    ]

    api_key = request.args.get("api_key")

    if api_key is None and len(request.args) > 0:
        return jsonify({"error": "Invalid query parameters"})

    if api_key and api_key != API_KEY:
        return jsonify({"error": "Invalid api key"})

    return jsonify({"news": news_data})