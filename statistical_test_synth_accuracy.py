# -*- coding: utf-8 -*-


from evaluation.statistical_tests import get_avg_rank_synth, print_CD_diagram, friedman_nemenyi_test_synth


'''include all models and datasets'''
#print(friedman_nemenyi_test_synth('accuracy_mean',ascending=False,to=True,titel="Predictive accuracy of detectors in the synthetic datasets"))
#print(friedman_nemenyi_test_synth('accuracy_mean',ascending=False,to=True,fname='plots/CD_accuracy_synth.png'))


'''include all models and abrupt datasets'''
#print(friedman_nemenyi_test_synth('accuracy_mean',ascending=False,gradual=False,to=True,titel="Predictive accuracy of detectors in the abrupt synthetic datasets"))
#print(friedman_nemenyi_test_synth('accuracy_mean',ascending=False,gradual=False,to=True,fname='plots/CD_accuracy_synth_abrupt.png'))

'''include all models and gradual datasets'''
#print(friedman_nemenyi_test_synth('accuracy_mean',ascending=False,abrupt=False,to=True,titel="Predictive accuracy of detectors in the gradual synthetic datasets"))
#print(friedman_nemenyi_test_synth('accuracy_mean',ascending=False,abrupt=False,to=True,fname='plots/CD_accuracy_synth_gradual.png'))


'''include all NB models and datasets'''
#print(friedman_nemenyi_test_synth('accuracy_mean',ascending=False,ensemble=False,ht=False,to=True,titel="Predictive accuracy of detectors with NB in the synthetic datasets"))
#print(friedman_nemenyi_test_synth('accuracy_mean',ascending=False,ensemble=False,ht=False,to=True,fname='plots/CD_accuracy_synth_NB.png'))

'''include all HT models and datasets'''
#print(friedman_nemenyi_test_synth('accuracy_mean',ascending=False,nb=False,ensemble=False,to=True,titel="Predictive accuracy of detectors with HT in the synthetic datasets"))
#print(friedman_nemenyi_test_synth('accuracy_mean',ascending=False,nb=False,ensemble=False,to=True,fname='plots/CD_accuracy_synth_HT.png'))

'''include all BOLE models and datasets'''
#print(friedman_nemenyi_test_synth('accuracy_mean',ascending=False,nb=False,ht=False,to=True,titel="Predictive accuracy of detectors with BOLE in the synthetic datasets"))
#print(friedman_nemenyi_test_synth('accuracy_mean',ascending=False,nb=False,ht=False,to=True,fname='plots/CD_accuracy_synth_BOLE.png'))


'''include all 10K datasets'''
#data, avg_rank = get_avg_rank_synth('accuracy_mean',ascending=False,sizes=['10K'])
#print_CD_diagram(data, avg_rank, titel="accuracy of detectors in the synthetic datasets of size 10K")
#print_CD_diagram(data, avg_rank, 'plots/CD_accuracy_synth_10K.png')

'''include all 20K datasets'''
#data, avg_rank = get_avg_rank_synth('accuracy_mean',ascending=False,sizes=['20K'])
#print_CD_diagram(data, avg_rank, titel="accuracy of detectors in the synthetic datasets of size 20K")
#print_CD_diagram(data, avg_rank, 'plots/CD_accuracy_synth_20K.png')

'''include all 50K datasets'''
#data, avg_rank = get_avg_rank_synth('accuracy_mean',ascending=False,sizes=['50K'])
#print_CD_diagram(data, avg_rank, titel="accuracy of detectors in the synthetic datasets of size 50K")
#print_CD_diagram(data, avg_rank, 'plots/CD_accuracy_synth_50K.png')

'''include all 100K datasets'''
#data, avg_rank = get_avg_rank_synth('accuracy_mean',ascending=False,sizes=['100K'])
#print_CD_diagram(data, avg_rank, titel="accuracy of detectors in the synthetic datasets of size 100K")
#print_CD_diagram(data, avg_rank, 'plots/CD_accuracy_synth_100K.png')

'''include all 500K datasets with BOCD'''
#data, avg_rank = get_avg_rank_synth('accuracy_mean',ascending=False,sizes=['500K'])
#print_CD_diagram(data, avg_rank, titel="accuracy of detectors in the synthetic datasets of size 500K")
#print_CD_diagram(data, avg_rank, 'plots/CD_accuracy_synth_500K.png')
'''include all 500K datasets'''
#data, avg_rank = get_avg_rank_synth('accuracy_mean',ascending=False,sizes=['500K'],
#                                  detectors=['basic','ADWIN','CUSUM','DDM','ECDD','EDDM','GMA','HDDMA','HDDMW','KSWIN','PH','RDDM','STEPD'])
#print_CD_diagram(data, avg_rank, titel="accuracy of detectors in the synthetic datasets of size 500K")

'''include all 1M datasets'''
#data, avg_rank = get_avg_rank_synth('accuracy_mean',ascending=False,sizes=['1M'],
#                                   detectors=['basic','ADWIN','CUSUM','DDM','ECDD','EDDM','GMA','HDDMA','HDDMW','KSWIN','PH','RDDM','STEPD'])
#print_CD_diagram(data, avg_rank, titel="accuracy of detectors in the synthetic datasets of size 1M")
#print_CD_diagram(data, avg_rank, 'plots/CD_accuracy_synth_1M.png')


'''include all Agrawal1 datasets'''
#data, avg_rank = get_avg_rank_synth('accuracy_mean',ascending=False,generators=['agrawal1'])
#print_CD_diagram(data, avg_rank, titel="accuracy of detectors in the synthetic datasets by the Agrawal1 generator")
#print_CD_diagram(data, avg_rank, 'plots/CD_accuracy_synth_agrawal1.png')

'''include all Agrawal2 datasets'''
#data, avg_rank = get_avg_rank_synth('accuracy_mean',ascending=False,generators=['agrawal2'])
#print_CD_diagram(data, avg_rank, titel="accuracy of detectors in the synthetic datasets by the Agrawal2 generator")
#print_CD_diagram(data, avg_rank, 'plots/CD_accuracy_synth_agrawal2.png')

'''include all Mixed datasets'''
#data, avg_rank = get_avg_rank_synth('accuracy_mean',ascending=False,generators=['mixed'])
#print_CD_diagram(data, avg_rank, titel="accuracy of detectors in the synthetic datasets by the Mixed generator")
#print_CD_diagram(data, avg_rank, 'plots/CD_accuracy_synth_mixed.png')

'''include all Sine datasets'''
#data, avg_rank = get_avg_rank_synth('accuracy_mean',ascending=False,generators=['sine'])
#print_CD_diagram(data, avg_rank, titel="accuracy of detectors in the synthetic datasets by the Sine generator")
#print_CD_diagram(data, avg_rank, 'plots/CD_accuracy_synth_sine.png')

'''include all SEA datasets'''
#data, avg_rank = get_avg_rank_synth('accuracy_mean',ascending=False,generators=['sea'])
#print_CD_diagram(data, avg_rank, titel="accuracy of detectors in the synthetic datasets by the SEA generator")
#print_CD_diagram(data, avg_rank, 'plots/CD_accuracy_synth_sea.png')

'''include all STAGGER datasets'''
#data, avg_rank = get_avg_rank_synth('accuracy_mean',ascending=False,generators=['stagger'])
#print_CD_diagram(data, avg_rank, titel="accuracy of detectors in the synthetic datasets by the STAGGER generator")
#print_CD_diagram(data, avg_rank, 'plots/CD_accuracy_synth_stagger.png')



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

