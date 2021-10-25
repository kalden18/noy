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

predictedC = regr.predict([[4,1,13,3,9,6,4.5,4.5]])
cint = int(predictedC)
predictedCO2 = round(cint)
predictedCv = vregr.predict([[4,1,13,3,9,6,4.5,4]])
cvint = int(predictedCv)
predictedCO2v = round(cvint)
train_x = predictedCO2[:80]
train_y = predictedCO2v[:80]

test_x = predictedCO2[80:]
test_y = predictedCO2v[80:]
mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))
print(mymodel)