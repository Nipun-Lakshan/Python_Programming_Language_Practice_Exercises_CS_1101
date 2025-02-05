# CS 1101 - Week 11 Videos - Matplotlib - Practice 10

import matplotlib.pyplot as plt
'''
Intro to Graph
==============

The number of views in Youtube got in the last 14 days.
'''

y_views = [
    534, 689, 258, 401, 724, 689, 435, 534, 545, 435, 423, 789, 905, 561
]
f_views = [
    534, 689, 258, 401, 724, 689, 435, 534, 545, 435, 423, 789, 905, 561
]
days = range(1, 15)

plt.bar([a - 0.25 for a in days],
        y_views,
        label='Youtube Views',
        width=0.25,
        align='edge')
plt.bar([a + 0.25 for a in days],
        f_views,
        label='Facebook Views',
        width=-0.25,
        align='edge')
plt.xlabel('Day No.')
plt.ylabel('Views')
plt.legend(loc='upper left')
plt.title('Daily Views For Youtube & Facebook Channels')
plt.grid(True, linewidth=1, color='b', linestyle='-.')
plt.xticks(days)
plt.show()
