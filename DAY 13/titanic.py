import pandas as pd
#Read csv file
df = pd.read_csv("training_titanic.csv")

#number of people who survived
df_sur= df[df['Survived'] == 1 ] # return DataFrame
print("Number of people survived")
print(df_sur['Survived'].value_counts())

#number of people died
df_die= df[df['Survived'] == 0 ] # return DataFrame
print("Number of people died")
print(df_die['Survived'].value_counts())

#Calculate and print the survival rates as proportions (percentage) 
df['Survived'].value_counts(normalize = True)

#Males that survived vs males that passed away
df_sub = df[df['Sex'] == 'male' ][['Survived']]
sub = df_sub['Survived'].value_counts()
print("Males that passed away")
print(sub[0])
print("Males that are still alive")
print(sub[1])

#Females that survived vs Females that passed away
df_sub = df[df['Sex'] == 'female' ][['Survived']]
sub = df_sub['Survived'].value_counts()
print("Females that passed away")
print(sub[0])
print("Females that are still alive")
print(sub[1])

#Does age play a role?

#removing NaN values
#df = df['Age'].dropna()
#df.count()
#we have to use mean in place of dropping the nan value beacuse of the key error

df['Age'] = df['Age'].fillna(df['Age'].mean())
#converting the series new_df to dataframe
#df = df.to_frame()

# running a for loop and asigning some values to series 
Child = pd.Series([])
for i in range(len(df)):
    if df["Age"][i] < 17: 
        Child[i]="1"
    else:
        Child[i]= "0"
#created a new coloumn
df.insert(6,'Child',Child)

#number of childs survived vs not survived
df_sub = df[df['Child'] == '1' ][['Survived']]
sub = df_sub['Survived'].value_counts()
print("Childs that passed away")
print(sub[0])
print("Childs that are still alive")
print(sub[1])




















