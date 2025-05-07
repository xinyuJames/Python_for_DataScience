from typing import List, Tuple

def histogram(input_dictionary: dict) -> list:
    # data is a dictionary that contains the following keys: 'data', 'n', 'min_val', 'max_val'
    # n is an integer
    # min_val and max_val are floats
    # data is a list

    # Write your code here
    data = input_dictionary['data']
    n = input_dictionary['n']
    min_val = input_dictionary['min_val']
    max_val = input_dictionary['max_val']

    if not isinstance(data, list) or not isinstance(n, int):
        # print("input type not correct")
        # print(isinstance(data, list))
        # print(isinstance(n, int))
        # print(isinstance(min_val, float))
        # print(isinstance(max_val, float))
        return []

    if min_val == max_val:
        print("Error: min_val and max_val are the same value")
        return []
    
    if min_val > max_val:
        min_val, max_val = max_val, min_val
    
    if n <= 0:
        # print("n < 0")
        return []
    
    hist = [0] * n

    w = (max_val - min_val) / n

    for x in data:
        if x < min_val or x > max_val:
            continue

        hist_index = int((x - min_val) / w)

        if hist_index >= n:
            continue
        elif hist_index < 0:
            continue

        hist[hist_index] += 1
    # return the variable storing the histogram
    # Output should be a list
    return hist

# Here, the function first checks if the lower and upper bounds are the same, 
# if they are it prints an error message and returns an empty list. 
# If lower bound is greater than upper bound, it swaps their values. 
# If number of bins is less than or equal to 0, it returns an empty list. 
# Then it initializes an empty list hist of length n and calculates the width of each bin. 
# Then it iterates through the data, 
# and for each value checks if it is within the range of the histogram and if it is, 
# it increments the bin it belongs to. Finally, it returns the histogram.




def combine_birthday_data(person_to_day: List[Tuple[str, int]], 
                          person_to_month: List[Tuple[str, int]], 
                          person_to_year: List[Tuple[str, int]]) -> dict:
    #person_to_day, person_to_month, person_to_year are list of tuples
    name_to_day = {name: day for name, day in person_to_day}
    name_to_year = {name: year for name, year in person_to_year}
    # Write your code here
    month_to_people_data_wlist = {}
    for name, month in person_to_month:
        day = name_to_day[name]
        year = name_to_year[name]
        age = 2025 - year
        person_data = (name, day, year, age)

        if month not in month_to_people_data_wlist:
            month_to_people_data_wlist[month] = []
        month_to_people_data_wlist[month].append(person_data)

    month_to_people_data = {}
    for month, people in month_to_people_data_wlist.items():
        if len(people) == 1:
            month_to_people_data[month] = people[0]
        else:
            month_to_people_data[month] = people
    
    return month_to_people_data

    # return the variable storing output
    # Output should be a dictionary


# We first define the current year as 2025, which will be used to calculate the age of each person later on.
# We create an empty dictionary month_to_people_data that will store the final data in the format specified in the problem statement.
# We iterate over the both values in the tuple of the person_to_month list (note that person_to_month is a list of tuples, which means each item in the list is a tuple) 
# using a for loop. For each iteration, we extract the corresponding day, year and age values from the person_to_day and person_to_year lists using the current name as the "key".
# We then use the current month as the key and a tuple of (name, day, year, age) as the value to update the month_to_people_data dictionary.
# Only change the value to a list data type, when there are multiple entries with the same key. This will help append for other tuples to the same month.
# Finally, we return the month_to_people_data dictionary as the output of the function.
