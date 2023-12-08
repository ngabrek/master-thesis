# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 18:05:54 2023

@author: nadin
"""
from river.datasets.synth import Agrawal

from river_adapted.concept_drift_stream import ConceptDriftStream

def create_abrupt_agrawal1_dataset(size, seed):
    drift_interval = size/5
    concept1 = Agrawal(classification_function=0, seed=seed)
    concept2= Agrawal(classification_function=1, seed=seed)
    concept3= Agrawal(classification_function=2, seed=seed)
    concept4= Agrawal(classification_function=3, seed=seed)
    concept5= Agrawal(classification_function=4, seed=seed)
    
    drift4 = ConceptDriftStream(
        stream=concept4,
        drift_stream=concept5,
        seed=seed, position=drift_interval, width=1)
    
    drift3 = ConceptDriftStream(
        stream=concept3,
        drift_stream=drift4,
        seed=seed, position=drift_interval, width=1)
    
    drift2 = ConceptDriftStream(
        stream=concept2,
        drift_stream=drift3,
        seed=seed, position=drift_interval, width=1)
    
    return ConceptDriftStream(
        stream=concept1,
        drift_stream=drift2,
        seed=seed, position=drift_interval, width=1)


def create_gradual_agrawal1_dataset(size, seed):
    drift_interval = size/5
    concept1 = Agrawal(classification_function=0, seed=seed)
    concept2= Agrawal(classification_function=1, seed=seed)
    concept3= Agrawal(classification_function=2, seed=seed)
    concept4= Agrawal(classification_function=3, seed=seed)
    concept5= Agrawal(classification_function=4, seed=seed)
    
    drift4 = ConceptDriftStream(
        stream=concept4,
        drift_stream=concept5,
        seed=seed, position=drift_interval, width=500
    )
    
    drift3 = ConceptDriftStream(
        stream=concept3,
        drift_stream=drift4,
        seed=seed, position=drift_interval, width=500
    )
    
    drift2 = ConceptDriftStream(
        stream=concept2,
        drift_stream=drift3,
        seed=seed, position=drift_interval, width=500
    )
    
    return ConceptDriftStream(
        stream=concept1,
        drift_stream=drift2,
        seed=seed, position=drift_interval, width=500
    )

def get_abrupt_agrawal1_datasets(size:int, seed:int, n:int) -> dict:
    datasets = {}
    name = str(size/1000)
    for i in range(0,n):
        datasets['agrawal1_abrupt_' + name + 'K_'+str(i)] = (create_abrupt_agrawal1_dataset(size, 23+i), size)
        
    return datasets
        
def get_gradual_agrawal1_datasets(size:int, seed:int, n:int) -> dict:
    datasets = {}
    name = str(size/1000)
    for i in range(0,n):
        datasets['agrawal1_gradual_' + name + 'K_'+str(i)] = (create_gradual_agrawal1_dataset(size, 23+i), size)
        
    return datasets
    