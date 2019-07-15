# conda activate py36gputorch100 && \
# cd /mnt/1T-5e7/mycodehtml/statistics_analysis/Statistical_analysis/SangChulLee_py/008_ANOVA/007_Two_way_ANOVA && \
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
import scipy as sp

# ================================================================================
# 2 factors for good taste chicken
# temperature of oil
# frying time 

# 2 factors really affect good taste?

# So, you should perform test

# Frying temp: 1000, 1500
# Frying time: 10min, 20min

# Temp and time are really important factors to the taste?

# There is interaction between temp and time?

# ================================================================================
# https://raw.githubusercontent.com/youngminpark2559/statistics_analysis/master/Statistical_analysis/SangChulLee_py/008_ANOVA/007_Two_way_ANOVA/pics/2019_07_14_21:50:31.png

# ================================================================================
# https://raw.githubusercontent.com/youngminpark2559/statistics_analysis/master/Statistical_analysis/SangChulLee_py/008_ANOVA/007_Two_way_ANOVA/pics/2019_07_14_21:50:47.png

# ================================================================================
# https://raw.githubusercontent.com/youngminpark2559/statistics_analysis/master/Statistical_analysis/SangChulLee_py/008_ANOVA/007_Two_way_ANOVA/pics/2019_07_14_21:51:38.png
