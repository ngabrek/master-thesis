# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 13:09:37 2023

@author: nadin
"""

from datasets.real_world import SensorStream
from evaluation.evaluation import evaluation
from utils.read_and_write import write_results_to_csv
 
#adapt these variables according the dataset under evaluation
generator = 'real-world'
variant = 'sensor-stream'

#the features in the Insects datasets are all continuous
nominal_features = None

#load the dataset
dataset ={'SensorStream': (SensorStream(), SensorStream().n_samples)}

#evaluate the dataset on ADWIN with the BOLE classifier and then write the results in a csv-file  
for i in range(1,250,50):
    bole = evaluation(dataset,nominal_attributes=nominal_features,nb=False,majclass=False,nochange=False,ht=False,basic=False,bocd=False,cusum=False,ddm=False,
                           ecdd=False,eddm=False,gma=False,hddma=False,hddmw=False,kswin=False,ph=False,rddm=False,stepd=False,seed=i)
    write_results_to_csv(f'results/{generator}/{variant}/{generator}_{variant}_bole_adwin_{i}.csv', bole) 



