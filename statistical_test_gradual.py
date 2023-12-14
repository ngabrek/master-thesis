# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 15:14:08 2023

@author: nadin
"""

from evaluation.statistical_tests import get_avg_rank_synth, print_CD_diagram

#all
data, avg_rank = get_avg_rank_synth('accuracy_mean',ascending=False,abrupt=False)
print_CD_diagram(data, avg_rank, 'plots/CD_gradual.png')

#10K synthetic datasets
data, avg_rank = get_avg_rank_synth('accuracy_mean',sizes=['10K'],ascending=False,abrupt=False)
print_CD_diagram(data, avg_rank, 'plots/CD_gradual_10K.png')

data, avg_rank = get_avg_rank_synth('accuracy_mean',sizes=['10K'],ascending=False,ensemble=False,ht=False,abrupt=False)
print_CD_diagram(data, avg_rank, 'plots/CD_gradual_10K_NB.png')

data, avg_rank = get_avg_rank_synth('accuracy_mean',sizes=['10K'],ascending=False,ensemble=False,nb=False,abrupt=False)
print_CD_diagram(data, avg_rank, 'plots/CD_gradual_10K_HT.png')

#data, avg_rank = get_avg_rank_synth('accuracy_mean',sizes=['10K'],ascending=False,nb=False,ht=False,abrupt=False)
#print_CD_diagram(data, avg_rank, 'plots/CD_gradual_10K_BOLE.png')

#20K synthetic datasets
data, avg_rank = get_avg_rank_synth('accuracy_mean',sizes=['20K'],ascending=False,abrupt=False)
print_CD_diagram(data, avg_rank, 'plots/CD_gradual_20K.png')

data, avg_rank = get_avg_rank_synth('accuracy_mean',sizes=['20K'],ascending=False,ensemble=False,ht=False,abrupt=False)
print_CD_diagram(data, avg_rank, 'plots/CD_gradual_20K_NB.png')

data, avg_rank = get_avg_rank_synth('accuracy_mean',sizes=['20K'],ascending=False,ensemble=False,nb=False,abrupt=False)
print_CD_diagram(data, avg_rank, 'plots/CD_gradual_20K_HT.png')

#data, avg_rank = get_avg_rank_synth('accuracy_mean',sizes=['20K'],ascending=False,nb=False,ht=False,abrupt=False)
#print_CD_diagram(data, avg_rank, 'plots/CD_gradual_20K_BOLE.png')
