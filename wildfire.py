import csv
import pan.wfapi


apikey = '<api key>'
# loop through all the hashes and put this into a List
with open("sample-hashes.txt", "r") as ins:
  rows = csv.reader(ins)
  L= []
  for hash in rows:
    print (hash[0])
    L.append(hash[0])

#make an API query to WF and do a bulk check
  WF = pan.wfapi.PanWFapi(api_key = apikey)
  WF.verdicts(hashes=L)
  print('hashes %s submitted' % L)

#print the xml response
  xml_response = WF.response_body
  print (xml_response)
