# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 12:25:52 2023

@author: nadin

"""
from utils.read_and_write import read_all_result_files

import pandas as pd 
import numpy as np
import scikit_posthocs as sp
import matplotlib.pyplot as plt

def create_dict_detectors_synth(metric:str, generators:list, sizes:list, detectors:list, nb:bool=True, ht:bool=True, ensemble:bool=True, abrupt:bool=True, gradual:bool=True) -> dict:
    
    """ This method creates a dictionary for the statistical evaluation of the synthetic datasets"""
    df = read_all_result_files()

    dict_detectors = {}
    for detector in detectors:
        dict_detectors[detector] = []

    for size in sizes:
        for generator in generators:
            for detector in detectors:
                if ht:
                    if abrupt:
                        df_abrupt_HT = df[(df['size']==size) & (df['generator']==generator) & (df['detector']==detector) & (df['drift_type']=='abrupt')
                                 & (df['classifier']=='HT')]
                        if df_abrupt_HT[metric].size != 0:
                            dict_detectors[detector].append(df_abrupt_HT[metric].values[0])
                        else: dict_detectors[detector].append(None)
                    if gradual:
                        df_gradual_HT =  df[(df['size']==size) & (df['generator']==generator) & (df['detector']==detector) & (df['drift_type']=='gradual')
                                 & (df['classifier']=='HT')]
                        if df_gradual_HT[metric].size != 0:
                            dict_detectors[detector].append(df_gradual_HT[metric].values[0])
                        else: dict_detectors[detector].append(None)
                if nb:
                    if abrupt:
                        df_abrupt_NB = df[(df['size']==size) & (df['generator']==generator) & (df['detector']==detector) & (df['drift_type']=='abrupt')
                                 & (df['classifier']=='NB')]
                        if df_abrupt_NB[metric].size != 0:
                            dict_detectors[detector].append(df_abrupt_NB[metric].values[0])
                        else: dict_detectors[detector].append(None)
                    if gradual:
                        df_gradual_NB =  df[(df['size']==size) & (df['generator']==generator) & (df['detector']==detector) & (df['drift_type']=='gradual')
                                 & (df['classifier']=='NB')]
                        if df_gradual_NB[metric].size != 0:
                            dict_detectors[detector].append(df_gradual_NB[metric].values[0])
                        else: dict_detectors[detector].append(None)
                        
                if ensemble:
                     if abrupt:
                         df_abrupt_BOLE = df[(df['size']==size) & (df['generator']==generator) & (df['detector']==detector) & (df['drift_type']=='abrupt')
                                  & (df['classifier']=='BOLE')]
                         if df_abrupt_BOLE[metric].size != 0:
                             dict_detectors[detector].append(df_abrupt_BOLE[metric].values[0])
                         else: dict_detectors[detector].append(None)
                     if gradual:
                         df_gradual_BOLE = df[(df['size']==size) & (df['generator']==generator) & (df['detector']==detector) & (df['drift_type']=='gradual')
                                  & (df['classifier']=='BOLE')]
                         if df_gradual_BOLE[metric].size != 0:
                             dict_detectors[detector].append(df_gradual_BOLE[metric].values[0])
                         else: dict_detectors[detector].append(None)               
                
    return dict_detectors

def create_dict_detectors_insects(metric:str, bal:bool=True, imbal:bool=True, classifiers=['NB','HT','BOLE'], drifts=['abrupt','gradual','incr','incr-abrupt','ince-reoc','ooc'], 
                                  detectors=['basic','ADWIN','BOCD','CUSUM','DDM','ECDD','EDDM','GMA','HDDMA','HDDMW','KSWIN','PH','RDDM','STEPD']) -> dict:
    
    """ This method creates a dictionary for the statistical evaluation of the Insects datasets"""
    df = read_all_result_files(generators=['insects'])
    df_insects = df[df['generator']=='Insects']
    df_bal = df_insects[df_insects['size']=='bal']
    df_imbal = df_insects[df_insects['size']=='imbal']
    
    dict_detectors = {}
    
    for detector in detectors: 
        dict_detectors[detector]=[]

    for drift in drifts:
        for detector in detectors:
            for classifier in classifiers:
                if bal:
                    df_current = df_bal[(df_bal['detector']==detector)&(df_bal['drift_type']==drift)&(df_bal['classifier']==classifier)]

                    if df_current[metric].size != 0:
                        dict_detectors[detector].append(df_current[metric].values[0])
                    else: dict_detectors[detector].append(None)
                if imbal:
                    df_current = df_imbal[(df_imbal['detector']==detector)&(df_imbal['drift_type']==drift)&(df_imbal['classifier']==classifier)]
                    if df_current[metric].size != 0:
                        dict_detectors[detector].append(df_current[metric].values[0])
                    else: dict_detectors[detector].append(None)
             
                
    return dict_detectors

def create_dict_detectors_real(metric:str,classifiers,datasets,detectors) -> dict:
    
    """ This method creates a dictionary for the statistical evaluation of the Insects datasets"""
    df = read_all_result_files(generators=['real-world'])
    
    dict_detectors = {}
    
    for detector in detectors: 
        dict_detectors[detector]=[]

    for dataset in datasets:
        for detector in detectors:
            for classifier in classifiers:
                df_current = df[(df['detector']==detector)&(df['classifier']==classifier)&(df['generator']==dataset)]

                if df_current[metric].size != 0:
                    dict_detectors[detector].append(df_current[metric].values[0])
                else: dict_detectors[detector].append(None)

    return dict_detectors

def get_mean(metric:str, nb:bool=True, ht:bool=True, abrupt:bool=True, gradual:bool=True) -> dict:
    dict_detectors = create_dict_detectors_synth(metric, nb=nb, ht=ht, abrupt=abrupt, gradual=gradual)
    
    for key in dict_detectors:
        new_dict = np.array(dict_detectors[key], dtype=np.float64)
        dict_detectors[key] = np.nanmean(new_dict)
    
    return dict_detectors

def get_avg_rank_synth(metric:str, generators:list=['agrawal1','agrawal2','mixed','sea','sine','stagger'], sizes:list=['10K','20K','50K','100K','500K','1M'], 
                       detectors:list=['basic','ADWIN','BOCD','CUSUM','DDM','ECDD','EDDM','GMA','HDDMA','HDDMW','KSWIN','PH','RDDM','STEPD'],
                       ascending=True, nb:bool=True, ht:bool=True, ensemble:bool=True, abrupt:bool=True, gradual:bool=True):
    
    """ This method computes the average ranks for the statistical test of the respective models over the synthetic datasets"""
    
    dict_detectors = create_dict_detectors_synth(metric, generators, sizes, detectors,nb=nb, ht=ht, ensemble=ensemble, abrupt=abrupt, gradual=gradual)
    
   # dict_detectors['BOCD*'] = dict_detectors.pop('BOCD')
                
    data = (
            pd.DataFrame(dict_detectors)
            .rename_axis('dataset')
            .melt(
                var_name='estimator',
                value_name='score',
                ignore_index=False,
                )
            .reset_index()
            )
    
    avg_rank = data.groupby('dataset').score.rank(ascending=ascending).groupby(data.estimator).mean()


    return data, avg_rank

def get_avg_rank_insects(metric:str, ascending=True, bal:bool=True, imbal:bool=True, classifiers=['NB','HT','BOLE'], drifts=['abrupt','gradual','incr','incr-abrupt','ince-reoc','ooc'], 
                                  detectors=['basic','ADWIN','BOCD','CUSUM','DDM','ECDD','EDDM','GMA','HDDMA','HDDMW','KSWIN','PH','RDDM','STEPD']):
    
    """ This method computes the average ranks for the statistical test of the respective models over the Insects datasets"""
    dict_detectors = create_dict_detectors_insects(metric, bal=bal, imbal=imbal, classifiers=classifiers, drifts=drifts, detectors=detectors)
    
    dict_detectors['BOCD*'] = dict_detectors.pop('BOCD')
                
    data = (
            pd.DataFrame(dict_detectors)
            .rename_axis('dataset')
            .melt(
                var_name='estimator',
                value_name='score',
                ignore_index=False,
                )
            .reset_index()
            )
    
    avg_rank = data.groupby('dataset').score.rank(ascending=ascending).groupby(data.estimator).mean()


    return data, avg_rank

def get_avg_rank_real(metric:str, ascending=True, classifiers=['NB','HT','BOLE'], datasets=['Covertype','Elec2','SensorStream'], 
                                  detectors=['basic','ADWIN','BOCD','CUSUM','DDM','ECDD','EDDM','GMA','HDDMA','HDDMW','KSWIN','PH','RDDM','STEPD']):
    
    """ This method computes the average ranks for the statistical test of the respective models over the real-world datasets"""
    dict_detectors = create_dict_detectors_real(metric,classifiers=classifiers,datasets=datasets,detectors=detectors)
    
    if 'SensorStream' in datasets:
        dict_detectors['BOCD*'] = dict_detectors.pop('BOCD')
                
    data = (
            pd.DataFrame(dict_detectors)
            .rename_axis('dataset')
            .melt(
                var_name='estimator',
                value_name='score',
                ignore_index=False,
                )
            .reset_index()
            )
    
    avg_rank = data.groupby('dataset').score.rank(ascending=ascending).groupby(data.estimator).mean()


    return data, avg_rank

def get_avg_rank_all(metric:str, ascending=True, classifiers=['NB','HT','BOLE'],datasets=['synthetic','real-world','insects'],
                 detectors=['basic','ADWIN','BOCD','CUSUM','DDM','ECDD','EDDM','GMA','HDDMA','HDDMW','KSWIN','PH','RDDM','STEPD']):
    
    """ This method computes the average ranks for the statistical test of the respective models over all datasets"""
    dict_detectors = {}
    
    dict_detectors_insects = create_dict_detectors_insects(metric, bal=True, imbal=True, classifiers=classifiers, drifts=['abrupt','gradual','incr','incr-abrupt','ince-reoc','ooc'], detectors=detectors)
    
    dict_detectors_synth = create_dict_detectors_synth(metric, 
                                                       generators=['agrawal1','agrawal2','mixed','sea','sine','stagger'], 
                                                       sizes=['10K','20K','50K','100K','500K','1M'],
                                                       detectors=detectors, 
                                                       nb=('NB' in classifiers), ht=('HT' in classifiers), ensemble=('BOLE' in classifiers),
                                                       abrupt=True, gradual=True)
        
    dict_detectors_real = create_dict_detectors_real(metric,classifiers=classifiers,datasets=['Covertype','Elec2','SensorStream'],detectors=detectors)
    
    for key,value in dict_detectors_insects.items():
        dict_detectors[key] = dict_detectors_insects[key] + dict_detectors_synth[key] + dict_detectors_real[key]
    
    
    data = (
            pd.DataFrame(dict_detectors)
            .rename_axis('dataset')
            .melt(
                var_name='estimator',
                value_name='score',
                ignore_index=False,
                )
            .reset_index()
            )
    
    avg_rank = data.groupby('dataset').score.rank(ascending=ascending).groupby(data.estimator).mean()


    return data, avg_rank


def print_CD_diagram(data,avg_rank,fname:str="",titel:str=""):

    test_results = sp.posthoc_nemenyi_friedman(
        data,
        melted=True,
        block_col='dataset',
        group_col='estimator',
        y_col='score',
        )
    sp.sign_plot(test_results)
    
    cm = 1/2.54 # centimeters in inches
    plt.figure(figsize=(12*cm, 2), dpi=100)
    
    if titel != "":
        plt.title('CD diagram: ' + titel)
        
    sp.critical_difference_diagram(ranks=avg_rank,
                                   sig_matrix=test_results,
                                   label_fmt_left='{label} [{rank:.2f}]  ',
                                   label_fmt_right='  [{rank:.2f}] {label}',
                                   label_props={'color':'black'},
                                   crossbar_props={'color':'red'},
                                   elbow_props={'color':'gray'})
    if fname == "":
        plt.show()
    else:
        plt.savefig(fname,bbox_inches='tight')
    

    
    
    
    