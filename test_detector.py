# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 13:30:39 2023

@author: nadin
"""

from river_adapted.progressive_validation import progressive_val_score
from datasets.stagger import get_abrupt_stagger_datasets
from river_adapted.retrain import DriftRetrainingClassifier
from river.tree import HoeffdingTreeClassifier
from frouros_adapted.eddm import EDDM
from river.metrics import Accuracy, CohenKappa

from evaluation.evaluation import evaluation_test


size=100

datasets = get_abrupt_stagger_datasets(size, 23, 1)

detector = EDDM()

models={}
models['HT_1']=DriftRetrainingClassifier(model=HoeffdingTreeClassifier(),drift_detector=detector)
models['HT_2']=DriftRetrainingClassifier(model=HoeffdingTreeClassifier(),drift_detector=detector)


for dataset_name, (dataset, size) in datasets.items():
    for model_name, model in models.items():
        detector.reset()
        results, time, memory = progressive_val_score(
            dataset=dataset.take(size), 
            model=model, 
            metric=Accuracy()+CohenKappa(),
            show_time=True,
            show_memory=True,
            print_every=size)
        
        print(results)
        

results = evaluation_test(datasets,nochange=False,majclass=False,nb=False)
print(results)


