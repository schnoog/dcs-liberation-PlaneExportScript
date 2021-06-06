#!/usr/bin/bash

SP=`dirname $(realpath $0)`
cd "$SP"


EndOfPlanes="plane_map = {"

IFS="
"

ALLPlanes=$(grep class planes.py | grep PlaneType)
for Plane in $ALLPlanes
do
echo $Plane
done


