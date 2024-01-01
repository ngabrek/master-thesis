# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 14:44:13 2023

@author: nadin
"""

from evaluation.statistical_tests import friedman_nemenyi_test_real

'''include all models and datasets'''
print(friedman_nemenyi_test_real('accuracy_mean',ascending=False,titel='Predictive accuracy of detectors in the real-world datasets'))
print(friedman_nemenyi_test_real('accuracy_mean',ascending=False,fname='plots/CD_accuracy_real'))


'''include all NB models and datasets'''
print(friedman_nemenyi_test_real('accuracy_mean',ascending=False,classifiers=['NB'],titel='Predictive accuracy of detectors with NB in the real-world datasets'))
print(friedman_nemenyi_test_real('accuracy_mean',ascending=False,classifiers=['NB'],fname='plots/CD_accuracy_real_NB'))

'''include all HT models and datasets'''
print(friedman_nemenyi_test_real('accuracy_mean',ascending=False,classifiers=['HT'], titel='Predictive accuracy of detectors with HT in the real-world datasets'))
print(friedman_nemenyi_test_real('accuracy_mean',ascending=False,classifiers=['HT'],fname='plots/CD_accuracy_real_HT'))

'''include all BOLE models and datasets'''
print(friedman_nemenyi_test_real('accuracy_mean',ascending=False,classifiers=['BOLE'], titel='Predictive accuracy of detectors with BOLE in the real-world datasets'))
print(friedman_nemenyi_test_real('accuracy_mean',ascending=False,classifiers=['BOLE'],fname='plots/CD_accuracy_real_BOLE'))


'''include all models in Electricity dataset'''
print(friedman_nemenyi_test_real('accuracy_mean',ascending=False,datasets=['Elec2'],titel='Predictive accuracy of detectors in the real-world dataset Elec2'))
print(friedman_nemenyi_test_real('accuracy_mean',ascending=False,datasets=['Elec2'],fname='plots/CD_accuracy_real_Elec2'))

'''include all models in Covertype dataset'''
print(friedman_nemenyi_test_real('accuracy_mean',ascending=False,datasets=['Covertype'],titel='Predictive accuracy of detectors in the real-world dataset Covertype'))
print(friedman_nemenyi_test_real('accuracy_mean',ascending=False,datasets=['Covertype'],fname='plots/CD_accuracy_real_Covertype'))

'''include all models in Sensor-stream datasets'''
print(friedman_nemenyi_test_real('accuracy_mean',ascending=False,datasets=['SensorStream'],titel='Predictive accuracy of detectors in the real-world dataset SensorStream'))
print(friedman_nemenyi_test_real('accuracy_mean',ascending=False,datasets=['SensorStream'],fname='plots/CD_accuracy_real_SensorStream'))