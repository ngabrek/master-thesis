# -*- coding: utf-8 -*-


from evaluation.statistical_tests import get_avg_rank_insects, print_CD_diagram


'''include all models and datasets'''
data, avg_rank = get_avg_rank_insects('accuracy_mean',ascending=False)
print_CD_diagram(data, avg_rank, titel="accuracy of detectors in the Insects datasets")
print_CD_diagram(data, avg_rank, 'plots/CD_accuracy_insects.png')


'''include all NB models and datasets'''
data, avg_rank = get_avg_rank_insects('accuracy_mean',ascending=False,classifiers=['NB'])
print_CD_diagram(data, avg_rank, titel="accuracy of detectors with NB in the Insects datasets")
print_CD_diagram(data, avg_rank, 'plots/CD_accuracy_insects_NB.png')

'''include all HT models and datasets'''
data, avg_rank = get_avg_rank_insects('accuracy_mean',ascending=False,classifiers=['HT'])
print_CD_diagram(data, avg_rank, titel="accuracy of detectors with HT in the Insects datasets")
print_CD_diagram(data, avg_rank, 'plots/CD_accuracy_insects_HT.png')

'''include all BOLE models and datasets'''
data, avg_rank = get_avg_rank_insects('accuracy_mean',ascending=False,classifiers=['BOLE'])
print_CD_diagram(data, avg_rank, titel="accuracy of detectors with BOLE in the Insects datasets")
print_CD_diagram(data, avg_rank, 'plots/CD_accuracy_insects_BOLE.png')

'''include all BOLE models and datasets'''
data, avg_rank = get_avg_rank_insects('accuracy_mean',ascending=False,classifiers=['HT','BOLE'])
print_CD_diagram(data, avg_rank, titel="accuracy of detectors with HT+BOLE in the Insects datasets")
print_CD_diagram(data, avg_rank, 'plots/CD_accuracy_insects_HT+BOLE.png')


'''include all models and balanced datasets'''
data, avg_rank = get_avg_rank_insects('accuracy_mean',ascending=False,imbal=False)
print_CD_diagram(data, avg_rank, titel="accuracy of detectors in the balanced Insects datasets")
print_CD_diagram(data, avg_rank, 'plots/CD_accuracy_insects_bal.png')

'''include all models and imbalanced datasets'''
data, avg_rank = get_avg_rank_insects('accuracy_mean',ascending=False,bal=False)
print_CD_diagram(data, avg_rank, titel="accuracy of detectors in the imbalanced Insects datasets")
print_CD_diagram(data, avg_rank, 'plots/CD_accuracy_insects_imbal.png')



