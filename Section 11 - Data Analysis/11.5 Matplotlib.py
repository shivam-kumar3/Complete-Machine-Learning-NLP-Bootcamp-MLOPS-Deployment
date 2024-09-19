'''
Data visualization with matplotlib

Matplotlib is a powerful plotting library for python that anables the creating of static, animated, and interactive visualization. it is widely used for data visulization in data science and analytics. in this lesson, we will cover the basic of matplotlib, including creating various types of plots and customizing them
'''

import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [4,8,16,32,165]

# line plot
plt.plot(x,y)
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
# plt.show()


# customized line plot

x = [1,2,3,4,5]
y = [4,8,16,32,80]

plt.plot(x,y,color = 'red',linestyle = ":",marker = "o", linewidth = 2, markersize = 5)
plt.grid(True)
# plt.show()

# multiple plots
# sample data

x = [1,2,3,4,5]
y1 = [1,4,9,16,25]
y2 = [1,2,3,4,5]

plt.figure(figsize=(9,5)) # size of the plot

plt.subplot(1,4,1)
plt.plot(x,y1,color='green')
plt.title("Plot 1")

plt.subplot(1,4,2)
plt.plot(y1,x,color = 'red')
plt.title("Plot 2")

plt.subplot(1,4,3)
plt.plot(y1,x,color = 'blue')
plt.title("Plot 3")

plt.subplot(1,4,4)
plt.plot(y1,x,color = 'orange')
plt.title("Plot 4")
plt.show()

# barplot
cat = ['A','B','C','D','E']
values = [5,6,7,8,5]

# create a bar plot
plt.bar(cat,values,color = 'blue')
plt.title("Bar Chart")
plt.xlabel("Categories")
plt.ylabel("values")

plt.show()


# Histogram
# Histogram are used to represent the distribution of a dataset. they divide the data into bins and counts the numbers of data points in each bin

data = [1,2,3,4,4,5,6,7,7,7,7,7,7,8,9,9,7,6,6,10]

plt.hist(data, color = 'red',bins = 5,edgecolor = 'black')
plt.show()


# creating scatter plot

x = [1,2,3,4,5]
y = [4,8,16,32,80]

plt.scatter(x,y,marker='x')
plt.show()


# pie chart
label = ['A','B','C','D']
size = [30,40,70,54]
colors = ['gold','green','blue','red']

plt.pie(size,labels=label , colors=colors,autopct='%1.1f%%',explode=0.2)
plt.show()


