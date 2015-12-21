
def saveToFile(kw, km, year, ac, gears, body, userPrice):
    f = open("C:\Python27\Projects\CarPrice\pricePrediction\DataFiles\outputfilePOLOVNI.txt", 'a')
    #klima, menjac, karos
    if body == "0" :
        body = "0,0,0"
    if body == "1":
        body = "1,0,0"
    if body == "2":
        body = "0,1,0"
    if body == "3":
        body = "0,0,1"
    f.write(kw+','+km+','+year+','+ac+','+gears+','+body+','+userPrice)
    f.close()