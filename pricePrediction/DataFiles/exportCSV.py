from pymongo import MongoClient
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
client = MongoClient()
db = client.diplomski
result = db.cars.find()
dict = []
for row in result:
    dict.append(row)
df = pd.DataFrame(data=dict)
df.to_csv('cars.csv', index=True, header=True, encoding="UTF-8")