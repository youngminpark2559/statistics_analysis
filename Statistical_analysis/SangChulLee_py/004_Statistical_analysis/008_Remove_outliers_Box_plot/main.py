# conda activate py36gputorch100 && \
# cd /mnt/1T-5e7/mycodehtml/statistics_analysis/Statistical_analysis/SangChulLee_py/004_Statistical_analysis/008_Remove_outliers_Box_plot && \
# rm e.l && python main.py \
# 2>&1 | tee -a e.l && code e.l

# ================================================================================
import pandas as pd
pd.set_option('display.max_colwidth', -1)
pd.set_option('display.max_columns',None)
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
from statsmodels.robust.scale import mad

# ================================================================================
# Ideal case
# /home/young/Pictures/2019_07_13_18:01:02.png

# ================================================================================
# Too low variance

# /home/young/Pictures/2019_07_13_18:02:21.png
# /home/young/Pictures/2019_07_13_18:02:43.png

# ================================================================================
# /home/young/Pictures/2019_07_13_18:03:13.png

# ================================================================================
weight_df=pd.read_csv("./Data/0401.wgt.csv",encoding='utf8')
# print("weight_df",weight_df)

# ================================================================================
weight_vals=weight_df["weight"]
sex_vals=weight_df["sex"]

# ================================================================================
# Basic box plot

fig,axes0=plt.subplots()

axes0.boxplot([weight_vals,sex_vals],sym="bo")

plt.title('Box plot of weight')
plt.xticks([1,2], ['weight','sex'])
plt.show()
# /home/young/Pictures/2019_07_13_18:11:38.png

# ================================================================================
fig,axes_for_hist_with_outlier=plt.subplots()
n,bins,patches=axes_for_hist_with_outlier.hist(weight_vals,bins=50)

plt.title("Histogram of weight data with outlier")
plt.xlabel("Weight value")
plt.ylabel("Number of people")
plt.show()
# /home/young/Pictures/2019_07_13_18:28:42.png

# ================================================================================
# Remove data where weight>75

removed_outlier_df=weight_df[~(weight_df["weight"]>75)]
print(removed_outlier_df)
#     id  weight  sex
# 0   1   40      2  
# 1   2   50      2  
# 2   3   56      1  
# 3   4   51      2  
# 4   5   55      1  
# 5   6   61      1  
# 7   8   44      2  
# 8   9   66      1  
# 9   10  60      1  
# 10  11  39      2  

# ================================================================================
fig,axes0=plt.subplots()

axes0.boxplot([removed_outlier_df["weight"],removed_outlier_df["sex"]],sym="bo")

plt.title('Box plot of weight')
plt.xticks([1,2], ['weight','sex'])
plt.show()
# /home/young/Pictures/2019_07_13_18:22:55.png

# ================================================================================
fig,axes_for_hist_with_outlier=plt.subplots()
n,bins,patches=axes_for_hist_with_outlier.hist(removed_outlier_df["weight"],bins=50)

plt.title("Histogram of weight data without outlier")
plt.xlabel("Weight value")
plt.ylabel("Number of people")
plt.show()
# /home/young/Pictures/2019_07_13_18:29:33.png

# ================================================================================
