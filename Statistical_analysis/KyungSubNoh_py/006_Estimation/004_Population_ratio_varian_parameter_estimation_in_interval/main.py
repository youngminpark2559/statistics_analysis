# conda activate py36gputorch100 && \
# cd /mnt/1T-5e7/mycodehtml/statistics_analysis/Statistical_analysis/KyungSubNoh_py/006_Estimation/004_Population_ratio_varian_parameter_estimation_in_interval && \
# rm e.l && python main.py \
# 2>&1 | tee -a e.l && code e.l

# ================================================================================
import numpy as np

# ================================================================================
# /home/young/Pictures/2019_07_16_19:36:35.png

# ================================================================================
# Population ratio: 
# credibility interval about sample ratio $$$\hat{p}$$$

# sample ratio $$$\hat{p}$$$
# when you extract sample data
# ratio of $$$\frac{t}{n}$$$
# $$$\dfrac{specific event}{number of sample}$$$

# ================================================================================
def calculate_population_ratio(hat_p,z_half_alpha,number_of_sample):
  lower_bound=hat_p-z_half_alpha*np.sqrt(hat_p*(1-hat_p)/number_of_sample)
  upper_bound=hat_p+z_half_alpha*np.sqrt(hat_p*(1-hat_p)/number_of_sample)
  return lower_bound,upper_bound

# ================================================================================
# /home/young/Pictures/2019_07_16_19:41:17.png

number_of_gas_stations=77
# c number_of_bad_gas_statations: number of gas stations which showed bad amount of oil
number_of_bad_gas_statations=5

z_half_alpha=1.96

hat_p=number_of_bad_gas_statations/number_of_gas_stations
# print("hat_p",hat_p)
# 0.06493506493506493

# ================================================================================
lower,upper=calculate_population_ratio(hat_p=hat_p,z_half_alpha=z_half_alpha,number_of_sample=number_of_gas_stations)
# print("lower",lower)
# 0.009895976304936237
# print("upper",upper)
# 0.11997415356519361

# ================================================================================
# /home/young/Pictures/2019_07_16_19:49:06.png

def number_of_sample_for_estimating_population_ratio(hat_p,z_half_alpha,d):
  sample_number=hat_p*(1-hat_p)*(z_half_alpha/d)**2
  return sample_number

# ================================================================================
# /home/young/Pictures/2019_07_16_19:50:46.png

z_half_alpha=1.96
hat_p=0.95
d=0.05

num_sample_size=number_of_sample_for_estimating_population_ratio(hat_p=hat_p,z_half_alpha=z_half_alpha,d=d)
# print("num_sample_size",num_sample_size)
# 72.99040000000005

# ================================================================================
# /home/young/Pictures/2019_07_16_19:53:08.png

# /home/young/Pictures/2019_07_16_19:53:51.png

# /home/young/Pictures/2019_07_16_19:54:01.png

# ================================================================================
# /home/young/Pictures/2019_07_16_19:55:36.png

