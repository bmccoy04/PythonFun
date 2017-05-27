import requests

print("Hello")

req = requests.get('http://apidev.accuweather.com/locations/v1/search?q=denham springs, la&apikey=hoArfRosT1215')

print(req.json())