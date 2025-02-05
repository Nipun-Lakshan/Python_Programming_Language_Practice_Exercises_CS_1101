# CS 1101 - Week 11 Videos - Matplotlib - Practice 01

import matplotlib.pyplot as plt

# Code 01
# views = [534, 689, 258, 401, 724, 689, 350]
# plt.plot(views)
# plt.show()

# Code 02
views = [534, 689, 258, 401, 724, 689, 350]
# days = [1, 2, 3, 4, 5, 6, 7]
days = range(1, 8)
# plt.plot(X,Y)
plt.plot(days, views)
plt.show()
