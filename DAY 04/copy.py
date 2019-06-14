import csv
#creating a new csv file
with open('copy.csv', mode='w') as employee_file:
    #opening an existing csv file
    with open("Salaries.csv") as csv_file:
        #reading data
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            #writing data in a new file
            writer = csv.writer(employee_file)
            writer.writerow(row)
csv_file.close()