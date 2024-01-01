# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 18:11:03 2023

@author: nadin
"""
# Import of basic packages
import numpy as np
import scipy.stats
import pandas as pd


def compute_memory(memory:str) -> float:
    
    """ This method converts the unit of the given memory usage into byte"""
    memory_list = memory.split(" ")
    memory_number = float(memory_list[0])
    memory_unit = memory_list[1]
    
    # computation is just the opposite of the function humanize_bytes in the river package 
    suffixes = ["B","KB","MB","GB","TB","PB"]
    rank = suffixes.index(memory_unit)
    
    if memory_number != 0:
        memory_byte = memory_number * (1024.0**rank)
    
    return memory_byte
    

def mean_confidence_interval(data:list, confidence=0.95):
    
    """ This method computes the mean and the confidence interval for given data of a metric"""
    
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    return round(m,4), round(h,4)


def create_collection(data:pd.DataFrame()) -> dict:
    
    """ This method converts a given dataframe into a dict to simplfy the computation of the confidence intevals"""
    
    #create an empty dataframe for the aggregation of the results 
    collection = {}
    
    #iterate over the given dataframe 
    for ind in data.index:
        #split the name assigned to the given result, which has the following format: generator_drifttype_datasetsize_seed (for synthetic datasets)
        split_name = data['dataset'][ind].split('_')
        
        #drop the information of the seed as we want to aggregate the results according to the generator and drift type (for synthetic datasets)
        rest = split_name.pop()
        
        #KSWIN was executed with 5 different seeds, so it needs further aggregation 
        if 'KSWIN' in data['model'][ind]:
            split_model_name = data['model'][ind].split('_')
            model_name = split_model_name[0] + '_KSWIN_' + split_model_name[2]
        else: model_name = data['model'][ind]
        
        if 'Insects' in data['dataset'][ind]:
            new_name = '_'.join(split_name)+'_'+rest+'_'+model_name
        #after seed is drop rejoin the name and add the information of the model (base classifier + detector)
        else:    
            new_name = '_'.join(split_name)+'_'+model_name
            
        if 'Covertype' in data['dataset'][ind] or 'Sensor' in data['dataset'][ind] or 'Elec2' in data['dataset'][ind]:
            new_name = rest+'_'+model_name

        #transform the runtime into seconds for the calculation of the confidence interval 
        split_time = data['time'][ind].split(':')
        time_sec = int(split_time[0])*60*60 + int(split_time[1])*60 + int(split_time[2])
        
        #tranform the memory consumption into bytes for the calculation of the confidence interval 
        memory_byte = compute_memory(data['memory'][ind])
        
        #transform the information on the position of the drifts into the required format for the calculation of the confidence interval 
        drifts_string=data['drifts'][ind]
        drifts_string=drifts_string.replace('[','')
        drifts_string=drifts_string.replace(']','')
        new_drift_list = drifts_string.split(',')
        
        #when dict already has entry for the dataset and model, add the results of the new seed to the entry 
        if new_name in collection:
            #get the corresponding entry
            entry = collection.get(new_name)
            #add the new accuracy to the results
            accuracy_list = entry[0]
            accuracy_list.append(data['accuracy'][ind])
            #add the new kappa to the results 
            kappa_list = entry[1]
            kappa_list.append(data['cohen kappa'][ind])
            #add the new runtime to the results
            time_list = entry[2]
            time_list.append(time_sec)
            #add the new memory cosumption to the results
            memory_list = entry[3]
            memory_list.append(memory_byte)
            #add the number of drifts to the results  
            drift_list = entry[4]
            #for the basic case (base classifier without detector) there are no drifts
            if "basic" in new_name or drifts_string=="":
                drift_list.append(0)
            #if drifts had been detected count the number of detected drifts 
            else:
                drift_list.append(len(new_drift_list))
            #add the updated entry to the dict
            collection[new_name] = [accuracy_list, kappa_list,time_list,memory_list,drift_list]

        #if no entry exists, create a new one r
        else:
            #entry if the results do not contain any concept drift detection
            if "basic" in new_name or drifts_string=="":
                collection[new_name] = [ [data['accuracy'][ind]], [data['cohen kappa'][ind]],[time_sec],[memory_byte],[0]]
            #entry when the results contain detected drifts 
            else:
                collection[new_name] = [ [data['accuracy'][ind]], [data['cohen kappa'][ind]],[time_sec],[memory_byte],[len(new_drift_list)]]
        
    return collection
            
        


def compute_confidence_interval(data:pd.DataFrame, confidence:float=0.95) -> pd.DataFrame:
    
    """ This method computes the confidence intervals for a given dataframe and returns it in a approriate format"""
    
    #transform the dataframe into a dict for the aggregation of the results of the respective models 
    data_collection = create_collection(data)

    #create an empty dataframe to store the results of the confidence interval computation 
    conf_intervals = pd.DataFrame(columns=['name','accuracy_mean', 'accuracy_conf',
                                           'cohen_kappas_mean', 'cohen_kappas_conf',
                                           'time_mean', 'time_conf',
                                           'memory_mean','memory_conf',
                                           'drifts_mean','drifts_conf'])
    
    #iterate over the dict and compute the confidence interval for each configuration 
    for name, value in data_collection.items():
        if "Insects" in name and "BOLE" not in name:
            accuracy_mean, accuracy_conf = round(value[0][0],4), 0 
            kappa_mean, kappa_conf = round(value[1][0],4), 0 
            time_mean, time_conf = round(value[2][0],4), 0 
            memory_mean, memory_conf = round(value[3][0],4), 0 
            drifts_mean, drifts_conf = round(value[4][0],4), 0 
        else:
            accuracy_mean, accuracy_conf = mean_confidence_interval(value[0])
            kappa_mean, kappa_conf = mean_confidence_interval(value[1])
            time_mean, time_conf = mean_confidence_interval(value[2])
            memory_mean, memory_conf = mean_confidence_interval(value[3])
            drifts_mean, drifts_conf = mean_confidence_interval(value[4])

        
        new_row=[name, accuracy_mean, accuracy_conf,
                 kappa_mean, kappa_conf, time_mean, time_conf,
                 memory_mean, memory_conf, drifts_mean, drifts_conf]

    
        
        conf_intervals.loc[len(conf_intervals)]=new_row
        


        
    return conf_intervals
    

