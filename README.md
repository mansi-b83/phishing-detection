# phishing-detection
Name- Mansi 
Class- B3 
Course- Computers 
Faculty Name- Pradnya Bhangale 
College- K.J.Somaiya College of Engineering

dataset.csv-
Dataset that has been used for implementation of this project.

dataset_dexcrption.py-
In this file I have imported required libraries. 
Read the csv file and displayed structure of the dataset.
Displayed  number of legitimate and phishing records in dataset.
Created heatmap that shows correlation of the features

feature extraction.py-
Created this file for extracting features to train the dataset. I have used 22 features.

classifiers.py-
Imported the reuired libraries to calculate results for Decision Tree Model and Random Forest Model
Read csv file to create pandas dataframe,preprocessed the data to reduce bias and displayed the first 5 rows of dataframe.
Implemented Decision Tree Classifier and Random Forest Classifier- Cross validated the data provided in dataset according to specified fold count i.e 10. and evaluated performance of cross validated data. Then calculated mean of obtained cross validated result. 

It was observed that Random Forest Classifier provided better accuracy,precision,recall and F1 score compared to Decison Tree Classifier

Output of classifiers:
![image](https://user-images.githubusercontent.com/83391233/116664398-09e3d400-a9b6-11eb-95d4-d84b3759ba71.png)



Steps to run this project:
1) Run dataset_description.py
2) Run feature_extraction.py
3) Run classifiers.py

Note: The dataset which you are using should be in same folder of the above files.
