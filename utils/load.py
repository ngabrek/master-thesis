# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 15:02:59 2023

@author: nadin
"""

# Set root path of the project for local imports
from pathlib import Path
import sys
path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

# Import locally adapted drift detection methods from the Frouros package 
from frouros_adapted.bocd import BOCD
from frouros_adapted.cusum import CUSUM
from frouros_adapted.geometric_moving_average import GeometricMovingAverage, GeometricMovingAverageConfig
from frouros_adapted.page_hinkley import PageHinkley
from frouros_adapted.ddm import DDM
from frouros_adapted.ecdd import ECDDWT
from frouros_adapted.eddm import EDDM
from frouros_adapted.hddm import HDDMA, HDDMW
from frouros_adapted.rddm import RDDM
from frouros_adapted.adwin import ADWIN
from frouros_adapted.kswin import KSWIN
from frouros_adapted.stepd import STEPD

# Import of base classifiers from the river package 
from river.dummy import NoChangeClassifier, PriorClassifier
from river.naive_bayes import GaussianNB
from river.tree import HoeffdingTreeClassifier
from river.ensemble import BOLEClassifier

# Import adapted class from the River package to combine base classifier with detector
from river_adapted.retrain import DriftRetrainingClassifier



def load_frouros_detectors(
    adwin:bool=True,bocd:bool=True,cusum:bool=True,ddm:bool=True,ecdd:bool=True,eddm:bool=True,gma:bool=True,gma_sensitive:bool=True,hddma:bool=True,
    hddmw:bool=True,kswin:bool=True,ph:bool=True,rddm:bool=True,stepd:bool=True) -> dict:
    
    '''This method returns a dictionary that contains all detectors from the Frouros package as indicated by the input'''
    detectors = {}
    if adwin:
        detectors['ADWIN']=ADWIN()
    if bocd:
        detectors['BOCD']=BOCD()
    if cusum:
        detectors['CUSUM']=CUSUM()
    if ddm:
        detectors['DDM']=DDM()
    if ecdd:
        detectors['ECDD']=ECDDWT()
    if eddm:
        detectors['EDDM']=EDDM()
    if gma:
        detectors['GMA']=GeometricMovingAverage()
    if gma_sensitive:
        detectors['GMA_sensitive']=GeometricMovingAverage(config=GeometricMovingAverageConfig(lambda_=0.3))
    if hddma:
        detectors['HDDMA']=HDDMA()
    if hddmw:
        detectors['HDDMW']=HDDMW()
    if kswin:
        detectors['KSWIN']=KSWIN()
    if ph:
        detectors['PH']=PageHinkley()
    if rddm:
        detectors['RDDM']=RDDM()
    if stepd:
        detectors['STEPD']=STEPD()
    return detectors


def load_frouros_models(nochange=True,majclass=True,nb:bool=True,ht:bool=True,
                        adwin:bool=True,bocd:bool=True,cusum:bool=True,ddm:bool=True,ecdd:bool=True,eddm:bool=True,gma:bool=True,gma_sensitive:bool=True,hddma:bool=True,
                        hddmw:bool=True,kswin:bool=True,ph:bool=True,rddm:bool=True,stepd:bool=True) -> dict:
    
    """This method returns a dictionary that pairs each detection method with each base classifier from the River package as indicated by the input"""
    
    detectors = load_frouros_detectors(adwin=adwin,bocd=bocd,cusum=cusum,ddm=ddm,ecdd=ecdd,eddm=eddm,gma=gma,gma_sensitive=gma_sensitive,hddma=hddma,hddmw=hddmw,kswin=kswin,ph=ph,
                                       rddm=rddm,stepd=stepd)
    models = {}

    if nochange:
        models['NoChange_basic_F'] = NoChangeClassifier()
    if majclass:
        models['MajClass_basic_F'] = PriorClassifier()
    if nb:
        models['NB_basic_F'] = GaussianNB()
    if ht:
        models['HT_basic_F'] = HoeffdingTreeClassifier()

    for detector_name, detector in detectors.items():
        if nb:
            if detector_name in ['ADWIN', 'BOCD', 'CUSUM', 'GMA', 'GMA_sensitive', 'KSWIN', 'PH']:
                models['NB_'+detector_name+'_F']=DriftRetrainingClassifier(model=GaussianNB(),drift_detector=detector,train_in_background=False)
            else:
                models['NB_'+detector_name+'_F']=DriftRetrainingClassifier(model=GaussianNB(),drift_detector=detector)
        if ht:
            if detector_name in ['ADWIN', 'BOCD', 'CUSUM', 'GMA', 'GMA_sensitive', 'KSWIN', 'PH']:
                models['HT_'+detector_name+'_F']=DriftRetrainingClassifier(model=HoeffdingTreeClassifier(),
                                                                           drift_detector=detector,train_in_background=False)
            else:
                models['HT_'+detector_name+'_F']=DriftRetrainingClassifier(model=HoeffdingTreeClassifier(),
                                                                           drift_detector=detector)
    return models

def load_frouros_ensemble(seed:int, ensemble:str='BOLE', nochange=True,majclass=True,nb:bool=True,ht:bool=True,
                          adwin:bool=True,bocd:bool=True,cusum:bool=True,ddm:bool=True,ecdd:bool=True,eddm:bool=True,gma:bool=True,gma_sensitive:bool=True,hddma:bool=True,
                          hddmw:bool=True,kswin:bool=True,ph:bool=True,rddm:bool=True,stepd:bool=True) -> dict:
    
    """This method returns a dictionary that pairs each detection method with the ensemble classifier BOLE from the River package as indicated by the input"""
    
    detectors = load_frouros_detectors(adwin=adwin,bocd=bocd,cusum=cusum,ddm=ddm,ecdd=ecdd,eddm=eddm,gma=gma,gma_sensitive=gma_sensitive,hddma=hddma,hddmw=hddmw,kswin=kswin,ph=ph,
                                       rddm=rddm,stepd=stepd)
    models = {}
    
    for detector_name, detector in detectors.items():
        if ensemble == 'BOLE':
            if nb:
                models['BOLE+NB_basic_F'] = BOLEClassifier(model=GaussianNB(),seed=seed)
                if detector_name in ['ADWIN', 'BOCD', 'CUSUM', 'GMA', 'GMA_sensitive', 'KSWIN', 'PH']:
                    models['BOLE+NB_'+detector_name+'_F']=BOLEClassifier(
                        model=DriftRetrainingClassifier(model=GaussianNB(),drift_detector=detector,train_in_background=False),
                        seed=seed)
                else:
                    models['BOLE+NB_'+detector_name+'_F']=BOLEClassifier(
                        model=DriftRetrainingClassifier(model=GaussianNB(),drift_detector=detector),
                        seed=seed)
            if ht:
                models['BOLE+HT_basic_F'] = BOLEClassifier(model=HoeffdingTreeClassifier(),seed=seed)
                if detector_name in ['ADWIN', 'BOCD', 'CUSUM', 'GMA', 'GMA_sensitive', 'KSWIN', 'PH']:
                    models['BOLE+HT_'+detector_name+'_F']=BOLEClassifier(
                        model=DriftRetrainingClassifier(model=HoeffdingTreeClassifier(),drift_detector=detector,train_in_background=False),
                        seed=seed)
                else:
                    models['BOLE+HT_'+detector_name+'_F']=BOLEClassifier(
                        model=DriftRetrainingClassifier(model=HoeffdingTreeClassifier(),drift_detector=detector),
                        seed=seed)
    
    return models



def load_models_test(nochange=False,majclass=False,nb:bool=False,ht:bool=True,
                        adwin:bool=False,bocd:bool=False,cusum:bool=False,ddm:bool=False,ecdd:bool=False,eddm:bool=True,gma:bool=False,gma_sensitive:bool=False,hddma:bool=False,
                        hddmw:bool=False,kswin:bool=False,ph:bool=False,rddm:bool=False,stepd:bool=False) -> dict:
    
    """This method returns a dictionary that pairs each detection method with each base classifier from the River package as indicated by the input"""
    
    detectors = load_frouros_detectors(adwin=adwin,bocd=bocd,cusum=cusum,ddm=ddm,ecdd=ecdd,eddm=eddm,gma=gma,gma_sensitive=gma_sensitive,hddma=hddma,hddmw=hddmw,kswin=kswin,ph=ph,
                                       rddm=rddm,stepd=stepd)
    models = {}

    for detector_name, detector in detectors.items():
        if ht:
            if detector_name in ['EDDM']:
                models['HT_EDDM_F1']=DriftRetrainingClassifier(model=HoeffdingTreeClassifier(),drift_detector=detector)
                models['HT_EDDM_F2']=DriftRetrainingClassifier(model=HoeffdingTreeClassifier(),drift_detector=detector)
    return models

