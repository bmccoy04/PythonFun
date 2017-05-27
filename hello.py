class Weather(object):
    def __init__(self, data):
        self.data = data
        self.name = 'Bryan'

import requests

w = Weather('data')

print("Hello" + w.name)

req = requests.get('http://apidev.accuweather.com/locations/v1/search?q=denham springs, la&apikey=hoArfRosT1215')

print(req.json())