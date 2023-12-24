# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 13:13:33 2023

@author: nadin
"""

from datasets.agrawal import get_agrawal_datasets
from evaluation.evaluation import evaluation
from utils.read_and_write import write_results_to_csv
 
#adapt these variables according the dataset under evaluation
generator = 'agrawal1'
size = 1_000_000

#get the size_name for the name of the dataset
if size == 1_000_000: size_name ='1M'
else: size_name = str(size//1000) + 'K'

#generate the gradual datasets, needs adaption different generator!
gradual, nominal_features = get_agrawal_datasets(1,size, gradual=True)

#evaluate the gradual datasets on all combinations with the BOLE classifier but BOCD and KSWIN and then write the results in a csv-file  
i = 1
gradual_bole = evaluation(gradual,nominal_attributes=nominal_features,nb=False,majclass=False,nochange=False,ht=False,bocd=False,kswin=False,seed=i)
write_results_to_csv(f'results/{generator}/{size_name}/{generator}_{size_name}_gradual_bole_{i}.csv', gradual_bole) 


