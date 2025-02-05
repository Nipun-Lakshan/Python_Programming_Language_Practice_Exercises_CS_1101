# CS 1101 - Week 11 Videos - Matplotlib - Practice 11

import matplotlib.pyplot as plt
'''
Intro to Graph
==============

The number of views in Youtube got in the last 14 days.
'''

y_views = [
    534, 689, 258, 401, 724, 689, 435, 534, 545, 435, 423, 789, 905, 561
]
bins = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
plt.hist(y_views, bins, label="Youtube Views")
plt.xlabel('Day No.')
plt.ylabel('Views')
plt.legend(loc='upper left')
plt.title('Daily Views For Youtube & Facebook Channels')
plt.grid(True, linewidth=1, color='b', linestyle='-.')
plt.xticks(bins)
plt.show()
