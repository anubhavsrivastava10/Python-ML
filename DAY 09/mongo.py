import pymongo
#import dns # required for connecting with SRV


client = pymongo.MongoClient("mongodb://new-user_31:anubhav123@cluster0-shard-00-00-drn7i.mongodb.net:27017,cluster0-shard-00-01-drn7i.mongodb.net:27017,cluster0-shard-00-02-drn7i.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test


mydb = client.DB1

def add_employee(name, age, rno, branch):
    unique_employee = mydb.employees.find_one({"Stud_roll_no":rno})
    if unique_employee:
        return "Employee already exists"
    else:
        mydb.student_record.insert_one(
            {
                    "Stud_Name" : name,
                    "Stud_Age" : age,
                    "Stud_roll_no" : rno,
                    "Stud_branch" : branch
            }
            )
    return "Employee added successfully"


def fetch_all_employee():
    user = mydb.yourcollectionname.find()
    for i in user:
        print (i)


add_employee('Doremon',19,123,'ME')
add_employee('Nobita',20,124,'CSE')
add_employee('Shinchan',11,125,'CSE')
add_employee('Susuka',21,126,'CSE')
add_employee('Dekisuki',22,124,'IT')
add_employee('Pikachu',22,124,'IT')

fetch_all_employee()
