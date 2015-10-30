import numpy as np 
from sklearn import linear_model, datasets, metrics, svm, cross_validation
import math, load

def getInfo(dataParams_test, dataPrice_test, clf):
	predicted = clf.predict(dataParams_test) #ocekujemo dataPrice_test
	
	mean_abs_error = metrics.mean_absolute_error(dataPrice_test, predicted)
	mean_sqr_error = metrics.mean_squared_error(dataPrice_test, predicted)

	print("Mean absolute error")
	print(mean_abs_error)
	print("Root mean squared error")
	print(math.sqrt(mean_sqr_error))
	print("How well does the model fit the data? 0-1 *************")
	print(clf.score(dataParams_test, dataPrice_test))

	# print("Coefficients: ")
	# koef = clf.coef_
	# for coef in koef:
	# 	print "{0:.2f}".format(float(coef))
	# print("Constant: ")
	# print(clf.intercept_)


def doLinear(trainSize=0.7):
	clf = linear_model.LinearRegression(normalize=True, n_jobs=-1)
	dataSet = load.getSet(trainSize)

	dataParams_train = dataSet[0]
	dataParams_test = dataSet[2]
	dataPrice_train = dataSet[1]
	dataPrice_test = dataSet[3]

	clf.fit(dataParams_train, dataPrice_train)
	print("****LINEAR****")
	if trainSize!=1:
		getInfo(dataParams_test, dataPrice_test, clf)
	return clf

def doRidge(trainSize=0.7):
	clf2 = linear_model.Ridge(alpha = .1, normalize=True)
	
	dataSet = load.getSet(trainSize)

	dataParams_train = dataSet[0]
	dataParams_test = dataSet[2]
	dataPrice_train = dataSet[1]
	dataPrice_test = dataSet[3]

	clf2.fit(dataParams_train, dataPrice_train)
	print("****RIDGE****")
	if trainSize!=1:
		getInfo(dataParams_test, dataPrice_test, clf2)

	return clf2

def doSvm(trainSize=0.7):
	clfSvm = svm.LinearSVR(C=1.0, epsilon=0.2)

	dataSet = load.getSet(trainSize)

	dataParams_train = dataSet[0]
	dataParams_test = dataSet[2]
	dataPrice_train = dataSet[1]
	dataPrice_test = dataSet[3]


	clfSvm.fit(dataParams_train, dataPrice_train)
	print("****SVR****")
	if trainSize!=1:
		getInfo(dataParams_test, dataPrice_test, clfSvm)
	return clfSvm
def makeModel(trainSize=0.7):
	
	doLinear()
	doRidge()
	doSvm()
	
	
def makeModelforView():
	clf = doLinear(1)

	return clf