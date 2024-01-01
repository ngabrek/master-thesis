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
variant = 'gradual'

#the features in the Insects datasets are all continuous
nominal_features = None


#load balanced dataset based on the variant
balanced = {f'Insects_{variant}_bal': (Insects(variant=f'{variant}_balanced'), Insects(variant=f'{variant}_balanced').n_samples)}
#evaluate the balanced datasets on all combinations with the BOLE classifier and then write the results in a csv-file  
for i in range(1,250,50):
    balanced_bole = evaluation(balanced,nominal_attributes=nominal_features,nb=False,majclass=False,nochange=False,ht=False,seed=i)
    write_results_to_csv(f'results/{generator}/{variant}/{generator}_{variant}_bal_bole_{i}.csv', balanced_bole)  
    
#load imbalanced dataset based on the variant
imbalanced = {f'Insects_{variant}_imbal': (Insects(variant=f'{variant}_imbalanced'), Insects(variant=f'{variant}_imbalanced').n_samples)}
#evaluate the imbalanced datasets on all combinations with the BOLE classifier and then write the results in a csv-file  
for i in range(1,250,50):
    imbalanced_bole = evaluation(imbalanced,nominal_attributes=nominal_features,nb=False,majclass=False,nochange=False,ht=False,seed=i)
    write_results_to_csv(f'results/{generator}/{variant}/{generator}_{variant}_imbalanced_bole_{i}.csv', imbalanced_bole)