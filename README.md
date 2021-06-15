<b>Introduction/Background</b>

The stock market is an area where people can go to invest their money for small amounts of a business in the form of shares. Many have attempted to predict the movement of the market, however many machine learning studies have failed to accurately capture the full nature of the market<sup>1</sup>. This can be a result of high volatility, commonly seen today in shares such as TSLA or GME, but also due to other algorithmic factors such as poor training data size as well as imperfect feature selection<sup>2</sup>. 

We aim to investigate either the NASDAQ 100 or S&P 500 over a period from 2012-2019 to investigate performance in paper trading by traditional machine learning algorithms. This will then be compared to personal performance in paper trading utilizing what is known individually to attempt to maximize profits. This will give a simple approach to the success of the algorithm while utilizing a vast amount of data to attempt to reach the most logical conclusions on what stocks to buy or sell based on their features.

<b>Problem definition:</b>

We aim to investigate the success in paper trading in comparison to what would be expected by an everyday person after training on an extended period of stock prices. This is in effort to determine the best features that dictate whether to buy or sell in order to maximize profit. 

<b>Methods</b>

To make the predictor, we will be using stock data sourced from Polygon.io. We will extract features from daily stock data such as opening value, daily highs and daily lows from 2012 to 2019 and create an algorithm that models the data. The algorithm will then predict whether the stock will rise or fall and pick the stocks that it believes will return the best value over time. 
Stock predictors have commonly used models made with logistic regression, neural networks, k-nearest neighbors and support-vector machines<sup>3</sup>. With logistic regression, we will model the stock data from a training set to an equation that could be used to predict whether the stock will rise or fall. Then we will compare this predictor to a set of testing data and compare with more successful models to adjust the equation to minimize loss.
We will also try an SVM for the predictive model. It will be used in a similar capacity to separate the stocks into more desirable and less desirable groups to decide which stocks are best to choose. 
With a Recurrent Neural Network, we could build a net with data from a fraction of the total time, for example 2012-2016, see how it predicts the next time period, 2017, and update the neurons to more accurately predict the outcome. 



<b>Potential results and Discussion</b>

To estimate results each of the team members will use 10000 demo dollars to trade (see graph below). The success scenario includes the model performing better than average among us by 500 dollars. Satisfactory scenario would be model performance within 200 dollars deviation from our average. Our comparison reference point has obvious self-interest, but might be inaccurate because of size sample and potential bias. In addition to that we will measure the performance of the model by number of winning vs losing trades and their respective average. 

![Image](<p>https://github.com/4jgm2000/stockTrader/blob/main/images/imageLikeEmbed.png</p>)

<p><img src="https://github.com/4jgm2000/stockTrader/blob/main/images/imageLikeEmbed.png" style:"height:300px; width:300px"></p>

<b>References</b>
<ol>
<li>https://www.google.com/url?q=https://www.hindawi.com/journals/mpe/2019/7816154/&sa=D&source=editors&ust=1623514864119000&usg=AOvVaw03PLyzhGS252HqnVZ1q3E</li>
<li>https://www.google.com/url?q=https://www.cis.upenn.edu/~mkearns/papers/KearnsNevmyvakaHFTRiskBooks.pdf&sa=D&source=editors&ust=1623515033628000&usg=AOvVaw3v4hX0a3VFQNYGUOP8y_Fl</li>
<li>https://www.google.com/url?q=https://www.sciencedirect.com/science/article/pii/S0957417415003334?casa_token%3DQMOeSwe1h_UAAAAA:havZZHXTnXKxqcW3lm97GbPdDN5AcgmDEw6BlPWN-9MKsh7mNEvuXgWFxwe0uhqQh83OfMDjy9w&sa=D&source=editors&ust=1623614701231000&usg=AOvVaw0h95VuQL3xZT5EE_Cm9LQc</li>
<li>Polygon.io - Stock Market Data APIs</li>
  <li>https://core.ac.uk/download/pdf/39667613.pdf</li>
  <li>https://www.ifk-cfs.de/fileadmin/downloads/publications/wp/09_10.pd</li>
  </ol>

