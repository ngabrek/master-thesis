# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 13:09:37 2023

@author: nadin
"""

from river.datasets import Elec2
from evaluation.evaluation import evaluation
from utils.read_and_write import write_results_to_csv
 
#adapt these variables according the dataset under evaluation
generator = 'real-world'
variant = 'electricity'

#the features in the Insects datasets are all continuous
nominal_features = ['day']

#load the dataset
dataset = {'Elec2': (Elec2(), Elec2().n_samples)}

#evaluate the dataset on naive baselines and all combinations with the Naive Bayes classifier and then write the results in a csv-file 
nb = evaluation(dataset,nominal_attributes=nominal_features,ht=False,bole=False)
write_results_to_csv(f'results/{generator}/{variant}/{generator}_{variant}_nb.csv', nb)

#evaluate the dataset on all combinations with the Hoeffding tree classifier and then write the results in a csv-file  
ht = evaluation(dataset,nominal_attributes=nominal_features,nb=False,majclass=False,nochange=False,bole=False)
write_results_to_csv(f'results/{generator}/{variant}/{generator}_{variant}_ht.csv', ht) 

#evaluate the dataset on all combinations with the BOLE classifier and then write the results in a csv-file  
for i in range(1,250,50):
    bole = evaluation(dataset,nominal_attributes=nominal_features,nb=False,majclass=False,nochange=False,ht=False,seed=i)
    write_results_to_csv(f'results/{generator}/{variant}/{generator}_{variant}_bole_{i}.csv', bole) 



