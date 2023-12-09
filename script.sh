# mkdir build
# cd build
# cmake -DOMP=ON -DNATIVE=ON .. 
# make
# cd ..

# ./abcboost_train -method robustlogit -data ./data/intel_image_80.train.csv -v 0.1 -J 20 -iter 210 -feature_split_sample_rate 0.1
# ./abcboost_unlearn -data ./data/intel_image_80.train.csv -model intel_image_80.train.csv_robustlogit_J20_v0.1.model -unlearning_ids_path unids_intel.txt
# ./abcboost_predict -data ./data/intel_image_80.test.csv -model intel_image_80.train.csv_robustlogit_J20_v0.1_unlearn.model

./abcboost_predict -data ./data/intel_image_80.test.csv -model intel_image_80.train.csv_robustlogit_J20_v0.1.model
