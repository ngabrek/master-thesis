# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 12:28:09 2023

@author: nadin
"""
from evaluation.statistical_tests import get_avg_rank_synth, print_CD_diagram, get_mean_synth, get_avg_rank_insects, get_mean_insects

'''include NB and HT on synthetic datasets'''
#data, avg_rank = get_avg_rank_synth('drifts_mean',ascending=False, ensemble=False)
#print_CD_diagram(data, avg_rank, titel="drifts of detectors with NB and HT in the synthetic datasets")
#print(get_mean_synth('drifts_mean',ensemble=False))

'''include NB and HT on Insect datasets'''
data, avg_rank = get_avg_rank_insects('accuracy_mean',ascending=False,drifts=['abrupt','gradual','incr-abrupt','ince-reoc'],
                                      classifiers=['NB','HT'])
print_CD_diagram(data, avg_rank, titel="accuracy of detectors with NB and HT in the Insects dataset variants abrupt, gradual, incr-abrupt and incr.-reocc.")
'''include NB and HT on Insect datasets'''
data, avg_rank = get_avg_rank_insects('drifts_mean',ascending=False,drifts=['abrupt','gradual','incr-abrupt','ince-reoc'],
                                      classifiers=['NB','HT'])
print_CD_diagram(data, avg_rank, titel="drifts of detectors with NB and HT in the Insects dataset variants abrupt, gradual, incr-abrupt and incr.-reocc.")
#abrupt, balanced
print('abrupt-bal')
print(get_mean_insects('drifts_mean',variants=['abrupt'],classifiers=['NB','HT'],imbal=False))
print()
#gradual, balanced
print('gradual-bal')
print(get_mean_insects('drifts_mean',variants=['gradual'],classifiers=['NB','HT'],imbal=False))
print()
#incremental-abrupt, balanced
print('incremental-abrupt-bal')
print(get_mean_insects('drifts_mean',variants=['incremental-abrupt'],classifiers=['NB','HT'],imbal=False))
print()
#incremental-reoccurring, balanced
print('incremental-reoccuring-bal')
print(get_mean_insects('drifts_mean',variants=['incremental-reoccurring'],classifiers=['NB','HT'],imbal=False))

#abrupt, imbalanced
print('abrupt-imbal')
print(get_mean_insects('drifts_mean',variants=['abrupt'],classifiers=['NB','HT'],bal=False))
print()
#gradual, imbalanced
print('gradual-imbal')
print(get_mean_insects('drifts_mean',variants=['gradual'],classifiers=['NB','HT'],bal=False))
print()
#incremental-abrupt, imbalanced
print('incremental-abrupt-imbal')
print(get_mean_insects('drifts_mean',variants=['incremental-abrupt'],classifiers=['NB','HT'],bal=False))
print()
#incremental-reoccurring, imbalanced
print('incremental-reoccuring-imbal')
print(get_mean_insects('drifts_mean',variants=['incremental-reoccurring'],classifiers=['NB','HT'],bal=False))
