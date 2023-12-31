# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 12:28:09 2023

@author: nadin
"""
from evaluation.statistical_tests import get_avg_rank_insects,print_CD_diagram,get_mean_synth, get_mean_insects, friedman_nemenyi_test_synth, friedman_nemenyi_test_insects

'''include NB and HT on synthetic datasets'''
#print(friedman_nemenyi_test_synth('drifts_mean',ascending=False,ensemble=False,to=True,titel="Average drifts of detectors in the synthetic datasets"))
#print(friedman_nemenyi_test_synth('drifts_mean',ascending=False,ensemble=False,to=True,fname='plots/CD_drifts_synth.png'))
#print(get_mean_synth('drifts_mean',ensemble=False))



'''include NB and HT on Insect datasets'''
print(friedman_nemenyi_test_insects('accuracy_mean',ascending=False,classifiers=['NB','HT'],drifts=['abrupt','gradual','incr-abrupt','ince-reoc'],titel='Accuracy of detectors with NB+HT in certain Insect datasets'))
print(friedman_nemenyi_test_insects('accuracy_mean',ascending=False,classifiers=['NB','HT'],drifts=['abrupt','gradual','incr-abrupt','ince-reoc'],fname='plots/CD_accuracy_insect_NB+HT'))

print(friedman_nemenyi_test_insects('drifts_mean',ascending=False,classifiers=['NB','HT'],drifts=['abrupt','gradual','incr-abrupt','ince-reoc'],titel='Drifts of detectors with NB+HT in certain Insect datasets'))
print(friedman_nemenyi_test_insects('drifts_mean',ascending=False,classifiers=['NB','HT'],drifts=['abrupt','gradual','incr-abrupt','ince-reoc'],fname='plots/CD_drifts_insect_NB+HT'))

'''abrupt, balanced Insect dataset'''
print('abrupt-bal')
print(get_mean_insects('drifts_mean',variants=['abrupt'],classifiers=['NB','HT'],imbal=False))
print()

'''gradual, balanced Insect dataset'''
print('gradual-bal')
print(get_mean_insects('drifts_mean',variants=['gradual'],classifiers=['NB','HT'],imbal=False))
print()

'''incremental-abrupt, balanced Insect dataset'''
print('incremental-abrupt-bal')
print(get_mean_insects('drifts_mean',variants=['incremental-abrupt'],classifiers=['NB','HT'],imbal=False))
print()

'''incremental-reoccurring, balanced Insect dataset'''
print('incremental-reoccuring-bal')
print(get_mean_insects('drifts_mean',variants=['incremental-reoccurring'],classifiers=['NB','HT'],imbal=False))
print()

'''abrupt, imbalanced Insect dataset'''
print('abrupt-imbal')
print(get_mean_insects('drifts_mean',variants=['abrupt'],classifiers=['NB','HT'],bal=False))
print()

'''gradual, imbalanced Insect dataset'''
print('gradual-imbal')
print(get_mean_insects('drifts_mean',variants=['gradual'],classifiers=['NB','HT'],bal=False))
print()

'''incremental-abrupt, imbalanced Insect dataset'''
print('incremental-abrupt-imbal')
print(get_mean_insects('drifts_mean',variants=['incremental-abrupt'],classifiers=['NB','HT'],bal=False))
print()

'''incremental-reoccurring, imbalanced Insect dataset'''
print('incremental-reoccuring-imbal')
print(get_mean_insects('drifts_mean',variants=['incremental-reoccurring'],classifiers=['NB','HT'],bal=False))
print()
