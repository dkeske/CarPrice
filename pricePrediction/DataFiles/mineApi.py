import json
import requests
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CarPrice.settings")
# Uncomment below for Django 1.7 +
import django
django.setup()

from pricePrediction.models import CarAd1


def parseJSON(param):
    novi = {}
    keys = ["power", "mileage", "year", "airCondition", "gearBox", "chassis", "price", "fuelType"]
    for key, val in param.iteritems():
        if key in keys:
            novi[key] = val
    return novi


def get_cars(pageID):
    r = requests.get('http://api.polovniautomobili.com/json/v3/getAds?' +
                     'pageID='+str(pageID)+'&SortingType=1&category=26&brandID=192&modelID=1824&old_or_new=both')
    classifieds = r.json()
    classifieds = classifieds.get('classifieds')

    # print classifieds[0].get('color')

    for car in classifieds:
        carId = car.get('AdID')
        url = 'http://api.polovniautomobili.com/json/v3/getAdDetails/'+str(carId)
        p = requests.get(url)
        carI = p.text
        carI = json.loads(carI)
        carI = parseJSON(carI)
        print carI
        # carI = '{"power":86, "mileage": 127000, "year":2007, "airCondition":"odjeb", "gearBox":"pada", "chassis":"lepa", "price":3000}'
        # carI = json.loads(carI)
        carAd1 = CarAd1.objects.create(idFromSite=carId, **carI)
        # print carAd1.power

for pageID in range(1, 48):
    get_cars(pageID)

