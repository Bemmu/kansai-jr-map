import os
import re
import django.utils.simplejson as json

def lines():
	lines = {}
	for fn in os.listdir("stops"):
		stops = open("stops/%s" % fn, "r").read().splitlines()
		color = stops[0].strip()
		stops = map(lambda x:x.strip(), stops[1:])
		stops = filter(lambda x:x != "", stops)
		edges = zip(stops[0:], stops[1:])
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
os.sys("/usr/local/bin/python > ")
print json.dumps(struct)
