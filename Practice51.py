# CS 1101 - Week 11 Videos - Matplotlib - Practice 04

import matplotlib.pyplot as plt
'''
Intro to Graph
==============

The number of views a youtube channel got in the last 7 days.
'''

views = [534, 689, 258, 401, 724, 689, 350]
days = range(1, 8)
'''
Plot Syntax Description
=======================

plot(x, y, label = '<name_of_the_graph>) // plot a graph with a legend.
'''

plt.plot(
    days,
    views,
    label='Youtube Views',
    color='r',
    marker='o',
    markerfacecolor='g',
    linestyle='--',
    linewidth=2
)  # linestyle can be name or symbol // solid . (Default) => dasheddot -. => dashed = '--
plt.xlabel('Day No.')
plt.ylabel('Views')
plt.legend(
    loc='lower right')  # Legend with changing the default location of upper left.
plt.title('Youtube Views on a Daily Basis')
plt.show()
