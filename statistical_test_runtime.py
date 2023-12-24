# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 14:44:13 2023

@author: nadin
"""

from evaluation.statistical_tests import get_avg_rank_real, get_avg_rank_insects, get_avg_rank_synth, get_avg_rank_all, print_CD_diagram

'''include all models in all datasets'''
data, avg_rank = get_avg_rank_all('time_mean')
print_CD_diagram(data, avg_rank, titel="runtime of detectors on all datasets (new)")

'''include all models in synthetic datasets'''
data, avg_rank = get_avg_rank_synth('time_mean')
print_CD_diagram(data, avg_rank, titel="runtime of detectors in the synthetic datasets (new)")

'''include all models in Insects datasets'''
data, avg_rank = get_avg_rank_insects('time_mean')
print_CD_diagram(data, avg_rank, titel="runtime of detectors in the Insects datasets (new)")

'''include all models in real-datasets'''
data, avg_rank = get_avg_rank_real('time_mean')
print_CD_diagram(data, avg_rank, titel="runtime of detectors in the real-world datasets (new)")


