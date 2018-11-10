# Query

This is using the elasticsearch for IMDB database query over 5.3 million screen records. Please go to your web browser and query since I have elasticsearch running in the background. You don't need to ssh into the server to do the query. 

1. <a href=https://github.com/kckenneth/Elasticsearch/blob/master/README.md>Setting up Elasticsearch</a> 
2. <a href=https://github.com/kckenneth/Elasticsearch/blob/master/imdb_elasticsearch.md>Creating IMDB database in elasticsearch</a> 
3. <a href=https://github.com/kckenneth/Elasticsearch/blob/master/kibana.md>Kibana plugin</a> 
4. <a href=https://github.com/kckenneth/Elasticsearch/blob/master/execution.md>Query in elasticsearch database</a>

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
http://169.54.131.136:9200/_search?q=comedy&pretty
```
There are `1,172,415` comedy screens. 

### Query 4. Count the number of screens that plays between 1990 and 2000.
```
http://169.54.131.136:9200/_search?q=startyear:\[1990+TO+2000\]&pretty
```
There are `209,384` screens in 10 years between 1990 and 2000. 

### Query 5. Histogram of the total run times over the years in screen production 

```
http://169.54.131.136:9200/_search?q=runtimeminutes:\[1+TO+5\]&pretty
```
There are `174,832` screens that runs between 1 and 5 minutes. 

# Note
I tried to install `Kibana` plugins. The setup is detailed <a href=https://github.com/kckenneth/Elasticsearch/blob/master/kibana.md>here</a>. However after succefully running Kibana at the default port `5601`, it asked me to update elasticsearch. So I installed the latest version `6.4.3`. But the latest elasticsearch version did not run. I tried in both CentOS and Ubuntu virtual servers. They both fail to run the elasticsearch 6.4.3 version. There was no discussion on the version because it was released very recently on November 6, 2018. So I stopped installing the plugins. 
