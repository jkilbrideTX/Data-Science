##   Use the fastfood.csv file to complete the following assignment. Create a file,
##    fastfood.py, that loads the .csv file and runs a regression predicting calories from
##    total_fat, sat_fat, cholesterol, and sodium, in that order. Add a constant using
##    sm.add_constant(data).

##    Then, print the following to two decimals
##    print(model.mse_total.round(2))
##    print(model.rsquared.round(2))
##    print(model.params.round(2))
##    print(model.pvalues.round(2))

import pandas as pd

import statsmodels.api as sm

fastfood_df = pd.read_csv("fastfood.csv")
fastfood_df

##  Make a dataframe of the items of interest
x = sm.add_constant(fastfood_df[['total_fat', 'sat_fat', 'cholesterol', 'sodium']])
#x = sm.add_constant(x, prepend=True)
y = fastfood_df[['calories']]



## Describe the model dependent, independent
mod = sm.OLS(y, x)

## Fit the model
res = mod.fit()

##  Summarize the model
print(res.mse_total.round(2))
print(res.rsquared.round(2))
print(res.params.round(2))
print(res.pvalues.round(2))


