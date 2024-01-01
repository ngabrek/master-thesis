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
from frouros_adapted.kswin import KSWIN, KSWINConfig
from frouros_adapted.stepd import STEPD

# Import of base classifiers from the river package 
from river.dummy import NoChangeClassifier, PriorClassifier
from river.naive_bayes import GaussianNB
from river.tree import HoeffdingTreeClassifier
from river.ensemble import BOLEClassifier

# Import adapted class from the River package to combine base classifier with detector
from river_adapted.retrain import DriftRetrainingClassifier



def load_frouros_detectors(adwin:bool,bocd:bool,cusum:bool,ddm:bool,ecdd:bool,eddm:bool,gma:bool,gma_sensitive:bool,hddma:bool,hddmw:bool,kswin:bool,
                           ph:bool,rddm:bool,stepd:bool) -> dict:
    
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
    #KSWIN is the only detector with randomness
    if kswin:
        for i in range(1,250,50):
            detectors[f'KSWIN{i}']=KSWIN(KSWINConfig(seed=i))
    if ph:
        detectors['PH']=PageHinkley()
    if rddm:
        detectors['RDDM']=RDDM()
    if stepd:
        detectors['STEPD']=STEPD()
    return detectors


def load_models(nominal_attributes, seed:int,
                nochange:bool,majclass:bool,nb:bool,ht:bool,bole:bool,
                basic:bool,adwin:bool,bocd:bool,cusum:bool,ddm:bool,ecdd:bool,eddm:bool,gma:bool,gma_sensitive:bool,hddma:bool,hddmw:bool,
                kswin:bool,ph:bool,rddm:bool,stepd:bool) -> dict:
    
    """This method returns a dictionary that pairs each detection method with each base classifier from the River package as indicated by the input"""
    
    #Load all the detectors as indicated by the input 
    detectors = load_frouros_detectors(adwin=adwin,bocd=bocd,cusum=cusum,ddm=ddm,ecdd=ecdd,eddm=eddm,gma=gma,gma_sensitive=gma_sensitive,hddma=hddma,hddmw=hddmw,kswin=kswin,ph=ph,
                                       rddm=rddm,stepd=stepd)
    models = {}

    #Load all baseline classifiers as indicated by the input 
    if nochange:
        models['NoChange_basic_F'] = NoChangeClassifier()
    if majclass:
        models['MajClass_basic_F'] = PriorClassifier()
    if nb and basic:
        models['NB_basic_F'] = GaussianNB()
    if ht and basic:
        models['HT_basic_F'] = HoeffdingTreeClassifier(nominal_attributes=nominal_attributes)
    if bole and basic:
        models['BOLE_basic_F'] = BOLEClassifier(model=HoeffdingTreeClassifier(nominal_attributes=nominal_attributes),seed=seed)

    #Load all combinations of base classifier and detector as indicated by the input by iterating over all relevant detectors
    for detector_name, detector in detectors.items():
        #Load all required combinations of the detection methods with the naive bayes classifier
        if nb:
            #Combination with detectors without warning level 
            if detector_name in ['ADWIN', 'BOCD', 'CUSUM', 'GMA', 'GMA_sensitive','PH'] or 'KSWIN' in detector_name:
                models['NB_'+detector_name+'_F']=DriftRetrainingClassifier(model=GaussianNB(),drift_detector=detector,train_in_background=False)
            #Combination with detectors with warning level
            else:
                models['NB_'+detector_name+'_F']=DriftRetrainingClassifier(model=GaussianNB(),drift_detector=detector)
        #Load all required combinations of the detection methods with the Hoeffding tree classifier        
        if ht:
            #Combination with detectors without warning level 
            if detector_name in ['ADWIN', 'BOCD', 'CUSUM', 'GMA', 'GMA_sensitive', 'PH'] or 'KSWIN' in detector_name:
                models['HT_'+detector_name+'_F']=DriftRetrainingClassifier(model=HoeffdingTreeClassifier(nominal_attributes=nominal_attributes),
                                                                           drift_detector=detector,train_in_background=False)
            #Combination with detectors with warning level
            else:
                models['HT_'+detector_name+'_F']=DriftRetrainingClassifier(model=HoeffdingTreeClassifier(nominal_attributes=nominal_attributes),
                                                                           drift_detector=detector)
        #Load all required combinations of the detection methods with the BOLE classifier        
        if bole:
            #Combination with detectors without warning level 
            if detector_name in ['ADWIN', 'BOCD', 'CUSUM', 'GMA', 'GMA_sensitive', 'PH'] or 'KSWIN' in detector_name:
                models['BOLE_'+detector_name+'_F']=BOLEClassifier(
                                                        model=DriftRetrainingClassifier(model=HoeffdingTreeClassifier(nominal_attributes=nominal_attributes),drift_detector=detector,train_in_background=False),
                                                        seed=seed)
            #Combination with detectors with warning level
            else:
                models['BOLE_'+detector_name+'_F']=BOLEClassifier(
                                                        model=DriftRetrainingClassifier(model=HoeffdingTreeClassifier(nominal_attributes=nominal_attributes),drift_detector=detector),
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
                models['NB_EDDM_F1']=DriftRetrainingClassifier(model=GaussianNB(),drift_detector=detector)
                models['NB_EDDM_F2']=DriftRetrainingClassifier(model=GaussianNB(),drift_detector=detector)
    return models

