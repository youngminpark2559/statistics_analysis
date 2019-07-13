# conda activate py36gputorch100 && \
# cd /mnt/1T-5e7/mycodehtml/statistics_analysis/Statistical_analysis/SangChulLee_py/004_Statistical_analysis/002_Geometric_mean && \
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
# /home/young/Pictures/2019_07_13_15:31:20.png

# ================================================================================
anual_salary=[250,3200,3700,4500,4800]
year=[2010,2011,2012,2013,2014]

mulplied=1
for one_salary in anual_salary:
  mulplied=mulplied*one_salary

# print("mulplied",mulplied)
# 63936000000000000

# ================================================================================
def nth_root_of_m(a,n):
    return pow(a,(1/n))

a=mulplied
n=len(year)
q=round(nth_root_of_m(a,n),3)
print(q)
# 2296.937

# ================================================================================
