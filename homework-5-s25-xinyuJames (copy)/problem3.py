import math as m
import numpy as np
import scipy.stats as stats

# import or paste dataset here
data = np.array([135, 140, 130, 145, 150, 138, 142, 137, 136, 148, 141, 139, 143, 147, 149, 134, 133, 146, 144, 132])

size = len(data)
mean = np.mean(data)
st = np.std(data, ddof=1)
se = st / np.sqrt(size)

# code for Question 1
print('Problem 1 Answers:')
# code below this line
c1 = 0.9
ts1 = stats.t.ppf(1 - (1 - c1)/2, size - 1)
margin1 = ts1 * se

max_v1 = mean + margin1
min_v1 = mean - margin1

print(f'Mean: {mean: .4f}')
print(f'Standard Error: {se: .4f}')
print(f'Standard Score: {ts1: .4f}')
print(f'Max CI: {max_v1: .4f}')
print(f'Min CI: {min_v1: .4f}')
print()
# code for Question 2
print('Problem 2 Answers:')
# code below this line
c2 = 0.95
ts2 = stats.t.ppf(1 - (1 - c2)/2, size - 1)
margin2 = ts2 * se

max_v2 = mean + margin2
min_v2 = mean - margin2
print(f'Standard Score: {ts2: .4f}')
print(f'Max CI: {max_v2: .4f}')
print(f'Min CI: {min_v2: .4f}')
print()
# code for Question 3
print('Problem 3 Answers:')
# code below this line
pop_mean = 5
#zs = (mean - pop_mean)/se
zs = stats.norm.ppf(1 - (1 - c2)/2)
margin3 = zs * se
max_v3 = mean + margin3
min_v3 = mean - margin3
print(f'Standard Score: {zs: .4f}')
print(f'Max CI: {max_v3: .4f}')
print(f'Min CI: {min_v3: .4f}')
