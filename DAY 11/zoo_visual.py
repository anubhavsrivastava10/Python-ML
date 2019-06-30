import csv
zoo_data = {}
with open('zoo.csv','rt') as ani:
    reader = csv.reader(ani,delimiter = ',')
    next(reader)
    for i in reader:
        if i[0] in zoo_data:
            zoo_data[i[0]] += int(i[2])
        else:
            zoo_data[i[0]] = int(i[2])

animal=[]
paani=[]
#storing value of uni name in a list
for x in zoo_data.keys():
    if x not in animal:
        animal.append(x)
#storing value of gre score in another list
for x in zoo_data.values():
    if x not in paani:
        paani.append(x)
        
#importing pyplot
from matplotlib import pyplot as plt
#plotting bar graph 

#adding details
plt.xlabel('Animals')
plt.ylabel('Water Usage')
plt.title('Water usage by different animals')

x_index = [0,1,2,3,4]
#plotting bar graph
plt.bar(x_index,paani,label='Water Usage')
# First Parameters is the indexes and second paramters is the labels
plt.xticks(x_index, animal)
#providing different colors
plt.legend()
#showing the plotted data
plt.show()
