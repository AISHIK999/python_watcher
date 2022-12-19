#!/bin/bash

while true;do
    for i in {0..5};do      # Run 5 instances
        python3 main.py &
    done
    wait
done
