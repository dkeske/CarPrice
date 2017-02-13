from pymongo import MongoClient
import requests
import time

def parseJSON(param):
    novi = {}
    keys = ["images", "photoLink"]
    for key, val in param.iteritems():
        if key not in keys:
            novi[key] = val
    return novi


def get_cars(pageID):
    r = requests.get('http://api.polovniautomobili.com/json/v3/getAds?' +
                     'pageID=' + str(pageID) + '&SortingType=1&category=26&brandID=192&modelID=1824&old_or_new=both')
    # http://api.polovniautomobili.com/json/v3/getAds?pageID=1&SortingType=1&category=26&brandID=192&modelID=1824&old_or_new=both
    classifieds = r.json()
    classifieds = classifieds.get('classifieds')
    for car in classifieds:
        car_id = car.get('AdID')
        url = 'http://api.polovniautomobili.com/json/v3/getAdDetails/' + str(car_id)
        p = requests.get(url)
        print p.status_code
        carI = p.json()
        # print carI
        carI = parseJSON(carI)
        # print carI
        result = db.cars_test.insert_one(
            carI
        )

if __name__ == "__main__":
    client = MongoClient()
    db = client.diplomski

    for page in range(1, 56): #52
        get_cars(page)
        time.sleep(5)
        print page
