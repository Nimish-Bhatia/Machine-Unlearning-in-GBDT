# # Specify the upper limit for random numbers
# limit=890  # Replace with your desired limit

# # Generate 80 random numbers between 0 and the specified limit
# seq 0 $((limit - 1)) | shuf -n 89 > unids_weather.txt

# echo "Random numbers generated and saved to unids.txt"


# ./abcboost_train -method robustlogit -data ./data/intel_image_80.train.csv -v 0.1 -J 20 -iter 10 -feature_split_sample_rate 0.1
# ./abcboost_unlearn -data ./data/intel_image_80.train.csv -model intel_image_80.train.csv_robustlogit_J20_v0.1.model -unlearning_ids_path unids_intel.txt
# ./abcboost_predict -data ./data/intel_image_80.test.csv -model intel_image_80.train.csv_robustlogit_J20_v0.1_unlearn.model

./abcboost_predict -data ./data/intel_image_80.test.csv -model intel_image_80.train.csv_robustlogit_J20_v0.1.model
