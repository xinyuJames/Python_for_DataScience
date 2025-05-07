def fun_map(func_1, func_2, L):
    '''
    Returns a new list R where each element in R is func_1(i) if the index 
    of i in L is divisible by 3, and func_2(i) otherwise.
    R = [func_1(L[0]), func_2(L[1]), func_2(L[2]), func_1(L[3]), ...]

    :param func_1: function to apply to elements at indices divisible by 3
    :param func_2: function to apply to elements at other indices
    :param L: list of elements
    :return R: list of results
    '''
    # Fill in
    R = []

    for i, value in enumerate(L):
        if i % 3 == 0:
            R.append(func_1(value))
        else:
            R.append(func_2(value))
    
    return R

def compose_map(func_1, func_2, L):
    """
    Returns a new list R where each element in R is fun2(fun1(i)) for the
    corresponding element i in L
    :param fun1: function
    :param fun2: function
    :param L: list
    :return R: list
    """
    # Fill in-
    R = []

    for value in L:
        R.append(func_2(func_1(value)))

    return R

def compose(func_1, func_2):
    # Fill in
    """
    Returns a new function ret_fun. ret_fun should take a single input i, and return
    fun1(fun2(i))
    :param fun1: function
    :param fun2: function
    :return ret_fun: function
    """
    def ret_fun(i):
        # Fill in
        return func_1(func_2(i))

    return ret_fun

def repeater(funlist, num_repeats):
    """
    Returns a new function ret_fun. This takes in a list of functions `funlist` and a list of integers `num_repeats`, 
    and returns a new function, `ret_fun`. The new function takes an input `x` and calls the 
    first function in `funlist` repeated a number of times equal to the first number 
    in the list `num_repeats`, and then calls the second function in `funlist` repeated 
    a number of times equal to the second number in the list `num_repeats`, continuing this
    pattern until the end of `funlist` is reached.
    :param fun: list of functions
    :param num_repeats: list of int
    :return ret_fun: function
    """
    def ret_fun(x):
        # Fill in
        value = x
        for func, repeats in zip(funlist, num_repeats):
            for i in range(repeats):
                value = func(value)
        return value

    return ret_fun

if __name__ == '__main__':

    def test1(x):
        return x * 3

    def test2(x):
        return x - 1

    data = [2,4,6,8,10,10,-3,-6,-7]

    # Testing the fun_map function
    print(fun_map(test1, test2, data)) # Calling the fun_map function with function test1 or test2 depending on index in list data where the list data is the argument

    # Testing the compose_map function
    print(compose_map(test1, test2, data)) # Calling the compose_map function with functions test1, test2 and the list data as the argument

    print(compose_map(test2, test1, data)) # Calling the compose_map function with functions test2, test1 and the list data as the argument (order of function input changed)

    # Using the compose function with functions test1 and test2 as arguments and returning its value to f1
    f1 = compose(test1, test2)

    # Running f1 with i=4
    print(f1(4))

    # Applying f1 on to each value in the list data
    print(list(map(f1, data)))

    # Using the compose function with functions test2 and test1 as arguments and returning its value to f2
    f2 = compose(test2, test1)

    # Running f2 with i=4
    print(f2(4))

    # Applying f2 on to each value in the list data
    print(list(map(f2, data)))

    # Testing the repeater function that with the function test1 with different num_repeats argument.
    z = repeater([test1, test2], [0 ,0])
    once = repeater([test1, test2], [1, 1])
    twice = repeater([test1, test2], [2, 2])
    thrice = repeater([test1, test2], [3, 3])

    print("repeat the two functions 0 times: {}".format(z(5)))
    print("repeat the two functions 1 time: {}".format(once(5)))
    print("repeat the two functions 2 times: {}".format(twice(5)))
    print("repeat the two functions 3 times: {}".format(thrice(5)))
