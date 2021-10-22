import pandas
from sklearn import linear_model

df = pandas.read_csv("C:/Users/kalden/documents/book.csv")

X = df[['away', 'Home']]
y = df['ftr']

regr = linear_model.LinearRegression()
regr.fit(X, y)

predictedCO2 = regr.predict([["5", "1"]])
if predictedCO2 == 1:
    print("home side wins !")
elif predictedCO2 == 0:
    print("away side wins !")
elif predictedCO2 == 2:
    print("its a draw !")    

