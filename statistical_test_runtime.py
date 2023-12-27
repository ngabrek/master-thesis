# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 14:44:13 2023

@author: nadin
"""

from evaluation.statistical_tests import get_avg_rank_real, get_avg_rank_insects, get_avg_rank_synth, get_avg_rank_all, print_CD_diagram, get_mean_all

'''include all models in all datasets'''
#data, avg_rank = get_avg_rank_all('time_mean')
#print_CD_diagram(data, avg_rank, titel="runtime of detectors on all datasets (new)")
#print_CD_diagram(data, avg_rank, 'plots/CD_runtime.png')

print(get_mean_all('time_mean'))

'''include all models in synthetic datasets'''
#data, avg_rank = get_avg_rank_synth('time_mean')
#print_CD_diagram(data, avg_rank, titel="runtime of detectors in the synthetic datasets (new)")
#print_CD_diagram(data, avg_rank, 'plots/CD_runtime_synth.png')

'''include all models in Insects datasets'''
#data, avg_rank = get_avg_rank_insects('time_mean')
#print_CD_diagram(data, avg_rank, titel="runtime of detectors in the Insects datasets (new)")
#print_CD_diagram(data, avg_rank, 'plots/CD_runtime_insects.png')

'''include all models in real-datasets'''
#data, avg_rank = get_avg_rank_real('time_mean')
#print_CD_diagram(data, avg_rank, titel="runtime of detectors in the real-world datasets (new)")
#print_CD_diagram(data, avg_rank, 'plots/CD_runtime_real.png')


'''include NB in all datasets'''
#data, avg_rank = get_avg_rank_all('time_mean',classifiers=['NB'])
#print_CD_diagram(data, avg_rank, titel="runtime of detectors with NB on all datasets (new)")
#print_CD_diagram(data, avg_rank, 'plots/CD_runtime_NB.png')

'''include HT in all datasets'''
#data, avg_rank = get_avg_rank_all('time_mean',classifiers=['HT'])
#print_CD_diagram(data, avg_rank, titel="runtime of detectors with HT on all datasets (new)")
#print_CD_diagram(data, avg_rank, 'plots/CD_runtime_HT.png')

'''include HT in all datasets'''
#data, avg_rank = get_avg_rank_all('time_mean',classifiers=['BOLE'])
#print_CD_diagram(data, avg_rank, titel="runtime of detectors with BOLE on all datasets (new)")
#print_CD_diagram(data, avg_rank, 'plots/CD_runtime_BOLE.png')

