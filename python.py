
import urllib2
import json


response = urllib2.urlopen('https://blockchain.info/ticker')

data = response.read()

ddata = json.loads(data)

item = ddata["USD"]["last"]

item = str(item)

fo = open('mypath/file.txt', 'a')

fo.write(item + '\n')

fo.close();


