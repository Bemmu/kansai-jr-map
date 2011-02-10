import django.utils.simplejson as json
import re

stop_locations = {}
ls = open("stop_locations", "r").read().splitlines()
for l in ls:
	m = re.match("\(([^,]+), ([^,]+)\) (.*)", l)
	if m:
		stop_locations[m.group(3)] = [float(m.group(1)), float(m.group(2))];
print "var stop_locations = " + json.dumps(stop_locations) + ";"

