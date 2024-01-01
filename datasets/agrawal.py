# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 18:05:54 2023

@author: nadin
"""
from river.datasets.synth import Agrawal
from river_adapted.concept_drift_stream import ConceptDriftStream

def create_agrawal_dataset(version:int,size:int,seed:int,gradual:bool):
    
    """This methods creates a data stream from the Agrawal generator with four concept drifts at regular interval based on the given size for the data set"""
    
    #based on the concept drift type, the concept drift is either sudden (width=1) or takes several instances (width=500)
    if gradual: width = 500
    else: width = 1

    #size of one concept
    drift_interval = size/5
    
    #based on the required version set mask for the classification function
    if version == 1: i = 0
    else: i = 5
    
    #definition of each concpet by switching the classification function
    concept1 = Agrawal(classification_function=0+i, seed=seed)
    concept2 = Agrawal(classification_function=1+i, seed=seed)
    concept3 = Agrawal(classification_function=2+i, seed=seed)
    concept4 = Agrawal(classification_function=3+i, seed=seed)
    concept5 = Agrawal(classification_function=4+i, seed=seed)
    
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
   


def get_agrawal_datasets(version:int,size:int,gradual:bool=False,seed:int=23) -> dict:
    
    """This method collects the given number of dataset generated from the Agrawal stream generator with the given size, seed, and drift type (abrupt or gradual)"""
    
    #initiate dict to collect the datasets 
    datasets = {}
    
    #get the right size of the dataset for its name in the dict, s.t. 10.000 instance are represented in name as '10K'
    if size == 1_000_000: name = '1M'
    else: name = str(size//1000) + 'K'
    
    #get the right number of datasets accoring to the dataset size 
    if size >= 500_000: n = 10
    else: n = 30
        
    #get the concept drift type for the name in the dict 
    if gradual: drift ='gradual'
    else: drift = 'abrupt'
        
    #collect the given number of datasets and store them with their size and corresponding name in the dict 
    for i in range(0,2*n,2):
        datasets[f'agrawal{version}_{drift}_' + name + '_'+str(i)] = (create_agrawal_dataset(version,size, seed+i,gradual), size)
        
    #return the dict with all datasets
    return datasets, get_nominal_attributes()

def get_nominal_attributes():
    
    """This method returns the names of the nominal features in a Agrawal dataset"""
    
    return ['elevel', 'car', 'zipcode']
        

    