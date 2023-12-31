# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 13:13:33 2023

@author: nadin
"""

from datasets.mixed import get_mixed_datasets
from evaluation.evaluation import evaluation
from utils.read_and_write import write_results_to_csv
 
#adapt these variables according the dataset under evaluation
generator = 'mixed'
size = 100_000

#get the size_name for the name of the dataset
if size == 1_000_000: size_name ='1M'
else: size_name = str(size//1000) + 'K'

#generate the abrupt datasets, needs adaption different generator!
abrupt, nominal_features = get_mixed_datasets(size)

#evaluate the abrupt datasets on all combinations with the BOLE classifier but BOCD and then write the results in a csv-file  
i = 1
abrupt_bole = evaluation(abrupt,nominal_attributes=nominal_features,nb=False,majclass=False,nochange=False,ht=False,bocd=False,seed=i)
write_results_to_csv(f'results/{generator}/{size_name}/{generator}_{size_name}_abrupt_bole_{i}.csv', abrupt_bole) 

