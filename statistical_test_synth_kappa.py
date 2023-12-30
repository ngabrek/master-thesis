# -*- coding: utf-8 -*-


from evaluation.statistical_tests import get_avg_rank_synth, print_CD_diagram, create_dict_detectors_synth, friedman_nemenyi_test_synth



'''include all models and datasets'''
#print(friedman_nemenyi_test_synth('cohen_kappas_mean',ascending=False,to=True,titel="Cohen's kappa of detectors in the synthetic datasets"))
#print(friedman_nemenyi_test_synth('cohen_kappas_mean',ascending=False,to=True,fname='plots/CD_kappa_synth.png'))


'''include all models and abrupt datasets'''
print(friedman_nemenyi_test_synth('cohen_kappas_mean',ascending=False,gradual=False,to=True,titel="Cohen's kappa of detectors in the abrupt synthetic datasets"))
print(friedman_nemenyi_test_synth('cohen_kappas_mean',ascending=False,gradual=False,to=True,fname='plots/CD_kappa_synth_abrupt.png'))


'''include all models and gradual datasets'''
print(friedman_nemenyi_test_synth('cohen_kappas_mean',ascending=False,abrupt=False,to=True,titel="Cohen's kappa of detectors in the gradual synthetic datasets"))
print(friedman_nemenyi_test_synth('cohen_kappas_mean',ascending=False,abrupt=False,to=True,fname='plots/CD_kappa_synth_gradual.png'))


'''include all NB models and datasets'''
#print(friedman_nemenyi_test_synth('cohen_kappas_mean',ascending=False,ensemble=False,ht=False,to=True,titel="Cohen's kappa of detectors with NB in the synthetic datasets"))
#print(friedman_nemenyi_test_synth('cohen_kappas_mean',ascending=False,ensemble=False,ht=False,to=True,fname='plots/CD_kappa_synth_NB.png'))

'''include all HT models and datasets'''
#print(friedman_nemenyi_test_synth('cohen_kappas_mean',ascending=False,nb=False,ensemble=False,to=True,titel="Cohen's kappa of detectors with HT in the synthetic datasets"))
#print(friedman_nemenyi_test_synth('cohen_kappas_mean',ascending=False,nb=False,ensemble=False,to=True,fname='plots/CD_kappa_synth_HT.png'))

'''include all BOLE models and datasets'''
#print(friedman_nemenyi_test_synth('cohen_kappas_mean',ascending=False,nb=False,ht=False,to=True,titel="Cohen's kappa of detectors with BOLE in the synthetic datasets"))
#print(friedman_nemenyi_test_synth('cohen_kappas_mean',ascending=False,nb=False,ht=False,to=True,fname='plots/CD_kappa_synth_BOLE.png'))


'''include all 10K datasets'''
#data, avg_rank = get_avg_rank_synth('accuracy_mean',ascending=False,sizes=['10K'])
#print_CD_diagram(data, avg_rank, titel="accuracy of detectors in the synthetic datasets of size 10K")

'''include all 20K datasets'''
#data, avg_rank = get_avg_rank_synth('accuracy_mean',ascending=False,sizes=['20K'])
#print_CD_diagram(data, avg_rank, titel="accuracy of detectors in the synthetic datasets of size 20K")

'''include all 50K datasets'''
#data, avg_rank = get_avg_rank_synth('accuracy_mean',ascending=False,sizes=['50K'])
#print_CD_diagram(data, avg_rank, titel="accuracy of detectors in the synthetic datasets of size 50K")

'''include all 100K datasets'''
#data, avg_rank = get_avg_rank_synth('accuracy_mean',ascending=False,sizes=['100K'])
#print_CD_diagram(data, avg_rank, titel="accuracy of detectors in the synthetic datasets of size 100K")

'''include all 500K datasets with BOCD'''
#data, avg_rank = get_avg_rank_synth('accuracy_mean',ascending=False,sizes=['500K'])
#print_CD_diagram(data, avg_rank, titel="accuracy of detectors in the synthetic datasets of size 500K")
'''include all 500K datasets'''
#data, avg_rank = get_avg_rank_synth('accuracy_mean',ascending=False,sizes=['500K'],
#                                  detectors=['basic','ADWIN','CUSUM','DDM','ECDD','EDDM','GMA','HDDMA','HDDMW','KSWIN','PH','RDDM','STEPD'])
#print_CD_diagram(data, avg_rank, titel="accuracy of detectors in the synthetic datasets of size 500K")

'''include all 1M datasets'''
#data, avg_rank = get_avg_rank_synth('accuracy_mean',ascending=False,sizes=['1M'],
#                                    detectors=['basic','ADWIN','CUSUM','DDM','ECDD','EDDM','GMA','HDDMA','HDDMW','KSWIN','PH','RDDM','STEPD'])
#print_CD_diagram(data, avg_rank, titel="accuracy of detectors in the synthetic datasets of size 1M")


'''include all Agrawal1 datasets'''
#data, avg_rank = get_avg_rank_synth('accuracy_mean',ascending=False,generators=['agrawal1'])
#print_CD_diagram(data, avg_rank, titel="accuracy of detectors in the synthetic datasets by the Agrawal1 generator")

'''include all Agrawal2 datasets'''
#data, avg_rank = get_avg_rank_synth('accuracy_mean',ascending=False,generators=['agrawal2'])
#print_CD_diagram(data, avg_rank, titel="accuracy of detectors in the synthetic datasets by the Agrawal2 generator")

'''include all Mixed datasets'''
#data, avg_rank = get_avg_rank_synth('accuracy_mean',ascending=False,generators=['mixed'])
#print_CD_diagram(data, avg_rank, titel="accuracy of detectors in the synthetic datasets by the Mixed generator")

'''include all Sine datasets'''
#data, avg_rank = get_avg_rank_synth('accuracy_mean',ascending=False,generators=['sine'])
#print_CD_diagram(data, avg_rank, titel="accuracy of detectors in the synthetic datasets by the Sine generator")

'''include all SEA datasets'''
#data, avg_rank = get_avg_rank_synth('accuracy_mean',ascending=False,generators=['sea'])
#print_CD_diagram(data, avg_rank, titel="accuracy of detectors in the synthetic datasets by the SEA generator")

'''include all STAGGER datasets'''
#data, avg_rank = get_avg_rank_synth('accuracy_mean',ascending=False,generators=['stagger'])
#print_CD_diagram(data, avg_rank, titel="accuracy of detectors in the synthetic datasets by the STAGGER generator")



'''include all NB models and abrupt datasets'''
#data, avg_rank = get_avg_rank_synth('accuracy_mean',ascending=False,gradual=False,ht=False,ensemble=False)
#print_CD_diagram(data, avg_rank, titel="accuracy of detectors with NB in the synthetic datasets with abrupt drifts")

'''include all NB models and gradual datasets'''
#data, avg_rank = get_avg_rank_synth('accuracy_mean',ascending=False,abrupt=False,ht=False,ensemble=False)
#print_CD_diagram(data, avg_rank, titel="accuracy of detectors with NB in the synthetic datasets with gradual drifts")


'''include all HT models and abrupt datasets'''
#data, avg_rank = get_avg_rank_synth('accuracy_mean',ascending=False,gradual=False,nb=False,ensemble=False)
#print_CD_diagram(data, avg_rank, titel="accuracy of detectors with HT in the synthetic datasets with abrupt drifts")

'''include all HT models and gradual datasets'''
#data, avg_rank = get_avg_rank_synth('accuracy_mean',ascending=False,abrupt=False,nb=False,ensemble=False)
#print_CD_diagram(data, avg_rank, titel="accuracy of detectors with HT in the synthetic datasets with gradual drifts")


'''include all BOLE models and abrupt datasets'''
#data, avg_rank = get_avg_rank_synth('accuracy_mean',ascending=False,gradual=False,nb=False,ht=False)
#print_CD_diagram(data, avg_rank, titel="accuracy of detectors with BOLE in the synthetic datasets with abrupt drifts")

'''include all BOLE models and gradual datasets'''
#data, avg_rank = get_avg_rank_synth('accuracy_mean',ascending=False,abrupt=False,nb=False,ht=False)
#print_CD_diagram(data, avg_rank, titel="accuracy of detectors with BOLE in the synthetic datasets with gradual drifts")

