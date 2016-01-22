# Car Price Prediction

## About the project

[Polovniautomobili] (http://www.polovniautomobili.com/) is the most popular website for selling new and used cars in Serbia. Next to its core functionality, it offers car tire search, registration price calculation, and others. Main idea of this project is to analyze car ads posted on the website, and predict the price of a car in relation to all the other cars posted on the website. The method of machine learning used to achieve this is linear regression. 

## Project interfaces

This project features two use cases:
1. A web page
2. A chrome extension

## Web page

Using the web page, the user can enter the data related to the car he wishes to evaluate, and the system will predict a price, using the existing dataset. If the user disagrees with the calculated price, he can enter the price he thinks is more reasonable in a dialog that pops up. The data entered is then added to the dataset, and used in the next prediction in an effort to train the system and make it more accurate.

## Chrome extension

The project features a restful web service, which responds to requests sent by the chrome extension [CarPriceChrome] (https://github.com/dkeske/CarPriceChrome). After the user activates the extension in Chrome, upon opening a car ad on polovniautomobili.com, the extension will make a request to the service, and send the cars relevant data. The result (predicted price) is displayed next to the ad title.

## Implementation


