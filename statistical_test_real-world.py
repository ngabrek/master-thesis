# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 14:44:13 2023

@author: nadin
"""

from evaluation.statistical_tests import get_avg_rank_real, print_CD_diagram

# Electricity
data, avg_rank = get_avg_rank_real('accuracy_mean',ascending=False,datasets=['Elec2'])
print(avg_rank)
print_CD_diagram(data, avg_rank, 'plots/CD_elec.png')

# Covertype
data, avg_rank = get_avg_rank_real('accuracy_mean',ascending=False,datasets=['Covertype'])
print(avg_rank)
print_CD_diagram(data, avg_rank, 'plots/CD_covertype.png')

# Sensor Stream
data, avg_rank = get_avg_rank_real('accuracy_mean',ascending=False,datasets=['SensorStream'])
print(avg_rank)
print_CD_diagram(data, avg_rank, 'plots/CD_sensor.png')

# All
data, avg_rank = get_avg_rank_real('accuracy_mean',ascending=False)
print(avg_rank)
print_CD_diagram(data, avg_rank, 'plots/CD_real.png')