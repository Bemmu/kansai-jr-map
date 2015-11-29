# Parses single station information from Ekitan
#
#pip install beautifulsoup4
# -*- coding:utf8 -*-
import bs4
from bs4 import BeautifulSoup
import urllib

def station(id):
	url = "http://ekitan.com/station/EnsenList?SFCODE=%s" % id
	html_doc = urllib.urlopen(url).read()
	soup = BeautifulSoup(html_doc, 'html.parser')
	#print(soup.prettify().encode('utf-8'))

	# Find the table which contains td of class line
	table = [t for t in soup.findAll('table') if t.find('td', {"class" : "line"})][0]

	# Now each <tr> describes a line
	lines = []
	for tr in table.findAll('tr'):	
		line = tr.find('td', {"class" : "line"}, recursive = False).text.encode('utf-8')

		# Find previous and next station in tds based on their class names
		prev_next_stations = []
		for c in ["station_03", "station_02"]:
			station_td = tr.find('td', {"class" : c}, recursive = False)
			try:
				station_id = station_td.find('a')['href'].split("=")[1]
				station_name = station_td.text.encode('utf-8')
			except:
				station_id = None
				station_name = None
			prev_next_stations.append({'id' : station_id, 'name' : station_name})

		lines.append({
			'prev_station' : prev_next_stations[0],
			'line_name' : line,
			'next_station' : prev_next_stations[1]
		})

	return soup.find('h1').text, lines

unexplored_station_ids = ["5006"]
explored_stations = {}
stations = {}

while unexplored_station_ids:
	station_id = unexplored_station_ids.pop()
	try:
		name, lines = station(station_id)
		explored_stations[station_id] = name
		print name
	except Exception, e:
		print e
		print "While trying to get %s" % station_id

	for line in lines:
		ids = [line["prev_station"]["id"], line["next_station"]["id"]]
		print ids
		for i in ids:
			if i is None:
				continue

			if not i in explored_stations:
				unexplored_station_ids.append(i)

print explored_stations

# for s in station("5006"):
# 	if s["prev_station"]["id"] 

# 	stations 


# 	print s["prev_station"]["name"], s["line_name"], s["next_station"]["name"]

