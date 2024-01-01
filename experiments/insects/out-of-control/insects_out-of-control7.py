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
variant = 'out-of-control'

#the features in the Insects datasets are all continuous
nominal_features = None


#load dataset based on the variant
dataset = {f'Insects_{variant}': (Insects(variant=f'{variant}'), Insects(variant=f'{variant}').n_samples)}

#evaluate the datasets on GMA with the BOLE classifier and then write the results in a csv-file  
for i in range(1,250,50):
    bole = evaluation(dataset,nominal_attributes=nominal_features,nb=False,majclass=False,nochange=False,ht=False,bocd=False,basic=False,adwin=False,cusum=False,
                               eddm=False,ddm=False,ecdd=False,hddma=False,hddmw=False,kswin=False,ph=False,rddm=False,stepd=False,seed=i)
    write_results_to_csv(f'results/{generator}/{variant}/{generator}_{variant}_bole_gma_{i}.csv', bole) 
