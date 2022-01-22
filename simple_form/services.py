import urllib.request, urllib.parse, urllib.error
import json
import ssl
from requests.models import PreparedRequest


url = 'http://api.openweathermap.org/data/2.5/weather?'
params = {'APPID':'25e8b9e17b72a2d527b94198844c9fe2'}



def get_weather(city):
    params["q"]=city+',usa'
    req = PreparedRequest()
    req.prepare_url(url, params)
    current_url = req.url

    fhand = urllib.request.urlopen(current_url)
    data = fhand.read()
    file = data.decode()
    js = json.loads(file)

    data = []
    data.append(js['name'])
    data.append(js['weather'][0]['description'])
    data.append(js['main']['temp'])
    data.append(js['main']['temp_max'])
    return data


