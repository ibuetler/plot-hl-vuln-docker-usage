# Plot HL usage
## Usage Script
```
#! /bin/bash

cd /opt/docker-manager/docker/config/tmp/

mydate=`date +%Y-%m-%d-%H-%M`

echo "================================================= `date`"
docker ps | egrep -v "timesketch|winattack|webattacker|docker-manager|traefik-error-page" > /home/hl/status/temp
cat /home/hl/status/temp | wc -l | awk -v gugus="$mydate" '{print "## "gugus,$1}'
cat /home/hl/status/temp 
cat docker-auslastung.log | egrep "##" | awk '{print $2,$3}'
```


