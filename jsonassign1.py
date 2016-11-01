import json
import urllib

address = raw_input('Enter location: ')

print 'Retrieving', address
uh = urllib.urlopen(address)
data = uh.read()
print 'Retrieved',len(data),'characters'

info = json.loads(data)

print 'Count:', len(info["comments"])
print 'Sum:', sum ([int(item["count"]) for item in info["comments"]])

