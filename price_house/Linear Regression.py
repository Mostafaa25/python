import pandas as pd
import sklearn as sk
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression as lr
from sklearn.model_selection import train_test_split as tts

######################################################################
# Data Loading and Exploration:
try:
    dt = pd.read_csv("aaa.csv")
except FileNotFoundError:
    print("Error: 'aaa.csv' file not found. Please check the file path.")
    exit()  # Exit the script if file not found
    
dt.head()
dt.info()
dt.describe()  # Additional data validation

plt.figure(figsize=(5, 5))

plt.scatter(x=dt['price'], y=dt['sqft_living']) 
plt.xlabel('prison')
plt.ylabel('years')
plt.show()
 
 

plt.figure(figsize=(7, 7))
plt.scatter(x=dt['price'], y=dt['grade'])
plt.xlabel('price')
plt.ylabel('grade')
plt.show()

print(dt.shape)
print(dt.columns)

#######################################################################
# Feature Selection (preparing data )and Visualization:
features = ['bedrooms', 'bathrooms', 'sqft_living',
            'sqft_lot', 'floors', 'waterfront', 'view', 'condition', 'grade',
            'sqft_above', 'sqft_basement', 'yr_built', 'yr_renovated',
            'lat', 'long']
X = dt[features]
y = dt['price']

sns.pairplot(dt, y_vars="price", x_vars=features, kind='reg', palette='spring')

#######################################################################
# Data Splitting: train , test
X_train, X_test, y_train, y_test = tts(X, y, test_size=0.3, random_state=5)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

#######################################################################
# Model Training and Evaluation (Linear Regression):
clf = lr()
clf.fit(X_train, y_train)
accuracy = clf.score(X_test, y_test)
print("Accuracy (Linear Regression): {}%".format(int(round(accuracy * 100))))

#######################################################################
# Prediction and Visualization:
pred = clf.predict(X_test)

plt.scatter(X_test['sqft_living'], y_test, color='red')  # Example using sqft_living
plt.plot(X_test['sqft_living'], pred, color='blue')
plt.title("Visuals for Test Dataset (Linear Regression)")
plt.xlabel("Space (sqft_living)")
plt.ylabel("Price")
plt.show()

#############################################################################
# Always ensure your input data has the same shape as the data used for model training
new_house1_features = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
new_house1_features = pd.DataFrame([new_house1_features], columns=features)  # Add feature names
predicted_price = clf.predict(new_house1_features)
print("Predicted price:", predicted_price)
#############################################################################

