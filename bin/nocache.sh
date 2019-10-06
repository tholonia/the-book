#!/bin/bash

sudo pkill nocache.sh

while :
do
   echo 1 > /proc/sys/vm/drop_caches
   sleep 1
done
