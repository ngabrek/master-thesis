# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 13:09:37 2023

@author: nadin
"""

from datasets.real_world import Covertype
from evaluation.evaluation import evaluation
from utils.read_and_write import write_results_to_csv
 
#adapt these variables according the dataset under evaluation
generator = 'real-world'
variant = 'covertype'

#load the dataset
covertype = Covertype()
dataset = {'Covertype': (covertype, covertype.n_samples)}

#nominal features in the Covertype dataset
nominal_features = covertype.get_nominal_features()

#evaluate the dataset on BOCD with the BOLE classifier and then write the results in a csv-file  
i = 51
bole = evaluation(dataset,nominal_attributes=nominal_features,nb=False,majclass=False,nochange=False,ht=False,basic=False,kswin=False,adwin=False,cusum=False,
                               ddm=False,ecdd=False,eddm=False,gma=False,hddma=False,stepd=False,hddmw=False,ph=False,rddm=False,seed=i)
write_results_to_csv(f'results/{generator}/{variant}/{generator}_{variant}_bole_bocd_{i}.csv', bole) 



