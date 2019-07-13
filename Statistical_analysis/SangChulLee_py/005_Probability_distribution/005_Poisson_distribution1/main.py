# conda activate py36gputorch100 && \
# cd /mnt/1T-5e7/mycodehtml/statistics_analysis/Statistical_analysis/SangChulLee_py/005_Probability_distribution/005_Poisson_distribution1 && \
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
from scipy.stats import binom

# ================================================================================
# https://raw.githubusercontent.com/youngminpark2559/statistics_analysis/master/Statistical_analysis/SangChulLee_py/005_Probability_distribution/005_Poisson_distribution1/pics/2019_07_13_21:26:48.png

# https://raw.githubusercontent.com/youngminpark2559/statistics_analysis/master/Statistical_analysis/SangChulLee_py/005_Probability_distribution/005_Poisson_distribution1/pics/2019_07_13_21:30:33.png

# https://raw.githubusercontent.com/youngminpark2559/statistics_analysis/master/Statistical_analysis/SangChulLee_py/005_Probability_distribution/005_Poisson_distribution1/pics/2019_07_13_21:31:06.png

