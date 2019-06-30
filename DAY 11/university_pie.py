import csv

dict1={}
#reading the csv file
with open("University_data.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    #skipping the first coloumn
    next(csv_reader)
    #creating a dict and storing data
    for item in csv_reader:
        if item[0] in dict1:
            dict1[item[0]] += int(item[1])
        else:
            dict1[item[0]] = int(item[1])
        
        

#finding minimum value
key_min = min(dict1.keys(), key=(lambda k: dict1[k]))
print(key_min)


uni=[]
score=[]
#storing value of uni name in a list
for x in dict1.keys():
    if x not in uni:
        uni.append(x)
#storing value of gre score in another list
for x in dict1.values():
    if x not in uni:
        score.append(x)
        
#importing pyplot
from matplotlib import pyplot as plt

#exploding minimum value
explode = (0,0,0,0,0.2)
#ploting the pie chart
plt.pie(score,labels=uni,explode=explode)

#keeping axis equal
plt.axis('equal')
#showing the plotted pie chart
plt.show()