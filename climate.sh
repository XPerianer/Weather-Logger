#!/bin/sh

t1=$(date +%s)
t1=$(($t1 + 30)) 
/usr/bin/python /root/climate.py
t2=$(date +%s)
sleep_seconds=$(($t1-$t2))
echo $sleep_seconds
sleep $sleep_seconds
/usr/bin/python /root/climate.py
