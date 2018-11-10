|Title |  Elasticsearch  |
|-----------|----------------------------------|
|Author | Kenneth Chen |
|Utility | Elasticsearch, CentOS |
|Date | 11/10/2018 |

# Elasticsearch

# Setup Virtual Machine (VM)

We will create a virtual server with CentOS, CPU=2, RAM=4GB, disk=100GB
```
$ slcli vs create --datacenter=sjc01 --domain=brad.com --hostname=elasticsearch --os=CENTOS_LATEST_64 --cpu=2 --memory=4096 --billing=hourly --disk=100
```

# Elasticsearch Installation

For Elasticsearch information, go <a href=https://www.elastic.co/downloads/elasticsearch>here</a>. 

Since our server in CentOS, a command `yum` is used instead of `apt-get` in Ubuntu. After we launched our virtual server, ssh into using the password. Once you're in the server, update the CentOS and install JAVA. 

```
# yum install -y epel-release && yum install -y java-1.8.0-openjdk-headless net-tools jq
```

### Testing the JAVA if it's properly installed
```
# echo export JAVA_HOME=\"$(readlink -f $(which java) | grep -oP '.*(?=/bin)')\" >> /root/.bash_profile
# source /root/.bash_profile
# $JAVA_HOME/bin/java -version

openjdk version "1.8.0_191"
OpenJDK Runtime Environment (build 1.8.0_191-b12)
OpenJDK 64-Bit Server VM (build 25.191-b12, mixed mode)
```

### Download Elasticsearch tarball and extract it
```
# curl -OL https://download.elastic.co/elasticsearch/elasticsearch/elasticsearch-1.7.0.tar.gz
# tar xzf elasticsearch-1.7.0.tar.gz
```

#### >> New version 6.4.3 
After I tested with the version 1.7.0, there was a new version `6.4.3` released on November 6, 2018. So I tested a new version. 
```
# curl -OL https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.4.3.tar.gz
# tar xzf elasticsearch-6.4.3.tar.gz
```

# Elasticsearch execution

To execute elasticsearch, go to the elasticsearch bin folder, `nohup` is running the program and `&` is leaving it in the background even when you exit the terminal so that you can ping the server with its port from other terminal. 
```
# cd elasticsearch-1.7.0
# nohup ./bin/elasticsearch &
```
If you want to stop the elasticsearch, which I needed to stop the `1.7.0` from running and don't want the two elasticsearch clash at the port, 
```
# pkill -f elasticsearch
```
I tried other commands to stop the elasticsearch, nothing worked. 
```
# /etc/init.d/elasticsearch stop
# sudo service elasticsearch stop
# sudo systemctl stop elasticsearch.service
```
You can check `# netstat -tnlp` to confirm nothing is listening at port `9200`. From the result, you can also know the `<PID>` number. So you can also kill the program by 
```
# kill -9 <PID>
```

#### >> New version 6.4.3 [Not running 2018/11/10]
```
# cd elasticsearch-6.4.3
# nohup ./bin/elasticsearch &
```

This launch the elasticsearch in the background at port `9200`. You can check if the server is listening. You need to first open a new terminal. 
```
$ ssh root@169.54.131.136
# netstat -tnlp 

Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 127.0.0.1:25            0.0.0.0:*               LISTEN      1317/master         
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      1242/sshd           
tcp6       0      0 ::1:25                  :::*                    LISTEN      1317/master         
tcp6       0      0 :::9200                 :::*                    LISTEN      10598/java          
tcp6       0      0 :::9300                 :::*                    LISTEN      10598/java          
tcp6       0      0 :::22                   :::*                    LISTEN      1242/sshd   
```
So the elasticsearch program is up and running and listening at the port `9200`. So we're good to go. There are two ways to test the elasticsearch. You can go to your local brower (your laptop) or you can test from the virtual server you're now in. 

### 1. Check from the browser
```
169.54.131.136:9200
```
### 2. Check from the VM terminal
```
# curl -X GET http://localhost:9200
```
Both will generate 
```
{
  "status" : 200,
  "name" : "Speedball",
  "cluster_name" : "elasticsearch",
  "version" : {
    "number" : "1.7.0",
    "build_hash" : "929b9739cae115e73c346cb5f9a6f24ba735a743",
    "build_timestamp" : "2015-07-16T14:31:07Z",
    "build_snapshot" : false,
    "lucene_version" : "4.10.4"
  },
  "tagline" : "You Know, for Search"
}
```
# Query in elasticsearch
You can query in elasticsearch. 
```
# curl -X GET http://localhost:9200/_search?q=test

{"took":2,"timed_out":false,"_shards":{"total":0,"successful":0,"failed":0},"hits":{"total":0,"max_score":0.0,"hits":[]}}
```
Since we don't have the query word `test` in our database, it throws out the empty database. You can make it prettier output by `jq`. 

```
# curl -X GET http://localhost:9200/_search?q=test | jq -r '.'

  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   121  100   121    0     0  15500      0 --:--:-- --:--:-- --:--:-- 17285
{
  "took": 1,
  "timed_out": false,
  "_shards": {
    "total": 0,
    "successful": 0,
    "failed": 0
  },
  "hits": {
    "total": 0,
    "max_score": 0,
    "hits": []
  }
}
```
# Updating Elasticsearch database

We will not making IMDB database in elasticsearch for easy query in next step. 

Follow those steps in <a href=https://github.com/kckenneth/Elasticsearch/blob/master/imdb_elasticsearch.md>here</a>.




