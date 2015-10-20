import numpy as np 
from sklearn import linear_model, datasets, metrics
import math

def makeModel(trainSize=0.7):
	
	f = open("outputfilePOLOVNI.txt")
	g = open("outputfilePOLOVNIcena.txt")
	h = open("ocena.txt", "w")

	dataParams = np.loadtxt(f, delimiter=',')[:,:]
	dataPrice = np.loadtxt(g)

	rowNumParams = dataParams.shape[0]
	rowNumPrice = dataPrice.shape[0]
	#odnos 70:30
	dataParams_train = dataParams[:rowNumParams*trainSize]
	dataParams_test = dataParams[rowNumParams*trainSize:]

	dataPrice_train = dataPrice[:rowNumPrice*trainSize]
	dataPrice_test = dataPrice[rowNumPrice*trainSize:]

	clf = linear_model.LinearRegression(normalize=True, n_jobs=-1)
	# clf = linear_model.Ridge (alpha = .2, normalize=True)

	clf.fit(dataParams_train, dataPrice_train)

	predicted = clf.predict(dataParams_test)

	mean_abs_error = metrics.mean_absolute_error(dataPrice_test, predicted)
	mean_sqr_error = metrics.mean_squared_error(dataPrice_test, predicted)
	print("Mean absolute error")
	print(mean_abs_error)
	print("Root mean squared error")
	print(math.sqrt(mean_sqr_error))



	# print(np.mean(clf.predict(dataParams_test)-dataPrice_test)**2)
	print("Coefficients: ")
	print(clf.coef_)
	# # print("Konstanta: ")
	# # print(clf.intercept_)
	print("How well does the model fit the data? 0-1")
	print(clf.score(dataParams_test, dataPrice_test))
	# print("Razlika: ")
	# print(clf.predict(dataParams_test)-dataPrice_test)
	# np.savetxt(h, clf.predict(dataParams_test)-dataPrice_test, fmt='%.2f')
	# recall, precision accuracy ?!
	return clf
def makeModelforView():
	f = open("pricePrediction\DataFiles\outputfilePOLOVNI.txt")
	g = open("pricePrediction\DataFiles\outputfilePOLOVNIcena.txt")
	
	dataParams = np.loadtxt(f, delimiter=',')
	dataPrice = np.loadtxt(g)

	clf = linear_model.LinearRegression(normalize=True, n_jobs=-1)
	# clf = linear_model.Ridge (alpha = .2, normalize=True)

	clf.fit(dataParams, dataPrice)

	return clf
makeModel()