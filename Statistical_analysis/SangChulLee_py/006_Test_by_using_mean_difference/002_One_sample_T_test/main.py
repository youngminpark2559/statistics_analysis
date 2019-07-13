# conda activate py36gputorch100 && \
# cd /mnt/1T-5e7/mycodehtml/statistics_analysis/Statistical_analysis/SangChulLee_py/006_Test_by_using_mean_difference/002_One_sample_T_test && \
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
import random

# ================================================================================
# /home/young/Pictures/2019_07_14_07:39:41.png

# Most cases use "two-sided test"
# equal or not equal

# /home/young/Pictures/2019_07_14_07:41:32.png

# Probability of H_0 is true is tested by using "two-sided test"

# ================================================================================
# Some cases should have to see "greater or less"
# Then, you can use "right-sided test" or "left-sided test"

# /home/young/Pictures/2019_07_14_07:43:12.png

# /home/young/Pictures/2019_07_14_07:42:47.png

# ================================================================================
OST_df=pd.read_csv('./Data/01.OST.csv',encoding='utf8')
# print("OST_df",OST_df)
#      weight
# 0  319.3148
# 1  241.9693
# 2  290.9807
# 3  276.0801
# 4  347.5499
# 5  298.8435
# 6  292.8708
# 7  303.5787
# 8  296.1497

# ================================================================================


