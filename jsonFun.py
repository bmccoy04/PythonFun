
import json

array = '{"fruits": ["apple", "banana", "orange"]}'
data  = json.loads(array)
print (data['fruits'])

array2 = '[{"fruits": ["apple", "banana", "orange"]}, {"fruits":["pear", "tang"]}]'
data2 = json.loads(array2)

print(data2[0]["fruits"][0])
print(len(data2))

for d in data2:
    for x in d['fruits']:
        print(x)