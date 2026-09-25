#!/bin/sh
# Statistics.

for j in $(seq 1 12)
do
  for i in $(seq 1 30)
  do
    t=$(./bin/run.sh $i $j)
    echo "$i,$j,$t"
  done
done
