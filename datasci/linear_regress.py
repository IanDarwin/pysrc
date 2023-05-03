''' Example of simple linear regression. I didn't write this;
    it is just the code from
    https://data36.com/linear-regression-in-python-numpy-polyfit/
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
students = {'hours': [29, 9, 10, 38, 16, 26, 50, 10, 30, 33, 43, 2, 39, 15, 44, 29, 41, 15, 24, 50],
            'test_results': [65, 7, 8, 76, 23, 56, 100, 3, 74, 48, 73, 0, 62, 37, 74, 40, 90, 42, 58, 100]}
student_data = pd.DataFrame(data=students)
print(students)
print(student_data)
x = student_data.hours
y = student_data.test_results
sp = plt.scatter(x,y)
# sp.savefig("/tmp/plot1.png")
model = np.polyfit(x, y, 1)
print(model)
predict = np.poly1d(model)
x_lin_reg = range(0, 51)
y_lin_reg = predict(x_lin_reg)
sp2=plt.plot(x_lin_reg, y_lin_reg, c = 'r')
# sp2.savefig("x.png")
