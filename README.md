<h1><b>Introduction/Background</b></h1>

The stock market is an area where people can go to invest their money for small amounts of a business in the form of shares. Many have attempted to predict the movement of the market, however many machine learning studies have failed to accurately capture the full nature of the market<sup>1</sup>. This can be a result of high volatility, commonly seen today in shares such as TSLA or GME, but also due to other algorithmic factors such as poor training data size as well as imperfect feature selection<sup>2</sup>. 

We aim to investigate the Russel 1000 index over a period from ~2000 (depending on the stock)-2019 to investigate performance in paper trading by traditional machine learning algorithms. This will then be compared to personal performance, among the group, in paper trading utilizing what we known individually about the market in an attempt to maximize profits. This will give a simple approach to the success of the algorithm while utilizing a vast amount of data to attempt to reach the most logical conclusions on what stocks to buy or sell based on their features. We will provide other methods of testing such as the analysis of passive index fund growth over our chosen testing period. This will give insight into the model's viability to outpreform safer and less volatile methods of stock trading.

<h2><b>Problem definition:</b></h2>

We aim to investigate the success in paper trading over the period of 2019-2020 in comparison to what would be expected by an everyday person(with the inclusion of some bias given we have an idea of the results). This is in effort to determine the best features that dictate whether to buy or sell in order to maximize profit, and whether it is possible to utilize this algorithm to match other forms of investing that come with less risk. 

<h1><b>Methods</b></h1>

To make the predictor, we will be using stock data sourced from <a href ='https://www.kaggle.com/jacksoncrow/stock-market-dataset'>Dataset</a>. We will extract features from daily stock data such as opening value, daily highs and daily lows from ~2000 to 2019 and create an algorithm that trains on the data. The algorithm will then predict whether the stock will rise or fall and pick the stocks that it believes will return the best value over time. This will vary from method to method on exactly what the algorithm is performing.

Stock predictors have commonly used models made with logistic regression, neural networks, k-nearest neighbors and support-vector machines<sup>3</sup>. With logistic regression, we will model the stock data from a training set to an equation that could be used to predict whether the stock will rise or fall. Then we will compare this predictor to a set of testing data and compare with more successful models to adjust the equation to minimize loss.
We will also try an SVM for the predictive model. It will be used in a similar capacity to separate the stocks into more desirable and less desirable groups to decide which stocks are best to choose. 
With a Recurrent Neural Network, we could build a net with data from a fraction of the total time, for example 2012-2016, see how it predicts the next time period, 2017, and update the neurons to more accurately predict the outcome.


<h2><b>Data Cleaning</b></h2>
For the data cleaning, most of the effort involved came from finding the proper tools to quickly and efficiently save the data in an accessible format. After some research, we decided on storing the data in a python dictionary that we would store as a massive json file. We used libraries such as pandas, json, and csv to do so, settling on a format of a dictionary containing dictionaries for each stock under consideration that then contained the relevant data (Date, open price, close price, etc.). This was then reduced to the stocks that are a part of the Russel 1000 index for the purpose of space and time efficiency. <br><br>

Additional Cleaning performed throughout included the fitting of the testing data to be until 2019, as well as making sure that all elements were the same length by populating the begining of each array with the first price that it contained. This is in order to minimize error in the functions while ensuring that all specifications are met for the function criteria.

<h3>PCA</h3>
To cut down on features, we ran the dataset of the stocks within the Russel 1000 index through PCA to determine redundancy within the data. It was found that on average for each stock, the opening price accounted for a vast majority of the variance and the dataset was reduced to the dates and opening prices accordingly.

<h2><b>Method 1: GMM</b></h2>

Our first method is Gaussian Mixture Modelling, in an attempt to cluster stocks by those that are good to buy and those that are good to sell. This is a less robust method, as it will only group these stocks which will result in holding the stock throughout the entire period. We first had to get the data into a usable format for the sklearn GMM method, and then created 3 groups by which to classify these stocks into. Those three groups would give us those that would be best to sell, buy, or hold. Although for testing purposed we will be holding all stocks throughout the period. We will select randomly from the group that we expect to be buy after visualization, and deterrmine the amount of money that will be made from these stocks. This will be repeated and averaged to get a more accurate result of the classifier. 



<h1><b>Results and Discussion</b></h1>

We used the testing method described in our proposal, each person starts with $10000 to pick a set of stocks starting in January 2019 and checking the value in January 2020. In general we chose from a set of stocks from the Russel 1000 index, which contains a variety of well known small-cap stocks. Since the GMM model was trained and tested from parts of this data, we also included the value of the Index for the same period. 

![](/images/money.jpg)


<b>References</b>
<ol>
<li>https://www.google.com/url?q=https://www.hindawi.com/journals/mpe/2019/7816154/&sa=D&source=editors&ust=1623514864119000&usg=AOvVaw03PLyzhGS252HqnVZ1q3E</li>
<li>https://www.google.com/url?q=https://www.cis.upenn.edu/~mkearns/papers/KearnsNevmyvakaHFTRiskBooks.pdf&sa=D&source=editors&ust=1623515033628000&usg=AOvVaw3v4hX0a3VFQNYGUOP8y_Fl</li>
<li>https://www.google.com/url?q=https://www.sciencedirect.com/science/article/pii/S0957417415003334?casa_token%3DQMOeSwe1h_UAAAAA:havZZHXTnXKxqcW3lm97GbPdDN5AcgmDEw6BlPWN-9MKsh7mNEvuXgWFxwe0uhqQh83OfMDjy9w&sa=D&source=editors&ust=1623614701231000&usg=AOvVaw0h95VuQL3xZT5EE_Cm9LQc</li>
<li>Polygon.io - Stock Market Data APIs</li>
  <li>https://core.ac.uk/download/pdf/39667613.pdf</li>
  <li>https://www.ifk-cfs.de/fileadmin/downloads/publications/wp/09_10.pd</li>
  </ol>

