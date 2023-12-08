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
from utils.load import load_frouros_models, load_frouros_ensemble, load_models_test
from river_adapted.progressive_validation import progressive_val_score


# Imports for the evaluation from the River package
from river.metrics import Accuracy, CohenKappa

# Import basic packages
import pandas as pd

def evaluation(datasets:dict,
                    nochange=True,majclass=True,nb:bool=True,ht:bool=True,
                    adwin:bool=True,bocd:bool=True,cusum:bool=True,ddm:bool=True,ecdd:bool=True,eddm:bool=True,gma:bool=True,gma_sensitive:bool=True,hddma:bool=True,
                    hddmw:bool=True,kswin:bool=True,ph:bool=True,rddm:bool=True,stepd:bool=True) -> pd.DataFrame:
    
    df = pd.DataFrame(columns=['dataset','model','accuracy','cohen kappa', 'time', 'memory','drifts'])
    
    for dataset_name, (dataset, size) in datasets.items():
        models = load_frouros_models(nochange=nochange,majclass=majclass,nb=nb,ht=ht,adwin=adwin,bocd=bocd,cusum=cusum,ddm=ddm,ecdd=ecdd,eddm=eddm,gma=gma,
                                         gma_sensitive=gma_sensitive,hddma=hddma,hddmw=hddmw,kswin=kswin,ph=ph,rddm=rddm,stepd=stepd)

        
           
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

def evaluation_ensemble(seed:int, datasets:dict, ensemble:str='BOLE',
                    nochange=False,majclass=False,nb:bool=False,ht:bool=True,
                    adwin:bool=True,bocd:bool=True,cusum:bool=True,ddm:bool=True,ecdd:bool=True,eddm:bool=True,gma:bool=True,gma_sensitive:bool=True,hddma:bool=True,
                    hddmw:bool=True,kswin:bool=True,ph:bool=True,rddm:bool=True,stepd:bool=True) -> pd.DataFrame:
    
    df = pd.DataFrame(columns=['dataset','model','accuracy','cohen kappa', 'time', 'memory','drifts'])
    
    for dataset_name, (dataset, size) in datasets.items():
        models = load_frouros_ensemble(seed=seed, ensemble=ensemble,nochange=nochange,majclass=majclass,nb=nb,ht=ht,adwin=adwin,bocd=bocd,cusum=cusum,ddm=ddm,ecdd=ecdd,eddm=eddm,gma=gma,
                                         gma_sensitive=gma_sensitive,hddma=hddma,hddmw=hddmw,kswin=kswin,ph=ph,rddm=rddm,stepd=stepd)
   
        for model_name, model in models.items():
            new_row = [dataset_name, model_name]
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



        
        

    

    