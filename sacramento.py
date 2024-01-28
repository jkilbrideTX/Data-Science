##   Use the sacramento.csv file to complete the following assignment. 
##   Create a file, sacramento.py, that loads the .csv file and runs a LOGISTIC REGRESSION. The
##    regression should predict whether or not a house has 1 or more than one
##    bathroom based on beds, sqft, and price, in that order.

##   You will need to create a new variable from baths, and it should make it such that
##    those observations of 1 bath correspond to a value of 0, and those with more
##    than 1 bath correspond to a 1.

##   Make sure to add a constant using sm.add_constant(X)

##   Your file should print the results in this way:
##    print(mod.params.round(2))
##    print(mod.pvalues.round(2))
##    print('The smallest p-value is for sqft')

import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf

sac_df = pd.read_csv("sacramento.csv")
#sac_df
#sac_df.keys()

##  Make a dataframe of the items of interest
## Independent variables (exog)
x = sm.add_constant(sac_df[['beds', 'sqft', 'price']])
#x

## recode baths for binary identification
def baths_binary(baths):
  if baths >1:
    return 1
  else:
    return 0

sac_df['bath_dummy'] = sac_df['baths'].apply(baths_binary) 

## dependent variable (endog)
y = sac_df[['bath_dummy']]
#y

## Describe and fit the model (endog,exog)
mod = sm.Logit(y,x).fit()

print(mod.params.round(2))
print(mod.pvalues.round(2))
print('The smallest p-value is for sqft')
