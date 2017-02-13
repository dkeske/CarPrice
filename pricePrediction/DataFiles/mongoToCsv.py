from pymongo import MongoClient
from unicodecsv import DictWriter

client = MongoClient()
db = client.diplomski

# cursor = db.cars.find({}, {"_id": 0, 'mileage': 1, 'year': 1, 'fuelType': 1, 'price': 1,
#                            'engineVolume': 1, 'power': 1, 'Karavan': 1, 'Hecbek': 1, 'Kupe': 1,
#                            'Kabriolet': 1, 'Minivan': 1, 'Limuzina': 1 , 'Dizel' :1, 'Benzin' :1,
#                            'TNG' :1, 'Metan' :1})

cursor = db.cars.find({}, {"_id": 0, 'mileage': 1, 'year': 1, 'fuelType': 1, 'price': 1,
                           'engineVolume': 1, 'power': 1, 'registration': 1, 'userType': 1,
                           'gearBox': 1, 'interiorMaterial': 1, 'chassis': 1})

with open('cars.csv', 'wb') as outfile:
    fields = ['mileage', 'year', 'fuelType', 'price', 'engineVolume', 'power', 'registration', 'userType',
              'gearBox', 'interiorMaterial', 'chassis']
    writer = DictWriter(outfile, fieldnames=fields)
    writer.writeheader()
    for x in cursor:
        writer.writerow(x)
