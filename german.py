##   Use the german_credit_data.csv file to complete the following assignment.
##   Create a file, german.py, that loads the .csv file and runs a regression predicting
##     credit amount from age and duration, in that order. Add a constant using
##     sm.add_constant(data).

##   You will need to rename the column 'Credit amount' to 'Credit_amount'.

##   Then, print the parameters and R-squared to 2 decimals using

import pandas as pd

import statsmodels.api as sm

german_df = pd.read_csv("german_credit_data.csv")
#german_df

##  Rename the column 'Credit amount' to 'Credit_amount'
german_df_rename = german_df.rename(columns={'Credit amount': 'Credit_amount'})
#german_df_rename

##  Make a dataframe of the items of interest
x = sm.add_constant(german_df_rename[['Age', 'Duration']])
#x

y = german_df_rename[['Credit_amount']]
#y

## Describe the model dependent, independent
model = sm.OLS(y, x)

## Fit the model
res = model.fit()

##  Summarize the model
print(res.params.round(2))
print(res.rsquared.round(2))

