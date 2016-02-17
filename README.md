# Car Price Prediction

## About the project

[Polovniautomobili] (http://www.polovniautomobili.com/) is the most popular website for selling new and used cars in Serbia. Next to its core functionality, it offers car tire search, registration price calculation, and others. Main idea of this project is to analyze car ads posted on the website, and predict the price of a car in relation to all the other cars posted on the website. The methods of machine learning used to achieve this are linear and ridge regression. 

## Project interfaces

This project features two use cases:

1. A web page
2. A chrome extension

### Web page

Using the web page, the user can enter the data related to the car he wishes to evaluate, and the system will predict a price, using the existing dataset. If the user disagrees with the calculated price, he can enter the price he thinks is more reasonable in a dialog that pops up. The data entered is then added to the dataset, and used in the next prediction in an effort to train the system and make it more accurate.

![Website screenshot](https://raw.githubusercontent.com/dkeske/CarPrice/master/pricePrediction/static/sellMegane.PNG "Website front page")

### Chrome extension

The project features a restful web service, which responds to requests sent by the chrome extension [CarPriceChrome] (https://github.com/dkeske/CarPriceChrome). After the user activates the extension in Chrome, upon opening a car ad on polovniautomobili.com, the extension will make a request to the service, and send the car's relevant data. The result (predicted price) is displayed next to the ad's title in bright orange.

## Implementation

The whole project is writen in [python 2.7.10](https://www.python.org/downloads/release/python-2710/) and [Django 1.8](https://www.djangoproject.com/start/overview/). 

### Data gathering

Data is gathered using the website, and the API. Data is scraped using python library [BeautifulSoup](https://pypi.python.org/pypi/beautifulsoup4), processed, and only the important properties are being saved. All the data curently used is scraped off the website, and API usage is still in development. 

### Dataset

Data is saved as a textual file in [DataFiles/outputfilePolovni.txt](https://github.com/dkeske/CarPrice/blob/master/pricePrediction/DataFiles/outputfilePOLOVNI.txt) and also in the sqlite3 database. Data model is located in [models.py](https://github.com/dkeske/CarPrice/blob/master/pricePrediction/models.py) :

class carAd(models.Model):

- kw : car's engine output in kilowats
- km : total mileage in kilometres
- year : year of production
- ac : type of air conditioning
- gears : type of transmission
- body : type of body
- price : listed price
- idFromSite : unique id on the website

After gathering, cathegorical values are vectorized, and displayed as zeroes and ones. Features with more than two cathegorical values are displayed using a sparse matrix, or "dummy values". Car's body type, which can take any of the four different values is transformed into 3 features, with all zeroes being the fourth one.

Generating training and testing set has an optional argument trainSize. If no value is provided, a training set containing 70 percent of the data is created, for purposes of analysis. If, on the other hand, the parameter is set to 1, the whole dataset will be used as training set, and no testing set will be created. The latter case is used when predicting a new car's value, using the whole dataset as training to improve accuracy.

### Linear and Ridge regression
Machine learning is implemented using the [scikit-learn](http://scikit-learn.org/stable/modules/linear_model.html) python library. Two classes are used, LinearRegression, and Ridge. Data is stored and procesed as [numpy](http://www.numpy.org/) arrays. 

Linear regression as a predictive model creates a relationship between a dependant variable, and one or more independent variables. In our case, car features make the independent variables, and the car price is the dependent one being predicted. Since we have more than one independent variable we are using multiple linear regression. The estimation method used is ordinary least squares (OLS), it is conceptually simple and computationally straightforward. The OLS method minimizes the sum of squared residuals.
 
Ridge regression is implemented using linear least squares with l2 regularization. This model solves a regression model where the loss function is the linear least squares function and regularization is given by the l2-norm. A parameter alpha is passed to the function, where small positive values of alpha improve the conditioning of the problem and reduce the variance of the estimates. 

### Technical realisation

## Analysis
















