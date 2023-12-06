#!/bin/bash

# # Specify the upper limit for random numbers
# limit=1000  # Replace with your desired limit

# # Generate 100 random numbers between 0 and the specified limit
# seq 0 $((limit - 1)) | shuf -n 100 > unids.txt

# echo "Random numbers generated and saved to unids.txt"


# ./abcboost_train -method robustlogit -data ./data/intel_image.train.csv -v 0.1 -J 20 -iter 100 -feature_split_sample_rate 0.1
# ./abcboost_unlearn -data ./data/intel_image.train.csv -model intel_image.train.csv_robustlogit_J20_v0.1.model -unlearning_ids_path unids.txt
# ./abcboost_predict -data ./data/intel_image.test.csv -model intel_image.train.csv_robustlogit_J20_v0.1_unlearn.model

./abcboost_predict -data ./data/intel_image.test.csv -model intel_image.train.csv_robustlogit_J20_v0.1.model
