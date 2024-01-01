# -*- coding: utf-8 -*-


from evaluation.statistical_tests import  friedman_nemenyi_test_insects


'''include all models and datasets'''
print(friedman_nemenyi_test_insects('accuracy_mean',ascending=False,titel='Predictive accuracy of detectors in the Insect datasets'))
print(friedman_nemenyi_test_insects('accuracy_mean',ascending=False,fname='plots/CD_accuracy_insect'))


'''include all NB models and datasets'''
print(friedman_nemenyi_test_insects('accuracy_mean',ascending=False,classifiers=['NB'],titel='Predictive accuracy of detectors with NB in the Insect datasets'))
print(friedman_nemenyi_test_insects('accuracy_mean',ascending=False,classifiers=['NB'],fname='plots/CD_accuracy_insect_NB'))

'''include all HT models and datasets'''
# pvalue of Friedman test larger than 0.05
print(friedman_nemenyi_test_insects('accuracy_mean',ascending=False,classifiers=['HT'],titel='Predictive accuracy of detectors with HT in the Insect datasets'))
print(friedman_nemenyi_test_insects('accuracy_mean',ascending=False,classifiers=['HT'],fname='plots/CD_accuracy_insect_HT'))

'''include all BOLE models and datasets'''
print(friedman_nemenyi_test_insects('accuracy_mean',ascending=False,classifiers=['BOLE'],titel='Predictive accuracy of detectors with BOLE in the Insect datasets'))
print(friedman_nemenyi_test_insects('accuracy_mean',ascending=False,classifiers=['BOLE'],fname='plots/CD_accuracy_insect_BOLE'))


'''include all models and balanced datasets'''
print(friedman_nemenyi_test_insects('accuracy_mean',ascending=False,imbal=False,titel='Predictive accuracy of detectors in the balanced Insect datasets'))
print(friedman_nemenyi_test_insects('accuracy_mean',ascending=False,imbal=False,fname='plots/CD_accuracy_insect_bal'))

'''include all models and imbalanced datasets'''
print(friedman_nemenyi_test_insects('accuracy_mean',ascending=False,bal=False,titel='Predictive accuracy of detectors in the imbalanced Insect datasets'))
print(friedman_nemenyi_test_insects('accuracy_mean',ascending=False,bal=False,fname='plots/CD_accuracy_insect_imbal'))



