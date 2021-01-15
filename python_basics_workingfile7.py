# -*- coding: utf-8 -*-
"""
Data Visualization - Seaborn
@author: Administrator
"""
"""
Seaborn is a complement to matplotlib and not a replacement for it.
 The reason is that it is built on top of matplotlib and you will often invoke 
 matplotlib functions directly to draw simpler plots already available through the
 pyplot namespace. Matplotlib is highly customizable, but it can be hard to know what
 settings to tweak to achieve an attractive plot. Seaborn comes with a number of 
 customized themes and a high-level interface for controlling the look of matplotlib figures.
It is tightly integrated with the PyData stack including support for NumPy and Pandas 
data structures and statistical routines from scipy and statsmodels.

Some of the features that seaborn offers are:
1. Several built-in themes for styling matplotlib graphics.
2. Tools for choosing color palettes to make beautiful plots that reveal patterns in your data.
3. Functions for visualizing univariate and bivariate distributions or for comparing them between subsets of data.
4. Tools that fit and visualize linear regression models for different kinds of independent and dependent variables.
5. Functions that visualize matrices of data and use clustering algorithms to discover structure in those matrices.
6. A function to plot statistical timeseries data with flexible estimation and representation of uncertainty around the estimate.
7. High-level abstractions for structuring grids of plots that let you easily build complex visualizations.
For reference and more details, please visit: https://seaborn.pydata.org/introduction.html

"""

#When you’re working with Seaborn, you can either use one of the built-in datasets that the library itself has to offer or you can load a Pandas DataFrame.

#load_dataset() function is used to start working with a built-in Seaborn data set.

import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset('tips')

sns.lmplot(x='total_bill', y='tip', data=tips)
plt.show()

#Bar Plot
import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset('tips')

sns.barplot(x = 'sex', y='total_bill', data=tips)
plt.show()

#count Plot

import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset('tips')

sns.countplot(x = 'sex', data = tips)
plt.show()

#Box Plot
import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset('tips')

sns.boxplot(x = 'day', y='total_bill', data=tips, palette='rainbow')
plt.show()

#Violin Plot
import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset('tips')

sns.violinplot(x = 'day', y='total_bill', data=tips, palette='rainbow')
plt.show()

