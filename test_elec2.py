# -*- coding: utf-8 -*-

from river.datasets import Elec2


dataset = Elec2()

print(dataset.desc + '\n')

for x, y in dataset.take(1):
    print(x.keys())
    print(list(x.values()),y)

print('\nAll features are numeric and continuous, but the day of the week\n')