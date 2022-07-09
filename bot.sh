#!/bin/bash

startChromeBot(){
    nestedFunction(){
        python3 main.py
        MY_PID=$!
        sleep 60m           # Run each instance for 60 mins
        kill -KILL $MY_PID
    }
    while true;do
        nestedFunction
    done
}

while true;do
    for i in {0..5};do      # Run 5 instances
        startChromeBot &
    done
    wait
done
