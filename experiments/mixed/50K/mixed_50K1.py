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
size = 50_000

#get the size_name for the name of the dataset
if size == 1_000_000: size_name ='1M'
else: size_name = str(size//1000) + 'K'

#generate the gradual datasets, needs adaption different generator!
gradual, nominal_features = get_mixed_datasets(size, gradual=True)
#evaluate the gradual datasets on naive baselines and all combinations with the Naive Bayes classifier and then write the results in a csv-file
gradual_nb = evaluation(gradual,nominal_attributes=nominal_features,ht=False,bole=False)
write_results_to_csv(f'results/{generator}/{size_name}/{generator}_{size_name}_gradual_nb.csv', gradual_nb) 
#evaluate the gradual datasets on all combinations with the Hoeffding tree classifier and then write the results in a csv-file
gradual_ht = evaluation(gradual,nominal_attributes=nominal_features,nb=False,majclass=False,nochange=False,bole=False)
write_results_to_csv(f'results/{generator}/{size_name}/{generator}_{size_name}_gradual_ht.csv', gradual_ht) 

