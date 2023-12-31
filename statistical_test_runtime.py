# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 14:44:13 2023

@author: nadin
"""

from evaluation.statistical_tests import get_mean_all, friedman_nemenyi_test_all, friedman_nemenyi_test_insects, friedman_nemenyi_test_real, friedman_nemenyi_test_synth

'''include all models in all datasets'''
print(friedman_nemenyi_test_all('time_mean',titel='Runtime of detectors in all datasets'))
print(friedman_nemenyi_test_all('time_mean',fname='plots/CD_runtime'))

print(get_mean_all('time_mean'))

'''include all models in synthetic datasets'''
print(friedman_nemenyi_test_synth('time_mean',to=True,titel="Runtime of detectors in the synthetic datasets"))
print(friedman_nemenyi_test_synth('time_mean',to=True,fname='plots/CD_runtime_synth.png'))
#abrupt drift
print(friedman_nemenyi_test_synth('time_mean',gradual=False,to=True,titel="Runtime of detectors in the abrupt synthetic datasets"))
print(friedman_nemenyi_test_synth('time_mean',to=True,gradual=False,fname='plots/CD_runtime_synth_abrupt.png'))
#gradual drift
print(friedman_nemenyi_test_synth('time_mean',abrupt=False,to=True,titel="Runtime of detectors in the gradual synthetic datasets"))
print(friedman_nemenyi_test_synth('time_mean',to=True,abrupt=False,fname='plots/CD_runtime_synth_gradual.png'))

'''include all models in Insects datasets'''
print(friedman_nemenyi_test_insects('time_mean',titel='Runtime of detectors in the Insect datasets'))
print(friedman_nemenyi_test_insects('time_mean',fname='plots/CD_runtime_insect'))

'''include all models in real-datasets'''
print(friedman_nemenyi_test_real('time_mean',titel='Runtime of detectors in the real-world datasets'))
print(friedman_nemenyi_test_real('time_mean',fname='plots/CD_runtime_real'))


'''include NB in all datasets'''
print(friedman_nemenyi_test_all('time_mean',classifiers=['NB'],titel='Runtime of detectors with NB in all datasets'))
print(friedman_nemenyi_test_all('time_mean',classifiers=['NB'],fname='plots/CD_runtime_NB'))

'''include HT in all datasets'''
print(friedman_nemenyi_test_all('time_mean',classifiers=['HT'],titel='Runtime of detectors with HT in all datasets'))
print(friedman_nemenyi_test_all('time_mean',classifiers=['HT'],fname='plots/CD_runtime_HT'))

'''include HT in all datasets'''
print(friedman_nemenyi_test_all('time_mean',classifiers=['BOLE'],titel='Runtime of detectors with BOLE in all datasets'))
print(friedman_nemenyi_test_all('time_mean',classifiers=['BOLE'],fname='plots/CD_runtime_BOLE'))



