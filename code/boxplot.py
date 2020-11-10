import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpathes
import random


class boxplot:
    def boxplot(ax,
                Data,
                outlier=True,
                box_facecolor='white',
                box_edgecolor='k',
                outlier_facecolor='r',
                outlier_edgecolor='r',
                whisker_edgecolor='k',
                median_edgecolor='k',
                box_alpha=1.0,
                outlier_alpha=1.0):
        h = max(max(p) for p in Data) + 0.1 * abs(max(max(p) for p in Data))
        l = min(min(p) for p in Data) + 0.1 * abs(min(min(p) for p in Data))
        count = len(Data)
        a = (h - l) / 2000
        if outlier == True:
            center = [round(((h - l) / (count + 1)) * (x + 1), 8) for x in range(count)]
        else:
            center = [round(((h - l) / (count + 1)) * (x + 1), 8) / a for x in range(count)]
        ax.axis('equal')
        i = 0
        for data in Data:
            data = sorted(data)
            # percentile
            p = [0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75]
            pen = [round((len(data) + 1) * x, 2) for x in p]
            d = [np.quantile(data, j) for j in p]

            # outlier
            IQR = d[-1] - d[0]
            upper = d[-1] + 1.5 * IQR
            lower = d[0] - 1.5 * IQR
            Upper = min(upper, data[-1])
            Lower = max(lower, data[0])
            outliers = []
            for p in data:
                if p > upper or p < lower:
                    outliers.append(p)
            if outlier == True:
                for p in outliers:
                    rect = mpathes.Ellipse((center[i], p), 0.04 * center[-1], 0.04 * center[-1],
                                           ec=outlier_edgecolor, fc=outlier_facecolor, alpha=outlier_alpha)
                    ax.add_patch(rect)

            # whisker
            ax.hlines(Upper, center[i] - 0.1 * center[0], center[i] + 0.1 * center[0], whisker_edgecolor)
            ax.hlines(Lower, center[i] - 0.1 * center[0], center[i] + 0.1 * center[0], whisker_edgecolor)
            ax.vlines(center[i], Lower, d[0], whisker_edgecolor)
            ax.vlines(center[i], d[-1], Upper, whisker_edgecolor)

            # median
            ax.hlines(d[5], center[i] - 0.2 * center[0], center[i] + 0.2 * center[0], median_edgecolor, lw=3)

            # box
            rect = mpathes.Rectangle((center[i] - 0.2 * center[0], d[0]), 0.4 * center[0], d[-1] - d[0],
                                     ec=box_edgecolor, fc=box_facecolor, alpha=box_alpha)
            ax.add_patch(rect)
            i += 1
        plt.show()

    def info_boxplot(ax,
                     Data,
                     multiplebox=True,
                     outlier=True,
                     box_facecolor='white',
                     box_edgecolor='k',
                     outlier_facecolor='r',
                     outlier_edgecolor='r',
                     whisker_edgecolor='k',
                     median_edgecolor='k',
                     box_alpha=1.0,
                     outlier_alpha=1.0):
        h = max(max(p) for p in Data) + 0.1 * abs(max(max(p) for p in Data))
        l = min(min(p) for p in Data) + 0.1 * abs(min(min(p) for p in Data))
        count = len(Data)
        a = (h - l) / 2000
        if outlier == True:
            center = [round(((h - l) / (count + 1)) * (x + 1), 8) for x in range(count)]
        else:
            center = [round(((h - l) / (count + 1)) * (x + 1), 8) / a for x in range(count)]
        print(center)
        ax.axis('equal')
        i = 0
        for data in Data:
            # percentile
            p = [0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75]
            pen = [round((len(data) + 1) * x, 8) for x in p]
            data = sorted(data)
            d = [np.quantile(data, i) for i in p]

            # outlier
            IQR = d[-1] - d[0]
            upper = d[-1] + 1.5 * IQR
            lower = d[0] - 1.5 * IQR
            Upper = min(upper, data[-1])
            Lower = max(lower, data[0])
            outliers = []
            for p in data:
                if p > upper or p < lower:
                    outliers.append(p)
            if outlier == True:
                for p in outliers:
                    rect = mpathes.Ellipse((center[i], p), 0.04 * center[-1], 0.04 * center[-1],
                                           ec=outlier_edgecolor, fc=outlier_facecolor, alpha=outlier_alpha)
                    ax.add_patch(rect)

            # whisker
            ax.hlines(Upper, center[i] - 0.1 * center[0], center[i] + 0.1 * center[0], whisker_edgecolor)
            ax.hlines(Lower, center[i] - 0.1 * center[0], center[i] + 0.1 * center[0], whisker_edgecolor)
            ax.vlines(center[i], Lower, d[0], whisker_edgecolor)
            ax.vlines(center[i], d[-1], Upper, whisker_edgecolor)

            # median
            ax.hlines(d[5], center[i] - 0.2 * center[0], center[i] + 0.2 * center[0], median_edgecolor, lw=3)

            # multiplebox
            if multiplebox == True:
                for x in d:
                    ax.hlines(d, center[i] - 0.2 * center[0], center[i] + 0.2 * center[0], box_edgecolor, lw=1)

            # box
            rect = mpathes.Rectangle((center[i] - 0.2 * center[0], d[0]), 0.4 * center[0], d[-1] - d[0],
                                     ec=box_edgecolor, fc=box_facecolor, alpha=box_alpha)
            ax.add_patch(rect)
            i += 1
        plt.show()

    def hist_boxplot(ax,
                     Data,
                     n_bins=10,
                     outlier=True,
                     box_facecolor='white',
                     box_edgecolor='k',
                     outlier_facecolor='r',
                     outlier_edgecolor='r',
                     whisker_edgecolor='k',
                     median_edgecolor='k',
                     bin_facecolor='#CECECE',
                     bin_edgecolor='k',
                     box_alpha=1.0,
                     outlier_alpha=1.0,
                     hist_alpha=1.0):
        i = 0
        h = max(max(p) for p in Data) + 0.1 * abs(max(max(p) for p in Data))
        l = min(min(p) for p in Data) + 0.1 * abs(min(min(p) for p in Data))
        count = len(Data)
        a = (h - l) / 2000
        if outlier == True:
            center = [round(((h - l) / (count + 1)) * (x + 1), 8) for x in range(count)]
        else:
            center = [round(((h - l) / (count + 1)) * (x + 1), 8) / a for x in range(count)]
        print(center)
        ax.axis('equal')
        for data in Data:
            # percentile
            p = [0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75]
            pen = [round((len(data) + 1) * x, 8) for x in p]
            data = sorted(data)
            d = [np.quantile(data, i) for i in p]

            # outlier
            IQR = d[-1] - d[0]
            upper = d[-1] + 1.5 * IQR
            lower = d[0] - 1.5 * IQR
            Upper = min(upper, data[-1])
            Lower = max(lower, data[0])
            outliers = []
            for p in data:
                if p > upper or p < lower:
                    outliers.append(p)
            if outlier == True:
                w = (data[-1] - data[0]) / n_bins
                for p in outliers:
                    rect = mpathes.Ellipse((center[i], p), 0.04 * center[-1], 0.04 * center[-1],
                                           ec=outlier_edgecolor, fc=outlier_facecolor, alpha=outlier_alpha)
                    ax.add_patch(rect)
            else:
                w = (Upper - Lower) / n_bins
            
            # hist
            bar_width = (center[1]-center[0])*0.6
            bins = [w * i for i in range(n_bins + 1)]
            Bin = []
            for k in range(n_bins):
                s = 0
                for j in data:
                    if j >= bins[k] and j < bins[k + 1]:
                        s += 1
                Bin.append(s)
            M = max(Bin)
            Mb = bar_width/M
            for c in range(len(Bin)):
                rect = mpathes.Rectangle((center[i], bins[c] + Lower), Bin[c]*Mb , w,
                                         ec=bin_edgecolor, fc=bin_facecolor, alpha=hist_alpha)
                ax.add_patch(rect)

            # whisker
            ax.hlines(Upper, center[i] - 0.1 * center[0], center[i], whisker_edgecolor)
            ax.hlines(Lower, center[i] - 0.1 * center[0], center[i], whisker_edgecolor)
            ax.vlines(center[i], Lower, d[0], whisker_edgecolor)
            ax.vlines(center[i], d[-1], Upper, whisker_edgecolor)

            # median
            ax.hlines(d[5], center[i] - 0.2 * center[0], center[i], median_edgecolor, lw=3)

            # box
            rect = mpathes.Rectangle((center[i] - 0.2 * center[0], d[0]), 0.2 * center[0], d[-1] - d[0],
                                     ec=box_edgecolor, fc=box_facecolor, alpha=box_alpha)
            ax.add_patch(rect)
            i += 1
        plt.show()

    def creative_boxplot(ax,
                         Data,
                         outlier=True,
                         box_facecolor='white',
                         box_edgecolor='k',
                         outlier_facecolor='b',
                         outlier_edgecolor=None,
                         whisker_edgecolor='k',
                         median_edgecolor='k',
                         box_alpha=1.0,
                         outlier_alpha=1.0,
                         point_alpha=0.3):
        h = max(max(p) for p in Data) + 0.1 * abs(max(max(p) for p in Data))
        l = min(min(p) for p in Data) + 0.1 * abs(min(min(p) for p in Data))
        count = len(Data)
        a = (h - l) / 2000
        if outlier == True:
            center = [round(((h - l) / (count + 1)) * (x + 1), 8) for x in range(count)]
            lw_l = 0.0001 * h
        else:
            center = [round(((h - l) / (count + 1)) * (x + 1), 8) / a for x in range(count)]
            lw_l = 0.005 * h
        print(center)
        ax.axis('equal')
        i = 0
        point = []
        for data in Data:
            data = sorted(data)
            # percentile
            p = [0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75]
            pen = [round((len(data) + 1) * x, 2) for x in p]
            d = [np.quantile(data, j) for j in p]

            # outlier
            IQR = d[-1] - d[0]
            upper = d[-1] + 1.5 * IQR
            lower = d[0] - 1.5 * IQR
            Upper = min(upper, data[-1])
            Lower = max(lower, data[0])
            outliers = []
            for p in data:
                if p > upper or p < lower:
                    outliers.append(p)
            if outlier == True:
                for p in outliers:
                    rect = mpathes.Ellipse((center[i], p), 0.04 * center[-1], 0.04 * center[-1],
                                           ec=outlier_edgecolor, fc=outlier_facecolor, alpha=outlier_alpha)
                    rect.set_alpha(0.7)
                    ax.add_patch(rect)
            # box
            rect = mpathes.Rectangle((center[i] - 0.2 * center[0], d[0]), 0.4 * center[0], d[-1] - d[0],
                                     ec=box_edgecolor, fc=box_facecolor, alpha=box_alpha)
            ax.add_patch(rect)

            # points
            for p in data:
                if p not in outliers:
                    x = center[i] - 0.05 * center[0] + random.uniform(0, 0.1 * center[0])
                    rect = mpathes.Ellipse((x, p), 0.01 * center[0], 0.01 * center[0], ec=outlier_edgecolor,
                                           fc=outlier_facecolor)
                    rect.set_alpha(point_alpha)
                    ax.add_patch(rect)

            # median
            ax.hlines(d[5], center[i] - 0.2 * center[0], center[i] + 0.2 * center[0], median_edgecolor, lw=3)
            
            # line
            point.append([center[i], d[5]])
            i += 1

        for i in range(len(point) - 1):
            x = point[i][0]
            y = point[i][1]
            arrow = mpathes.FancyArrowPatch((point[i][0], point[i][1]), (point[i + 1][0], point[i + 1][1]),
                                            arrowstyle='-', lw=lw_l, color='g')
            ax.add_patch(arrow)
        plt.show()