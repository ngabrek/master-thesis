# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 13:09:37 2023

@author: nadin
"""

from river.datasets import Insects
from evaluation.evaluation import evaluation
from utils.read_and_write import write_results_to_csv
 
#adapt these variables according the dataset under evaluation
generator = 'insects'
variant = 'out-of-control'

#the features in the Insects datasets are all continuous
nominal_features = None


#load dataset based on the variant
dataset = {f'Insects_{variant}': (Insects(variant=f'{variant}'), Insects(variant=f'{variant}').n_samples)}
#evaluate the balanced datasets on naive baselines and all combinations with the Naive Bayes classifier and then write the results in a csv-file 
nb = evaluation(dataset,nominal_attributes=nominal_features,ht=False,bole=False)
write_results_to_csv(f'results/{generator}/{variant}/{generator}_{variant}_nb.csv', nb)
#evaluate the datasets on all combinations with the Hoeffding tree classifier and then write the results in a csv-file  
ht = evaluation(dataset,nominal_attributes=nominal_features,nb=False,majclass=False,nochange=False,bole=False)
write_results_to_csv(f'results/{generator}/{variant}/{generator}_{variant}_ht.csv', ht) 

