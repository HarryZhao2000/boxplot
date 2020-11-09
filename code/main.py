from boxplot import boxplot as bx
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('/Users/hurryzhao/Downloads/android_test_inspector-master/results_merged.csv')
data = [data.stars.dropna().tolist(),data.contributors.dropna().tolist(),data.commits.dropna().tolist()]

fig,ax = plt.subplots()
bx.boxplot(ax,data,outlier=False)
