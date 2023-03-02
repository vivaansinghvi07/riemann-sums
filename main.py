import math
import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mp
mp.use('Agg')

print("Please follow the following rules when entering a function:\n")
print("To raise a number to the power of another, use ** notation")
print("To multiply a constant with x, use c*x, not cx")
print("To take a square, cube, or any root of a number, raise it to a fractional power")
print("Use parentheses when needed")
print("When referencing pi, type in 'pi' and use it as a normal number")
print("When referencing e, type in 'e' and use it as a normal number")

inp = input("\nEnter an expression in terms of x below, using the aforementioned notation: \n")

pi = 3.1415926535
e = 2.718281828

trig = {"sin(": "math.sin(",
        "cos(": "math.cos(",
        "tan(": "math.tan(",
        "sec(": "math.sec(",
        "cot(": "math.cot(",
        "csc(": "math.csc("}

for item in trig: 
    inp = inp.replace(item, trig[item], 10)

func = lambda x: eval(inp)

try: 
    func(1)
except:
    raise NameError("FOLLOW THE RULES")
    
while(True):
    method = input("\nWould you like a: Left Riemann Sum (l), Right Riemann Sum (r), or Midpoint Riemann Sum (m)? ")
    if(method in 'lrm' and method != ""):
        break
    print("Please enter either l, r, or m")

while(True):
    try:
        lower = eval(input("\nWhat is the lower bound? "))
        upper = eval(input("\nWhat is the upper bound? "))
        break
    except:
        print("Enter a number doofus")
        continue

while(True):
    try:
        count = int(input("\nHow many rectangles do you want? "))
        break
    except:
        print("Enter an integer stupid")
        continue

interval = (upper - lower)/float(count)

summ = 0

xval = np.linspace(lower, upper, 100)

def f(x):
    y = []
    for item in x:
        y.append(func(item))
    return y

plt.plot(xval, f(xval), color='black')

if method == 'l':
    for i in range(count):
        summ += interval * func(lower + i * interval)
        bar = lower + i * interval
        plt.bar(bar, func(bar), interval, align='edge')

elif method == 'r':
    for i in range(1, count + 1):
        summ += interval * func(lower + i * interval)
        bar = lower + i * interval
        plt.bar(bar, func(bar), -(interval), align='edge')

elif method == 'm':
    for i in range(1, count + 1):
        summ += interval * func(lower + (i - 0.5) * interval)
        bar = lower + (i - 0.5) * interval
        plt.bar(bar, func(bar), interval)

print(f"\nThe Riemann sum of the function is: {round(summ, 3)}")
plt.savefig('graph.png')