import numpy as np
# import os
from pricePrediction import models
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
