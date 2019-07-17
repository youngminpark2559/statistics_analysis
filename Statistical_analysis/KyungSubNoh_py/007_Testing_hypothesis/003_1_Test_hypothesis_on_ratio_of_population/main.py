# conda activate py36gputorch100 && \
# cd /mnt/1T-5e7/mycodehtml/statistics_analysis/Statistical_analysis/KyungSubNoh_py/007_Testing_hypothesis/003_1_Test_hypothesis_on_ratio_of_population && \
# rm e.l && python main.py \
# 2>&1 | tee -a e.l && code e.l

# ================================================================================
import numpy as np

# ================================================================================
# ./pics/2019_07_16_22:23:00.png

# ./pics/2019_07_16_22:23:34.png

# ================================================================================
# H_0: p=0.8
# H_1: p<0.8

n=100
p=0.8
p_hat=0.81
p_value=0.05

def calculate_z(p_hat,p_0,n):
  z_val=(p_hat-p_0)/np.sqrt(p_0*(1-p_0)/n)
  return z_val

z_val=calculate_z(p_hat=p_hat,p_0=p,n=n)
# print("z_val",z_val)
# 0.2500000000000002

# ================================================================================
# ./pics/2019_07_16_22:28:26.png

# ================================================================================

