# Create your views here.
from django.shortcuts import render
import os


def calculatePrice(kw, km, year, ac, gears, body):
	import numpy as np 
	from sklearn import linear_model, datasets
	module_dir = os.path.dirname(__file__)  # get current directory
	
	f = open(os.path.join(module_dir, "outputfilePOLOVNI.txt"))
	g = open(os.path.join(module_dir, "outputfilePOLOVNIcena.txt"))
	h = open(os.path.join(module_dir, "ocena.txt"), 'w')

	dataParams = np.loadtxt(f, delimiter=',')
	dataPrice = np.loadtxt(g)
	clf = linear_model.Ridge (alpha = .3, normalize=True)
	clf.fit(dataParams, dataPrice)
	kw = int(kw)
	km = int(km)
	year = int(year)
	ac = int(ac)
	gears = int(gears)
	body = int(body)
	prediction = clf.predict([kw, km, year, ac, gears, body])
	return prediction[0]
	#dodaj da uci, korisnik unosi cenu koju je stavio na oglas, i onda je dodajemo u dataset

def home (request):
	if request.method == 'GET':
		return render(request, 'index.html')
	if request.method == 'POST':
		kw = request.POST['kw']
		km = request.POST['km']
		year = request.POST['year']
		ac = request.POST['ac']
		gears = request.POST['gears']
		body = request.POST['body']

		price = calculatePrice(kw, km, year, ac, gears, body)

		return render(request, 'index.html', {'price':price, 'kw':kw, 'km':km, 'year':year, 'ac':ac, 'gears':gears, 'body':body})