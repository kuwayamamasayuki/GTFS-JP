#!/bin/sh

for GTFS in inputs/*.zip; do
  g=${GTFS#inputs/}
  h=${g%.zip}
  i=`echo $h | sed -e 's/[\(\) ]/_/g'`
  echo $i
  mkdir outputs/$i
  python ../../../feedvalidator.py --extension=extensions.GTFS-JP -l 1000 -m -n -o outputs/$i/$i.html "$GTFS" > outputs/$i/log.txt 2>&1
done
