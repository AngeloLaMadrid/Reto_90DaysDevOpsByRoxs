#!/bin/bash

TABLA=5

for i in {1..10}; do
    RESULTADO=$((TABLA * i))
    echo "$TABLA x $i = $RESULTADO"
done
