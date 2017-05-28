import urllib

url = "http://www.google.com"
f = urllib.urlopen(url)

print(f.read())