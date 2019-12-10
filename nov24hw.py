sum = 0
for i in range(1,51):
    sum += i
print(sum)

import numpy as np
n = 50
f = np.zeros(n+1)
f[0] = 0
f[1] = 1
for i in range(2, n+1):
    f[i] = f[i-1]+f[i-2]
t = np.zeros(n+1)
t[0] = 0
for j in range(1, n+1):
    t[j] = t[j-1] + j
print(t)
sumF = sum(f)
sumT = sum(t)
if sumF > sumT:
    print("The fibonnaci sequence's sum is greater than the triangle sequence's sum.")
elif sumF == sumT:
    print("The fibonnaci sequence's sum is equal to the triangle sequence's sum.")
else:
    print("The fibonnaci sequence's sum is less than the triangle sequence's sum.")
