def problem0(num):
    """
        This is a sample problem and solution that won't be graded. Its purpose is just to familiarize
        yourself with functions and the format for this homework

        The objective of this sample problem is to determine if the num is divisible by 3, if it is, the function will
        return the string "divisible" otherwise it will return "not divisible"

        We will use the modulo operator "%"  (might come in handy in other homework problems - worth a google search!)
    """

    if num % 3: #Use modulo operator to get remainder. If it not 0 (which would be interpreted like a 'False' in the if statement, then we know it is not divisible by 3
        return "not divisible"
    else:
        return "divisible"




def problem1(year):
    """
    When given a year, determine if the year is even or odd, but if it is an election year (divisible by 4) return

    To be a leap year, the year number must be divisible by four - except for end-of-century years, which must be divisible by 400. This means that the year 2000 was a leap year, although 1900 was not.

    Odd year: Return a string "odd"
    Even year: Return "even" unless it is leap year, then return a string "leap"
    leap year: Return a string "leap"
    

    """
    if year % 100 == 0:
        if year % 400 == 0:
            return "leap"
        else:
            return "even"
    elif year % 4 == 0:
        return "leap"
    elif year % 2 == 0:
        return "even"
    else:
        return "odd"
    
      #when you complete your function get rid of the pass (This only allows the code to run when you have an incomplete function)


def problem2(given_number):
    """
    When given a return a list of all values that are trianglular numbers that are less than or equal to the given_number
    triangle number: https://en.wikipedia.org/wiki/Triangular_number

    Remember you are returning a list of numbers!
    

    """
    numList = []

    for i in range(1,given_number):
        num = 0
        for j in range(0,i + 1):
            num += j
        
        if num <= given_number:
            numList.append(int(num))
        else:
            break

    return numList

      #when you complete your function get rid of the pass (This only allows the code to run when you have an incomplete function)

#When you run this python file you should be able to check your work with these test cases

if __name__ == '__main__' :
    #Below are the Test Cases!
    print("\nProblem 0:")
    print("Student answer was:", problem0(1), "    Problem 0 answer correct?",problem0(1)=='not divisible', )
    print("Student answer was:", problem0(2), "    Problem 0 answer correct?",problem0(2)=='not divisible', )
    print("Student answer was:", problem0(3), "    Problem 0 answer correct?",problem0(3)=='divisible', )
    print("Student answer was:", problem0(4), "    Problem 0 answer correct?",problem0(4)=='not divisible', )

    print("\nProblem 1:")
    print("Problem 1 answer correct?",problem1(2025)=='odd', "    Student answer was:", problem1(2025))
    print("Problem 1 answer correct?",problem1(2024)=='leap', "    Student answer was:", problem1(2024))
    print("Problem 1 answer correct?",problem1(2023)=='odd', "    Student answer was:", problem1(2023))
    print("Problem 1 answer correct?",problem1(2022)=='even', "    Student answer was:", problem1(2022))
    print("Problem 1 answer correct?",problem1(2020)=='leap', "    Student answer was:", problem1(2020))
    print("Problem 1 answer correct?",problem1(2000)=='leap', "    Student answer was:", problem1(2000))
    print("Problem 1 answer correct?",problem1(1900)=='even', "    Student answer was:", problem1(1900))

    print("\nProblem 2:")
    print("Problem 2 answer correct?",problem2(8)==[1, 3, 6], "      Student answer was:", problem2(8))
    print("Problem 2 answer correct?",problem2(10)==[1, 3, 6, 10], "      Student answer was:", problem2(10))
    print("Problem 2 answer correct?",problem2(16)==[1, 3, 6, 10, 15], "      Student answer was:", problem2(16))
    print("Problem 2 answer correct?",problem2(21)==[1, 3, 6, 10, 15, 21], "      Student answer was:", problem2(21))
