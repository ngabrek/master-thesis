# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 14:44:13 2023

@author: nadin
"""

from evaluation.statistical_tests import get_avg_rank_real, print_CD_diagram

'''include all models and datasets'''
data, avg_rank = get_avg_rank_real('accuracy_mean',ascending=False)
print_CD_diagram(data, avg_rank, titel="accuracy of detectors in the real-world datasets (new)")


'''include all NB models and datasets'''
data, avg_rank = get_avg_rank_real('accuracy_mean',ascending=False,classifiers=['NB'])
print_CD_diagram(data, avg_rank, titel="accuracy of detectors with NB in the real-world datasets (new)")

'''include all HT models and datasets'''
data, avg_rank = get_avg_rank_real('accuracy_mean',ascending=False,classifiers=['HT'])
print_CD_diagram(data, avg_rank, titel="accuracy of detectors with HT in the real-world datasets (new)")

'''include all BOLE models and datasets'''
data, avg_rank = get_avg_rank_real('accuracy_mean',ascending=False,classifiers=['BOLE+HT'])
print_CD_diagram(data, avg_rank, titel="accuracy of detectors with BOLE in the real-world datasets (new)")


'''include all models in Electricity dataset'''
data, avg_rank = get_avg_rank_real('accuracy_mean',ascending=False,datasets=['Elec2'])
print_CD_diagram(data, avg_rank, titel="accuracy of detectors in the Electricity dataset (new)")

'''include all models in Covertype dataset'''
data, avg_rank = get_avg_rank_real('accuracy_mean',ascending=False,datasets=['Covertype'])
print_CD_diagram(data, avg_rank, titel="accuracy of detectors in the Covertype dataset (new)")

'''include all models in Sensor-stream datasets'''
data, avg_rank = get_avg_rank_real('accuracy_mean',ascending=False,datasets=['SensorStream'])
print_CD_diagram(data, avg_rank, titel="accuracy of detectors in the Sensor Stream (new)")