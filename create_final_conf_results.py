# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 12:00:20 2023

@author: nadin
"""

from utils.create_results_file import create_results_file
from utils.read_and_write import write_results_to_csv

#generators = ['agrawal1', 'agrawal2', 'mixed', 'sine','stagger','sea']
#sizes = ['10K', '20K', '50K', '100K', '500K', '1M']

generators = ['agrawal2','sine']
sizes = ['10K']


for generator in generators:
    print(generator)
    for size in sizes:
        print(size)
        df = create_results_file(f'results/{generator}/{size}')
        write_results_to_csv(f'results/{generator}/final_results/conf_{generator}_{size}_f.csv', df, index=False, sep=';')

