# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 13:30:39 2023

@author: nadin
"""

from river_adapted.progressive_validation import progressive_val_score
from datasets.stagger import get_stagger_datasets
from datasets.mixed import create_mixed_dataset
from river_adapted.retrain import DriftRetrainingClassifier
from river.ensemble import BOLEClassifier
from river.tree import HoeffdingTreeClassifier
from river.naive_bayes import GaussianNB
from frouros_adapted.eddm import EDDM
from river.metrics import Accuracy, CohenKappa
from utils.load import load_frouros_detectors

from evaluation.evaluation import evaluation_test,evaluation

def load_models(detectors):
    models={}
    
    for detector_name, detector in detectors.items():
        #models['HT_1']=DriftRetrainingClassifier(model=HoeffdingTreeClassifier(nominal_attributes=None),drift_detector=detector)
        #models['HT_2']=DriftRetrainingClassifier(model=HoeffdingTreeClassifier(nominal_attributes=None),drift_detector=detector)
        #models['NB_1']=DriftRetrainingClassifier(model=GaussianNB(),drift_detector=detector)
        #models['NB_2']=DriftRetrainingClassifier(model=GaussianNB(),drift_detector=detector)
        models['BOLE_1']=BOLEClassifier(model=DriftRetrainingClassifier(model=HoeffdingTreeClassifier(nominal_attributes=None),drift_detector=detector),seed=23)
        models['BOLE_2']=BOLEClassifier(model=DriftRetrainingClassifier(model=HoeffdingTreeClassifier(nominal_attributes=None),drift_detector=detector),seed=23)
    
    return models 

size=1000

datasets = {'mixed':(create_mixed_dataset(size,23,False),size)}


detectors =load_frouros_detectors(False, False, False, False, False, True, False, False, False, False, False, False, False, False)




print("first results for identical model without detector reset")
for dataset_name, (dataset, size) in datasets.items():
    #load models
    models = load_models(detectors)
    for model_name, model in models.items():
        results, time, memory = progressive_val_score(
        dataset=dataset.take(size), 
        model=model, 
        metric=Accuracy()+CohenKappa(),
        show_time=True,
        show_memory=True,
        print_every=size)

        print(results)
        
        
print("second results for identical model without detector reset")
for dataset_name, (dataset, size) in datasets.items():
    #load models
    models = load_models(detectors)
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
    #load models
    models = load_models(detectors)
    for model_name, model in models.items():
        #reset detector for new model
        if hasattr(model,'reset_detector'):
            model.reset_detector()
            print('reset')
        if hasattr(model.model,'reset_detector'):
            model.model.reset_detector()
            print('reset')

        results, time, memory = progressive_val_score(
        dataset=dataset.take(size), 
        model=model, 
        metric=Accuracy()+CohenKappa(),
        show_time=True,
        show_memory=True,
        print_every=size)

        print(results)
        
print('This shows that a reset of the detector is required!')

print(evaluation(datasets))




