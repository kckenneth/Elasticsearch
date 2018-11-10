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
5380000 records inserted
5390000 records inserted
5394864 records inserted
```
It took an hour and half to insert all imdb basic database (5.4 millions records) into elasticsearch. 

## Query 
Sample query on `Carmencita` movie name. 

```
# curl -X GET 'http://localhost:9200/artist/_search?q=Carmencita
```
Output
```
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1979  100  1979    0     0   158k      0 --:--:-- --:--:-- --:--:--  175k
{
  "took": 6,
  "timed_out": false,
  "_shards": {
    "total": 5,
    "successful": 5,
    "failed": 0
  },
  "hits": {
    "total": 6,
    "max_score": 6.274984,
    "hits": [
      {
        "_index": "imdb",
        "_type": "imdb_basic",
        "_id": "tt0453643",
        "_score": 6.274984,
        "_source": {
          "genres": "Short",
          "tconst": "tt0453643",
          "startyear": "1897",
          "runtimeminutes": "\\N",
          "originaltitle": "Carmencita",
          "endyear": "\\N",
          "primarytitle": "Carmencita",
          "titletype": "short",
          "isadult": "0"
        }
      },
      {
        "_index": "imdb",
        "_type": "imdb_basic",
        "_id": "tt0000001",
        "_score": 6.095662,
        "_source": {
          "genres": "Documentary,Short",
          "tconst": "tt0000001",
          "startyear": "1894",
          "runtimeminutes": "1",
          "originaltitle": "Carmencita",
          "endyear": "\\N",
          "primarytitle": "Carmencita",
          "titletype": "short",
          "isadult": "0"
        }
      },
      {
        "_index": "imdb",
        "_type": "imdb_basic",
        "_id": "tt0764727",
        "_score": 4.8765297,
        "_source": {
          "genres": "Comedy,Musical,Romance",
          "tconst": "tt0764727",
          "startyear": "1948",
          "runtimeminutes": "\\N",
          "originaltitle": "Carmencita mia",
          "endyear": "\\N",
          "primarytitle": "Carmencita mia",
          "titletype": "movie",
          "isadult": "0"
        }
      },
      {
        "_index": "imdb",
        "_type": "imdb_basic",
        "_id": "tt0372198",
        "_score": 4.2669353,
        "_source": {
          "genres": "Short",
          "tconst": "tt0372198",
          "startyear": "1999",
          "runtimeminutes": "5",
          "originaltitle": "Carmencita, esta noche vas a ver",
          "endyear": "\\N",
          "primarytitle": "Carmencita, esta noche vas a ver",
          "titletype": "short",
          "isadult": "0"
        }
      },
      {
        "_index": "imdb",
        "_type": "imdb_basic",
        "_id": "tt7200526",
        "_score": 4.2669353,
        "_source": {
          "genres": "Comedy,Drama,Romance",
          "tconst": "tt7200526",
          "startyear": "2017",
          "runtimeminutes": "\\N",
          "originaltitle": "El cumpleaños de Carmencita",
          "endyear": "\\N",
          "primarytitle": "El cumpleaños de Carmencita",
          "titletype": "tvEpisode",
          "isadult": "0"
        }
      },
      {
        "_index": "imdb",
        "_type": "imdb_basic",
        "_id": "tt7200522",
        "_score": 3.764848,
        "_source": {
          "genres": "Comedy,Drama,Romance",
          "tconst": "tt7200522",
          "startyear": "2017",
          "runtimeminutes": "\\N",
          "originaltitle": "Una noche muy especial para Carmencita",
          "endyear": "\\N",
          "primarytitle": "Una noche muy especial para Carmencita",
          "titletype": "tvEpisode",
          "isadult": "0"
        }
      }
    ]
  }
}
```

There are total 6 hits for `Carmencita` query. 

### Query 1. Count the number of screens that come out in 1990

```
#  curl -X GET 'http://localhost:9200/_search?q=1990' | jq -r '.'

  "hits": {
    "total": 39028,
    "max_score": 3.2078505,
    "hits": [
      {
    ...
    ...
```
There are `39,028` screens in year 1990. Since this is an international movie database and this particular database has all kinds of screens; short, documentary, movie, film, play, so it makes sense. We can also shorten our output by directly targeting the `total` in our jq query. 

```
# curl -X GET 'http://localhost:9200/_search?q=1990' | jq -C '.hits.total'

39028
```
### Query 2. Count the number of screens that are 'short' 
```
# # curl -X GET 'http://localhost:9200/_search?q=1990' | jq -C '.hits.total'

784902
```
Total short screens has `784,902` out of 5.4 million records. 

### Query 3. Count the screen genre: Comedy
```
# curl -X GET 'http://localhost:9200/_search?q=comedy' | jq '.hits.total'

1172415
```
There are `1,172,415` comedy screens. 

### Query 4. Count the number of screens that plays between 1990 and 2000.
```
# curl -X GET 'http://localhost:9200/_search?q=startyear:\[1990+TO+2000\]&pretty'

  "hits" : {
    "total" : 600744,
    "max_score" : 1.0,
    "hits" : [ {
```
There are `600,744` screens in 10 years between 1990 and 2000. 

### Query 5. Histogram of the total run times over the years in screen production 

```
# curl -X GET 'http://localhost:9200/_search?q=runtimeminutes:\[1+TO+5\]&pretty'

  "hits" : {
    "total" : 1091410,
    "max_score" : 1.0,
    "hits" : [ {
```
Over 1 million screens runs between 1 minute to 5 minutes. 











 
