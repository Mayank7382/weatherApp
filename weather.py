import requests
import json
import pyttsx3

city = input("Enter the name of the city: ")
url = f"http://api.weatherapi.com/v1/current.json?key=57d6454172af40dabca202713232503&q={city}"
r = requests.get(url)
wdic = json.loads(r.text)
temp_c = wdic["current"]["temp_c"]
last_updated = wdic["current"]["last_updated"]
is_day = wdic["current"]["is_day"]

day_or_night = "day" if is_day == 1 else "night"

engine = pyttsx3.init()
engine.say(f"The current weather in {city} is {temp_c} degrees. It is currently {day_or_night}time and was last updated at {last_updated}")
print(f"The current weather in {city} is {temp_c:.1f} degrees. It is currently {day_or_night} time and was last updated at {last_updated}")
engine.runAndWait()
