# Making IMDB database in Elasticsearch

```
#!/usr/bin/python

import os
import sys
import csv
from elasticsearch import Elasticsearch

# by default we connect to localhost:9200
es = Elasticsearch()

index='voters'
doc_type='voter'

fname = sys.argv[1]

with open(fname) as f:
    csvreader = csv.reader(f, delimiter='\t', quotechar='"')

	# extract headers
    headers = next(csvreader)

	# lowercase headers
    headers = [h.lower() for h in headers]

    id = 0
    for fields in csvreader:
        body = {}
        for i in range(len(fields)):
            body[headers[i]] = fields[i]
            print("This is headers {}".format(headers[i]))
            print("This is fields {}".format(fields[i]))
            print("This is an entire body {}".format(body))
		result = es.index(index=index, doc_type=doc_type, id=body["voter_id"], body=body)
        id += 1
		# print result

		# break
        if (id % 10000 == 0):
            print("{} records inserted".format(id))
	
    print("{} records inserted".format(id))
 ```
 
 
