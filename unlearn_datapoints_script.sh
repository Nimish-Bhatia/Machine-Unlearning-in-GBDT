# Specify the upper limit for random numbers
limit=1200  # Replace with your desired limit

# Generate 80 random numbers between 0 and the specified limit
seq 0 $((limit - 1)) | shuf -n 24 > unids_coffee.txt
limit=428
seq 0 $((limit - 1)) | shuf -n 9 > unids_dog.txt
limit=3540
seq 0 $((limit - 1)) | shuf -n 71 > unids_flower.txt
limit=14034
seq 0 $((limit - 1)) | shuf -n 281 > unids_intel.txt
limit=468
seq 0 $((limit - 1)) | shuf -n 10 > unids_vehicle.txt
echo "Random numbers generated "
