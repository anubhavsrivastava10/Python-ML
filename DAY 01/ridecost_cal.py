distance = input("Enter the distance to and fro> ")
distance = float(distance)
distance = distance * 2
cost = input("Enter the cost of fuel per litres> ")
cost = float(cost)
average = input("Enter the average of the vehicle> ")
average = float(average)
ltr = distance / average
ltr = float(ltr)
total_cost = ltr * cost
print(total_cost)