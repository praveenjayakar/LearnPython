#!/bin/bash


servers=("server1" "server2" "server3")

echo $servers

for server in ${servers[@]};
do
	echo $server
done


enviromments=("dev" "sit" "replica" "prod")

for env in ${enviromments[@]};
do
	echo "deploying in: " $env
done

