#!/bin/bash


while 
	kubectl get deploy web1 | grep -q 2/2 ;
do
	echo "waiting to deployment to ready....."
	sleep 10
done


