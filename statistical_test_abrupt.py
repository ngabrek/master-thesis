# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 15:14:08 2023

@author: nadin
"""

from evaluation.statistical_tests import get_avg_rank_synth, print_CD_diagram

data, avg_rank = get_avg_rank_synth('accuracy_mean',sizes=['10K'],ascending=False,ensemble=False,gradual=False)
print_CD_diagram(data, avg_rank, 'plots/CD_abrupt_10K.png')

data, avg_rank = get_avg_rank_synth('accuracy_mean',sizes=['10K'],ascending=False,ensemble=False,ht=False,gradual=False)
print_CD_diagram(data, avg_rank, 'plots/CD_abrupt_10K_NB.png')

data, avg_rank = get_avg_rank_synth('accuracy_mean',sizes=['10K'],ascending=False,ensemble=False,nb=False,gradual=False)
print_CD_diagram(data, avg_rank, 'plots/CD_abrupt_10K_HT.png')
