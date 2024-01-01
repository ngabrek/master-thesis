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
size = 10_000

#get the size_name for the name of the dataset
if size == 1_000_000: size_name ='1M'
else: size_name = str(size//1000) + 'K'

#generate the abrupt datasets, needs adaption different generator!
abrupt, nominal_features = get_stagger_datasets(size)
#evaluate the abrupt datasets on naive baselines and all combinations with the Naive Bayes classifier and then write the results in a csv-file 
abrupt_nb = evaluation(abrupt,nominal_attributes=nominal_features,ht=False,bole=False)
write_results_to_csv(f'results/{generator}/{size_name}/{generator}_{size_name}_abrupt_nb.csv', abrupt_nb)
#evaluate the abrupt datasets on all combinations with the Hoeffding tree classifier and then write the results in a csv-file  
abrupt_ht = evaluation(abrupt,nominal_attributes=nominal_features,nb=False,majclass=False,nochange=False,bole=False)
write_results_to_csv(f'results/{generator}/{size_name}/{generator}_{size_name}_abrupt_ht.csv', abrupt_ht) 
#evaluate the abrupt datasets on all combinations with the BOLE classifier and then write the results in a csv-file  
#for i in range(1,250,50):
#    abrupt_bole = evaluation(abrupt,nominal_attributes=nominal_features,nb=False,majclass=False,nochange=False,ht=False,seed=i)
#    write_results_to_csv(f'results/{generator}/{size_name}/{generator}_{size_name}_abrupt_bole_{i}.csv', abrupt_bole) 

#generate the gradual datasets, needs adaption different generator!
gradual, nominal_features = get_stagger_datasets(size, gradual=True)
#evaluate the gradual datasets on naive baselines and all combinations with the Naive Bayes classifier and then write the results in a csv-file
gradual_nb = evaluation(gradual,nominal_attributes=nominal_features,ht=False,bole=False)
write_results_to_csv(f'results/{generator}/{size_name}/{generator}_{size_name}_gradual_nb.csv', gradual_nb) 
#evaluate the gradual datasets on all combinations with the Hoeffding tree classifier and then write the results in a csv-file
gradual_ht = evaluation(gradual,nominal_attributes=nominal_features,nb=False,majclass=False,nochange=False,bole=False)
write_results_to_csv(f'results/{generator}/{size_name}/{generator}_{size_name}_gradual_ht.csv', gradual_ht) 
#evaluate the gradual datasets on all combinations with the BOLE classifier and then write the results in a csv-file  
#for i in range(1,250,50):
#    gradual_bole = evaluation(gradual,nominal_attributes=nominal_features,nb=False,majclass=False,nochange=False,ht=False,seed=i)
#    write_results_to_csv(f'results/{generator}/{size_name}/{generator}_{size_name}_gradual_bole_{i}.csv', gradual_bole) 


#originally executed with BOLE, but there was an error in the evaluation of the BOLE classifier such that it had to be recalculated