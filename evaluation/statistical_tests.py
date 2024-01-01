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
from scipy import stats

def create_dict_detectors_synth(metric:str, generators:list=['agrawal1','agrawal2','mixed','sea','sine','stagger'], 
                                sizes:list=['10K','20K','50K','100K','500K','1M'], 
                                detectors:list=['basic','ADWIN','BOCD','CUSUM','DDM','ECDD','EDDM','GMA','HDDMA','HDDMW','KSWIN','PH','RDDM','STEPD'], 
                                nb:bool=True, ht:bool=True,ensemble:bool=True, 
                                abrupt:bool=True, gradual:bool=True, friedman:bool=False) -> dict:
    
    """ This method creates a dictionary for the statistical evaluation of the synthetic datasets"""
    df = read_all_result_files()
    value = None 
    if friedman:
        value = 0

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
                        else: dict_detectors[detector].append(value) #was None before
                    if gradual:
                        df_gradual_HT =  df[(df['size']==size) & (df['generator']==generator) & (df['detector']==detector) & (df['drift_type']=='gradual')
                                 & (df['classifier']=='HT')]
                        if df_gradual_HT[metric].size != 0:
                            dict_detectors[detector].append(df_gradual_HT[metric].values[0])
                        else: dict_detectors[detector].append(value)  #was None before
                if nb:
                    if abrupt:
                        df_abrupt_NB = df[(df['size']==size) & (df['generator']==generator) & (df['detector']==detector) & (df['drift_type']=='abrupt')
                                 & (df['classifier']=='NB')]
                        if df_abrupt_NB[metric].size != 0:
                            dict_detectors[detector].append(df_abrupt_NB[metric].values[0])
                        else: dict_detectors[detector].append(value)  #was None before
                    if gradual:
                        df_gradual_NB =  df[(df['size']==size) & (df['generator']==generator) & (df['detector']==detector) & (df['drift_type']=='gradual')
                                 & (df['classifier']=='NB')]
                        if df_gradual_NB[metric].size != 0:
                            dict_detectors[detector].append(df_gradual_NB[metric].values[0])
                        else: dict_detectors[detector].append(value)  #was None before
                        
                if ensemble:
                     if abrupt:
                         df_abrupt_BOLE = df[(df['size']==size) & (df['generator']==generator) & (df['detector']==detector) & (df['drift_type']=='abrupt')
                                  & (df['classifier']=='BOLE')]
                         if df_abrupt_BOLE[metric].size != 0:
                             dict_detectors[detector].append(df_abrupt_BOLE[metric].values[0])
                         else: dict_detectors[detector].append(value)  #was None before
                     if gradual:
                         df_gradual_BOLE = df[(df['size']==size) & (df['generator']==generator) & (df['detector']==detector) & (df['drift_type']=='gradual')
                                  & (df['classifier']=='BOLE')]
                         if df_gradual_BOLE[metric].size != 0:
                             dict_detectors[detector].append(df_gradual_BOLE[metric].values[0])
                         else: dict_detectors[detector].append(value)  #was None before              
                
    return dict_detectors

def create_dict_detectors_insects(metric:str, bal:bool, imbal:bool, classifiers:list, drifts:list,detectors:list,friedman:bool=False) -> dict:
    
    """ This method creates a dictionary for the statistical evaluation of the Insects datasets"""
    
    df = read_all_result_files(generators=['insects'])
    df_insects = df[df['generator']=='Insects']
    df_bal = df_insects[df_insects['size']=='bal']
    df_imbal = df_insects[df_insects['size']=='imbal']
    
    dict_detectors = {}
    value = None
    
    if friedman:
        value=0
        
    
    for detector in detectors: 
        dict_detectors[detector]=[]

    for drift in drifts:
        for detector in detectors:
            for classifier in classifiers:
                if bal:
                    df_current = df_bal[(df_bal['detector']==detector)&(df_bal['drift_type']==drift)&(df_bal['classifier']==classifier)]

                    if df_current[metric].size != 0:
                        dict_detectors[detector].append(df_current[metric].values[0])
                    else: dict_detectors[detector].append(value)
                if imbal:
                    df_current = df_imbal[(df_imbal['detector']==detector)&(df_imbal['drift_type']==drift)&(df_imbal['classifier']==classifier)]
                    if df_current[metric].size != 0:
                        dict_detectors[detector].append(df_current[metric].values[0])
                    else: dict_detectors[detector].append(value)
             
                
    return dict_detectors

def create_dict_detectors_real(metric:str,classifiers:list,datasets:list,detectors:list,friedman:bool=False) -> dict:
    """ This method creates a dictionary for the statistical evaluation of the real-world datasets"""
    df = read_all_result_files(generators=['real-world'])
    
    value = None 
    if friedman:
        value = 0
    
    dict_detectors = {}
    
    for detector in detectors: 
        dict_detectors[detector]=[]

    for dataset in datasets:
        for detector in detectors:
            for classifier in classifiers:
                df_current = df[(df['detector']==detector)&(df['classifier']==classifier)&(df['generator']==dataset)]

                if df_current[metric].size != 0:
                    dict_detectors[detector].append(df_current[metric].values[0])
                else: dict_detectors[detector].append(value)

    return dict_detectors

def get_mean_synth(metric:str, generators:list=['agrawal1','agrawal2','mixed','sea','sine','stagger'],
                   sizes:list=['10K','20K','50K','100K','500K','1M'], 
                   detectors:list=['basic','ADWIN','BOCD','CUSUM','DDM','ECDD','EDDM','GMA','HDDMA','HDDMW','KSWIN','PH','RDDM','STEPD'], 
                   nb:bool=True, ht:bool=True, ensemble:bool=True, abrupt:bool=True, gradual:bool=True) -> dict:
    
    dict_detectors = create_dict_detectors_synth(metric=metric, generators=generators, sizes=sizes,
                                                 detectors=detectors, nb=nb, ht=ht, ensemble=ensemble,
                                                 abrupt=abrupt, gradual=gradual)
    
    for key in dict_detectors:
        new_dict = np.array(dict_detectors[key], dtype=np.float64)
        dict_detectors[key] = np.nanmean(new_dict)
    
    return dict_detectors

def get_mean_insects(metric:str, 
                   variants:list=['abrupt','gradual','incremental-abrupt','incremental-reoccurring'], 
                   classifiers=['NB','HT'],
                   detectors:list=['basic','ADWIN','BOCD','CUSUM','DDM','ECDD','EDDM','GMA','HDDMA','HDDMW','KSWIN','PH','RDDM','STEPD'], 
                   nb:bool=True, ht:bool=True, ensemble:bool=True, bal:bool=True, imbal:bool=True) -> dict:
    
    dict_detectors = create_dict_detectors_insects(metric=metric, bal=bal, imbal=imbal, 
                                                   classifiers=classifiers, drifts=variants, detectors=detectors) 
    
    for key in dict_detectors:
        new_dict = np.array(dict_detectors[key], dtype=np.float64)
        dict_detectors[key] = np.nanmean(new_dict)
    
    return dict_detectors

def get_mean_all(metric:str, 
                  classifiers=['NB','HT','BOLE'],datasets=['synthetic','real-world','insects'],
                  detectors=['basic','ADWIN','BOCD','CUSUM','DDM','ECDD','EDDM','GMA','HDDMA','HDDMW','KSWIN','PH','RDDM','STEPD']) -> dict:
    
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
        
    for key in dict_detectors:
        new_dict = np.array(dict_detectors[key], dtype=np.float64)
        dict_detectors[key] = np.nanmean(new_dict)
    
    return dict_detectors

def get_avg_rank_synth(metric:str, generators:list=['agrawal1','agrawal2','mixed','sea','sine','stagger'], sizes:list=['10K','20K','50K','100K','500K','1M'], 
                       detectors:list=['basic','ADWIN','BOCD','CUSUM','DDM','ECDD','EDDM','GMA','HDDMA','HDDMW','KSWIN','PH','RDDM','STEPD'],
                       ascending=True, nb:bool=True, ht:bool=True, ensemble:bool=True, abrupt:bool=True, gradual:bool=True, to:bool=False):
    
    """ This method computes the average ranks for the statistical test of the respective models over the synthetic datasets"""
    
    dict_detectors = create_dict_detectors_synth(metric, generators, sizes, detectors,nb=nb, ht=ht, ensemble=ensemble, abrupt=abrupt, gradual=gradual)
    
    if to:
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

def get_avg_rank_insects(metric:str, ascending=True, bal:bool=True, imbal:bool=True, classifiers:list=['NB','HT','BOLE'], drifts:list=['abrupt','gradual','incremental','incremental-abrupt','incremental-reoccurring'], 
                                  detectors:list=['basic','ADWIN','BOCD','CUSUM','DDM','ECDD','EDDM','GMA','HDDMA','HDDMW','KSWIN','PH','RDDM','STEPD']):
    
    """ This method computes the average ranks for the statistical test of the respective models over the Insects datasets"""
    dict_detectors = create_dict_detectors_insects(metric, bal=bal, imbal=imbal, classifiers=classifiers, drifts=drifts, detectors=detectors)
    
    if 'incremental' in drifts and 'BOCD' in detectors and 'BOLE' in classifiers and bal:
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
    
    if 'SensorStream' in datasets and 'BOCD' in dict_detectors:
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
    
    if 'BOCD' in dict_detectors :
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
        
def friedman_nemenyi_test_all(metric:str, ascending=True, classifiers=['NB','HT','BOLE'],datasets=['synthetic','real-world','insects'],
                              detectors=['basic','ADWIN','BOCD','CUSUM','DDM','ECDD','EDDM','GMA','HDDMA','HDDMW','KSWIN','PH','RDDM','STEPD'], fname:str='', titel:str=''):
    
    ''' This method first computed the Friedman test, if it was successfull the post-hoc Nemenyi test is applied '''
    
    #Friedman test can not handle None values, consequently an separate dictionary is loaded, where the None values are represented as 0 
    dict_detectors = {}
    dict_detectors_insects = create_dict_detectors_insects(metric, bal=True, imbal=True, classifiers=classifiers, 
                                                           drifts=['abrupt','gradual','incr','incr-abrupt','ince-reoc','ooc'], detectors=detectors, 
                                                           friedman=True)
    dict_detectors_synth = create_dict_detectors_synth(metric, 
                                                       generators=['agrawal1','agrawal2','mixed','sea','sine','stagger'], 
                                                       sizes=['10K','20K','50K','100K','500K','1M'],
                                                       detectors=detectors, 
                                                       nb=('NB' in classifiers), ht=('HT' in classifiers), ensemble=('BOLE' in classifiers),
                                                       abrupt=True, gradual=True, friedman=True)
    dict_detectors_real = create_dict_detectors_real(metric,classifiers=classifiers,datasets=['Covertype','Elec2','SensorStream'],detectors=detectors,
                                                     friedman=True)
    
    for key,value in dict_detectors_insects.items():
        dict_detectors[key] = dict_detectors_insects[key] + dict_detectors_synth[key] + dict_detectors_real[key]
    
    results = stats.friedmanchisquare(*dict_detectors.values())
    
    if results.pvalue < 0.05:
        #Nemenyi test works with None values and would generated corrupted results on 0s, as it would always rank them last
        data, avg_rank = get_avg_rank_all(metric=metric, ascending=ascending, classifiers=classifiers, datasets=datasets, detectors=detectors)
        
        if titel !='':
            print_CD_diagram(data, avg_rank, fname='', titel=titel)
        if fname !='':
            print_CD_diagram(data, avg_rank, fname=fname, titel='')
        if titel == '' and fname == '':
            print_CD_diagram(data, avg_rank, fname=fname, titel=titel)
    
    # returns if Friedman test passed and consequently if Nemenyi test was computed
    return results.pvalue < 0.05

def friedman_nemenyi_test_insects(metric:str, classifiers:list=['NB','HT','BOLE'],
                                  drifts:list=['abrupt','gradual','incremental','incremental-abrupt','incremental-reoccurring'],
                       detectors:list=['basic','ADWIN','BOCD','CUSUM','DDM','ECDD','EDDM','GMA','HDDMA','HDDMW','KSWIN','PH','RDDM','STEPD'],
                       ascending=True, bal:bool=True, imbal:bool=True, fname:str='', titel:str=''):
    
    ''' This method first computed the Friedman test, if it was successfull the post-hoc Nemenyi test is applied '''
    
    #Friedman test can not handle None values, consequently an separate dictionary is loaded, where the None values are represented as 0 
    dict_detectors = create_dict_detectors_insects(metric=metric, bal=bal, imbal=imbal, classifiers=classifiers, 
                                                   drifts=drifts,detectors=detectors,friedman=True)
    
    results = stats.friedmanchisquare(*dict_detectors.values())
    
    if results.pvalue < 0.05:
        #Nemenyi test works with None values and would generated corrupted results on 0s, as it would always rank them last
        data, avg_rank = get_avg_rank_insects(metric=metric, ascending=ascending, bal=bal, imbal=imbal, classifiers=classifiers, drifts=drifts, 
                                          detectors=detectors)
        
        if titel !='':
            print_CD_diagram(data, avg_rank, fname='', titel=titel)
        if fname !='':
            print_CD_diagram(data, avg_rank, fname=fname, titel='')
        if titel == '' and fname == '':
            print_CD_diagram(data, avg_rank, fname=fname, titel=titel)
    
    # returns if Friedman test passed and consequently if Nemenyi test was computed
    return results.pvalue < 0.05

def friedman_nemenyi_test_synth(metric:str, generators:list=['agrawal1','agrawal2','mixed','sea','sine','stagger'], sizes:list=['10K','20K','50K','100K','500K','1M'], 
                       detectors:list=['basic','ADWIN','BOCD','CUSUM','DDM','ECDD','EDDM','GMA','HDDMA','HDDMW','KSWIN','PH','RDDM','STEPD'],
                       ascending=True, nb:bool=True, ht:bool=True, ensemble:bool=True, abrupt:bool=True, gradual:bool=True, to:bool=False, fname:str='', titel:str=''):
    
    ''' This method first computed the Friedman test, if it was successfull the post-hoc Nemenyi test is applied '''
    
    #Friedman test can not handle None values, consequently an separate dictionary is loaded, where the None values are represented as 0 
    dict_detectors = create_dict_detectors_synth(metric=metric, generators=generators,sizes=sizes,detectors=detectors, 
                                    nb=nb, ht=ht, ensemble=ensemble, abrupt=abrupt, gradual=gradual, friedman=True)
    
    results = stats.friedmanchisquare(*dict_detectors.values())
    
    if results.pvalue < 0.05:
        #Nemenyi test works with None values and would generated corrupted results on 0s, as it would always rank them last
        data, avg_rank = get_avg_rank_synth(metric=metric, generators=generators, sizes=sizes, detectors=detectors,
                           ascending=ascending, nb=nb, ht=ht, ensemble=ensemble, abrupt=abrupt, gradual=gradual, to=to)
        
        if titel !='':
            print_CD_diagram(data, avg_rank, fname='', titel=titel)
        if fname !='':
            print_CD_diagram(data, avg_rank, fname=fname, titel='')
        if titel == '' and fname == '':
            print_CD_diagram(data, avg_rank, fname=fname, titel=titel)
    
    # returns if Friedman test passed and consequently if Nemenyi test was computed
    return results.pvalue < 0.05
    
def friedman_nemenyi_test_real(metric:str, datasets:list=['Covertype','Elec2','SensorStream'], classifiers:list=['NB','HT','BOLE'],
                       detectors:list=['basic','ADWIN','BOCD','CUSUM','DDM','ECDD','EDDM','GMA','HDDMA','HDDMW','KSWIN','PH','RDDM','STEPD'],
                       ascending=True, fname:str='', titel:str=''):
    
    ''' This method first computed the Friedman test, if it was successfull the post-hoc Nemenyi test is applied '''
    
    #Friedman test can not handle None values, consequently an separate dictionary is loaded, where the None values are represented as 0 
    dict_detectors = create_dict_detectors_real(metric=metric, classifiers=classifiers,datasets=datasets,detectors=detectors, friedman=True)
    
    results = stats.friedmanchisquare(*dict_detectors.values())
    
    if results.pvalue < 0.05:
        #Nemenyi test works with None values and would generated corrupted results on 0s, as it would always rank them last
        data, avg_rank = get_avg_rank_real(metric=metric, classifiers=classifiers, detectors=detectors, datasets=datasets,
                           ascending=ascending)
        
        if titel !='':
            print_CD_diagram(data, avg_rank, fname='', titel=titel)
        if fname !='':
            print_CD_diagram(data, avg_rank, fname=fname, titel='')
        if titel == '' and fname == '':
            print_CD_diagram(data, avg_rank, fname=fname, titel=titel)
            
    print(results.pvalue)
    # returns if Friedman test passed and consequently if Nemenyi test was computed
    return results.pvalue < 0.05

    
    
    
    