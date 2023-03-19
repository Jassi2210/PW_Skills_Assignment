#!/usr/bin/env python
# coding: utf-8

# # Q1: What is Matplotlib? Why is it used? Name five plots that can be plotted using the Pyplot module of Matplotlib. 
# ## Ans1- Matplotlib is a popular open-source data visualization library for Python. It provides a wide range of tools for creating various types of high-quality, customizable plots and charts.
# 
# # Matplotlib is used in various fields like scientific computing, data analysis, finance, and machine learning for visualizing data and making it easier to understand. Matplotlib is highly customizable, and users can tweak various aspects of the plot to make it look and feel as desired. Matplotlib can create a wide variety of plots, including line plots, scatter plots, bar plots, histograms, pie charts, and many more.
# 
# # Here are five types of plots that can be plotted using the Pyplot module of Matplotlib:
# 
# # 1.Line Plot: A line plot is a basic plot that represents data points connected with straight lines. It is useful for visualizing trends in data over time.
# 
# # 2. Scatter Plot: A scatter plot is used to display the relationship between two variables. It represents data as a collection of points, where each point represents a single observation.
# 
# # 3.Bar Plot: A bar plot is used to represent categorical data with rectangular bars. Each bar represents a category, and the height of the bar represents the value associated with that category.
# 
# # 4.Histogram: A histogram is used to visualize the distribution of a continuous variable. It represents data as a series of contiguous, non-overlapping bars.
# 
# # 5.Pie Chart: A pie chart is used to represent data as a percentage of a whole. It is useful for visualizing the relative proportions of different categories in a dataset.

# In[ ]:





# ## Q2: What is a scatter plot? Use the following code to generate data for x and y. Using this generated data plot a scatter plot.
# # import numpy as np
# # np.random.seed(3)
# # x = 3 + np.random.normal(0, 2, 50)
# # y = 3 + np.random.normal(0, 2, len(x))
# # Note: Also add title, xlabel, and ylabel to the plot.
# ## Ans2- A scatter plot is a type of plot that displays the relationship between two numerical variables. It is created by plotting one variable on the x-axis and the other variable on the y-axis. Each point on the plot represents a pair of values for the two variables. Scatter plots are useful for visualizing the correlation or lack thereof between two variables.

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

np.random.seed(3)
x = 3 + np.random.normal(0, 2, 50)
y = 3 + np.random.normal(0, 2, len(x))

plt.scatter(x, y)
plt.title('Scatter Plot of X and Y')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()


# In[ ]:





# ## Q3: Why is the subplot() function used? Draw four line plots using the subplot() function.
# Use the following data:
# import numpy as np
# For line 1: x = np.array([0, 1, 2, 3, 4, 5]) and y = np.array([0, 100, 200, 300, 400, 500])
# For line 2: x = np.array([0, 1, 2, 3, 4, 5]) and y = np.array([50, 20, 40, 20, 60, 70])
# For line 3: x = np.array([0, 1, 2, 3, 4, 5]) and y = np.array([10, 20, 30, 40, 50, 60])
# For line 4: x = np.array([0, 1, 2, 3, 4, 5]) and y = np.array([200, 350, 250, 550, 450, 150])
# 
# Ans3- The subplot() function in Matplotlib is used to create multiple plots in a single figure. It allows us to create a grid of subplots and specify the position of each plot using row and column indices. The subplot() function takes three arguments: the number of rows, the number of columns, and the index of the current plot.

# In[5]:


import numpy as np
import matplotlib.pyplot as plt

# Data for line 1
x1 = np.array([0, 1, 2, 3, 4, 5])
y1 = np.array([0, 100, 200, 300, 400, 500])

# Data for line 2
x2 = np.array([0, 1, 2, 3, 4, 5])
y2 = np.array([50, 20, 40, 20, 60, 70])

# Data for line 3
x3 = np.array([0, 1, 2, 3, 4, 5])
y3 = np.array([10, 20, 30, 40, 50, 60])

# Data for line 4
x4 = np.array([0, 1, 2, 3, 4, 5])
y4 = np.array([200, 350, 250, 550, 450, 150])

# Create a figure with four subplots
fig, axs = plt.subplots(2, 2, figsize=(8, 6))

# Plot line 1 in the first subplot
axs[0, 0].plot(x1, y1)
axs[0, 0].set_title('Line 1')

# Plot line 2 in the second subplot
axs[0, 1].plot(x2, y2)
axs[0, 1].set_title('Line 2')

# Plot line 3 in the third subplot
axs[1, 0].plot(x3, y3)
axs[1, 0].set_title('Line 3')

# Plot line 4 in the fourth subplot
axs[1, 1].plot(x4, y4)
axs[1, 1].set_title('Line 4')

# Add a title for the entire figure
fig.suptitle('Four Line Plots')

# Adjust the spacing between subplots
plt.subplots_adjust(hspace=0.5, wspace=0.3)

# Display the plot
plt.show()


# In[ ]:





# ## Q4: What is a bar plot? Why is it used? Using the following data plot a bar plot and a horizontal bar plot.
# # import numpy as np
# # company = np.array(["Apple", "Microsoft", "Google", "AMD"])
# # profit = np.array([3000, 8000, 1000, 10000])
# 
# ## Ans- A bar plot is a way to represent data using rectangular bars, where the height or length of each bar corresponds to the value being represented. It is often used to compare data between different categories.
# 
# # A vertical bar plot is created using the bar() function, while a horizontal bar plot is created using the barh() function in Matplotlib.

# In[11]:


import numpy as np
import matplotlib.pyplot as plt

# Data for the bar plot
company = np.array(["Apple", "Microsoft", "Google", "AMD"])
profit = np.array([3000, 8000, 1000, 10000])

# Create a vertical bar plot
plt.bar(company, profit)
plt.title('Company Profit')
plt.xlabel('Company')
plt.ylabel('Profit')
plt.show()

# Create a horizontal bar plot
plt.barh(company, profit)
plt.title('Company Profit')
plt.xlabel('Profit')
plt.ylabel('Company')
plt.show()


# In[ ]:





# ## Q5: What is a box plot? Why is it used? Using the following data plot a box plot.
# # box1 = np.random.normal(100, 10, 200)
# # box2 = np.random.normal(90, 20, 200)
# ## Ans5- A box plot is a graphical representation of the distribution of a set of data through their quartiles. It consists of a box, which represents the second and third quartiles, and whiskers that extend from the box to represent the minimum and maximum values in the data set. Box plots are useful for identifying outliers and comparing distributions between different groups.

# In[12]:


import numpy as np
import matplotlib.pyplot as plt

# Data for the box plot
box1 = np.random.normal(100, 10, 200)
box2 = np.random.normal(90, 20, 200)

# Combine the two data sets
data = [box1, box2]

# Create a box plot
plt.boxplot(data)
plt.title('Box Plot')
plt.xticks([1, 2], ['Box 1', 'Box 2'])
plt.ylabel('Values')
plt.show()


# In[ ]:




