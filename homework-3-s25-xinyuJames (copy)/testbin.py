import numpy as np
import matplotlib.pyplot as plt
from Problem1 import *

# file_path = "C:/Users/liuxi/Desktop/2025 SPR/ECE_20875/Python_for_DataScience/homework-3-s25-xinyuJames/input.txt"
file_path = "input.txt"
data = np.loadtxt(file_path)
lo = min(data)
hi = max(data)


print('Uncomment the first segment to verify the histogram you have generated and the normalized histogram you have generated')

histo = plt.hist(data, 10, (lo, hi))[0]
norm_h = norm_histogram(histo)
print("histogram: ", histo)
print("normalized histogram: ", norm_h)


print('Uncomment the second segment to verify the J value you have generated')

ch = compute_j(plt.hist(data, 5, (lo, hi))[0], (hi - lo) / 5, 1000)
print(ch)


print('Uncomment the third segment to verify the sweep of J values you have generated')

ro = sweep_n(data, lo, hi, 1, 100)
print(ro)


print('Uncomment the fourth segment to verify the min J score you have generated')

minV = find_min(sweep_n(data, lo, hi, 1, 100))
print(minV)

