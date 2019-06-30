import pandas as pd
import numpy as np
import os
from matplotlib import pyplot as plt
final = pd.DataFrame()
d=1880
lst = os.listdir()
for item in lst:
    df = pd.read_csv(item,header=None)#
    df.insert(3,'Year',d,True)
    d+=1
    final = pd.concat([df,final] , ignore_index = True)#
df_rank = final.groupby(['Year'])
#count the number of males and females
final[1].value_counts()
#top 5 female name in year #****
result_temp = final[final["Year"]==1880].head(5)
result_temp.index= [x for x in range(result_temp.shape[0])]
#top 5 male name in year #****
result_temp1 = final[(final["Year"]==1880) & (final[1]== 'M')].head(5)
result_temp1.index= [x for x in range(result_temp.shape[0])]
#sum of the births column by sex as the total number of births in that year
table1 = pd.pivot_table(final , values=2 ,index=[1],columns=['Year'],aggfunc=np.sum)
#plotting graph for table
index = []
index1=[]
x = table1.keys().tolist()
y = table1.iloc[0]
z = table1.iloc[1]
for number in x:
    index1.append(number+0.35)
    index.append(number-0.35)
plt.bar(index,y,width=0.3,color='blue',label='Female')
plt.bar(index1,y,width=0.3,color='red',label='Male')
plt.legend()
plt.xlabel("Year")
plt.ylabel("Count")
plt.title('results of the above activity to show total births by sex and year ')
plt.show()