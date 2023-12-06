#!/bin/bash

# Specify the upper limit for random numbers
limit=1000  # Replace with your desired limit

# Generate 100 random numbers between 0 and the specified limit
seq 0 $((limit - 1)) | shuf -n 100 > unids.txt

echo "Random numbers generated and saved to unids.txt"
