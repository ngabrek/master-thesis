# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 18:12:01 2023

@author: nadin
"""

from river.datasets.synth import STAGGER

from river_adapted.concept_drift_stream import ConceptDriftStream

def create_stagger_dataset(size:int,seed:int,gradual:bool):
    
    """This methods creates a data stream from the STAGGER generator with four concept drifts at regular interval based on the given size for the data set"""
    
    #based on the concept drift type, the concept drift is either sudden (width=1) or takes several instances (width=500)
    if gradual:
        width = 500
    else:
        width = 1

    #size of one concept
    drift_interval = size/5
    
    #definition of each concpet by switching the classification function 
    concept1 = STAGGER(classification_function=0, seed=seed)
    concept2= STAGGER(classification_function=1, seed=seed)
    concept3= STAGGER(classification_function=2, seed=seed)
    concept4= STAGGER(classification_function=0, seed=seed)
    concept5= STAGGER(classification_function=1, seed=seed)
    
    #generating the concept drift stream and introducing a concept drift by changing the concept after one drift interval
    drift4 = ConceptDriftStream(
        stream=concept4,
        drift_stream=concept5,
        seed=seed, position=drift_interval, width=width)
    
    drift3 = ConceptDriftStream(
        stream=concept3,
        drift_stream=drift4,
        seed=seed, position=drift_interval, width=width)
    
    drift2 = ConceptDriftStream(
        stream=concept2,
        drift_stream=drift3,
        seed=seed, position=drift_interval, width=width)
    
    #return the stream after the last concept drift was introduced
    return ConceptDriftStream(
        stream=concept1,
        drift_stream=drift2,
        seed=seed, position=drift_interval, width=width)


def get_stagger_datasets(size:int,gradual:bool=False,seed:int=23, n:int=30) -> dict:
    
    """This method collects the given number of dataset generated from the STAGGER stream generator with the given size, seed, and drift type (abrupt or gradual)"""
    
    #initiate dict to collect the datasets 
    datasets = {}
    #get the right size of the dataset for its name in the dict, s.t. 10.000 instance are represented in name as '10K'
    name = str(size//1000)
    #get the concept drift tyoe for the name in the dict 
    if gradual:
        drift ='gradual'
    else:
        drift = 'abrupt'
    
    #collect the given number of datasets and store them with their size and corresponding name in the dict 
    for i in range(0,n):
        datasets[f'stagger_{drift}_' + name + 'K_'+str(i)] = (create_stagger_dataset(size, seed+i,gradual),size)
    
    #return the dict with all datasets
    return datasets
        
def get_nominal_features():
    """This method returns the names of the nominal features in a STAGGER dataset"""
    return STAGGER().feature_names