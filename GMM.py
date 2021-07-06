import numpy as numpy
import pandas as pd
import json

from sklearn.mixture import GaussianMixture
# turn dictionary into panda dataframe, import and use as array for GMM
inputArray = np.array([1, 2])
gm = GaussianMixture(n_components=3, random_state=0).fit_predict(inputArray)

