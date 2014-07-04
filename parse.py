from collections import OrderedDict
import json

# Nice way to visualize data
with open('data.json') as json_file:
	json_data = json.load(json_file, object_pairs_hook=OrderedDict)

	print json.dumps(json_data, indent=2)

print "\n"
print "-----" * 4
print "\n"

# Single urls
with open('data.json') as json_file:
	json_data = json.load(json_file)

	for data in json_data:
		print json_data[0]['trends'][0]['url']

print "\n"
print "-----" * 4
print "\n"

# All uls
with open('data.json') as json_file:
	json_data = json.load(json_file)

	for data in json_data:
		for value in json_data[0]['trends']:
			print value['url']


print "\n"
print "-----" * 4
print "\n"