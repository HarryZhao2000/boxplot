from boxplot import boxplot as bx
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../results_merged.csv')
t_d1 = data.commits[data.last_updated=='2017-08-28']
t_d2 = data.commits[data.last_updated=='2017-08-26']
t_d3 = data.commits[data.last_updated=='2017-08-24']
t_d4 = data.commits[data.last_updated=='2017-08-22']
t_d5 = data.commits[data.last_updated=='2017-08-20']

t_d=[t_d1,t_d2,t_d3,t_d4,t_d5]

fig,ax = plt.subplots()
bx.creative_boxplot(ax,t_d,outlier=False)
