import requests


def get_weather(city):

    url = f"https://wttr.in/{city}?format=j1"

    response = requests.get(url)

    data = response.json()

    temperature = data["current_condition"][0]["temp_C"]

    condition = data["current_condition"][0]["weatherDesc"][0]["value"]

    humidity = data["current_condition"][0]["humidity"]

    return temperature, condition, humidity