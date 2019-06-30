import pandas as pd

dataset  = pd.read_csv('Female_Stats.csv')

features = dataset.iloc[:,1:]
labels = dataset.iloc[:,0]

import statsmodels.api as sm
features = sm.add_constant(features)

features_opt = features[:]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()

#print(regressor_OLS.params[1])
#print(regressor_OLS.params[2])

x = labels[0].mean()

#for inc in mother's height

features_opt = features.momheight + 1
features_opt = features_opt.to_frame()

# Fitting Linear Regression to the dataset
from sklearn.linear_model import LinearRegression
lin_reg_1 = LinearRegression()
lin_reg_1.fit(features_opt, labels)

lst1=[]
for item in labels:
    y = lin_reg_1.predict(item)
    lst1.append(y)
    
df = pd.DataFrame(lst1)
z=df[0].mean()
diff = z-x
print("For Mom height inc by 1 : " + str(diff))

#for inc in Father's height

features_opt = features.dadheight + 1
features_opt = features_opt.to_frame()

# Fitting Linear Regression to the dataset
from sklearn.linear_model import LinearRegression
lin_reg_1 = LinearRegression()
lin_reg_1.fit(features_opt, labels)

lst1=[]
for item in labels:
    y = lin_reg_1.predict(item)
    lst1.append(y)
    
df = pd.DataFrame(lst1)
z=df[0].mean()
diff = z-x
print("For Dad height inc by 1 : " + str(diff))
