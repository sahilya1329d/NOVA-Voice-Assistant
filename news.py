import requests
import os
from dotenv import load_dotenv
from speech import speak


load_dotenv()


def get_news():

    api_key = os.getenv("NEWS_API_KEY")

    url = f"https://newsdata.io/api/1/news?apikey={api_key}&country=in&language=en"

    response = requests.get(url)

    data = response.json()

    return data


def get_headlines():

    data = get_news()

    articles = data["results"]

    headlines = []

    for article in articles[:5]:
        headlines.append(article["title"])

    return headlines


def speak_news():

    headlines = get_headlines()

    speak("Here are the latest headlines.")

    for headline in headlines:
        speak(headline)