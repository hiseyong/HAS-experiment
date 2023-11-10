import numpy as np
import matplotlib.pyplot as plt

x = [0.08, 0.07,0.062, 0.05, 0.04, 0.03] #여기에 기앖 값들을 입력할 것
y = [230, 210, 170,150,130,70] #여기에 기압 값들에 따른 물기둥 높이를 입력할 것

x = np.array(x)
y = np.array(y)

plt.scatter(x, y, label='real data', color='red', marker='o')
plt.plot(x, y, label='Linear Regression Line', color='blue', linestyle='dotted')
plt.legend()

plt.show()
