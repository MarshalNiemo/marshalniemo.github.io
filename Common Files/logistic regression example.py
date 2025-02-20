import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
import math


'''
Logistic regression is a sigmoid curve that runs from 0 to 1.
It's best used for discrete, binary random variables.
'''

#example data; hours of study vs. whether you passed the test
x = np.array([0.8, 1.1, 1.8, 2.1, 2.4, 2.7, 3.5, 4.3, 4.4, 5.4, 6.3, 6.3, 7.7, 7.9, 8.0, 8.5, 8.7, 9.1, 9.6, 9.9, 13.7]).reshape(-1,1)
'''
This model can accept a multivariable input, so it expects a 2D numpy array for the input.
Reshape converts our input into a 1xn 2D array for that purpose
'''


y = np.array([0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1])
'''
The random variable is binary; it is 0 or 1. In this case, you either pass the test or not.
'''

model = LogisticRegression()
model.fit(x,y)


fig,ax = plt.subplots(1,1)
ax.scatter(x,y)
plot_x = np.linspace(0, 15, 100).reshape(-1,1)
ax.plot(plot_x, model.predict(plot_x))
plt.show()
'''
The model's prediction is binary; if we want the actual sigmoid curve, we need to pull out the coefficients.
'''

B = [ model.intercept_.item(), model.coef_.item()]
print("Optimized Coefficients:", B[0])
print("Intercept:", B[1])

'''
logreg is the logistic regression function; logit is the inverse of the logistic regression function.
'''
def logreg(x):
    X = x[0]
    return math.exp(B[1]*X + B[0]) / (1 + math.exp(B[1]*X + B[0]))

def logit(x):
    y = x[0]
    return (math.log(y / (1-y)) - B[0]) / B[1]

'''
A limitation of logistic regression is that it assumes an infinite space for the independent variable;
e.g. we're assuming that if you studied for an infinite amount of time, the odds of passing the test are 1.
This may not be true, as factors may guarantee a limit to the risk of success or failure
'''

fig,ax = plt.subplots(1,1)

ax.scatter(x,y)
plot_x = np.linspace(0, 15, 100)
log_curve = [logreg([x]) for x in plot_x]

ax.plot(plot_x, log_curve)
plt.show()