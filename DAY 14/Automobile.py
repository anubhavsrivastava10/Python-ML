#importing files
import pandas as pd
#reading csv file
df = pd.read_csv("Automobile.csv")
#arranging them in sorted order according to maker's
x = df['make'].value_counts()
#changing to dataframe
df_ = pd.DataFrame(x)
#finding first 10 makers
y = df_.head(10)
#plotting a pie chart
explode = (0.2, 0, 0, 0, 0, 0, 0, 0, 0, 0)
plot = y.plot.pie(y='make', figsize=(5,5), explode=explode)