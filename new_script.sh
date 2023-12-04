# ./abcboost_train -method robustlogit -data ./data/Train_coffee.csv -v 0.1 -J 20 -iter 5 -feature_split_sample_rate 0.1
./abcboost_unlearn -data ./data/Train_coffee.csv -model Train_coffee.csv_robustlogit_J20_v0.1.model -unlearning_ids_path unids.txt
./abcboost_predict -data ./data/test_coffee.csv -model Train_coffee.csv_robustlogit_J20_v0.1.model
./abcboost_predict -data ./data/test_coffee.csv -model Train_coffee.csv_robustlogit_J20_v0.1_unlearn.model
