# obtain data from http://download.geofabrik.de/asia/india-latest.osm.bz2

import xml.etree.ElementTree as etree
from string import punctuation

f=open('locations.txt','w')
a=0

for event, elem in etree.iterparse('india-latest.osm', events=('start', 'end', 'start-ns', 'end-ns')):
  
  x = elem.find('tag')
  
  if x != None and x.attrib['k'] == 'name':
    
    a=a+1
    if a&1:

      attrib = x.attrib['v']
      for j in punctuation:
        attrib = attrib.replace(j,'')

      attrib = attrib.strip()
      attrib = attrib.replace('  ','\n')
      attrib = attrib.replace(' ','\n')

      try:
        f.write(attrib+'\n')
        print attrib
      except:
        pass

f.close()
   



