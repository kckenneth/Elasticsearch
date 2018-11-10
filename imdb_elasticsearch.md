# Making IMDB database in Elasticsearch

For inserting database into elasticsearch by python API, go <a href=https://elasticsearch-py.readthedocs.io/en/master/>here</a>. 

Using python API, we will update one of the IMDB publicly available in our elasticsearch. We will first download the IMDB zipped file in our virtual server. Since this is a tab separated file (`.tsv`) and huge, we will avoid open the file in one go, instead we will insert the database into elasticsearch on the fly one at a time. <a href=https://www.imdb.com/interfaces/>IMDB</a> `title.basics.tsv.gz` is used in this exercise. 

## Install Elasticsearch in Python
```
# pip install elasticsearch
# curl -O https://datasets.imdbws.com/title.basics.tsv.gz
# gunzip -k title.basics.tsv.gz
```
Make sure you use `-O` when you download the file. `-k` is to keep when decompressing the gunzipped file. 

## Python API script

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

	# to check regulary if the database is properly inserted
        if (count % 10000 == 0):
            print("{} records inserted".format(count))
	
    print("{} records inserted".format(count))
 ```
 
## Inserting IMDB into Elasticsearch !

Before you launch the python script, make sure you already launched the elasticsearch which will be listening at port `9200`. 

```
# chmod 755 imdb_insert.py
# python imdb_insert.py title.basics.tsv
10000 records inserted
20000 records inserted
...
...
650000 records inserted
```
It took minutes to insert all imdb basic database into elasticsearch. 

## Query 

### Query 1. Count the number of screens that come out in 1990

```
# curl -X GET 'http://localhost:9200/artist/_search?q=Carmencita
```

### Query 2. Count the number of screens that are 'short' 


### Query 3. Count the number of screens that plays at least an hour `total run times`


### Query 4. Histogram of the total run times over the years in screen production 


### Query 5. Count the type of screen genres





 
