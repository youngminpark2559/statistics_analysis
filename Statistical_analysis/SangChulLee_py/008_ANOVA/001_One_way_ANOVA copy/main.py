# conda activate py36gputorch100 && \
# cd /mnt/1T-5e7/mycodehtml/statistics_analysis/Statistical_analysis/SangChulLee_py/008_ANOVA/001_One_way_ANOVA && \
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
# K companies run 4 cafes (A region, B region, C region, D region)

# Satisfaction of each cafes has different values?

# If difference happens, which cafe has lowest satisfaction?

# ================================================================================
# H_0:
# there is no satisfaction difference in 4 cafes
# $$$H_0:\mu_1=\mu_2=\mu_3=\mu_4$$$

# H_1:
# there is at least one pair of difference from 4 cafes
# $$$H_1: \mu_1 \ne \mu_2 \;\;\; or \mu_1 \ne \mu_3 \;\;\; ... \;\;\; \mu_3 \ne \mu_4$$$

# ================================================================================
# https://raw.githubusercontent.com/youngminpark2559/statistics_analysis/master/Statistical_analysis/SangChulLee_py/008_ANOVA/001_One_way_ANOVA/pics/2019_07_14_16:13:10.png

# ================================================================================
# https://raw.githubusercontent.com/youngminpark2559/statistics_analysis/master/Statistical_analysis/SangChulLee_py/008_ANOVA/001_One_way_ANOVA/pics/2019_07_14_16:22:32.png
