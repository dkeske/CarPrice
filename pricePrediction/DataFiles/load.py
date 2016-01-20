import numpy as np
import pickle
from sklearn.feature_extraction import DictVectorizer
# import os
import os
##########
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CarPrice.settings")
# Uncomment below for Django 1.7 +
import django
django.setup()
##########
from pricePrediction import models

def getSet1():
    fields = ['chassis', 'airCondition', 'gearBox', 'fuelType', 'mileage', ]
    featureList = models.CarAd1.objects.values()
    v = DictVectorizer(sparse=False)
    X = v.fit_transform(featureList)
    # v.restrict(['idFromSite'])
    print v.vocabulary_
    print v.get_feature_names()
    F = X[:, :18]
    S = X[:, 19:]
    sum = np.concatenate((F, S), axis=1)
    print F.shape
    print S.shape
    print sum.shape
    # for elem in X[0]:
    #     print elem
    with open("dataModel.p", 'w') as f: #write whole model into file
        pickle.dump(sum, f, 2)
    return [sum, [], [], []]


def getSet(trainSize=0.7):
    # dirname = os.path.dirname(__file__)
    # f = open(dirname+ '/outputfilePOLOVNI.txt')
    #
    # dataAllParams = np.loadtxt(f, delimiter=',')
    # np.random.shuffle(dataAllParams)
    #
    # dataParams= dataAllParams[:, :-1]
    # dataPrice = dataAllParams[:, -1:]
    dataParams = []
    dataPrice = []


    for carAd in models.carAd.objects.all():
        body = carAd.body.split(",")
        dataParams.append([carAd.kw, carAd.km, carAd.year, carAd.ac, carAd.gears, body[0], body[1], body[2]])
        dataPrice.append([carAd.price])

    dataParams = np.array(dataParams).astype(np.float)
    dataPrice = np.array(dataPrice).astype(np.float)
    dataPrice = np.squeeze(np.asarray(dataPrice))


    rowNumParams = len(dataParams)
    rowNumPrice = len(dataPrice)

    dataParams_train = dataParams[:rowNumParams*trainSize]
    dataPrice_train = dataPrice[:rowNumPrice*trainSize]

    dataParams_test = dataParams[rowNumParams*trainSize:]
    dataPrice_test = dataPrice[rowNumPrice*trainSize:]

    return [dataParams_train, dataPrice_train, dataParams_test, dataPrice_test]
if __name__ == "__main__":
    getSet1()