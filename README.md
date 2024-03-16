# Problem Statement
The problem at hand involves unlearning in multiclass image classification, specifically within datasets where each folder corresponds to a distinct class. The objective is to develop an unlearning methodology that allows the removal of specific classes from the model without necessitating a complete retraining of the entire dataset. This unlearning process should be tailored to multiclass scenarios, addressing challenges such as the removal of class-specific information, maintaining model performance on retained classes, and achieving adaptability to evolving dataset requirements. The goal is to design an efficient and effective unlearning framework that enhances the model's versatility and responsiveness in multiclass classification scenarios without the need for extensive retraining.

# Unlearning

The implementation for paper [Machine Unlearning in Gradient Boosting Decision Trees](https://dl.acm.org/doi/10.1145/3580305.3599420) (Accepted on KDD 2023).
Unlearning support training, unlearning and tuning. This implementation base on the toolkit of [ABCBoost](https://github.com/pltrees/abcboost).

## Quick Start
### Installation guide
Run the following commands to build ABCBoost from source:
```
git clone https://github.com/huawei-lin/Unlearning.git
cd Unlearning
mkdir build
cd build
cmake ..
make -j
cd ..
```
This will create three executables (`abcboost_train`, `abcboost_predict`, `abcboost_unlearn`, and `abcboost_clean`) in the `abcboost` directory.
`abcboost_train` is the executable to train models.
`abcboost_predict` is the executable to validate and inference using trained models.
`abcboost_unlearn` is the executable to unlearn a given collection of training data from a trained model.
`abcboost_clean` is the executable to clean csv data.

### Datasets 

Two datasets are provided under `data/` folder: [pendigits](https://archive.ics.uci.edu/dataset/81/pen+based+recognition+of+handwritten+digits) and [optdigits](https://archive.ics.uci.edu/dataset/80/optical+recognition+of+handwritten+digits).

### Training
We support both `Robust LogitBoost` and `MART`. Because `Robust LogitBoost` uses second-order information to compute the gain for tree plits, it often improves `MART`. Users can replace `robustlogit` by `mart` to test different algorithms. 
```
./abcboost_train -method robustlogit -data ./data/optdigits.train.csv -v 0.1 -J 20 -iter 100 -feature_split_sample_rate 0.1
```
This command will generate `optdigits.train.csv_robustlogit_J20_v0.1.model` that used for the following unlearning or tuning.

### Unlearning
Here we would like to unlearn (delect) the 9-th data sample from the `optdigits.train.csv_robustlogit_J20_v0.1.model`.
Please note that it need to load the original data of the model.
```
echo 9 > unids.txt # Unlearn 9-th data sample
./abcboost_unlearn -data ./data/optdigits.train.csv -model optdigits.train.csv_robustlogit_J20_v0.1.model -unlearning_ids_path unids.txt
```

### Predicting
Here we would like to evaluate these three models in `./data/optdigits.test.csv`.
```
./abcboost_predict -data ./data/optdigits.test.csv -model optdigits.train.csv_robustlogit_J20_v0.1.model
./abcboost_predict -data ./data/optdigits.test.csv -model optdigits.train.csv_robustlogit_J20_v0.1_unlearn.model
```
### Plots
Here we have plotted the error v/s iterations plot for both the original as well as the unlearned model for all datasets:

![alt text](https://github.com/Prateek692/Unlearning/blob/main/graph_coffee_bean.png?raw=true)

![alt text](https://github.com/Prateek692/Unlearning/blob/main/graph_dog.png?raw=true)

![alt text](https://github.com/Prateek692/Unlearning/blob/main/graph_flower.png?raw=true)

![alt text](https://github.com/Prateek692/Unlearning/blob/main/graph_intel.png?raw=true)

![alt text](https://github.com/Prateek692/Unlearning/blob/main/graph_vehicle.png?raw=true)

## More Configuration Options:
#### Data related:
* `-data_min_bin_size` minimum size of the bin
* `-data_max_n_bins` max number of bins (default 1000)
* `-data_path, -data` path to train/test data
#### Tree related:
* `-tree_max_n_leaves`, `-J` (default 20)
* `-tree_min_node_size` (default 10)
* `-tree_n_random_layers` (default 0)
* `-feature_split_sample_rate` (default 1.0)
#### Model related:
* `-model_data_sample_rate` (default 1.0)
* `-model_feature_sample_rate` (default 1.0)
* `-model_shrinkage`, `-shrinkage`, `-v`, the learning rate (default 0.1)
* `-model_n_iterations`, `-iter` (default 1000)
* `-model_n_classes` (default 0) the max number of classes allowed in this model (>= the number of classes on current dataset, 0 indicates do not set a specific class number)
* `-model_name`, `-method` regression/lambdarank/mart/abcmart/robustlogit/abcrobustlogit (default robustlogit)
#### Unlearning related:
* `-unlearning_ids_path` path to unlearning indices
* `-lazy_update_freq` (default 1)
#### Parallelism:
* `-n_threads`, `-threads` (default 1)
#### Other:
* `-save_log`, 0/1 (default 0) whether save the runtime log to file
* `-save_model`, 0/1 (default 1)
* `-save_prob`, 0/1 (default 0) whether save the prediction probability for classification tasks
* `-save_importance`, 0/1 (default 0) whether save the feature importance in the training


## References

```
@inproceedings{DBLP:conf/kdd/LinCL023,
  author       = {Huawei Lin and
                  Jun Woo Chung and
                  Yingjie Lao and
                  Weijie Zhao},
  title        = {Machine Unlearning in Gradient Boosting Decision Trees},
  booktitle    = {Proceedings of the 29th {ACM} {SIGKDD} Conference on Knowledge Discovery
                  and Data Mining, {KDD}},
  address      = {Long Beach, CA},
  pages        = {1374--1383},
  year         = {2023}
}
```
```
@article{DBLP:journals/corr/abs-2207-08770,
  author    = {Ping Li and
               Weijie Zhao},
  title     = {Package for Fast ABC-Boost},
  journal   = {CoRR},
  volume    = {abs/2207.08770},
  year      = {2022}
}
```


## Copyright and License
Apache-2.0 license.
