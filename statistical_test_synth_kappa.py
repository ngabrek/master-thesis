# -*- coding: utf-8 -*-


from evaluation.statistical_tests import friedman_nemenyi_test_synth


'''include all models and datasets'''
print(friedman_nemenyi_test_synth('cohen_kappas_mean',ascending=False,to=True,titel="Cohen's kappa of detectors in the synthetic datasets"))
print(friedman_nemenyi_test_synth('cohen_kappas_mean',ascending=False,to=True,fname='plots/CD_kappa_synth.png'))


'''include all models and abrupt datasets'''
print(friedman_nemenyi_test_synth('cohen_kappas_mean',ascending=False,gradual=False,to=True,titel="Cohen's kappa of detectors in the abrupt synthetic datasets"))
print(friedman_nemenyi_test_synth('cohen_kappas_mean',ascending=False,gradual=False,to=True,fname='plots/CD_kappa_synth_abrupt.png'))


'''include all models and gradual datasets'''
print(friedman_nemenyi_test_synth('cohen_kappas_mean',ascending=False,abrupt=False,to=True,titel="Cohen's kappa of detectors in the gradual synthetic datasets"))
print(friedman_nemenyi_test_synth('cohen_kappas_mean',ascending=False,abrupt=False,to=True,fname='plots/CD_kappa_synth_gradual.png'))


'''include all NB models and datasets'''
print(friedman_nemenyi_test_synth('cohen_kappas_mean',ascending=False,ensemble=False,ht=False,to=True,titel="Cohen's kappa of detectors with NB in the synthetic datasets"))
print(friedman_nemenyi_test_synth('cohen_kappas_mean',ascending=False,ensemble=False,ht=False,to=True,fname='plots/CD_kappa_synth_NB.png'))

'''include all HT models and datasets'''
print(friedman_nemenyi_test_synth('cohen_kappas_mean',ascending=False,nb=False,ensemble=False,to=True,titel="Cohen's kappa of detectors with HT in the synthetic datasets"))
print(friedman_nemenyi_test_synth('cohen_kappas_mean',ascending=False,nb=False,ensemble=False,to=True,fname='plots/CD_kappa_synth_HT.png'))

'''include all BOLE models and datasets'''
print(friedman_nemenyi_test_synth('cohen_kappas_mean',ascending=False,nb=False,ht=False,to=True,titel="Cohen's kappa of detectors with BOLE in the synthetic datasets"))
print(friedman_nemenyi_test_synth('cohen_kappas_mean',ascending=False,nb=False,ht=False,to=True,fname='plots/CD_kappa_synth_BOLE.png'))



