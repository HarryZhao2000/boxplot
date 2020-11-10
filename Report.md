# **Report of Project 1**

## Group members
**Group 5**
+ Haoran Zhao
+ Zhaoyuan Zhai

<br>


## ABSTRCT

Because of the limitation of traditional box plot like exact values not retained, unclear data distribution, and difficulty to compare, we want to build a new module **powerful_boxplot** that offer way to draw new types of box plots to meet our needs. In this module, we have 4 ways to build 4 different box plots, which are normal boxplot, info_boxplot, hist_boxplot and a creative creative_boxplot, to meet different situations. These three new box plots all offer more information or more exact values.

<br>

## Table of Contents

- [Background](#background)
- [Contribution](#contribution)
- [Principles](#principles)
- [Difficuties](#difficuties)
- [Documentation](#documentation)
- [Test](#test)

<br>

## Background

The built-in boxplot method in matplotlib have the advantage of showing upper bound, lower bound, median, 25% quartiles and 75% quartiles some limits, which cannot solve by changing the given parameters, such as exact values not retained, unclear data distribution, and difficulty to compare. Therefore, we need to rewrite boxplot from scratch to remove the limits.

To better compare the data between different categories, we rewrite the **boxplots method** with ```matplotlib.patches```. **This method put multiple boxplots into one graph** so that user can compare the statistic information of different categories intuitively.

The original boxplot method only show the value of median, 25% percentile, 75% percentile. However, user also wants to get detailed information about the stratification within a smaller range. The **info_boxplot method** was created to solve this problem, which show every 5% percentile from Q1 to Q3 with a vertical line. User can see each percentile clearly from the boxplot.

To show the distribution of data, **hist_boxplot method** mix the histogram with boxplots, through the histogram of default 10 bins, user can get the information of distribution, the length of each bin represents the number in certain range.

The **creative_boxplot method** aims to show exact values in boxplots, giving an insight of the degree of density and more clear distribution of data. With the gradient of color indicates the dense of data, user can get the information for distribution within a smaller range, which is more user-friendly than two previous methods.

<br>

## Contribution

- Haoran Zhao

  He takes over the development of  `boxplot()`,`info_boxplot()` and `hist_boxplot()`, and the task to test them on real dataset. Besides he wrote the Difficulty part and Abstract part in the report.

- Zhaoyuan Zhai

  He takes over the development of  `creative_boxplot()`, and he wrote the Documentation part, Principle part and Background part in the report.

<br>

## Principles
Visualization Principles

1. Above all else, show the data.
2. Maximize the data-ink ratio.
3. Erase non-data ink.
4. Erase redundant data-ink.
5. Revise and edit.

### Apply princples into plots
+ To meet the first principle.The boxplots, info_boxplots, hist_boxplots, creative_boxplots are just show the boxplots and relevant elements, nothing else.
+ To meet the second principle. We achieved that the data-ink ratio of boxplot into maximum. 
+ To meet the third principle. We change the background into white to erase non-data ink.
+ To meet the fourth principle. We only add the necessary elements of boxplots and histogram ( in creative_boxplot, actual points and line are used to show trend and dense of data).

<br>

## Difficuties

- The circle drawn is an ellipse.

  At the begining, I tried to use ``` matplotlib.patches.Circle``` to draw the outliers and other points, it looked like a ellipse rather than a circle. It was because that the scale of the axes were not equal, and the same length were not looked same in X and Y dirction on the screen. Thus, we used ```ax.axis('equal')``` to let the scale of the axes be equal.

- The height of hist is too large.

  While tring large data on `hist_boxplot()` , the hist is often so large that it blocks out the next picture. To solve this issue, we use $\frac{\text { Distance between boxplots } \times \text { Length of current hist }}{\text { Length of longest hist }}$ as the length of hist instead of reall length.

<br>

## Documentation
<font size=5>**boxplot.boxplot**</font>

```
boxplot.boxplot(ax, Data, outlier=True, box_facecolor='white', box_edgecolor='k', outlier_facecolor='r', outlier_edgecolor='r', whisker_edgecolor='k', median_edgecolor='k', box_alpha=1.0, outlier_alpha=1.0)
```

Make a box and whisker plot in the axes.

Make a box and whisker plot for every column in Data. 
+ The box extends from 25% percentile to 75% percentile, with a horizontal line in the location of median value. 
+ The whisker extend from 25% percentile to lower bound, and from 75% percentile to upper bound to show the range of data.
+ The upper vertical line shows the upper bound, and the lower vertical line shows the lower bound.
+ The outliers are the points that value larger than upper bound or smaller than lower bound.
### **Parameters:**
```
ax: axes.Axes object
    ax refer to a single Axes object.

Data: list or numpy.array
    Data should be an iteratable object.

outlier: bool
    Data point that its value larger than upper bound or smaller than lower bound, optional, default: True.

box_facecolor: str
    Set the face color of rectangle, optional, default: 'white'.

box_edgecolor: str
    Set the edge color of rectangle, optional, default: 'k'.

outlier_facecolor: str
    Set the face color of outlier, optional, default: 'r'.

outlier_edgecolor: str
    Set the edge color of outlier, optional, default: 'r'.

whisker_edgecolor: str
    Set the edge color of whisker, optional, default: 'k'.

median_edgecolor: str
    Set the line color of median, optional, default: 'k'.

box_alpha: float
    Set the transparency of rectangle, optional, default: 1.0.

outlier_alpha: float
    Set the transparency of outlier, optional, default: 1.0.
```
### Examples
```python
# boxplot
fig,ax = plt.subplots()
boxplot(ax,data,outlier_facecolor='w', outlier_edgecolor='k',outlier=True)
```
<img src=./Plot/boxplot.png>

<font size=5>**boxplot.info_boxplot**</font>

```
boxplot.info_boxplot(ax, Data, multiplebox=True, outlier=True, box_facecolor='white', box_edgecolor='k', outlier_facecolor='r', outlier_edgecolor='r', whisker_edgecolor='k', median_edgecolor='k', box_alpha = 1.0, outlier_alpha = 1.0)
```
Make a box and whisker plot in the axes with multiple percentile lines.
+ **Compared to the original boxplot** , the info_boxplot shows the every 5% percentile from Q1 to Q3 with a vertical line, e.g. 25%, 30%, 35%, 40%, 45%, 50%, 55%, 60%, 65%, 70%, 75%. 
+ This boxplot is **more imformative** than original boxplot, which shows the range of value for data in a smaller percentile range.
+ Other elements are the same as original boxplots.
+ **However**, sometimes, **two lines can be very dense**, making user confused and hard to read, which is not user-friendly.

### **Parameters**
```
ax: axes.Axes object
    ax refer to a single Axes object.

Data: list or numpy.array
    Data should be an iteratable object.

multiplebox: bool
    Show every 5% percentile from Q1 to Q3 in boxplot, optional, default: True.

outlier: bool
    Data point that its value larger than upper bound or smaller than lower bound, optional, default: True.

box_facecolor: str
    Set the face color of rectangle, optional, default: 'white'.

box_edgecolor: str
    Set the edge color of rectangle, optional, default: 'k'.

outlier_facecolor: str
    Set the face color of outlier, optional, default: 'r'.

outlier_edgecolor: str
    Set the edge color of outlier, optional, default: 'r'.

whisker_edgecolor: str
    Set the edge color of whisker, optional, default: 'k'.

median_edgecolor: str
    Set the line color of median, optional, default: 'k'.

box_alpha: float
    Set the transparency of rectangle, optional, default: 1.0.

outlier_alpha: float
    Set the transparency of outlier, optional, default: 1.0.
```
### Examples
```python
# info_boxplot
fig,ax = plt.subplots()
plt.figure(figsize=(16,16))
info_boxplot(ax,data,outlier=False,multiplebox=True)
```
<img src=./Plot/info_boxplot.png>

<font size=5>**boxplot.hist_boxplot**</font>

```
boxplot.hist_boxplot(ax, Data, n_bins=10, outlier=True,
 box_facecolor='white', box_edgecolor='k', 
 outlier_facecolor='r', outlier_edgecolor='r', whisker_edgecolor='k', median_edgecolor='k', bin_facecolor='#CECECE', bin_edgecolor='k', box_alpha = 1.0, outlier_alpha = 1.0, hist_alpha=1.0)
 ```

Make a box and whisker plot in the axes on the left of the graph, with histogram on the right of the graph.
+ **Compared to the original boxplot**, the hist_boxplot mix between a original boxplot and a histogram, showing the distribution of data and the relative value for each range.

+ Other elements are the same as original boxplots.

+ **However**, the number of bins is still small, resulting in **not detailed display of distribution** .

### **Parameters**
```
ax: axes.Axes object
    ax refer to a single Axes object.

Data: list or numpy.array
    Data should be an iteratable object.

n_bins: int
    The number of bins for histogram, optional, default: 10.

outlier: bool
    Data point that its value larger than upper bound or smaller than lower bound, optional, default: True.

box_facecolor: str
    Set the face color of rectangle, optional, default: 'white'.

box_edgecolor: str
    Set the edge color of rectangle, optional, default: 'k'.

outlier_facecolor: str
    Set the face color of outlier, optional, default: 'r'.

outlier_edgecolor: str
    Set the edge color of outlier, optional, default: 'r'.

whisker_edgecolor: str
    Set the edge color of whisker, optional, default: 'k'.

median_edgecolor: str
    Set the line color of median, optional, default: 'k'.

bin_facecolor: str
    Set the face color of bins, optional, default: '#CECECE'.

bin_edgecolor: str
    Set the edge color of bins, optional, default: 'k'.

box_alpha: float
    Set the transparency of rectangle, optional, default: 1.0.

outlier_alpha: float
    Set the transparency of outlier, optional, default: 1.0.

hist_alpha: float
    Set the transparency of histograms, optional, default: 1.0.
```

### Examples
```python
# hist_boxplot
fig,ax = plt.subplots()
hist_boxplot(ax,data,outlier=False)
```
<img src=./Plot/hist_boxplot.png>

<font size=5>**boxplot.creative_boxplot**</font>

```
boxplot.creative_boxplot(ax, Data, outlier=True, box_facecolor='white', box_edgecolor='k',  outlier_facecolor='r', outlier_edgecolor=None, whisker_edgecolor='k', median_edgecolor='k', box_alpha = 1.0, outlier_alpha = 1.0, point_alpha=0.3)
 ```

Make a box and whisker plot in the axes with actual data points.
+ **Compared to the original boxplot**, the creative_boxplot function plot **actual data points** in the graph, showing the location and degree of dense for the data. The points are draw with 30% default transparency, so **the gradient of color indicates the dense of data**. The darker, the denser.

+ **Besides**, the creative_boxplot connects the median of different boxplots with a default green line, showing the variation of median for different boxplots intuitively. Also the green lin can show the trend of median with time changes.

+ Other elements are the same as original boxplots.

### **Parameters**
```
ax: axes.Axes object
    ax refer to a single Axes object.

Data: list or numpy.array
    Data should be an iteratable object.

outlier: bool
    Data point that its value larger than upper bound or smaller than lower bound, optional, default: True.

box_facecolor: str
    Set the face color of rectangle, optional, default: 'white'.

box_edgecolor: str
    Set the edge color of rectangle, optional, default: 'k'.

outlier_facecolor: str
    Set the face color of outlier, optional, default: 'b'.

outlier_edgecolor: str
    Set the edge color of outlier, optional, default: None.

whisker_edgecolor: str
    Set the edge color of whisker, optional, default: 'k'.

median_edgecolor: str
    Set the line color of median, optional, default: 'k'.

box_alpha: float
    Set the transparency of rectangle, optional, default: 1.0.

outlier_alpha: float
    Set the transparency of outlier, optional, default: 1.0.

point_alpha: float
    Set the transparency of points, optional, default: 0.3.
```
### Examples
```python
# creative_boxplot
fig,ax = plt.subplots()
creative_boxplot(ax,data,outlier=False)
```
<img src=./Plot/creative_boxplot.png>

## Test

We have tested our module with integers and floats, it works very well and while we test with a invalid input like a string, the module will return a massage that *"Wrong data type, please input a list of numerical list"*, which shows the robustness of our module. Also, we test all the parameters and make sure all of them can work well. Besides, we use dataset from [android_test_inspector](https://github.com/luiscruz/android_test_inspector) as a real dataset to test the module, it works well.