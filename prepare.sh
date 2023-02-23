#!/bin/bash
if [ $# -eq 0 ]
then
	echo "missing argument: log file"
	exit
fi

echo "date,usage" > source-log
cat $1 | grep -E "##" | awk '{print $2","$3}' >> source-log


