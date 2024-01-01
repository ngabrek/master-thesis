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
size = 100_000

#get the size_name for the name of the dataset
if size == 1_000_000: size_name ='1M'
else: size_name = str(size//1000) + 'K'

#generate the abrupt datasets, needs adaption different generator!
abrupt, nominal_features = get_stagger_datasets(size)
#evaluate the abrupt datasets on naive baselines and all combinations with the Naive Bayes classifier but the BOCD detector and then write the results in a csv-file 
abrupt_nb = evaluation(abrupt,nominal_attributes=nominal_features,ht=False,bole=False,bocd=False)
write_results_to_csv(f'results/{generator}/{size_name}/{generator}_{size_name}_abrupt_nb.csv', abrupt_nb)


#generate the gradual datasets, needs adaption different generator!
gradual, nominal_features = get_stagger_datasets(size, gradual=True)
#evaluate the gradual datasets on naive baselines and all combinations with the Naive Bayes classifier but the BOCD detector and then write the results in a csv-file
gradual_nb = evaluation(gradual,nominal_attributes=nominal_features,ht=False,bole=False,bocd=False)
write_results_to_csv(f'results/{generator}/{size_name}/{generator}_{size_name}_gradual_nb.csv', gradual_nb) 

