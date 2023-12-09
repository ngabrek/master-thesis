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
size = 500_000

#get the size_name for the name of the dataset
if size == 1_000_000: size_name ='1M'
else: size_name = str(size//1000) + 'K'

#generate the gradual datasets, needs adaption different generator!
gradual, nominal_features = get_mixed_datasets(size, gradual=True)

#evaluate the gradual datasets on BOCD with the Naive Bayes classifier and then write the results in a csv-file
gradual_nb = evaluation(gradual,nominal_attributes=nominal_features,ht=False,bole=False,majclass=False,nochange=False,basic=False,adwin=False,cusum=False,ddm=False,
                       ecdd=False,eddm=False,gma=False,hddma=False,hddmw=False,kswin=False,ph=False,rddm=False,stepd=False)
write_results_to_csv(f'results/{generator}/{size_name}/{generator}_{size_name}_gradual_nb_bocd.csv', gradual_nb) 
