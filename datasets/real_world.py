# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 11:25:23 2023

@author: nadin
"""

from __future__ import annotations

from river import stream

from . import base

from sklearn import datasets


class Covertype(base.Dataset):

    def __init__(self):
        super().__init__(
            task=base.MULTI_CLF,
            n_classes=7,
            n_features=54,
            n_samples=581_012
        )

    def __iter__(self):
        return stream.iter_sklearn_dataset(datasets.fetch_covtype())


class SensorStream(base.FileDataset):

    def __init__(self):
        super().__init__(
            filename="sensorstream.arff",
            task=base.MULTI_CLF,
            n_classes=54,
            n_features=5,
            n_samples=2_219_803
        )

    def __iter__(self):
        return stream.iter_arff(self.path, target='class')

