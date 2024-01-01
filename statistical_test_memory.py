# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 14:44:13 2023

@author: nadin
"""

from evaluation.statistical_tests import get_mean_all, friedman_nemenyi_test_all,friedman_nemenyi_test_insects,friedman_nemenyi_test_real,friedman_nemenyi_test_synth

'''include all models in all datasets'''
print(friedman_nemenyi_test_all('memory_mean',titel='Memory consumption of detectors in all datasets'))
print(friedman_nemenyi_test_all('memory_mean',fname='plots/CD_memory'))

print(get_mean_all('memory_mean'))

'''include all models in synthetic datasets'''
print(friedman_nemenyi_test_synth('memory_mean',to=True,titel="Memory consumption of detectors in the synthetic datasets"))
print(friedman_nemenyi_test_synth('memory_mean',to=True,fname='plots/CD_memory_synth.png'))
#abrupt drift
print(friedman_nemenyi_test_synth('memory_mean',gradual=False,to=True,titel="Memory consumption of detectors in the abrupt synthetic datasets"))
print(friedman_nemenyi_test_synth('memory_mean',to=True,gradual=False,fname='plots/CD_memory_synth_abrupt.png'))
#gradual drift
print(friedman_nemenyi_test_synth('memory_mean',abrupt=False,to=True,titel="Memory consumption of detectors in the gradual synthetic datasets"))
print(friedman_nemenyi_test_synth('memory_mean',to=True,abrupt=False,fname='plots/CD_memory_synth_gradual.png'))

'''include all models in Insects datasets'''
print(friedman_nemenyi_test_insects('memory_mean',titel='Memory consumption of detectors in the Insect datasets'))
print(friedman_nemenyi_test_insects('memory_mean',fname='plots/CD_memory_insect'))

'''include all models in real-datasets'''
print(friedman_nemenyi_test_real('memory_mean',titel='Memory consumption of detectors in the real-world datasets'))
print(friedman_nemenyi_test_real('memory_mean',fname='plots/CD_memory_real'))


'''include NB in all datasets'''
print(friedman_nemenyi_test_all('memory_mean',classifiers=['NB'],titel='Memory consumption of detectors with NB in all datasets'))
print(friedman_nemenyi_test_all('memory_mean',classifiers=['NB'],fname='plots/CD_memory_NB'))

'''include HT in all datasets'''
print(friedman_nemenyi_test_all('memory_mean',classifiers=['HT'],titel='Memory consumption of detectors with HT in all datasets'))
print(friedman_nemenyi_test_all('memory_mean',classifiers=['HT'],fname='plots/CD_memory_HT'))

'''include HT in all datasets'''
print(friedman_nemenyi_test_all('memory_mean',classifiers=['BOLE'],titel='Memory consumption of detectors with BOLE in all datasets'))
print(friedman_nemenyi_test_all('memory_mean',classifiers=['BOLE'],fname='plots/CD_memory_BOLE'))

