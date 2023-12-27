# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 18:14:03 2023

@author: nadin
"""
from pathlib import Path
import sys
import os 
path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

# Import to write and read csv files
import pandas as pd

def write_results_to_csv(path:str, results:pd.DataFrame, index:bool=True, sep:str=','):
    
    """Write the results of the model evaluation into a csv-file"""
    
    results.to_csv(path,index=index, sep=sep) 


def read_results_from_csv(filepath:str, index:bool=True, sep:str=',')->pd.DataFrame:
     
    """Read evaluation results from a csv file and transform it into a pandas DataFrame for further analysis"""
    
    if index:    
        return pd.read_csv(filepath, header=0, index_col=0, sep=sep)
    else:
        return pd.read_csv(filepath, header=0, sep=sep)
    
    
def read_all_result_files(generators=['agrawal1','agrawal2','mixed','sine','stagger','sea','insects','real-world'])->pd.DataFrame:
    current_path = os.getcwd()

    final_df = pd.DataFrame()

    for generator in generators:
        os.chdir(f'results/{generator}/final_results')
        
        csv_files = [f for f in os.listdir() if f.endswith('.csv')]
       
        for csv in csv_files:
            df = read_results_from_csv(csv, index=False, sep=';')
            final_df = pd.concat([df, final_df], ignore_index=True)
            
        os.chdir(current_path)


    return final_df.drop_duplicates(keep='first')

