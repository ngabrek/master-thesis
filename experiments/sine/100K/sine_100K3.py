# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 13:13:33 2023

@author: nadin
"""

from datasets.sine import get_sine_datasets
from evaluation.evaluation import evaluation
from utils.read_and_write import write_results_to_csv
 
#adapt these variables according the dataset under evaluation
generator = 'sine'
size = 100_000

#get the size_name for the name of the dataset
if size == 1_000_000: size_name ='1M'
else: size_name = str(size//1000) + 'K'

#generate the abrupt datasets, needs adaption different generator!
abrupt, nominal_features = get_sine_datasets(size)

#evaluate the abrupt datasets on BOCD with the Hoeffding tree classifier and then write the results in a csv-file  
abrupt_ht = evaluation(abrupt,nominal_attributes=nominal_features,nb=False,majclass=False,nochange=False,bole=False,basic=False,adwin=False,cusum=False,ddm=False,
                       ecdd=False,eddm=False,gma=False,hddma=False,hddmw=False,kswin=False,ph=False,rddm=False,stepd=False)
write_results_to_csv(f'results/{generator}/{size_name}/{generator}_{size_name}_abrupt_ht_bocd.csv', abrupt_ht) 

