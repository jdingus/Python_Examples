from collections import OrderedDict
import json
import pprint # used to print unicode files

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

# """Another option to use is the PrettyPrinter class"""
# pp = pprint.PrettyPrinter(indent=4)  #create instance of class first to use
# pp.pprint(json_data)

# print "\n"
# print "-----" * 4
# print "\n"

# All uls
with open('data.json') as json_file:
	json_data = json.load(json_file)

#print len(json_data[0]['trends']) # 'trends' is a list of dicts print # entries

def 
	for data in json_data:
		i=1
		for value in json_data[0]['trends']:
			# pp.pprint(value["name"] + " : " + value["url"] )
			name_tweet =  value["name"].encode('utf-8')
			url_tweet = value['url'].encode('utf-8')
			print 'This is the {} entry in the list.'.format('#'+str(i))
			print 'The name of the tweet is : {}'.format(name_tweet)
			print 'The url is : {}'.format(url_tweet)
			print '\n'
			print '------' *4
			i+=1
"""
1. Start with entire JSON object
2. Since it's wrapped in a list, iterate through it with a for loop
3. Next, work your way to the inner key ('trends') that contains the url
4. Loop through the values and output the 'url'
"""