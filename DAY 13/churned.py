import pandas as pd
#Read csv file
df = pd.read_csv("Telecom_churn.csv")

#Predict the count of Churned customer availing both voice mail plan and international plan schema
df_sub = df[(df['international plan'] == 'yes') & (df['voice mail plan'] == 'yes')]
dd_sub = df_sub[(df_sub['churn'] == True)]
print(dd_sub['international plan'].value_counts())

#Total charges for international calls made by churned and non-churned customer and visualize it
df_churn = df[(df['churn'] == True)]
summ = df_churn['total intl charge'].sum()

df_notchurn = df[(df['churn'] != True)]
summ1 = df_notchurn['total intl charge'].sum()

#Predict the state having highest night call minutes for churned customer
maxx = df['total night minutes'].max()
df_sub = df[(df['total night minutes'] == maxx )]
print(df_sub['state'])

#Visualize -
#    a. the most popular call type among churned user
#    b. the minimum charges among all call type among churned user

df_churn = df[(df['churn'] == True)]
sum_day = df_churn['total day calls'].sum()
sum_eve = df_churn['total eve calls'].sum()
sum_night = df_churn['total night calls'].sum()
sum_int = df_churn['total intl calls'].sum()
def maximum(a, b, c, d): 
  
    if (a >= b) and (a >= b) and (a >= c): 
        print('total day calls')
  
    elif (b >= a) and (b >= c)  and (b >= d): 
        print('total eve calls') 
        
    elif (c >= a) and (c >= b)  and (c >= d): 
        print('total night calls')
        
    else: 
        print('total int calls') 
          
maximum(sum_day,sum_eve,sum_night,sum_int)
  
df_churn = df[(df['churn'] == True)]
sum_day = df_churn['total day charge'].sum()
sum_eve = df_churn['total eve charge'].sum()
sum_night = df_churn['total night charge'].sum()
sum_int = df_churn['total intl charge'].sum()
def maximum(a, b, c, d): 
  
    if (a >= b) and (a >= b) and (a >= c): 
        print('total day charge')
  
    elif (b >= a) and (b >= c)  and (b >= d): 
        print('total eve charge') 
        
    elif (c >= a) and (c >= b)  and (c >= d): 
        print('total night charge')
        
    else: 
        print('total int charge') 
          
maximum(sum_day,sum_eve,sum_night,sum_int)

        
#Which category of customer having maximum account lenght?
#   Predict and print it
maxx = df['account length'].max()
df_sub = df[(df['account length'] == maxx )]
x = df_sub['churn']
print(x)

#Predict a relation between the customer and customer care service that 
#whether churned customer have shown their concern to inform the customer care 
#service about their problem or not

# running a for loop and asigning some values to series 
Service = pd.Series([])
for i in range(len(df_churn)):
    if df["customer service calls"][i] == 0: 
        Service[i]="0"
    else:
        Service[i]= "1"
#created a new coloumn
df_churn.insert(6,'Service',Service)

#number of customer showed interest vs no interest
df_sub = df_churn[df_churn['Service'] == '1' ]
sub = df_sub['Service'].value_counts()
print("Customer that showed concern")
print(sub)
df_sub = df_churn[df_churn['Service'] == '0' ]
sub = df_sub['Service'].value_counts()
print("Customer that didn't show concern")
print(sub)


#In which area code the international plan is most availed?
maxx = df['international plan'].max()
df_sub = df[(df['international plan'] == maxx )]
print(df_sub['area code'])
