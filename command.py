import webbrowser
from speech import speak
from datetime import datetime
import subprocess
from weather import get_weather
from news import speak_news


def tell_weather(city):
    temperature, condition, humidity = get_weather(city)

    speak(
        f"The temperature in {city} is {temperature} degrees Celsius. "
        f"The weather is {condition}. Humidity is {humidity} percent."
    )

def open_calculator():
    subprocess.Popen("calc.exe")

def open_vscode():
    subprocess.Popen("vscode.exe")



def tell_time():
    current_time = datetime.now().strftime("%I:%M %p")
    speak(f"The time is {current_time}")

def tell_date():
    current_date = datetime.now().strftime("%d %B %Y")
    speak(f"The date is {current_date}")    

def open_youtube():
    webbrowser.open("https://www.youtube.com")

def play_music(song):
    url = "https://www.youtube.com/results?search_query=" + song.replace(" ", "+")
    webbrowser.open(url)    


def open_google():
    webbrowser.open("https://www.google.com")

def search_google(query):
    url = "https://www.google.com/search?q=" + query.replace(" ", "+")
    webbrowser.open(url)

def open_instagram():
    webbrowser.open("https://www.instagram.com")


def process_command(command):

    command = command.lower()

    if "youtube" in command:
        speak("Opening YouTube")
        open_youtube()

    elif "google" in command:
        speak("Opening Google")
        open_google()

    elif "instagram" in command:
        speak("Opening Instagram")
        open_instagram()

    elif "time" in command:
        tell_time()

    elif "date" in command:
        tell_date()

    elif "play" in command:
        song = command.replace("play", "")
        song = song.replace("song", "")
        song = song.replace("music", "")
        song = song.strip()

        speak(f"Searching for {song}")
        play_music(song)

    elif "search" in command:
        search = command.replace("search", "")
        search = search.replace("define", "")
        search = search.replace("find", "")
        search = search.strip()

        speak(f"Searching for {search}")
        search_google(search)

    elif "calculator" in command:
        speak("opening calculator")
        open_calculator()

    elif "weather" in command:
        city = command.replace("weather", "")
        city = city.replace("in", "")
        city = city.strip()

        if city == "":
            city = "Varanasi"

        tell_weather(city)

    elif "news" in command:
        speak_news()   