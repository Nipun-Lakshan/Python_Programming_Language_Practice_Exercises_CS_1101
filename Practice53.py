# CS 1101 - Week 11 Videos - Matplotlib - Practice 06

import matplotlib.pyplot as plt
'''
Intro to Graph
==============

The number of views in marketing channels got in the last 7 days. [Youtube, Facebook, Whatsapp]
'''

y_views = [534, 689, 258, 401, 724, 689, 4045]
f_views = [123, 342, 700, 304, 405, 650, 6543]
t_views = [202, 209, 176, 415, 820, 389, 3987]
days = range(1, 8)

plt.plot(days,
         y_views,
         label='Youtube Views',
         color='r',
         marker='o',
         markerfacecolor='r')
plt.plot(days,
         f_views,
         label='Facebook Views',
         color='b',
         marker='o',
         markerfacecolor='b')
plt.plot(days,
         t_views,
         label='Twitter Views',
         color='y',
         marker='o',
         markerfacecolor='y')

plt.xlabel('Day No.')
plt.ylabel('Views')
plt.legend(loc='lower right'
           )  # Legend with changing the default location of upper left.
plt.xlim(1, 5)
plt.ylim(100, 900)
plt.title('Daily Views For Marketing Channels')
plt.show()
