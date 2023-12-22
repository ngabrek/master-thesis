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
variant = 'incremental'

#the features in the Insects datasets are all continuous
nominal_features = None


#load balanced dataset based on the variant
balanced = {f'Insects_{variant}_bal': (Insects(variant=f'{variant}_balanced'), Insects(variant=f'{variant}_balanced').n_samples)}
#evaluate the balanced datasets on BOCD with the BOLE classifier and then write the results in a csv-file  
i = 51
balanced_bole = evaluation(balanced,nominal_attributes=nominal_features,nb=False,majclass=False,nochange=False,ht=False,
                               kswin=False,basic=False,adwin=False,cusum=False, eddm=False,ddm=False,ecdd=False,gma=False,
                               hddma=False,stepd=False,hddmw=False,ph=False,rddm=False,seed=i)
write_results_to_csv(f'results/{generator}/{variant}/{generator}_{variant}_bal_bole_bocd_{i}.csv', balanced_bole)  