# A comparison of concept drift detectors in an online learning setting 
### presented by Nadine Gabrek

This repository contains the code for the execution of the experiments, which produced the relevant results for the master-thesis.
It predominantly applies the River and Frours library for the evaluation of data streams and concept drift detection methods.
Furthermore, it contains all obtained experimental results. 

## Structure 
The directory, which contains the relevant execution files to start the experiments, is called "experiments". Here, the respecitve files are further sorted into folders according to their underlying datasets, such that there exist one folder for the real-world datasets, one for the semi-real Insect datasets, and due to their large amount one folder for each synthetic data stream generator. In the folders regarding the generators the files are further sorted according to their dataset size, while for the real-world datasets they are sorted into folders for the individual real-world datasets, and concerning the Insect dataset they are classified based on the respective dataset variant. For each Python file, there exist a complementary Shell-Script file as the experiments were run on the bwUniCluster 2.0. We further included all the output files from the execution on the cluster in the corresponding folders. 
As the concept drift detection from the Frouros library are not compatible with the evaluation framework in River, minor adaptions of the respective 
Code from the aforementioned libraries was necessary. The adapted classes are in the directoried 'frouros_adapted' and 'river_adapted', respecitvely, where each adaption is marked by a explainatory comment.

The results of the experiments are aggregated in the "results" directory, were the respecitve CSV files are sorted according to the structure in the "experiments" directory. 
However, each dataset or generator folder additionally contains a "final_results" folder, were the computed confidence intervals of the results of the respective dataset type are stored. 

The main code for the evaluation of the configurations is placed in the "evaluation" directory. It contains the Python file with the relevant methods for the execution of the evaluation as well as as Python file for the conducted statistical tests. 
The execution files for the statistical test are stored in the main directory, while the generated CD graphs from the Nemenyi test are stored in the "plots" directory. 

The code for the generation or assessment of the required datasets, which is called during the evaluation, is stored in the "dataset" directory. It contains a Python file for every data stream generator as well as a Python file for the real-world datasets that cannot directly be included from the River library. Therefore, the directory also holds the ARFF file of the Sensor Stream dataset.

In the 'utils' directory, Python files with different utility methods, e.g., for the reading and writing of the results from and into csv-files or for the computation of the confidence intervals of the results, are stored. 

Additional code files in the overarching directory contain the code for the post-hoc statistical test as well as further small test conducted in the course of this work.

## Instruction for the executing of the experiments
Because the experiments were processed on the bwUniCluster 2.0, no main file was used to execute the individual experiments. However, the experiments were executed in individual jobs, which had a maximal runtime of 3 hours.
Therefore, all relevant execution files for the computation of the requires results, as well as their respective SSH files, are in the "experiments" folder.

Usually, it should be possible to simply execute the individual Python file. In case of problems, it might work to start the execution via the command prompt. Therefore, the commands, as included in the respective SH file, should be executed.
The individual results will be stored in the the "results" directory.

When all experiments were executed, the Python file 'create_final_conf_results.py' in the overarching directory must be run, such that the confidence interval of the results over the repeted executions on the synthetic datasets as well as the BOLE classifier and KSWIN detector are computed. The results on the confidence intervals will be stored in the "final_results" folder in the respecitve dataset folder in the "results" directory.

Finally, the files for the Nemenyi test, which also are located in the overarching directory, must be executed to obtain the results on the comparison in form of CD graphs on the average ranks of the detection methods. The corresponding CD graphs are additionally stored in the "plots" directory.

## Packages
Here is the list of all packages implemented in the used conda environment on the bwUniCluster 2.0, where the most important ones are highlighted. 

![grafik](https://github.com/ngabrek/master-thesis/assets/133040502/e76a391d-d85d-4fa8-a98c-f74f770ef5f1)




