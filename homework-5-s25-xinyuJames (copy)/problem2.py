import numpy as np
import math as m
import scipy.stats as stats
from scipy.stats import norm
from scipy.stats import t

myFile = open("c:/Users/liuxi/Desktop/2025 SPR/ECE_20875/Python_for_DataScience/homework-5-s25-xinyuJames/city_vehicle_survey.txt")
data1 = myFile.readlines()
data1 = [float(x) for x in data1]
myFile.close()

pop_mean = 5

# code for question 2
print('Problem 2 Answers:')
# code below this line

size = len(data1)
mean = np.mean(data1)
st = np.std(data1, ddof=1)
se = st / np.sqrt(size)
z_score = (mean - pop_mean) / se
p_value = 2 * norm.cdf(-abs(z_score))
print(f'Size: {size: .4f}')
print(f'Mean: {mean: .4f}')
print(f'Standard Error: {se: .4f}')
print(f'Standard Score: {z_score: .4f}')
print(f'p-value: {p_value: .4f}')
print()


# code for question 3
print('Problem 3 Answers:')
# code below this line
z_score = norm.ppf(0.05 / 2)
se = abs((mean - pop_mean) / z_score)
min_size = (st / se) ** 2
print(f'Standard Error: {se: .4f}')
print(f'Minimum Size: {min_size: .4f}')
print()


myFile1 = open('c:/Users/liuxi/Desktop/2025 SPR/ECE_20875/Python_for_DataScience/homework-5-s25-xinyuJames/vehicle_data_1.txt')
data1 = myFile1.readlines()

myFile2 = open('c:/Users/liuxi/Desktop/2025 SPR/ECE_20875/Python_for_DataScience/homework-5-s25-xinyuJames/vehicle_data_2.txt')
data2 = myFile2.readlines()

data1 = [float(x) for x in data1]
data2 = [float(y) for y in data2]
myFile1.close()
myFile2.close()


# code for question 5
print('Problem 5 Answers:')
# code below this line
size1 = len(data1)
size2 = len(data2)
mean1 = np.mean(data1)
mean2 = np.mean(data2)
st1 = np.std(data1, ddof=1)
st2 = np.std(data2, ddof=1)
se = np.sqrt((st1**2) / size1 + (st2**2) / size2)
z_score = (mean1 - mean2) / se
p_value = 2 * norm.cdf(-abs(z_score))
print(f'Size 1: {size1: .4f}')
print(f'Size 2: {size2: .4f}')
print(f'Mean 1: {mean1: .4f}')
print(f'Mean 2: {mean2: .4f}')
print(f'Standard Error: {se: .4f}')
print(f'Standard Score: {z_score: .4f}')
print(f'p-value: {p_value: .4e}')
print()





