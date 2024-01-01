# -*- coding: utf-8 -*-


from evaluation.statistical_tests import friedman_nemenyi_test_synth


'''include all models and datasets'''
print(friedman_nemenyi_test_synth('accuracy_mean',ascending=False,to=True,titel="Predictive accuracy of detectors in the synthetic datasets"))
print(friedman_nemenyi_test_synth('accuracy_mean',ascending=False,to=True,fname='plots/CD_accuracy_synth.png'))


'''include all models and abrupt datasets'''
print(friedman_nemenyi_test_synth('accuracy_mean',ascending=False,gradual=False,to=True,titel="Predictive accuracy of detectors in the abrupt synthetic datasets"))
print(friedman_nemenyi_test_synth('accuracy_mean',ascending=False,gradual=False,to=True,fname='plots/CD_accuracy_synth_abrupt.png'))

'''include all models and gradual datasets'''
print(friedman_nemenyi_test_synth('accuracy_mean',ascending=False,abrupt=False,to=True,titel="Predictive accuracy of detectors in the gradual synthetic datasets"))
print(friedman_nemenyi_test_synth('accuracy_mean',ascending=False,abrupt=False,to=True,fname='plots/CD_accuracy_synth_gradual.png'))


'''include all NB models and datasets'''
print(friedman_nemenyi_test_synth('accuracy_mean',ascending=False,ensemble=False,ht=False,to=True,titel="Predictive accuracy of detectors with NB in the synthetic datasets"))
print(friedman_nemenyi_test_synth('accuracy_mean',ascending=False,ensemble=False,ht=False,to=True,fname='plots/CD_accuracy_synth_NB.png'))

'''include all HT models and datasets'''
print(friedman_nemenyi_test_synth('accuracy_mean',ascending=False,nb=False,ensemble=False,to=True,titel="Predictive accuracy of detectors with HT in the synthetic datasets"))
print(friedman_nemenyi_test_synth('accuracy_mean',ascending=False,nb=False,ensemble=False,to=True,fname='plots/CD_accuracy_synth_HT.png'))

'''include all BOLE models and datasets'''
print(friedman_nemenyi_test_synth('accuracy_mean',ascending=False,nb=False,ht=False,to=True,titel="Predictive accuracy of detectors with BOLE in the synthetic datasets"))
print(friedman_nemenyi_test_synth('accuracy_mean',ascending=False,nb=False,ht=False,to=True,fname='plots/CD_accuracy_synth_BOLE.png'))


'''include all NB models and abrupt datasets'''
print(friedman_nemenyi_test_synth('accuracy_mean',ascending=False,ensemble=False,ht=False,gradual=False,to=True,titel="Predictive accuracy of detectors with NB in the abrupt synthetic datasets"))
print(friedman_nemenyi_test_synth('accuracy_mean',ascending=False,ensemble=False,ht=False,gradual=False,to=True,fname='plots/CD_accuracy_synth_abrupt_NB.png'))

'''include all NB models and gradual datasets'''
print(friedman_nemenyi_test_synth('accuracy_mean',ascending=False,ensemble=False,ht=False,abrupt=False,to=True,titel="Predictive accuracy of detectors with NB in the gradual synthetic datasets"))
print(friedman_nemenyi_test_synth('accuracy_mean',ascending=False,ensemble=False,ht=False,abrupt=False,to=True,fname='plots/CD_accuracy_synth_gradual_NB.png'))


'''include all HT models and abrupt datasets'''
print(friedman_nemenyi_test_synth('accuracy_mean',ascending=False,ensemble=False,nb=False,gradual=False,to=True,titel="Predictive accuracy of detectors with HT in the abrupt synthetic datasets"))
print(friedman_nemenyi_test_synth('accuracy_mean',ascending=False,ensemble=False,nb=False,gradual=False,to=True,fname='plots/CD_accuracy_synth_abrupt_HT.png'))

'''include all HT models and gradual datasets'''
print(friedman_nemenyi_test_synth('accuracy_mean',ascending=False,ensemble=False,nb=False,abrupt=False,to=True,titel="Predictive accuracy of detectors with HT in the gradual synthetic datasets"))
print(friedman_nemenyi_test_synth('accuracy_mean',ascending=False,ensemble=False,nb=False,abrupt=False,to=True,fname='plots/CD_accuracy_synth_gradual_HT.png'))


'''include all BOLE models and abrupt datasets'''
print(friedman_nemenyi_test_synth('accuracy_mean',ascending=False,nb=False,ht=False,gradual=False,to=True,titel="Predictive accuracy of detectors with BOLE in the abrupt synthetic datasets"))
print(friedman_nemenyi_test_synth('accuracy_mean',ascending=False,nb=False,ht=False,gradual=False,to=True,fname='plots/CD_accuracy_synth_abrupt_BOLE.png'))

'''include all BOLE models and gradual datasets'''
print(friedman_nemenyi_test_synth('accuracy_mean',ascending=False,nb=False,ht=False,abrupt=False,to=True,titel="Predictive accuracy of detectors with BOLE in the gradual synthetic datasets"))
print(friedman_nemenyi_test_synth('accuracy_mean',ascending=False,nb=False,ht=False,abrupt=False,to=True,fname='plots/CD_accuracy_synth_gradual_BOLE.png'))


'''include all NB+HT models and abrupt datasets'''
print(friedman_nemenyi_test_synth('accuracy_mean',ascending=False,ensemble=False,gradual=False,to=True,titel="Predictive accuracy of detectors with NB and HT in the abrupt synthetic datasets"))
print(friedman_nemenyi_test_synth('accuracy_mean',ascending=False,ensemble=False,gradual=False,to=True,fname='plots/CD_accuracy_synth_abrupt_NB+HT.png'))

'''include all NB+HT models and gradual datasets'''
print(friedman_nemenyi_test_synth('accuracy_mean',ascending=False,ensemble=False,abrupt=False,to=True,titel="Predictive accuracy of detectors with NB and HT in the gradual synthetic datasets"))
print(friedman_nemenyi_test_synth('accuracy_mean',ascending=False,ensemble=False,abrupt=False,to=True,fname='plots/CD_accuracy_synth_gradual_NB+HT.png'))

