# Linear regression
source - https://bigdata-madesimple.com/how-to-run-linear-regression-in-python-scikit-learn/

Scikit-learn is a powerful Python module for machine learning. It contains function for regression, classification,
clustering, model selection and dimensionality reduction. Today, I will explore the sklearn.linear_model module which
contains “methods intended for regression in which the target value is expected to be a linear combination of the
input variables”.

Scikit Learn
- import linear regression from sci-kit learn module.
- drop the price column as I want only the parameters as my X values
- store linear regression object in a variable
- If you want to look inside the linear regression object, you can do so by typing LinearRegression.
  and the press <tab> key. This will give a list of functions available inside linear regression object.
- Important functions to keep in mind while fitting a linear regression model are:

- lm.fit() -> fits a linear model

- lm.predict() -> Predict Y using the linear model with estimated coefficients
- lm.score() -> Returns the coefficient of determination (R^2). A measure of how well observed outcomes are
   replicated by the model, as the proportion of total variation of outcomes explained by the model.
- explore the functions inside lm object by pressing lm.<tab>
- .coef_ gives the coefficients and .intercept_ gives the estimated intercepts.

Fitting a Linear Model
- In [20]: lm.fit(X, bos.PRICE)
- Out[20]: LinearRegression(copy_X=True, fit_intercept=True, normalize=False)
- construct a data frame that contains features and estimated coefficients.
- calculate the predicted prices (Y^i) using lm.predict

Training and validation data sets
In practice you wont implement linear regression on the entire data set, you will have to split the data
sets into training and test data sets. So that you train your model on training data and see how well it 
performed on test data.

divide your data sets randomly. Scikit learn provides a function called train_test_split to do this.

Input:
print “Fit a model X_train, and calculate MSE with Y_train:”, np.mean((Y_train – lm.predict(X_train)) ** 2)

print “Fit a model X_train, and calculate MSE with X_test, Y_test:”, np.mean((Y_test – lm.predict(X_test)) ** 2)

Output:
Fit a model X_train, and calculate MSE with Y_train: 19.5467584735 Fit a model X_train, and calculate MSE with X_test,
Y_test: 28.5413672756

Residual Plots
Residual plots are a good way to visualize the errors in your data. If you have done a good job then your data should
be randomly scattered around line zero. If you see structure in your data, that means your model is not capturing some
thing. Maye be there is a interaction between 2 variables that you are not considering, or may be you are measuring
time dependent data. If you get some structure in your data, you should go back to your model and check whether you
are doing a good job with your parameters.



