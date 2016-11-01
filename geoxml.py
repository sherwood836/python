import urllib
import xml.etree.ElementTree as ET

address = raw_input('Enter location: ')

print 'Retrieving', address
uh = urllib.urlopen(address)
data = uh.read()
print 'Retrieved',len(data),'characters'

tree = ET.fromstring(data)


results = tree.findall('.//count')

print 'Count:', len(results)
print 'Sum:', sum([int(count.text) for count in results])


