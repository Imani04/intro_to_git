"""
multiples of 3 and 5.py
if we list all the natural numbers below 10 that are multiples of
3 or 5 we get 3, 5, 6 and 9. The sum of these multiples is 23

Find the sum of all the multiplesof 3 or 5 below 1000
"""

a = []
b = []
for x in range(1000):
    if(x % 3 == 0):
        a.append(x)
    elif(x % 5 == 0):
        b.append(x)

print(sum(a + b))
