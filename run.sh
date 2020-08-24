#!/bin/bash

for i in {1..500} ; do
    python duplicate.py -i $1 -o \"$i-$2\"
done