# Car Price Prediction

## About the project

[Polovniautomobili] (http://www.polovniautomobili.com/) is the most popular website for selling new and used cars in Serbia. Next to its core functionality, it offers car tire search, registration price calculation, and others. Main idea of this project is to analyze car ads posted on the website, and predict the price of a car in relation to all the other cars posted on the website. The methods of machine learning used to achieve this are linear and ridge regression. 

## Project interfaces

This project features two use cases:
1. A web page
2. A chrome extension

### Web page

Using the web page, the user can enter the data related to the car he wishes to evaluate, and the system will predict a price, using the existing dataset. If the user disagrees with the calculated price, he can enter the price he thinks is more reasonable in a dialog that pops up. The data entered is then added to the dataset, and used in the next prediction in an effort to train the system and make it more accurate.

### Chrome extension

The project features a restful web service, which responds to requests sent by the chrome extension [CarPriceChrome] (https://github.com/dkeske/CarPriceChrome). After the user activates the extension in Chrome, upon opening a car ad on polovniautomobili.com, the extension will make a request to the service, and send the car's relevant data. The result (predicted price) is displayed next to the ad's title in bright orange.

## Implementation

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

Generating training and testing set has an optional argument trainSize. If no value is provided, a training set containing 70 percent of the data is created, for puroses of analysis. If, on the other hand, the parameter is set to 1, the whole dataset will be used as training set, and no testing set will be created. The latter case is used when predicting a new car's value.

### Linear and Ridge regression
Machine learning is implemented using the [scikit-learn](http://scikit-learn.org/stable/modules/linear_model.html) python library. Two classes are used, LinearRegression, and Ridge. 

### Technical realisation

## Analysis
