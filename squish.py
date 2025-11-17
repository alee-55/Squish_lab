import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.stats import norm
from fitting_functions import *
data = np.loadtxt("Marshmellow_data.csv", delimiter=",", dtype=str)
x = data[1:, 0].astype(np.float32)
y= data[1:,1].astype(np.float32)
print("y = ", y)
print("x = ", x)

params, params_cov = scipy.optimize.curve_fit(linear, x, y)
slope = round(params[0],2)
intercept = round(params[1],2)
###Exercise 1

print_equation(slope, intercept, "cm" , "g")
# Equation of the line: y = -0.01cm/g+6.83cm

### Exercise 2

plt.figure()
plt.scatter(x, y, label='Data')
plt.plot(x, linear(slope, x, intercept),label='Linear Fit') 
plt.legend(loc='best')
plt.ylabel("Centimeters") 
plt.xlabel("Grams") 
plt.show()
