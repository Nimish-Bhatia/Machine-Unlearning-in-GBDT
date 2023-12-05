# ./abcboost_train -method mart -data ./data/intel_image.train.csv -v 0.1 -J 20 -iter 80 -feature_split_sample_rate 0.1
./abcboost_unlearn -data ./data/intel_image.train.csv -model intel_image.train.csv_mart_J20_v0.1.model -unlearning_ids_path unids.txt
./abcboost_predict -data ./data/intel_image.test.csv -model intel_image.train.csv_mart_J20_v0.1.model
./abcboost_predict -data ./data/intel_image.test.csv -model intel_image.train.csv_mart_J20_v0.1_unlearn.model
