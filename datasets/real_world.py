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
    
    def get_nominal_features():
        return  ['Wilderness_Area_0', 'Wilderness_Area_1', 'Wilderness_Area_2', 'Wilderness_Area_3', 'Soil_Type_0', 'Soil_Type_1', 'Soil_Type_2', 
                            'Soil_Type_3', 'Soil_Type_4', 'Soil_Type_5', 'Soil_Type_6', 'Soil_Type_7', 'Soil_Type_8', 'Soil_Type_9', 'Soil_Type_10', 'Soil_Type_11', 
                            'Soil_Type_12', 'Soil_Type_13', 'Soil_Type_14', 'Soil_Type_15', 'Soil_Type_16', 'Soil_Type_17', 'Soil_Type_18', 'Soil_Type_19', 'Soil_Type_20',
                            'Soil_Type_21', 'Soil_Type_22', 'Soil_Type_23', 'Soil_Type_24', 'Soil_Type_25', 'Soil_Type_26', 'Soil_Type_27', 'Soil_Type_28', 'Soil_Type_29',
                            'Soil_Type_30', 'Soil_Type_31', 'Soil_Type_32', 'Soil_Type_33', 'Soil_Type_34', 'Soil_Type_35', 'Soil_Type_36', 'Soil_Type_37', 'Soil_Type_38',
                            'Soil_Type_39']


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

