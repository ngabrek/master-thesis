# -*- coding: utf-8 -*-

from datasets.real_world import SensorStream


dataset = SensorStream()

for x, y in dataset.take(1):
    print(x.keys())
    print(list(x.values()),y)

print('All features are numeric and continuous')