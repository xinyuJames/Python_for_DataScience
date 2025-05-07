import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Part 1
# Function that normalizes features in training set to zero mean and unit variance.
def normalize_train(X_train):
    # Input
    # --------------------
    # X_train : Training data, a numpy array with shape (n_samples, n_features),
    #         where n_samples is the number of samples in the training data, and 
    #         n_features is the number of features in the data
    #
    # Output
    # --------------------
    # X : The normalized version of the feature matrix, a numpy array
    # trn_mean : The mean of each column in the training set, float
    # trn_std : The std dev of each column in the training set, float
    
    '''
    Fill in your code here
    '''
    trn_mean = np.mean(X_train, axis=0)
    trn_std = np.std(X_train, axis=0)
    X = np.array((X_train-trn_mean)/trn_std)
    
    

    return X, trn_mean, trn_std

# Part 2
# Function that normalizes testing set according to mean and std of training set

def normalize_test(X_test, trn_mean, trn_std):
    
    # Input
    # --------------------
    # X_test : Testing data, a numpy array with shape (n_samples, n_features)
    # trn_mean : Mean of each column in training set, float
    # trn_std : Standard deviation of each column in training set, float
    #
    # Output
    # --------------------
    # X : The normalized version of the feature matrix, X_test

    '''
    Fill in your code here
    '''
    X = np.array((X_test - trn_mean)/trn_std)
    
    

    return X


# Part 3
# Function to return a numpy array generated with `np.logspace` with a length
# of 51 starting from 1E^-1 and ending at 1E^3
def get_lambda_range():
    
    # Input
    # --------------------
    # Nothing
    #
    # Output
    # --------------------
    # lmbda : numpy array of logarithmically spaced values
    
    '''
    Fill in your code here
    '''

    lmbda = np.logspace(-1, 3, num=51)


    return lmbda



# Part 4
# Function that trains a ridge regression model on the input dataset with lambda=1
def train_model(X_train, y_train, l):
    # Input
    # --------------------
    # X_train : Feature matrix
    # y_train : Target variable vector
    # l : Regularization parameter
    #
    # Output
    # --------------------
    # model : A numpy object containing the trained model

    '''
    Fill in your code here
    '''
    model = Ridge(alpha=l, fit_intercept=True)
    model.fit(X_train, y_train)

    return model

# Part 5
# Function that calculates the mean squared error of the model on the input dataset
def error(X, y, model):
    
    # Input
    # ------------------
    # X : Feature matrix
    # y : Target variable vector
    # model : Numpy model object
    #
    # Output
    # ------------------
    # mse : Mean squared error

    '''
    Fill in your code here
    '''
    y_p = model.predict(X)
    mse = np.mean((y-y_p)**2)

    return mse


def main():
    # Importing dataset
    # step 1 : read csv
    df = pd.read_csv("c:/Users/liuxi/Desktop/2025 SPR/ECE_20875/Python_for_DataScience/homework-7-s25-xinyuJames/AAPL.csv")
    # step 2 : identify the column(s) we want to remove
    remove_features = ["Date"]
    # step 3: create extra column for prediction by shifting
    # rows of `Close` columns by one to obtain next day's closing price
    df["Prediction"] = pd.Series(np.append(df["Close"][1:].to_numpy(), [0]))
    # step 4: drop the last row because it would have invalid value after the shift.
    df.drop(df.tail(1).index, inplace=True)
    # step 5: remove the columns identified in step 2
    df.drop(remove_features, axis=1, inplace=True)
    # step 6: create X by dropping the `Prediction` column
    X = np.array(df.drop(["Prediction"], axis=1))
    # step 7: Store `Prediction` column in y array
    y = np.array(df["Prediction"])
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, shuffle=False
    )


    # Problem 1:
    # Complete the function 'normalize_train' above
    #X_train, trn_mean, trn_std = normalize_train(X_train)
    # Problem 2:
    # Complete the function 'normalize_test' above
    #X_test = normalize_test(X_test, trn_mean, trn_std)

    # Normalizing training and testing data
    [X_train, trn_mean, trn_std] = normalize_train(X_train)
    X_test = normalize_test(X_test, trn_mean, trn_std)


    # Problem 3: 
    # Complete the function 'get_lambda_range'.
    # Problem 4:
    # Complete the function 'train_model' above.
    # Problem 5:
    # Complete the function 'error' above.

    # Define the range of lambda to test
    lmbda = get_lambda_range()
    # uncomment the below line to help verify your answer is correct.
    # lmbda = [1, 500, 1000, 2500]
    # make sure to re-comment above line so that the lambda checked during grading is from 'get_lambda_range'
    MODEL = []
    MSE = []
    for l in lmbda:
        # Train the regression model using a regularization parameter of l
        model = train_model(X_train, y_train, l)

        # Evaluate the MSE on the test set
        mse = error(X_test, y_test, model)

        # Store the model and mse in lists for further processing
        MODEL.append(model)
        MSE.append(mse)

    # Part 6
    # Plot the MSE as a function of lmbda
    # Note that the code to find MSE has already been completed in part 5.
    ''' 
    fill in your code below 
    '''
    plt.figure() # <<< fill in here 

    plt.semilogx(lmbda, MSE, marker='o')
    plt.xlabel("Lambda")
    plt.ylabel("Mean Squared Error")
    plt.title("MSE vs Lambda")

    plt.show()

    # Find best value of lmbda in terms of MSE
    # Record this value on the writeup
    ''' 
    fill in your code below 
    '''
    ind = np.argmin(MSE)   # <<< fill in here
    [lmda_best, MSE_best, model_best] = [lmbda[ind], MSE[ind], MODEL[ind]]

    print(
        "Best lambda tested is "
        + str(lmda_best)
        + ", which yields an MSE of "
        + str(MSE_best)
    )

    # Part 7
    # Using the best model found above, write out the model coefficients and intercept
    # Record this value on the writeup
    ''' 
    fill in your code below 
    '''
    print(
        "Best coefficients is "
        + str(model_best.coef_)
        + ", Best intercept is "
        + str(model_best.intercept_)
    )

    
    # Part 8
    # Load GOOG.csv 
    # This process will be similar to steps 1-7 where AAPL.csv is loaded
    # Note that you should NOT call 'train_test_split' in this part.
    ''' 
    fill in your code below 
    '''
    goog = pd.read_csv("c:/Users/liuxi/Desktop/2025 SPR/ECE_20875/Python_for_DataScience/homework-7-s25-xinyuJames/GOOG.csv")
    goog.drop(remove_features, axis=1, inplace=True)
    goog["Prediction"] = pd.Series(np.append(goog["Close"][1:].to_numpy(), [0]))
    goog.drop(goog.tail(1).index, inplace=True)
    



    X_goog = np.array(goog.drop(["Prediction"], axis=1))  # <<< fill in here (similar to step 6)
    y = np.array(goog["Prediction"])  # <<< fill in here (similar to step 7)

    # normalize X similar to X_test
    X_goog_norm = normalize_test(X_goog, trn_mean, trn_std)
    y_hat = model_best.predict(X_goog_norm)  # <<< fill in here (use your best model from Part 7)

    # plot y and y_hat
    plt.figure()
    '''
    fill in your code here
    '''
    plt.plot(y, label="Actual GOO")
    plt.plot(y_hat, label="Predicted GOOG")
    plt.xlabel("Time")
    plt.ylabel("Price")
    plt.title("Actual vs. Predicted")
    plt.legend()
    plt.show()
    return model_best


if __name__ == "__main__":
    model_best = main()
