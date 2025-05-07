import numpy as np
import matplotlib.pyplot as plt

# Function that returns fitted model parameters to the dataset at datapath for each choice in degrees.
# 

def main(datapath, degrees):
    
    # Input
    # --------------------
    # datapath : A string specifying a .txt file 
    # degrees : A list of positive integers.
    #    
    # Output
    # --------------------
    # paramFits : a list with the same length as degrees, where paramFits[i] is the list of
    #             coefficients when fitting a polynomial of d = degrees[i].
    
    paramFits = []

    file = open(datapath, 'r')
    data = file.readlines()
    x = []
    y = []
    for line in data:
        [i, j] = line.split()
        x.append(float(i))
        y.append(float(j))
        
    # iterate through each n in the list degrees, calling the feature_matrix and least_squares functions to solve
    # for the model parameters in each case. Append the result to paramFits each time.
    '''
    fill in your code here
    '''

    for n in degrees:
        fm = feature_matrix(x, n)
        ls = least_squares(fm, y)
        paramFits.append(ls)

    return paramFits


# Function that returns the feature matrix for fitting a polynomial of degree d based on the explanatory variable
# samples in x.
#

def feature_matrix(x, d):
    
    # Input
    # --------------------
    # x: A list of the independent variable samples
    # d: An integer
    #
    # Output
    # --------------------
    # X : A list of features for each sample, where X[i][j] corresponds to the jth coefficient
    #     for the ith sample. Viewed as a matrix, X should have dimension (samples, d+1).

    # There are several ways to write this function. The most efficient would be a nested list comprehension
    # which for each sample in x calculates x^d, x^(d-1), ..., x^0.
    # Please be aware of which matrix colum corresponds to which degree polynomial when completing the writeup.
    '''
    fill in your code here
    '''
    X = list(list(i**j for j in range(d, -1, -1)) for i in x)

    return X


# Function that returns the least squares solution based on the feature matrix X and corresponding target variable samples in y.
def least_squares(X, y):
    # Input
    # --------------------
    # X : A list of features for each sample
    # y : a list of target variable samples.
    #
    # Outut
    # --------------------
    # B : a list of the fitted model parameters based on the least squares solution.
    
    X = np.array(X)
    y = np.array(y)

    # Use the matrix algebra functions in numpy to solve the least squares equations. This can be done in just one line.
    '''
    fill in your code here
    '''
    B = list(np.linalg.inv(X.T @ X) @ X.T @ y)

    return B


if __name__ == "__main__":
    datapath = "c:/Users/liuxi/Desktop/2025 SPR/ECE_20875/Python_for_DataScience/homework-7-s25-xinyuJames/poly.txt"

    file = open(datapath, 'r')
    data = file.readlines()
    x = []
    y = []
    for line in data:
        [i, j] = line.split()
        x.append(float(i))
        y.append(float(j))

    ### Problem 1 ###
    # ODO: Complete 'main, 'feature_matrix', and 'least_squares' functions above

    ### Problem 2 ###
    # The paramater values for degrees 2 and 4 have been provided as test cases in the README.
    # The output should match up to at least 3 decimal places rounded 
    
    
    
    # Write out the resulting estimated functions for each d.
    degrees = [1, 2, 3, 4, 5, 6] # ODO: Update the degrees,d to include 1, 3, 5 and 6. i.e. [1,2,3,4,5,6] and
    paramFits = main(datapath, degrees)
    for idx in range(len(degrees)):
        print("y_hat(x_"+str(degrees[idx])+")")
        print(paramFits[idx])
        print("****************")

    ### Problem 3 ###
    # TODO: Visualize the dataset and these fitted models on a single graph
    # Use the 'scatter' and 'plot' functions in the `matplotlib.pyplot` module.

    # Draw a scatter plot
    plt.scatter(x, y, color='black', label='data')
    x.sort() # Ensures the scatter plot looks nice

    for i, n in enumerate(degrees):
        y_hat = np.polyval(paramFits[i], x)
        plt.plot(x, y_hat, label="Degree " + str(n))
        
        
        

    plt.xlabel('x', fontsize=16)
    plt.ylabel('y', fontsize=16)
    plt.legend(fontsize=10, loc='upper left')

    plt.show()

    ### Problem 4 ###
    # TODO: when x = 4; what is the predicted output
    # Use the degree that best matches the data as determined in Problem 3 above.
    
    '''
    fill in your code here
    '''
    best_index = degrees.index(4)
    best_params = paramFits[best_index]
    y_pred = np.polyval(best_params, 4)
    print("Predicted y using degree {} y predict: {:.3f}".format(4, y_pred))


