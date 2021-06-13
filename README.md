Introduction/Background
The stock market is an area where people can go to invest their money for small amounts of a business in the form of shares. Many have attempted to predict the movement of the market, however many machine learning studies have failed to accurately capture the full nature of the market (Source 1). This can be a result of high volatility, commonly seen today in shares such as TSLA or GME, but also due to other algorithmic factors such as poor training data size as well as imperfect feature selection (Source 2). 

We aim to investigate (A SPECIFIC AREA OF STOCKS) over a period from 2012-2019 to investigate performance in paper trading by traditional machine learning algorithms. This will then be compared to personal performance in paper trading utilizing what is known individually to attempt to maximize profits. This will give a simple approach to the success of the algorithm while utilizing a vast amount of data to attempt to reach the most logical conclusions on what stocks to buy or sell.

Problem definition: 

We aim to investigate the success in paper trading in comparison to what would be expected by an everyday person after training on an extended period of stock prices. This is in effort to determine the best features that dictate whether to buy or sell in order to maximize profit. 

Methods

To make the predictor, we will be using stock data sourced from Polygon.io. We will extract features from daily stock data such as opening value, daily highs and daily lows from 2012 to 2019 and create an algorithm that models the data. The algorithm will then predict whether the stock will rise or fall and pick the stocks that it believes will return the best value over time. 
Stock predictors have commonly used models made with logistic regression, neural networks, k-nearest neighbors and support-vector machines (source 3). With logistic regression, we will model the stock data from a training set to an equation that could be used to predict whether the stock will rise or fall. Then we will compare this predictor to a set of testing data and compare with more successful models to adjust the equation to minimize loss.
We will also try an SVM for the predictive model. It will be used in a similar capacity to separate the stocks into more desirable and less desirable groups to decide which stocks are best to choose. 
We may also use a Neural Network



Potential results and Discussion (The results and methods may change over the course of this class while you are working on the project and it is fine; that's why it is called research)

The success scenario includes the model performing better than average among by [percentage] us over a period of [number of days]. Satisfactory scenario would be model performance within +- [percentage]. Out comparison reference point (out performance with[Specific are of stock] is has obvious self-interest, but might be inaccurate because of size sample and potential bias. To increase statistical significance we consider comparing the performance of model with index funds.

