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
```

### Download Elasticsearch tarball and extract it
```
# curl -OL https://download.elastic.co/elasticsearch/elasticsearch/elasticsearch-1.7.0.tar.gz
# tar xzf elasticsearch-1.7.0.tar.gz
```
# Elasticsearch execution



