import requests
import json
import win32com.client as wk
print("welcome to our weather App")
city = input("enter the name of the city:")
url = f"https://api.weatherapi.com/v1/current.json?key=f5bad27ba04b4c2589e171005233107&q={city}"
r = requests.get(url)
sp = wk.Dispatch("SAPI.SpVoice")
whtdic = json.loads(r.text)
wemp =(whtdic["current"] ["temp_c"])
wlstup =(whtdic["current"]["last_updated"])
whum =(whtdic["current"]["humidity"])
wfeel =(whtdic["current"]["feelslike_c"])
tell = f"the current weather in the {city} is {wemp} and it was last updated on{wlstup} and the current humidity is {whum},it feel's like{wfeel}"
sp.speak(tell)
end = ("thank you for visiting our weather app beta and please be assured we will work to improve our sevice for you. Bye vist again")
print(end)
sp.speak(end)
