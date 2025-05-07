import numpy as np
import matplotlib.pyplot as plt


def norm_histogram(histogram):
    """
    takes a list of counts and converts to a list of probabilities, outputs the probability list.
    :param histogram: a numpy ndarray object
    :return: list
    """
    # please delete the "pass" below and your code starts here...

    total = np.sum(histogram)

    if total == 0:
        return [0] * len(histogram)
    
    return (histogram / total).tolist()



def compute_j(histogram, bin_width, num_samples):
    """
    takes list of counts, uses norm_histogram function to output the histogram of probabilities, 
    then calculates compute_j for one specific bin width (reference: histogram.pdf page19)
    :param histogram: list
    :param bin_width: float
    :param num_samples: int
    :return: float
    """
    # please delete the "pass" below and your code starts here...
    prob = norm_histogram(histogram)

    p_squared_sum = sum(p_element**2 for p_element in prob)
    j = (2/((num_samples - 1) * bin_width)) - ((num_samples + 1)/ ((num_samples - 1) * bin_width)) * p_squared_sum

    return j

def sweep_n(data, min_val, max_val, min_bins, max_bins):
    """
    find the optimal bin
    calculate compute_j for a full sweep [min_bins to max_bins]
    please make sure max_bins is included in your sweep
    
    The variable "data" is the raw data that still needs to be "processed"
    with matplotlib.pyplot.hist to output the histogram

    You must utilize the variables (data, min_val, max_val, min_bins, max_bins) 
    in your code for 'sweep_n' to determine the correct input to the function 'matplotlib.pyplot.hist',
    specifically the values to (x, bins, range).
    Other input variables of 'matplotlib.pyplot.hist' can be set as default value.
    
    :param data: list
    :param min_val: int
    :param max_val: int
    :param min_bins: int
    :param max_bins: int
    :return: list
    """
    # please delete the "pass" below and your code starts here...
    j_list = []

    for b_value in range(min_bins, max_bins + 1):
        b_heights = plt.hist(data, b_value, (min_val, max_val))[0]
        plt.clf()
        b_width = (max_val - min_val) / b_value
        j = compute_j(b_heights, b_width, len(data))
        j_list.append(j)

    return j_list


def find_min(l):
    """
    takes a list of numbers and returns the three smallest number in that list and their index.
    return a dict i.e. 
    {index_of_the_smallest_value: the_smallest_value, index_of_the_second_smallest_value: the_second_smallest_value, ...}
    
    For example:
        A list(l) is [14,27,15,49,23,41,147]
        Then you should return {0: 14, 2: 15, 4: 23}

    :param l: list
    :return: dict: {int: float}
    """
    # please delete the "pass" below and your code starts here...
    sorted_pairs = sorted(enumerate(l), key=lambda x: x[1])
    return {idx: val for idx, val in sorted_pairs[:3]}


if __name__ == "__main__":
    data = np.loadtxt("input.txt")  # reads data from input.txt
    lo = min(data)
    hi = max(data)
    bin_l = 1
    bin_h = 100
    js = sweep_n(data, lo, hi, bin_l, bin_h)
    """
    the values bin_l and bin_h represent the lower and higher bound of the range of bins.
    They will change when we test your code and you should be mindful of that.
    """
    print(find_min(js))
