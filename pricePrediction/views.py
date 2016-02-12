# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import traceback

from pricePrediction.models import CarAd


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

def getIdFromUrl(url):
    idFromSite = url.split('/')[-2]
    return idFromSite

def calculatePrice(kw, km, year, ac, gears, body):
    import DataFiles.analize as an

    clf = an.makeModelforView()
    kw = int(kw)
    km = int(km)
    year = int(year)
    ac = int(ac)
    gears = int(gears)
    if type(body) != list:
        body = parseBody(body)
    else:
        body = [float(body[0]), float(body[1]), float(body[2])]
    parameters = [kw, km, year, ac, gears]
    parameters.extend(body)

    prediction = clf.predict(parameters)
    return "{0:.2f}".format(prediction[0])


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
            traceback.print_exc()
            return render(request, 'index.html')


def userSubmit(request):
    # from DataFiles.save import saveToFile
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
            carAdInstance = CarAd(kw=kw, km=km, year=year, ac=ac, gears=gears, body=body, price=userPrice)
            carAdInstance.save()
            # saveToFile(kw, km, year, ac, gears, body, userPrice)
            # return HttpResponse(status=200)
            return render('index.html', {'cars': CarAd.objects.all()})
        except Exception, e:
            traceback.print_exc()
            return HttpResponse(status=403)

@csrf_exempt
def chrome(request):
    if request.method == 'POST':
        try:
            url = request.POST['url']
            idFromSite = getIdFromUrl(url)
            car = CarAd.objects.filter(idFromSite=idFromSite)[0]
            price = calculatePrice(car.kw, car.km, car.year, car.ac, car.gears, car.body.split(','))
            return render(request, 'chrome.html', {'price': price})
        except Exception as e:
            # traceback.print_exc()
            return render(request, 'chrome.html', {'price': "?"})
