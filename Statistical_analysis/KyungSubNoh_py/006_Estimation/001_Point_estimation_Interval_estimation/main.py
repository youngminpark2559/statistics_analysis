# conda activate py36gputorch100 && \
# cd /mnt/1T-5e7/mycodehtml/statistics_analysis/Statistical_analysis/KyungSubNoh_py/006_Estimation/001_Point_estimation_Interval_estimation && \
# rm e.l && python main.py \
# 2>&1 | tee -a e.l && code e.l

# ================================================================================
import numpy as np

# ================================================================================
# Point estimation
# Express estimated parameter of population in specific numerical value

# Time for going to school: 30 min

# ================================================================================
# Interval estimation
# Express estimated parameter of population in min-max range

# Time for going to school: 25-35 min

# ================================================================================
# Estimate

# Estimator

# ================================================================================
# /home/young/Pictures/2019_07_16_16:22:07.png

# ================================================================================
# /home/young/Pictures/2019_07_16_16:26:28.png

# Interval estimation = credibility score + min&max estimated parameter interval
# "95% credibility score" + "45% +-3%"

# ================================================================================
# /home/young/Pictures/2019_07_16_16:29:20.png

# ================================================================================
# /home/young/Pictures/2019_07_16_16:29:50.png

# English test
# mean=500
# standard_error=100

# in credibility 90%, estimate mean parameter (as interval) of population
# in credibility 95%, estimate mean parameter (as interval) of population
# in credibility 99%, estimate mean parameter (as interval) of population

# ================================================================================
def calculate_estimated_mean_interval(X_bar,standard_error,z):
  lower_bound=X_bar-z*standard_error
  upper_bound=X_bar+z*standard_error
  return lower_bound,upper_bound

# ================================================================================
# in credibility 90% (z=1.64), estimate mean parameter (as interval) of population

lower_bound_90,upper_bound_90=calculate_estimated_mean_interval(X_bar=500,standard_error=100,z=1.64)
# print("lower_bound_90",lower_bound_90)
# 336.0
# print("upper_bound_90",upper_bound_90)
# 664.0

# ================================================================================
# in credibility 95% (z=1.96), estimate mean parameter (as interval) of population

lower_bound_95,upper_bound_95=calculate_estimated_mean_interval(X_bar=500,standard_error=100,z=1.96)
# print("lower_bound_95",lower_bound_95)
# 304.0
# print("upper_bound_95",upper_bound_95)
# 696.0

# ================================================================================
# in credibility 99% (z=2.58), estimate mean parameter (as interval) of population

lower_bound_99,upper_bound_99=calculate_estimated_mean_interval(X_bar=500,standard_error=100,z=2.58)
# print("lower_bound_99",lower_bound_99)
# 242.0
# print("upper_bound_99",upper_bound_99)
# 758.0

# ================================================================================
# /home/young/Pictures/2019_07_16_16:38:16.png

# ================================================================================
