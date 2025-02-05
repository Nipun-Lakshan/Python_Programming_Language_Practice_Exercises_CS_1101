# CS 1101 - Week 11 Videos - Matplotlib - Practice 09

import matplotlib.pyplot as plt
'''
Intro to Graph
==============

The number of views in Youtube got in the last 14 days.
'''

y_views = [534, 689, 258, 401, 724, 689, 435, 534, 545, 435, 423, 789, 905, 561]
days = range(1, 15)

plt.scatter(days,
         y_views,
         label='Youtube Views',
         marker='o',
         facecolor='r')
plt.xlabel('Day No.')
plt.ylabel('Views')
plt.legend(loc='upper left') 
plt.title('Daily Views For Youtube Channel')
plt.grid(True, linewidth=1, color='b', linestyle='-.')
plt.show()
