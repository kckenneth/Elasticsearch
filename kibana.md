# Kibana

Kibana is a plugin for elasticsearch and make the querying much easier. 

# Installation of Kibana

<a href=https://www.elastic.co/guide/en/kibana/current/rpm.html>Installing Kibana in CentOS.</a>
```
# wget https://artifacts.elastic.co/downloads/kibana/kibana-6.4.3-x86_64.rpm
# sudo rpm --install kibana-6.4.3-x86_64.rpm
```

Check which system I run. 
```
# ps -p 1

  PID TTY          TIME CMD
    1 ?        00:00:03 systemd
```

# Change the Configuratino in kibana.yml

```
# vi /etc/kibana/kibana.yml

server.port: 5601
server.host: "169.54.131.136"
```
Uncomment both port and host. Change the host from `<localhost>` to `<169.54.131.136>`. 

# Launch Kibana

```
# /etc/init.d/kibana start
```

Go to the browser
```
169.54.131.136:5601
```
