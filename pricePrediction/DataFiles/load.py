import numpy as np
def getSet(trainSize=0.7):
    f = open('outputfilePOLOVNI.txt')

    dataAllParams = np.loadtxt(f, delimiter=',')
    np.random.shuffle(dataAllParams)

    dataParams= dataAllParams[:,:-1]
    dataPrice = dataAllParams[:,-1:]
    dataPrice = np.squeeze(np.asarray(dataPrice))

    rowNumParams = dataParams.shape[0]
    rowNumPrice = dataPrice.shape[0]

    dataParams_train = dataParams[:rowNumParams*trainSize]
    dataPrice_train = dataPrice[:rowNumPrice*trainSize]

    dataParams_test = dataParams[rowNumParams*trainSize:]
    dataPrice_test = dataPrice[rowNumPrice*trainSize:]

    return [dataParams_train, dataPrice_train, dataParams_test, dataPrice_test]