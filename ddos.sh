#!/bin/bash

nb_bot="${1:-40}"

trap 'echo "Caught SIGINT, killing all subprocesses..."; kill 0' SIGINT

for ((i=1; i<=nb_bot; i++))
do
	echo "Starting Dos bot n°$i"
	./dos.sh &
done

wait
