# -*- coding: utf-8 -*-
"""
Data Visualisations

@author: Administrator
"""
"""
Matplotlib is the brainchild of John Hunter (1968-2012), who, along with its many contributors,
 have put an immeasurable amount of time and effort into producing a piece of software utilized
 by thousands of scientists worldwide. Matplotlib can be used in Python scripts, the Python 
 and IPython shells, the Jupyter notebook, web application servers, and other graphical user
 interface toolkits. A large number of third party packages extend and build on Matplotlib
 functionality, including several higher-level plotting interfaces (seaborn, holoviews,
 ggplot, …), and two projection and mapping toolkits (basemap and cartopy).


Following are the six basic steps of creating any plot:
Step 1: Import libraries
Step 2: Prepare your data
Step 3: Select your plot (line, histogram, pic…etc.)
Step 4: Use the relevant method to build the plot.
Step 5: Customize the plot.
Step 6: Show the plot
"""

#Basic Line Plot
# Step 1: import external libraries
import matplotlib.pyplot as plt
import numpy as np

# Step 2: Sample Data for plotting
x = np.linspace(0, 5, 11)
y = x ** 2

#Step 3 & 4:
plt.plot(x, y, 'r')

#Step 5:
plt.xlabel('X Axis Title Here')
plt.ylabel('Y Axis Title Here')
plt.title('String Title Here')

#Step 6:
plt.show()


# Sinusoidal line plot

# Sample Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

# Note that using plt.subplots below is equivalent to using
# fig = plt.figure() and then ax = fig.add_subplot(111)
fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
title='About as simple as it gets, folks')
ax.grid()

plt.show()


#Histogram
np.random.seed(19680801)

# example data
mu = 100 # mean of distribution
sigma = 15 # standard deviation of distribution
x = mu + sigma * np.random.randn(437)

num_bins = 50

fig, ax = plt.subplots()

# the histogram of the data
n, bins, patches = ax.hist(x, num_bins)

# add a 'best fit' line
y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
ax.plot(bins, y, '--')
ax.set_xlabel('Smarts')
ax.set_ylabel('Probability density')
ax.set_title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')

# Tweak spacing to prevent clipping of ylabel
fig.tight_layout()
plt.show()


"""
Bar chart
"""

N = 5
menMeans = (20, 35, 30, 35, 27)
womenMeans = (25, 32, 34, 20, 25)
menStd = (2, 3, 4, 1, 2)
womenStd = (3, 5, 2, 3, 3)
ind = np.arange(N) # the x locations for the groups
width = 0.35 # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, menMeans, width, yerr=menStd)
p2 = plt.bar(ind, womenMeans, width,
bottom=menMeans, yerr=womenStd)

plt.ylabel('Scores')
plt.title('Scores by group and gender')
plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
plt.yticks(np.arange(0, 81, 10))
plt.legend((p1[0], p2[0]), ('Men', 'Women'))

plt.show()


""""
Pie Charts
""""

# Prepare your data
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
fracs = [15, 30, 45, 10]

#Draw Pie chart
plt.pie(fracs, labels=labels, autopct='%1.1f%%', shadow=True)

plt.show()

"""
Scatter Plot
"""

# Fixing random state for reproducibility
np.random.seed(19680801)

N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = (30 * np.random.rand(N))**2 # 0 to 15 point radii

plt.scatter(x, y,s=area, c=colors, alpha=0.5)
plt.show()


