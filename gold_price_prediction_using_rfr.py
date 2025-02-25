# 
##GOLD PRICE PREDICTION USING RFR

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

data=pd.read_csv("gold_price_data.csv")
data.head()
#GLD -GOLD PRICE
#USO - CRUDE PRICE IN USA
#SLV - SILVER PRICE
#EUR/USD -CURRENCY PRICE IN EURO

data.tail()

data.shape

data.isnull().sum()
# No missing values

data.describe()

#checking correlation

num_data = data.select_dtypes(include=['number'])
correlation = num_data.corr()

plt.figure(figsize=(8, 8))
sns.heatmap(correlation, cbar=True, square=True, fmt='.1f',annot=True,annot_kws={'size':8},cmap='Blues')
plt.title('Correlation Heatmap')
plt.show()

print(correlation['GLD'])

#Gold and Silver are positively correlated
#Gold and Crude are negatively correlated

sns.distplot(data['GLD'],color='Blue')

x=data.drop(['Date','GLD'],axis=1)
  y=data['GLD']

print(x)

print(y)

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=2)

from sklearn.ensemble import RandomForestRegressor

regressor = RandomForestRegressor(n_estimators=100)
regressor.fit(x_train, y_train)

test_data_pred=regressor.predict(x_test)
print(test_data_pred)

#R-SQUARED ERROR
#Actual vs predicted
error_score=metrics.r2_score(y_test,test_data_pred)
print("R squared error:",error_score)

y_test=list(y_test)
plt.plot(y_test,color='blue',label='Actual Value')
plt.plot(test_data_pred,color='green',label='Predicted Value')
plt.title('Actual Price vs Predicted Price')
plt.xlabel('Number of values')
plt.ylabel('GLD Price')
plt.legend()

