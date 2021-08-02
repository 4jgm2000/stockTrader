<h1><b>Introduction/Background</b></h1>

The stock market is an area where people can go to invest their money for small amounts of a business in the form of shares. Many have attempted to predict the movement of the market, however many machine learning studies have failed to accurately capture the full nature of the market<sup>1</sup>. This can be a result of high volatility, commonly seen today in shares such as TSLA or GME, but also due to other algorithmic factors such as poor training data size as well as imperfect feature selection<sup>2</sup>. 

We aim to investigate the Russel 1000 index over a period from ~2000 (depending on the stock)-2019 to investigate performance in paper trading by traditional machine learning algorithms. This will then be compared to personal performance, among the group, in paper trading style utilizing what we know individually about the market in an attempt to maximize profits. This will give a simple approach to the success of the algorithm while utilizing a vast amount of data to attempt to reach the most logical conclusions on what stocks to buy or sell based on their features. We will provide other methods of testing such as the analysis of passive index fund growth over our chosen testing period. This will give insight into the model's viability to outperform safer and less volatile methods of stock trading. We do not expect the model to revolutionize the way we attempt to model the market, but give insight into the viability of utilizing AI rather than safer investment opportunities.

<h2><b>Problem definition:</b></h2>

We aim to investigate the success in paper trading over the period of 2019-2020 in comparison to what would be expected by an everyday person(with the inclusion of some bias given we have an idea of the results). This is in effort to determine the best features that dictate whether to buy or sell in order to maximize profit, and whether it is possible to utilize this algorithm to match other forms of investing that come with less risk. 

<h2><b>Data Cleaning</b></h2>
For the data cleaning, most of the effort involved came from finding the proper tools to quickly and efficiently save the data in an accessible format. After some research, we decided on storing the data in a python dictionary that we would store as a massive json file. We used libraries such as pandas, json, and csv to do so, settling on a format of a dictionary containing dictionaries for each stock under consideration that then contained the relevant data ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']. This was then reduced to the stocks that are a part of the Russel 1000 index for the purpose of space and time efficiency. <br><br>

Additional Cleaning performed throughout included the fitting of the testing data to be until 2019, as well as making sure that all elements were the same length by populating the begining of each array with the first price that it contained. This is in order to minimize error in the functions while ensuring that all specifications are met for the function criteria.

<h3>PCA</h3>
To cut down on features, we ran the dataset of the stocks within the Russel 1000 index through PCA to determine redundancy within the data. It was found that on average for each stock, the opening price accounted for a vast majority of the variance and the dataset was reduced to the dates and opening prices accordingly.

<h1><b>Methods</b></h1>

To make the predictor, we will be using stock data sourced from this <a href ='https://www.kaggle.com/jacksoncrow/stock-market-dataset'>Dataset</a> found on kaggle.com. We will extract features from daily stock data such as opening value, daily highs and daily lows from ~2000 to 2019 and create an algorithm that trains on the data. The algorithm will then predict whether the stock will rise or fall and pick the stocks that it believes will return the best value over time. This will vary from method to method on exactly what the algorithm is performing.

Stock predictors have commonly used models made with logistic regression, neural networks, k-nearest neighbors and support-vector machines<sup>3</sup>. With logistic regression, we will model the stock data from a training set to an equation that could be used to predict whether the stock will rise or fall. Then we will compare this predictor to a set of testing data and compare with more successful models to adjust the equation to minimize loss.
We will also try an SVM for the predictive model. It will be used in a similar capacity to separate the stocks into more desirable and less desirable groups to decide which stocks are best to choose. 
With a Recurrent Neural Network, we could build a net with data from a fraction of the total time, for example 2012-2016, see how it predicts the next time period, 2017, and update the neurons to more accurately predict the outcome.

<h2><b>Method 1: GMM</b></h2>

Our first method is Gaussian Mixture Modelling, in an attempt to cluster stocks by those that are good to buy and those that are good to sell. This is a less robust method, as it will only group these stocks which will result in holding the stock throughout the entire period. We first had to get the data into a usable format for the sklearn GMM method, and then created 3 groups by which to classify these stocks into. Those three groups would give us those that would be best to sell, buy, or hold. Although for testing purposes we will be holding all stocks throughout the period. We will select randomly from the group that we expect to be the "buy" classification after visualization, and determine the amount of money that will be made from these stocks. This will be repeated and averaged to get a more accurate result of the classifier. 

<h2><b>Method 2: Polynomial Regression</b></h2>

We decided to use regression for our second method. Since we had reduced our feature set to just the opening values, it seemed like polynomial regression would be most appropriate. Because of the data issues we experienced for GMM, particularly the variable date ranges, we decided the best use of Regression would be to model each stock individually from its first value up to the start of 2019. The resulting model would then be used to estimate the value of the stock after 1 year. The stocks with the best estimated gain would be chosen as “buy” stocks.

<h2><b>Method 3: Neural Network</b></h2>

Our final method is that the creation of a Neural Network to select which stocks would be profitable and should be bought. The first issue we ran into is that most of the Neural Networks that we researched involved supervised learning- in other words, the problem would be reduced to a simpler classification problem. Consequently, we researched Self-Organizing Maps, which are essentially Neural Networks that label data independent of human intervention and parameters. However, we were unable to find an adequate implementation that would function with our dataset and keras, and implementing our own was beyond our abilities. Thus, we stuck to having the Neural Network classify stocks based on whether they were profitable, which we based on those stocks being in the top 10% of stocks.

<h1><b>Results and Discussion</b></h1>

We used the testing method described in our proposal, each person starts with $10000 to pick a set of stocks starting in January 2019 and checking the value in January 2020. In general we chose from a set of stocks from the Russel 1000 index, which contains a variety of well known small-cap stocks. Since the GMM model was trained and tested from parts of this data, we also included the value of the Index for the same period. 

![](/images/personalImg.png)

Because 2019 was a great year for the economy, everyone gained from their choice of stocks, and even if the stock picker chose randomly, it would have likely gained value regardless. However, the results from the first test were very promising. 

<h2>GMM</h2>
The GMM average final total was $15,258 beating all but one group member. This was roughly a 18% increase over the index fund growth during the period from 2019-2020. Key stocks chosen by the algorithm include GOOG, NVDA, C, as well as others. Further data cleaning should be done to ensure that these results are as robust as possible, as during implementation certain stock datasets were deemed to be unviable due to skewing the groupings. If these were to all be cleaned up rather than looked over it could provide better results that could potentially yield even more money. This method, although simplistic, shows that it is possible to model the market and achieve growth that would rival that of a passive index fund. Future methods should work to increase the potential for stock growth as well as adding new capabilities such as buying and selling throughout the period to gather more money. 

<h2>Polynomial Regression</h2>
The regression performed surprisingly well, picking 10 stocks that valued at $17,543 after a year which is 35% better than the index fund. This was mainly due to 2 stocks, IOVA and CVNA, that tripled in value that year. Most of the others gained 10% - 50%, which was typical for 2019. Despite the positive results, the regression over estimated the value gained by all of these. It estimated that the 10th best would triple in value while the best would increase 81 fold. Metrics for the regression were two RSMEs. The first measured the actual and predicted numerical stocks prices, giving a value of 67.066. The other which measured the relative gain from 2019 to 2020 meaning that if the stock was estimated to gain 50% over the year, y_predicted would be 1.5 and if it actually gained 20%, y_actual would be 1.2. This value was 2.814. This was modelled using 2nd degree polynomials only and the overestimations were exacerbated when higher degrees were used. This shows clearly why Regression is preferred for use or interpolation often cautioned against use for extrapolation. It’s difficult to say if this method should be trusted even with the results of this one data set.

<h2>Neural Network</h2>

The Neural Network performed well, firmly beating out the index, GMM, and humans with a selection of 57 stocks that were valued at $17,154, which is approximately 33% better than the index fund. Those results were strong & promising, but could have most likely been improved on in several ways. Firstly, as mentioned in the above Method discussion, Self-Organizing maps could have been used to remove human interpretation of the data and change the problem from supervised learning to unsupervised learning. Secondly, a more rigorous classification method of which stocks were "pickable" and which were not, as well as which stocks were "superstars" (i.e. more money should have been invested in them) could have been implemented. Thirdly, the architecture (and specifically the input dimensions of the Neural Network) could have been improved & changed to allow for inputting of time series data of varying length; manipulating the Neural Network to function with time series data was another significant issue of the implementation. Lastly, the hyperparameters of the Neural Network including but not limited to the number of layers and size of each layer could have been implemented.

<h2>Conclusion</h2>

![](images/finalAlgo.png)

Overall, each method resulted in stock picks that outperformed most of the personal picks and the index fund that they were picked from. As a peak into predicting the stock market, these are promising results with some qualifications. The GMM picked many well-performing stocks, 9 out of 10 gained more than 30% value over the year. It provided consistency in its picks. The polynomial regression, on the other hand, picked some of the best performing stocks, 2 that tripled in value. However, others in the best 10 list were underperforming. Four gained less than 30% over the year. The neural network performed nearly as well as the regression even with a larger list of best stocks.
 
Being a great year for the market, 2019, it was expected that most stocks would do well, and our methods all predicted some of the best performing stocks, but it can’t be precisely said what makes them the best and how much they will increase. Perhaps testing years with a stagnant or bear market could prove the models less effective or counterproductive. Our models weren’t exceptionally complicated and made very general assessments, so in future iterations, more  rigorous classification and precise prediction would be desired.
 


<h1><b>References</b></h1>
<ol>
<li>https://www.google.com/url?q=https://www.hindawi.com/journals/mpe/2019/7816154/&sa=D&source=editors&ust=1623514864119000&usg=AOvVaw03PLyzhGS252HqnVZ1q3E</li>
<li>https://www.google.com/url?q=https://www.cis.upenn.edu/~mkearns/papers/KearnsNevmyvakaHFTRiskBooks.pdf&sa=D&source=editors&ust=1623515033628000&usg=AOvVaw3v4hX0a3VFQNYGUOP8y_Fl</li>
<li>https://www.google.com/url?q=https://www.sciencedirect.com/science/article/pii/S0957417415003334?casa_token%3DQMOeSwe1h_UAAAAA:havZZHXTnXKxqcW3lm97GbPdDN5AcgmDEw6BlPWN-9MKsh7mNEvuXgWFxwe0uhqQh83OfMDjy9w&sa=D&source=editors&ust=1623614701231000&usg=AOvVaw0h95VuQL3xZT5EE_Cm9LQc</li>
<li>Polygon.io - Stock Market Data APIs</li>
  <li>https://core.ac.uk/download/pdf/39667613.pdf</li>
  <li>https://www.ifk-cfs.de/fileadmin/downloads/publications/wp/09_10.pd</li>
  <li>https://www.kaggle.com/jacksoncrow/stock-market-dataset</li>
  </ol>

