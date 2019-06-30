import csv

#reading csv file
A=[]
B=[]
with open("sealevel.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    #skipped reading first line
    next(csv_reader)
    # row has the list of all columns
    #string data of each row in a list
    for row in csv_reader:
        A.append(row[0])
        B.append(row[1])
        
from matplotlib import pyplot as plt

#adding details
plt.xlabel('Year')
plt.ylabel('Increased Inches')
plt.title('Sea Level Rise')

#plotting the graph
plt.plot(A,B,label='inches',linestyle='dashed')

#providing different colors
plt.legend()
#showing the graph
plt.show()
        
#the suuden chaneg in the graph is known as outliners
