def stencil(data, f, width):
    """
    1) perform a stencil using the filter function f with 'width', on list data.
    2) return the resulting list output.
    3) note that if len(data) is k, len(output) would be k - width + 1.
    4) f will accept input a list of size 'width' and return a single number.

    :param data: list
    :param f: function
    :param width: int
    :return output: list
    """
    # Fill in
    result = []

    for value in range(len(data) - width + 1):
        result.append(f(data[value:value+width]))
    
    return result


def create_box(box):
    """
    1) This function takes in a list, box.
    The box_filter function defined below accepts a list L of length len(box) and returns a simple
    convolution of it with the list, box.

    2) The meaning of this box filter is as follows:
    for each element of input list L, multiply L[i] by box[len(box) - 1  - i],
    sum the results of all of these multiplications and return the sum.

    3) For a box of length 3, box_filter(L) should return:
      (box[2] * L[0] + box[1] * L[1] + box[0] * L[2]),
      similarly, for a box of length 4, box_filter should return:
      (box[3] * L[0] + box[2] * L[1] + box[1] * L[2] + box[0] * L[3])

    The function create_box returns the box_filter function, as well as the length
    of the input list box

    :param box: list
    :return box_filter: function, len(box): int
    """

    # Fill in
    def box_filter(L):
        # Fill in
        if len(box) != len(L):
            print("Calling box filter with the wrong length list. Expected length of list should be {}.".format(len(box)))
            return 0
        
        sum = 0
        for i in range(len(box)):
            sum += box[len(box) - 1 - i] * L[i]
        
        return sum

    return box_filter, len(box)


if __name__ == '__main__':
    # The block of code under the `if __name__ == '__main__':` statement is only executed when the script is run as the main program.
    # This block is not executed if the script is imported as a module.
    
    def mov_avg(L):
        # The `mov_avg` function takes in a list `L` and returns the moving average of its elements.
        return float(sum(L)) / 3
    
    # Define a function `sum_sq` that takes in a list `L` and returns the sum of the squares of the elements in `L`.
    def sum_sq(L):
        return sum([i ** 2 for i in L])
    
    data = [2,4,6,8,10,10,-3,-6,-7]
    
    print(stencil(data, mov_avg, 2))
    print(stencil(data, sum_sq, 5))
    
    # note that this creates a moving average!
    box_f1, width1 = create_box([1.0 / 4, 1.0 / 4, 1.0 / 4, 1.0/4])
    print(stencil(data, box_f1, width1))
    
    box_f2, width2 = create_box([-0.2, -0.3, 0.3, 0.2])
    print(stencil(data, box_f2, width2))
