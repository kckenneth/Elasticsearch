# Query

This is using the elasticsearch for IMDB database query over 5.3 million screen records. Please go to your web browser and query since I have elasticsearch running in the background. You don't need to ssh into the server to do the query. 

### Query 1. Count the number of screens that come out in 1990
```
http://169.54.131.136:9200/_search?q=1990&pretty
```
There are `39,028` screens in year 1990. 

### Query 2. Count the number of screens that are 'short' 
```
http://169.54.131.136:9200/_search?q=short&pretty
```
There are `784,902` screens that fall into `short` genre out of 5.4 million records. 

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
