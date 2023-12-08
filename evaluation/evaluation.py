# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 18:22:44 2023

@author: nadin

"""
# Set root path of the project for local imports
from pathlib import Path
import sys
path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

# Local imports
from utils.load import load_models, load_models_test
from river_adapted.progressive_validation import progressive_val_score


# Imports for the evaluation from the River package
from river.metrics import Accuracy, CohenKappa

# Import basic packages
import pandas as pd


def evaluation(datasets:dict,nominal_attributes=None,seed:int=23,
               nochange:bool=True,majclass:bool=True,nb:bool=True,ht:bool=True,bole:bool=True,
               basic:bool=True,adwin:bool=True,bocd:bool=True,cusum:bool=True,ddm:bool=True,ecdd:bool=True,eddm:bool=True,gma:bool=True,gma_sensitive:bool=False,hddma:bool=True,
               hddmw:bool=True,kswin:bool=True,ph:bool=True,rddm:bool=True,stepd:bool=True) -> pd.DataFrame:
    
    """This method runs the evaluation on given datasets for the given combinations of base learner and concept drift detectors"""
    
    #initialize the dataframe to store the evaluation results 
    df = pd.DataFrame(columns=['dataset','model','accuracy','cohen kappa', 'time', 'memory','drifts'])
    
    #iterate over the given datasets and evaluate them
    for dataset_name, (dataset, size) in datasets.items():
        #first, load the required models (base learner, detectors, and their combinations)
        models = load_models(nominal_attributes=nominal_attributes,seed=seed,
                             nochange=nochange,majclass=majclass,nb=nb,ht=ht,bole=bole,
                             basic=basic,adwin=adwin,bocd=bocd,cusum=cusum,ddm=ddm,ecdd=ecdd,eddm=eddm,gma=gma,gma_sensitive=gma_sensitive,
                             hddma=hddma,hddmw=hddmw,kswin=kswin,ph=ph,rddm=rddm,stepd=stepd)
 
        
        #start the evaluation process for all models and store it in the dataframe
        df = start_evaluation_process(dataset_name, dataset, size, models, df)
    
    #return the dataframe with all evaluation results 
    return df


def start_evaluation_process(dataset_name:str,dataset,size,models,df:pd.DataFrame) -> pd.DataFrame:
    #iterate over each model and evaluate it on the current dataset 
    for model_name, model in models.items():
        #initialize a new row to store the evaluation results of the model on the given dataset
        new_row = [dataset_name, model_name]
        #reset detector for new model
        if hasattr(model,'reset_detector'):
            model.reset_detector()
        #evaluate the model on the given dataset
        results, time, memory = progressive_val_score(
                    dataset=dataset.take(size), 
                    model=model, 
                    metric=Accuracy()+CohenKappa(),
                    show_time=True,
                    show_memory=True,
                    print_every=size)
        #store the evaluation results in the new row
        new_row.extend([results[0].get(), results[1].get(), time, memory])

        #if available get the detected drifts from the model and add them to the new row 
        if hasattr(model,'get_drifts'):
            new_row.append(model.get_drifts())
        else:
            new_row.append([])
        
        #add the new row to the dataframe
        df.loc[len(df)] = new_row

    #return the dataframe with all evaluation results for the given dataset
    return df

def evaluation_test(datasets:dict,
                    nochange=True,majclass=True,nb:bool=True,ht:bool=True,
                    adwin:bool=True,bocd:bool=True,cusum:bool=True,ddm:bool=True,ecdd:bool=True,eddm:bool=True,gma:bool=True,gma_sensitive:bool=True,hddma:bool=True,
                    hddmw:bool=True,kswin:bool=True,ph:bool=True,rddm:bool=True,stepd:bool=True) -> pd.DataFrame:
    
    df = pd.DataFrame(columns=['dataset','model','accuracy','cohen kappa', 'time', 'memory','drifts'])
    
    for dataset_name, (dataset, size) in datasets.items():
        models = load_models_test()

        for model_name, model in models.items():
            new_row = [dataset_name, model_name]
            model.reset_detector()
            results, time, memory = progressive_val_score(
                        dataset=dataset.take(size), 
                        model=model, 
                        metric=Accuracy()+CohenKappa(),
                        show_time=True,
                        show_memory=True,
                        print_every=size)
            new_row.extend([results[0].get(), results[1].get(), time, memory])

            if hasattr(model,'get_drifts'):
                new_row.append(model.get_drifts())
            else:
                new_row.append([])
                
            df.loc[len(df)] = new_row
    
    return df



        
        

    

    