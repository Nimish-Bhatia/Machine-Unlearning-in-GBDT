mkdir build
cd build
cmake -DOMP=ON -DNATIVE=ON .. 
make
cd ..
# Training
./abcboost_train -method robustlogit -data ./data/optdigits.train.csv -v 0.1 -J 20 -iter 100 -feature_split_sample_rate 0.1
./abcboost_train -method mart -data ./data/optdigits.train.csv -v 0.1 -J 20 -iter 100 -feature_split_sample_rate 0.1
# Unlearning
echo 9 > unids.txt # Unlearn 9-th data sample
./abcboost_unlearn -data ./data/optdigits.train.csv -model optdigits.train.csv_robustlogit_J20_v0.1.model -unlearning_ids_path unids.txt
./abcboost_unlearn -data ./data/optdigits.train.csv -model optdigits.train.csv_mart_J20_v0.1.model -unlearning_ids_path unids.txt
#Prediction
./abcboost_predict -data ./data/optdigits.test.csv -model optdigits.train.csv_robustlogit_J20_v0.1.model
./abcboost_predict -data ./data/optdigits.test.csv -model optdigits.train.csv_robustlogit_J20_v0.1_unlearn.model
./abcboost_predict -data ./data/optdigits.test.csv -model optdigits.train.csv_mart_J20_v0.1.model
./abcboost_predict -data ./data/optdigits.test.csv -model optdigits.train.csv_mart_J20_v0.1_unlearn.model
python graph.py