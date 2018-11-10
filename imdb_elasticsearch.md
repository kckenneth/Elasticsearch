# Making IMDB database in Elasticsearch

For inserting database into elasticsearch by python API, go <a href=https://elasticsearch-py.readthedocs.io/en/master/>here</a>. 

Using python API, we will update one of the IMDB publicly available in our elasticsearch. We will first download the IMDB tarbar in our virtual server. Since this is a tab separated file (`.tsv`) and huge, we will avoid open the file in one go, instead we will insert the database into elasticsearch on the fly one at a time. <a href=https://www.imdb.com/interfaces/>IMDB</a> `title.basics.tsv.gz` is used in this exercise. 

## 1. Install Elasticsearch in Python
```
# pip install elasticsearch
```

## 2. Python API script

```
# vi imdb_insert.py
```
Copy and paste the following script

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
 
 
