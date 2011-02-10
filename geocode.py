def latlng(address):
	from django.utils import simplejson as json
	import urllib2
	address = urllib2.quote(address)
	url = "http://maps.google.com/maps/geo?q="+address+"&output=json&sensor=true_or_false&key=ABQIAAAAgcMljB8YddihXjpZyiDsqhQOAULMTQkhNTZJG1WOu8te36qONhTsQzp3hfXUkLAIoHceXL_7Yd3tlA"
	reply = urllib2.urlopen(url).read()
	obj = json.loads(reply)
	coords = obj["Placemark"][0]["Point"]["coordinates"]
	return (coords[0], coords[1])

def load_mapping():
	m = {}
	for l in open("station_names_that_google_maps_understands.txt", "r").read().splitlines():
		start = l[0:l.rfind(" ")]
		end = l[1+l.rfind(" "):]
		m[end] = start
	return m

import time, sys
mapping = load_mapping()
uniq = open("unique_stops", "r").read().splitlines()
#uniq = ["Suehirochou", "Sugamo-Shinden"]

for stop in uniq:
	if stop.strip() == "": continue
	
	stopname = stop.strip() + " Station" if stop not in mapping else mapping[stop].strip()

	retries = 3
	coords = "-"
	while retries > 0:
		try:
			retries -= 1
			coords = latlng(stopname)
		except:
			wait = (4-retries)**2
			sys.stderr.write("Retry after %d secs" % wait)
			time.sleep((4-retries)**2)

	print "%s %s" % (coords, stop)

#print str(latlng("Akabane-Iwabuchi Station"))
