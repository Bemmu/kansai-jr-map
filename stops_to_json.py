import os
import re
import django.utils.simplejson as json

def edges_from_stops(stops):
	edges = []
	prev_stop = None
	for stop in stops:
		if stop == "": # signifies branch line
			prev_stop = None
			continue
		if prev_stop:
			edges.append([prev_stop, stop])
		prev_stop = stop
	return edges

def lines():
	lines = {}
	for fn in os.listdir("stops"):
		stops = open("stops/%s" % fn, "r").read().splitlines()
		color = stops[0].strip()
		stops = map(lambda x:x.strip(), stops[1:])
		edges = edges_from_stops(stops)

		lines[fn.replace("_", " ")] = {
			"edges" : edges,
			"color" : color
		}
	return lines
	
def stops():
	stop_locations = {}
	ls = open("stop_locations", "r").read().splitlines()
	for l in ls:
		m = re.match("\(([^,]+), ([^,]+)\) (.*)", l)
		if m:
			stop_locations[m.group(3)] = [float(m.group(1)), float(m.group(2))];
	return stop_locations

struct = {
	"lines" : lines(),
	"stops" : stops()
}
	
import os
#os.system("/usr/local/bin/python geocode.py > stop_locations")
print "var sub = " + json.dumps(struct) + ";"
