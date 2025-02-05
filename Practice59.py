# CS 1101 - Week 11 Videos - Matplotlib - Practice 12

import matplotlib.pyplot as plt

labels = ['Facebook', 'Youtube', 'Linkedin', 'Instagram']
views = [357, 798, 343, 205]
explode = [0, 0, 0, 0.2]
#views = [0.3, 0.1, 0.1, 0.1]  # Total should be greater than or equal to one. Otherwise Pie chart will come with missing a part unless normalize is false in plot command attribute
plt.pie(views,
        labels=labels,
        explode=explode,
        autopct='%1.1f%%',
        shadow=True, 
        wedgeprops={'width': 0.3}) # Give Doughnut Graph when width less than 1. When width equals to 1, then it is a pie chart, If exceeding 1, then cannot recognize it.
plt.show()
