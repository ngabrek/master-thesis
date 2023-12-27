# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 14:44:13 2023

@author: nadin
"""

from evaluation.statistical_tests import get_avg_rank_real, get_avg_rank_insects, get_avg_rank_synth, get_avg_rank_all, print_CD_diagram, get_mean_all

'''include all models in all datasets'''
data, avg_rank = get_avg_rank_all('memory_mean')
print_CD_diagram(data, avg_rank, titel="memory of detectors on all datasets (new)")
print_CD_diagram(data, avg_rank, 'plots/CD_memory.png')

print(get_mean_all('memory_mean'))

'''include all models in synthetic datasets'''
data, avg_rank = get_avg_rank_synth('memory_mean')
print_CD_diagram(data, avg_rank, titel="memory of detectors in the synthetic datasets (new)")
print_CD_diagram(data, avg_rank, 'plots/CD_memory_synth.png')

'''include all models in Insects datasets'''
data, avg_rank = get_avg_rank_insects('memory_mean')
print_CD_diagram(data, avg_rank, titel="memory of detectors in the Insects datasets (new)")
print_CD_diagram(data, avg_rank, 'plots/CD_memory_insects.png')

'''include all models in real-datasets'''
data, avg_rank = get_avg_rank_real('memory_mean')
print_CD_diagram(data, avg_rank, titel="memory of detectors in the real-world datasets (new)")
print_CD_diagram(data, avg_rank, 'plots/CD_memory_real.png')


'''include NB in all datasets'''
data, avg_rank = get_avg_rank_all('memory_mean',classifiers=['NB'])
print_CD_diagram(data, avg_rank, titel="memory of detectors with NB on all datasets (new)")
print_CD_diagram(data, avg_rank, 'plots/CD_memory_NB.png')

'''include HT in all datasets'''
data, avg_rank = get_avg_rank_all('memory_mean',classifiers=['HT'])
print_CD_diagram(data, avg_rank, titel="memory of detectors with HT on all datasets (new)")
print_CD_diagram(data, avg_rank, 'plots/CD_memory_HT.png')

'''include HT in all datasets'''
data, avg_rank = get_avg_rank_all('memory_mean',classifiers=['BOLE'])
print_CD_diagram(data, avg_rank, titel="memory of detectors with BOLE on all datasets (new)")
print_CD_diagram(data, avg_rank, 'plots/CD_memory_BOLE.png')

