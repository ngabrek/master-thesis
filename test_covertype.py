# -*- coding: utf-8 -*-

from datasets.real_world import Covertype

dataset = Covertype()

for x, y in dataset.take(1):
    print(x.keys())
    print(list(x.values()),y)

print('The features Wilderness-Area and Soil-Type are nominal features')