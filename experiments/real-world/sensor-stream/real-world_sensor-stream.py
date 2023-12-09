# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 13:09:37 2023

@author: nadin
"""

from datasets.real_world import SensorStream
from evaluation.evaluation import evaluation
from utils.read_and_write import write_results_to_csv
 
#adapt these variables according the dataset under evaluation
generator = 'real-world'
variant = 'sensor-stream'

#the features in the Insects datasets are all continuous
nominal_features = None

#load the dataset
dataset ={'SensorStream': (SensorStream(), SensorStream().n_samples)}

#evaluate the dataset on naive baselines and all combinations with the Naive Bayes classifier and then write the results in a csv-file 
nb = evaluation(dataset,nominal_attributes=nominal_features,ht=False,bole=False)
write_results_to_csv(f'results/{generator}/{variant}/{generator}_{variant}_nb.csv', nb)



