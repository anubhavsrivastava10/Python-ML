
#info data
girls_grades = [89, 90, 70, 89, 100, 80, 90, 100, 80, 34]
boys_grades = [30, 29, 49, 48, 100, 48, 38, 45, 20, 30]
grades_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

#importing pyplot
from matplotlib import pyplot as plt

#additional info
plt.xlabel('Grades Range')
plt.ylabel('Grades')
plt.title('Grades Comparison')

#plotting the scattered graph
plt.scatter(grades_range, girls_grades, marker='d', color='red',label="Girls Grade".format('.')); 
plt.scatter(grades_range, boys_grades, marker='o', color='blue',label="Boys Grade".format('.')); 

#providing differentiable info between markers
plt.legend()
#showing the graph
plt.show()