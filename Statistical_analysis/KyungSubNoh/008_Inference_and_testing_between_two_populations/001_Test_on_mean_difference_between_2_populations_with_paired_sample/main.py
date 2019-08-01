# conda activate py36gputorch100 && \
# cd /mnt/1T-5e7/mycodehtml/statistics_analysis/Statistical_analysis/KyungSubNoh_py/008_Inference_and_testing_between_two_populations/001_Test_on_mean_difference_between_2_populations_with_paired_sample && \
# rm e.l && python main.py \
# 2>&1 | tee -a e.l && code e.l

# ================================================================================
import numpy as np
import pandas as pd

# ================================================================================
# 2 populations
# 2 sample data

# 1. check up mean different

# ================================================================================
# /home/young/Pictures/2019_07_18_11:18:37.png

# ================================================================================
# /home/young/Pictures/2019_07_18_11:20:09.png

# ================================================================================
# /home/young/Pictures/2019_07_18_11:21:25.png

# ================================================================================
# /home/young/Pictures/2019_07_18_11:23:39.png

# ================================================================================
id=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
before=[75,74,75,75,83,77,82,62,77,82,72,75,78,71,68,76,71,54,75,77,82,74,76,70,77,82,62,77,82,68]
after=[73,74,76,71,76,68,75,61,68,75,70,71,71,70,67,73,74,50,76,68,75,74,73,69,68,75,61,68,75,67]
num_of_people=len(id)

d={'id':id,
   'before':before,
   'after':after}
weight_before_after_df=pd.DataFrame(d)
# print("weight_before_after_df",weight_before_after_df)
#     id  before  after
# 0    1      75     73
# 1    2      74     74
# 2    3      75     76

# ================================================================================
d_x_bar=np.sum(weight_before_after_df["before"]-weight_before_after_df["after"])/num_of_people
# print("d_x_bar",d_x_bar)
# 3.9

# ================================================================================
difference_weight=weight_before_after_df["before"]-weight_before_after_df["after"]
variance_of_d_x=np.sum(np.power(difference_weight-d_x_bar,2))/(num_of_people-1)
print("variance_of_d_x",variance_of_d_x)
# 13.196551724137935

# ================================================================================
std_of_d_x=np.sqrt(variance_of_d_x)
# print("std_of_d_x",std_of_d_x)
# 3.6327058405736534

# ================================================================================
# Standard error

std_err_of_d_x_bar=std_of_d_x/np.sqrt(num_of_people)
# print("std_err_of_d_x_bar",std_err_of_d_x_bar)
# 0.6632383112209852

# ================================================================================
# /home/young/Pictures/2019_07_18_11:41:11.png

# ================================================================================
# /home/young/Pictures/2019_07_18_11:41:57.png

# ================================================================================
# /home/young/Pictures/2019_07_18_11:42:36.png

# ================================================================================
# /home/young/Pictures/2019_07_18_11:44:43.png

# ================================================================================
# /home/young/Pictures/2019_07_18_11:45:55.png

