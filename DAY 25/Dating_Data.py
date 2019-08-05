import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#reading the whole data
dataset = pd.read_csv('Dating_Data.csv', encoding='Latin')

''''
    What does a person look for in a partner? (both male and female)
'''
#finding the coloumns with right data
features = dataset[['attr1_1','sinc1_1','intel1_1','fun1_1','amb1_1','shar1_1','gender']]
#dropping the null value
features = features.dropna()
#for female
z = features[features['gender'] == 0]
z = z.drop(['gender'], axis=1)
#for male
s = features[features['gender'] == 1]
s = s.drop(['gender'], axis=1)
#finding mean
z_mean = z.mean(axis=0)
s_mean = s.mean(axis=0)
#creating objects
objects = ('attr1_1','sinc1_1','intel1_1','fun1_1','amb1_1','shar1_1')
x_index=[1,2,3,4,5,6]
#plotting bar graph for female
plt.bar(x_index, z_mean, color='blue')
plt.xticks(x_index, objects)
#plotting bar graph for male
plt.bar(x_index, s_mean , color='red')
plt.xticks(x_index, objects)


'''
    What does a person think that their partner would look for in them? Do you 
    think what a man thinks a woman wants from them matches to what women 
    really wants in them or vice versa. TIP: If it doesn’t then it will be one sided :)
'''
#getting the data
features = dataset[['attr4_1','sinc4_1','intel4_1','fun4_1','amb4_1','shar4_1','gender']]
#dropping the null value
features = features.dropna()
#for female
z = features[features['gender'] == 0]
z = z.drop(['gender'], axis=1)
#for male
s = features[features['gender'] == 1]
s = s.drop(['gender'], axis=1)
#finding the mean
z_mean = z.mean(axis=0)
s_mean = s.mean(axis=0)
#creating object
objects = ('attr1_1','sinc1_1','intel1_1','fun1_1','amb1_1','shar1_1')
x_index=[1,2,3,4,5,6]

#creating distance with the bars
bar = 0.3
r1 = np.arange(len(objects))
r2 = [x + bar for x in r1]

#plotting the bar graph
plt.bar(r1,z_mean, color='blue',label = 'men')
plt.bar(r2,s_mean, color='red', label = 'women')
plt.xticks(x_index, objects)
plt.legend()


'''
    How often do they go out (not necessarily on dates)?
'''
#getting the data
features = dataset[['go_out','gender']]
#dropping the null value
features = features.dropna()

#for female
z = features[features['gender'] == 0]
z = z.drop(['gender'], axis=1)
#for male
s = features[features['gender'] == 1]
s = s.drop(['gender'], axis=1)

#finding the occurance count
z_val = z['go_out'].value_counts()
s_val = s['go_out'].value_counts()

#definig objects
objects = s_val.keys()
x_index=[1,2,3,4,5,6,7]

#creating the distance with the two graphs
bar = 0.3
r1 = np.arange(len(objects))
r2 = [x + bar for x in r1]

#plotting the bar graph
plt.bar(r1,z_val, color='blue',label = 'female')
plt.bar(r2,s_val, color='red', label = 'male')
plt.xticks(x_index, objects)
plt.legend()

'''
    In which activities are they interested?
'''
#getting the data from the dataset
features = dataset.iloc[:,50:67]
#dropping the null value
features = features.dropna()

#creating labels
labels = []
for col in features.columns: 
    labels.append(col)
#getting index
x_index =[]
for x in range(0,len(labels)):
    x_index.append(x)
#finding mean()
feat_mean = features.mean(axis=0)

#plotting the bar graph
plt.bar(x_index, feat_mean, color='blue')
plt.xticks(x_index, labels)

'''
    If the partner is from the same race are they more keen to go for a date?
'''
#getting coloumn from dataset
features = dataset[['samerace','date']]
#dropping the null value
features = features.dropna()

#selcting who got on a date with same race
race = features[features['samerace']== 1]
#finding how many times they went on a date
val_count = features['date'].value_counts()

#creating labels
labels = s_val.keys()
x_index=[1,2,3,4,5,6,7]

#plotting the graph
plt.bar(x_index,val_count)
plt.xticks(x_index,labels)

'''
    What are the least desirable attributes in a male partner? Does this differ for female partners?
'''
#getting the right coloumn from the dataset
features = dataset[['attr1_s','sinc1_s','intel1_s','fun1_s','amb1_s','shar1_s','gender']]
#dropping the null value
features = features.dropna()

#for male partners
z = features[features['gender'] == 1]
z = z.drop(['gender'], axis=1)
#finding the mean value
z_mean = z.mean(axis=0)

#for female partners
fem = features[features['gender'] == 0]
fem = fem.drop(['gender'], axis=1)
#finding the mean value
fem_mean = fem.mean(axis=0)

#creating labels
labels = z_mean.keys()
x_index = [1,2,3,4,5,6]

#bar graph for men
plt.bar(x_index,z_mean)
plt.xticks(x_index,labels)
#bar graph for female
plt.bar(x_index,fem_mean)
plt.xticks(x_index,labels)


'''
    How important do people think attractiveness is in potential mate selection vs. its real impact?
'''
#choosing the coloumn from the dataset
features = dataset[['attr1_1','attr1_2']]
#dropping the null value
features = features.dropna()

#finding the mean of the potential mate selection in attributes
potential = features['attr1_1'].mean()
#the real impact of the attractiveness
impact = features['attr1_2'].mean()

#adding them to one list
str1=[potential,impact]

#creating labels
labels = ('Potential' , 'real impact')
x_label= [1,2]

#plotting the bar graph
plt.bar(x_label , str1)
plt.xticks(x_label,labels)