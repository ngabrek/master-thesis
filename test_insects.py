# -*- coding: utf-8 -*-

from river.datasets import Insects


dataset = Insects(variant='abrupt_balanced')

for x, y in dataset.take(1):
    print(list(x.values()),y)

print('All features are numeric and continuous')