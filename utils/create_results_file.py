# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 12:19:14 2023

@author: nadin
"""

import pandas as pd
import os 
from utils.read_and_write import read_results_from_csv
from utils.confidence_interval import compute_confidence_interval

def create_results_file(folder_path:str):
    
    """ This method merges all the results and creates the respective files with the final results and their confidence intervals"""
    
    #save current path to go back later
    current_path = os.getcwd()
    
    #change path to directory that contains the csv files with the results
    os.chdir(folder_path)
    csv_files = [f for f in os.listdir() if f.endswith('.csv')]
    
    #create an empty dataframe where all the result data is merged
    df_all = pd.DataFrame()
    
    #iterate over all the results files and store the data in the dataframe 
    for csv in csv_files:
        df = read_results_from_csv(csv)
        df_all = pd.concat([df_all, df],axis=0,ignore_index=True)
      
    print(len(df_all))
    
    #get rid of potential duplicates that can occur because of recalculations 
    #NB
    df_nb = df_all[df_all['model']=='NB_basic_F']
    df_nb_no_duplicates = df_nb.drop_duplicates(subset=['dataset', 'model'])
    
    #HT 
    df_ht = df_all[df_all['model']=='HT_basic_F']
    df_ht_no_duplicates = df_ht.drop_duplicates(subset=['dataset', 'model'])
    
    #NoChange 
    df_nc = df_all[df_all['model']=='NoChange_basic_F']
    df_nc_no_duplicates = df_nc.drop_duplicates(subset=['dataset', 'model'])
    
    #MajClass
    df_mc = df_all[df_all['model']=='MajClass_basic_F']
    df_mc_no_duplicates = df_mc.drop_duplicates(subset=['dataset', 'model'])
    
    #BOLE
    df_bole = df_all[df_all['model']=='BOLE+HT_basic_F']
    df_bole_no_duplicates = df_bole.drop_duplicates(subset=['dataset', 'model','accuracy','cohen kappa','drifts'])
    
    df_rest = df_all[(df_all['model']!='NB_basic_F') & (df_all['model']!='HT_basic_F') & (df_all['model']!='NoChange_basic_F') & (df_all['model']!='MajClass_basic_F') & 
                     (df_all['model']!='BOLE+HT_basic_F')]
    
    #concet all the dataframe without duplicates to one dataframe
    df_all_no_duplicates = pd.concat([df_nb_no_duplicates, df_ht_no_duplicates, df_nc_no_duplicates, df_mc_no_duplicates,df_bole_no_duplicates, df_rest],axis=0,ignore_index=True)
    #df_all_no_duplicates = df_all_no_duplicates[df_all_no_duplicates['model'].str.contains('GMA_sensitive')==False]
    
    #check if there had been duplicates
    print(len(df_all_no_duplicates))
    
    #compute the confidence intervals for the results 
    df_conf = compute_confidence_interval(df_all_no_duplicates)
    
    #transform the results of the confidence interval computation into a dataframe
    final_df= create_dataframe(df_conf)
    
    #check if the correct number of models had been aggregated
    print(len(final_df))

    #reset the path 
    os.chdir(current_path)

    #return the dataframe with the final confidence intervals
    return final_df
       
      


def create_dataframe(data:pd.DataFrame()) -> pd.DataFrame():
    
    """ This method converts a given dataframe in the appropriate formate for the final results file"""
    
    dataframe = pd.DataFrame(columns=['generator','drift_type','size','classifier','detector','accuracy_mean', 'accuracy_conf',
                                           'cohen_kappas_mean', 'cohen_kappas_conf',
                                           'time_mean', 'time_conf',
                                           'memory_mean','memory_conf',
                                           'drifts_mean','drifts_conf'])
    
    
    for ind in data.index:
        split_name = data['name'][ind].split('_')
        dataset = split_name[0]
        
        if 'incr_abrupt' in data['name'][ind] or 'incr_reoc' in data['name'][ind]:
            drift_type = split_name[1] + "-" + split_name[2]
            size = split_name[3]
            classifier = split_name[4]
            detector = split_name[5]
        elif 'ofc' in data['name'][ind]:
            drift_type = split_name[1]
            size = split_name[1]
            classifier = split_name[2]
            detector = split_name[3]
        elif 'Covertype' in data['name'][ind] or 'Elec2' in data['name'][ind] or 'Sensor' in data['name'][ind]:
            drift_type = 'none'
            size = 'none'
            classifier = split_name[1]
            detector = split_name[2]
        else:
            drift_type = split_name[1]
            size = split_name[2]
            classifier = split_name[3]
            detector = split_name[4]
            
        if 'sensitive' in data['name'][ind]:
            detector = split_name[4] + "_" + split_name[5]
            
            
        new_entry = [dataset,drift_type,size,classifier,detector,data['accuracy_mean'][ind],data['accuracy_conf'][ind],
                     data['cohen_kappas_mean'][ind], data['cohen_kappas_conf'][ind],
                     data['time_mean'][ind], data['time_conf'][ind],
                     data['memory_mean'][ind], data['memory_conf'][ind],
                     data['drifts_mean'][ind], data['drifts_conf'][ind]]
        
    
        dataframe.loc[len(dataframe)] = new_entry
        
        
    return dataframe

        

    