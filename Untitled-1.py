import pandas
from sklearn import linear_model
import numpy

df = pandas.read_csv("m 1.csv")

X = df[['hsot',"ashot","hshot",'asot','hs','as','hr','ar']]
y = df['ag']

regr = linear_model.LinearRegression()
regr.fit(X, y)

vX = df[['hsot',"ashot","hshot",'asot','hs','as','hr','ar']]
vy = df['hg']

vregr = linear_model.LinearRegression()
vregr.fit(vX, vy)

predictedC = regr.predict([[4,1,13,3,9,6,4,4]])
cint = int(predictedC)
predictedCO2 = round(cint)
predictedCv = vregr.predict([[4,1,13,3,9,6,4,4]])
cvint = int(predictedCv)
predictedCO2v = round(cvint)
