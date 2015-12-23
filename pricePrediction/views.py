# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse

from pricePrediction.models import carAd


def parseBody(body):
    if body == "0":
        return [0,0,0]
    if body == "1":
        return [1,0,0]
    if body == "2":
        return [0,1,0]
    if body == "3":
        return [0,0,1]
    #Limuzina 0
    #Hecbek   1
    #Karavan  2
    #Kupe     3

def calculatePrice(kw, km, year, ac, gears, body):
    import DataFiles.analize as an

    clf = an.makeModelforView()
    kw = int(kw)
    km = int(km)
    year = int(year)
    ac = int(ac)
    gears = int(gears)
    body = parseBody(body)

    parametres = [kw, km, year, ac, gears]
    parametres.extend(body)

    prediction = clf.predict(parametres)
    return "{0:.2f}".format(prediction[0])
#dodaj da uci, korisnik unosi cenu koju je stavio na oglas, i onda je dodajemo u dataset
#dodaj i modal za unos :)

def home (request):
    if request.method == 'GET':
        return render(request, 'index.html')
    if request.method == 'POST':
        try:
            kw = request.POST['kw']
            km = request.POST['km']
            year = request.POST['year']
            ac = request.POST['ac']
            gears = request.POST['gears']
            body = request.POST['body']

            price = calculatePrice(kw, km, year, ac, gears, body)

            return JsonResponse({'price':price})
        # return render(request, 'index.html', {'price':price, 'kw':kw, 'km':km, 'year':year, 'ac':ac, 'gears':gears, 'body':body})
        except Exception, e:
            return render(request, 'index.html')


def userSubmit(request):
    from DataFiles.save import saveToFile
    if request.method == 'POST':
        try:
            kw = request.POST['kw']
            km = request.POST['km']
            year = request.POST['year']
            ac = request.POST['ac']
            gears = request.POST['gears']
            body = request.POST['body']
            userPrice = request.POST['userPrice']
            if body == "0" :
                body = "0,0,0"
            if body == "1":
                body = "1,0,0"
            if body == "2":
                body = "0,1,0"
            if body == "3":
                body = "0,0,1"
            carAdInstance = carAd(kw=kw, km=km, year=year, ac=ac, gears=gears, body=body, price=userPrice)
            carAdInstance.save()
            # saveToFile(kw, km, year, ac, gears, body, userPrice)
            return HttpResponse(status=200)
        except Exception, e:
            return HttpResponse(status=403)
