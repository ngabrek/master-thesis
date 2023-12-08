# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 13:30:39 2023

@author: nadin
"""

from river_adapted.progressive_validation import progressive_val_score
from datasets.stagger import get_stagger_datasets
from datasets.mixed import get_mixed_datasets
from river_adapted.retrain import DriftRetrainingClassifier
from river.tree import HoeffdingTreeClassifier
from river.naive_bayes import GaussianNB
from frouros_adapted.eddm import EDDM
from river.metrics import Accuracy, CohenKappa
from utils.load import load_frouros_detectors

from evaluation.evaluation import evaluation_test,evaluation

size=1000

datasets, nominal_attributes = get_mixed_datasets(size, n=1)


detectors =load_frouros_detectors(False, False, False, False, False, True, False, False, False, False, False, False, False, False)

models={}

for detector_name, detector in detectors.items():
    models['HT_1']=DriftRetrainingClassifier(model=HoeffdingTreeClassifier(nominal_attributes=None),drift_detector=detector)
    models['HT_2']=DriftRetrainingClassifier(model=HoeffdingTreeClassifier(nominal_attributes=None),drift_detector=detector)
    #models['NB_1']=DriftRetrainingClassifier(model=GaussianNB(),drift_detector=detector)
    #models['NB_2']=DriftRetrainingClassifier(model=GaussianNB(),drift_detector=detector)

print("results for identical model without detector reset")
for dataset_name, (dataset, size) in datasets.items():
    for model_name, model in models.items():
        results, time, memory = progressive_val_score(
        dataset=dataset.take(size), 
        model=model, 
        metric=Accuracy()+CohenKappa(),
        show_time=True,
        show_memory=True,
        print_every=size)

        print(results)
        
print("results for identical model with detector reset")
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
        
print('This shows that a reset of the detector is required!')


