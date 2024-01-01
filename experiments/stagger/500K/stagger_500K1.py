# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 13:13:33 2023

@author: nadin
"""

from datasets.stagger import get_stagger_datasets
from evaluation.evaluation import evaluation
from utils.read_and_write import write_results_to_csv
 
#adapt these variables according the dataset under evaluation
generator = 'stagger'
size = 500_000

#get the size_name for the name of the dataset
if size == 1_000_000: size_name ='1M'
else: size_name = str(size//1000) + 'K'

#generate the abrupt datasets, needs adaption different generator!
abrupt, nominal_features = get_stagger_datasets(size)

#evaluate the abrupt datasets on all combinations with the Hoeffding tree classifier and then write the results in a csv-file  
abrupt_ht = evaluation(abrupt,nominal_attributes=nominal_features,nb=False,majclass=False,nochange=False,bole=False)
write_results_to_csv(f'results/{generator}/{size_name}/{generator}_{size_name}_abrupt_ht.csv', abrupt_ht) 



