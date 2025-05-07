import scipy.stats as stats
import numpy as np


def get_data(filename):
    return np.loadtxt(filename)


def get_coordinates(data, each_dist):
    # Part B
    """
    calculates the QQ plot given an array of data and a name of a distribution
    outputs a tuple of 2 numpy arrays from the output of the QQ plot
    :param data: np.ndarray
    :param each_dist: str
    :return: (np.ndarray, np.ndarray)
    """
    # Your code starts here...
    X, Y = stats.probplot(data, dist=each_dist)[0]
    return X, Y


def calculate_distance(x, y):
    # Part B
    """
    calculates the projected distance between x and y
    returns the distance as a float
    :param x: float
    :param y: float
    :return: float
    """
    # Your code starts here...
    return ((x - (x + y)/2)**2 + (y - (x + y)/2)**2)**0.5


def find_dist(data):
    # Part B
    """
    from a dictionary of distribution names and their respective errors, finds the distribution having the minimum value
    outputs the minimum value and the name of the distribution
    :param data: dict: {str: float}
    :return: (str, float)
    """
    # Your code starts here...
    dist = min(data, key=data.get)
    return (dist, float(data[dist]))


def main(data_file):
    """
    Input a csv file and return distribution type, the error corresponding to the distribution type (e.g. return ('norm', 0.32))
    :param: *.csv file name (str)
    :return: (str, float)
    """
    data = get_data(data_file)
    dists = ("norm", "expon", "uniform", "wald")
    sum_err = [0] * 4
    for ind, each_dist in enumerate(dists):
        X, Y = get_coordinates(data, each_dist)
        for x, y in zip(X, Y):
            sum_err[ind] += calculate_distance(x, y)
    return find_dist(dict(zip(dists, sum_err)))


if __name__ == "__main__":
    for each_dataset in [
        # "C:/Users/liuxi/Desktop/2025 SPR/ECE_20875/Python_for_DataScience/homework-3-s25-xinyuJames/sample_norm.csv",
        # "C:/Users/liuxi/Desktop/2025 SPR/ECE_20875/Python_for_DataScience/homework-3-s25-xinyuJames/sample_expon.csv",
        # "C:/Users/liuxi/Desktop/2025 SPR/ECE_20875/Python_for_DataScience/homework-3-s25-xinyuJames/sample_uniform.csv",
        # "C:/Users/liuxi/Desktop/2025 SPR/ECE_20875/Python_for_DataScience/homework-3-s25-xinyuJames/sample_wald.csv",
        # "C:/Users/liuxi/Desktop/2025 SPR/ECE_20875/Python_for_DataScience/homework-3-s25-xinyuJames/distA.csv",
        # "C:/Users/liuxi/Desktop/2025 SPR/ECE_20875/Python_for_DataScience/homework-3-s25-xinyuJames/distB.csv",
        # "C:/Users/liuxi/Desktop/2025 SPR/ECE_20875/Python_for_DataScience/homework-3-s25-xinyuJames/distC.csv",
        "sample_norm.csv",
        "sample_expon.csv",
        "sample_uniform.csv",
        "sample_wald.csv",
        "distA.csv",
        "distB.csv",
        "distC.csv",
    ]:
        print(main(each_dataset))
