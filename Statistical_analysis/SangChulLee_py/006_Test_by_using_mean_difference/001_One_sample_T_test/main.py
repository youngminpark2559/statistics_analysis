# conda activate py36gputorch100 && \
# cd /mnt/1T-5e7/mycodehtml/statistics_analysis/Statistical_analysis/SangChulLee_py/006_Test_by_using_mean_difference/001_One_sample_T_test && \
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
# /home/young/Pictures/2019_07_13_22:32:39.png

# ================================================================================
# /home/young/Pictures/2019_07_13_22:33:31.png

# ================================================================================
# /home/young/Pictures/2019_07_13_22:34:07.png

# ================================================================================
# /home/young/Pictures/2019_07_13_22:34:26.png

# ================================================================================
# null hypothesis
# B_store_icecream_pint=320

# complaint: it's not 320g

# analysis_result=inspect(samples)

# analysis_result[weight]>320?

# ================================================================================
# c mu_0: null hypothesis
mu_0=320

# c n: number of sample
n=100

# sample_weights=

rand_num=np.random.uniform(280.5,330.5,size=n)
# print("rand_num",rand_num)
# [294.93885527 292.2874684  306.18961425 329.49364321 304.97933284
#  329.41743477 322.63301281 285.24224825 280.73207103 286.82748719

sample_mean=np.array(rand_num).mean()
# print("sample_mean",sample_mean)
# 305.810340097144

# ================================================================================
var_value=np.array(rand_num).var()
# 204.26635798691711

std_value=np.sqrt(var_value)
# print("std_value",std_value)
# 15.206624758178286

standard_error=var_value/np.sqrt(n)
# print("standard_error",standard_error)
# 18.447914389486588


# ================================================================================


f_x











