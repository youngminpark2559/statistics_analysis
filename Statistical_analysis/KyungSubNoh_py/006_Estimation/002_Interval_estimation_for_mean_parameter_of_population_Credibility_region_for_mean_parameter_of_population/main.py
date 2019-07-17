# conda activate py36gputorch100 && \
# cd /mnt/1T-5e7/mycodehtml/statistics_analysis/Statistical_analysis/KyungSubNoh_py/006_Estimation/002_Interval_estimation_for_mean_parameter_of_population_Credibility_region_for_mean_parameter_of_population && \
# rm e.l && python main.py \
# 2>&1 | tee -a e.l && code e.l

# ================================================================================
import numpy as np

# ================================================================================
# Estimate population's mean parameter in interval

# 1. When you know std parameter of population
# ./pics/2019_07_16_16:43:21.png

# ================================================================================
# ./pics/2019_07_16_16:45:58.png

# A company
# Estimate mean lifespan of bulb of population

# Extract 200 number of bulbs
# sample_mean_lifespan=30000 hours
# population_std=500 hours

# Estimate mean parameters with 95% credibility (z=1.96)

# ================================================================================
def estimate_population_mean_parameter_interval(X_bar,z,population_std,number_of_sample_points):
  lower_bound=X_bar-z*population_std/np.sqrt(number_of_sample_points)
  uppper_bound=X_bar+z*population_std/np.sqrt(number_of_sample_points)
  return lower_bound,uppper_bound

# ================================================================================
lower_bound,uppper_bound=estimate_population_mean_parameter_interval(X_bar=30000,z=1.96,population_std=500,number_of_sample_points=200)
# print("lower_bound",lower_bound)
# 29930.703535443718
# print("uppper_bound",uppper_bound)
# 30069.296464556282

# ================================================================================
# ./pics/2019_07_16_16:58:30.png

# ================================================================================
# Estimate population's mean parameter in interval

# 1. When you don't know std parameter of population (general case)
# Use sample data's std

# Since you don't know population's std, credibility range becomes large

# And you use t distribution (when you don't know population's parameters) than z distribution

# ./pics/2019_07_16_17:01:47.png

# ================================================================================
# ./pics/2019_07_16_17:02:15.png

# 12 number students' height values

# with 95% credibility, estimate population's mean parameter in interval

# ================================================================================
heights=[168,160,170,162,168,163,164,167,175,179,161,155]

number_of_sample_points=len(heights)

sample_data_mean=np.mean(heights)
# print("sample_data_mean",sample_data_mean)
# 166.0

# ================================================================================
subtracted=heights-sample_data_mean
# print("subtracted",subtracted)
# [  2.  -6.   4.  -4.   2.  -3.  -2.   1.   9.  13.  -5. -11.]

powered_by_2=np.power(subtracted,2)
# print("powered_by_2",powered_by_2)
# [  4.  36.  16.  16.   4.   9.   4.   1.  81. 169.  25. 121.]

summed=np.sum(powered_by_2)

divided=summed/(12-1)

sample_data_std=np.sqrt(divided)
# print("sqrted",sqrted)
# 6.646940512883967

# ================================================================================
standard_error=sample_data_std/np.sqrt(12)
# print("standard_error",standard_error)
# 1.918806447200494

# ================================================================================
degree_of_freedom=12-1

# ================================================================================
# 95%
# t_half_alpha=2.201
t_half_alpha=2.221

def estimate_population_mean_parameter_in_interval(sample_data_mean,t_half_alpha,sample_data_std,number_of_sample_points):
  lower_bound=sample_data_mean-t_half_alpha*(sample_data_std/number_of_sample_points)
  upper_bound=sample_data_mean+t_half_alpha*(sample_data_std/number_of_sample_points)
  return lower_bound,upper_bound

lower_bound,upper_bound=estimate_population_mean_parameter_in_interval(
  sample_data_mean=sample_data_mean,t_half_alpha=t_half_alpha,
  sample_data_std=sample_data_std,number_of_sample_points=number_of_sample_points)
print("lower_bound",lower_bound)
# 164.7808403275952
print("upper_bound",upper_bound)
# 167.2191596724048

# ================================================================================
