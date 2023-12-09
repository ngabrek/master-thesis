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
variant = 'incremental-abrupt'

#the features in the Insects datasets are all continuous
nominal_features = None


#load balanced dataset based on the variant
balanced = {f'Insects_{variant}_bal': (Insects(variant=f'{variant}_balanced'), Insects(variant=f'{variant}_balanced').n_samples)}
#evaluate the balanced datasets on naive baselines and all combinations with the Naive Bayes classifier and then write the results in a csv-file 
balanced_nb = evaluation(balanced,nominal_attributes=nominal_features,ht=False,bole=False)
write_results_to_csv(f'results/{generator}/{variant}/{generator}_{variant}_bal_nb.csv', balanced_nb)
#evaluate the balanced datasets on all combinations with the Hoeffding tree classifier and then write the results in a csv-file  
balanced_ht = evaluation(balanced,nominal_attributes=nominal_features,nb=False,majclass=False,nochange=False,bole=False)
write_results_to_csv(f'results/{generator}/{variant}/{generator}_{variant}_bal_ht.csv', balanced_ht) 

#load imbalanced dataset based on the variant
imbalanced = {f'Insects_{variant}_imbal': (Insects(variant=f'{variant}_imbalanced'), Insects(variant=f'{variant}_imbalanced').n_samples)}
#evaluate the imbalance datasets on naive baselines and all combinations with the Naive Bayes classifier and then write the results in a csv-file 
imbalanced_nb = evaluation(imbalanced,nominal_attributes=nominal_features,ht=False,bole=False)
write_results_to_csv(f'results/{generator}/{variant}/{generator}_{variant}_imbal_nb.csv', imbalanced_nb)
#evaluate the imbalanced datasets on all combinations with the Hoeffding tree classifier and then write the results in a csv-file  
imbalanced_ht = evaluation(imbalanced,nominal_attributes=nominal_features,nb=False,majclass=False,nochange=False,bole=False)
write_results_to_csv(f'results/{generator}/{variant}/{generator}_{variant}_imbal_ht.csv', imbalanced_ht) 