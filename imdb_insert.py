#!/usr/bin/python

import sys
import csv
from elasticsearch import Elasticsearch

# Creating es object class
es = Elasticsearch()

index='imdb'
doc_type='imdb_basic'

# to get the name of the file we're inserting into elasticsearch
fname = sys.argv[1]

with open(fname) as f:
    csvreader = csv.reader(f, delimiter='\t', quotechar='"')

    # extract headers
    # for python2, it's csvreader.next()
    # for python3, it's next(csvreader)
    headers = csvreader.next()

    # lowercase headers
    headers = [h.lower() for h in headers]

    count = 0
    for fields in csvreader:
        body = {}
        for i in range(len(fields)):
            body[headers[i]] = fields[i]
        result = es.index(index=index, doc_type=doc_type, id=body["tconst"], body=body)
        count += 1

	# break
        if (count == 10000):
            print("{} records inserted".format(count))
	
    print("{} records inserted".format(count))
