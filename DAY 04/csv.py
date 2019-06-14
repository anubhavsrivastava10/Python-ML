dict1={}
import csv
with open("passwd",mode="rt") as file: #to open a file remove it's extension
    for line in file:
        feild = line.split(":")
        if feild[0] != '#':
            dict1[feild[0]] = dict1.get(feild[0],feild[2])
        with open('employee.csv', mode='a') as employee_file:
            employee_writer = csv.writer(employee_file, delimiter=' ')
            for key,value in dict1.items():
                employee_writer.writerow([key,value])
    
