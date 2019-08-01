# conda activate py36gputorch100 && \
# cd /mnt/1T-5e7/mycodehtml/statistics_analysis/Statistical_analysis/KyungSubNoh_py/008_Inference_and_testing_between_two_populations/002_004_Example && \
# rm e.l && python main.py \
# 2>&1 | tee -a e.l && code e.l

# ================================================================================
import numpy as np
import pandas as pd

# ================================================================================
id=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
A_company=[18,16,17,15,14,19,16,15,18,15,16,17,15,14,19,12,16,18,15,17]
B_company=[16,15,16,14,15,18,13,15,12,17,15,16,18,12,14,15,16,15,15,17]

d={'id':id,
   'A_company':A_company,
   'B_company':B_company}
companies_batter_time_df=pd.DataFrame(d)
# print("companies_batter_time_df",companies_batter_time_df)
#     id  A_company  B_company
# 0    1         18         16
# 1    2         16         15
# 2    3         17         16
# 3    4         15         14
# 4    5         14         15

# ================================================================================


