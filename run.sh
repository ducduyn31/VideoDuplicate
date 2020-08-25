#!/bin/bash

outname=$(basename -- "$2")
extension="${outname##*.}"
outname="${outname%.*}"

for i in {1..5} ; do
    python duplicate.py -i $1 -o $outname-$i.$extension
done