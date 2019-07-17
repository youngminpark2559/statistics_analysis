# conda activate py36gputorch100 && \
# cd /mnt/1T-5e7/mycodehtml/statistics_analysis/Statistical_analysis/KyungSubNoh_py/006_Estimation/003_Decide_number_of_sample_data && \
# rm e.l && python main.py \
# 2>&1 | tee -a e.l && code e.l

# ================================================================================
import numpy as np

# ================================================================================
# Large sample data: good, credibility increases

# $$$\bar{X} +- z_{\frac{\alpha}{2}} * standard error \\ $$$
# $$$= \bar{X} +- z_{\frac{\alpha}{2}} * \frac{\sigma}{\sqrt{n}}$$$

# $$$ n = \dfrac{z_{\frac{\alpha}{2} * \sigma}}{d} $$$
# d: allowed error

# ================================================================================
# ./pics/2019_07_16_19:16:53.png

# credibility=0.99
z=2.58
# allowed error
d=100
population_std=150

def calculate_number_of_sample_data(z,population_std,d):
  num_sample_data=(z*population_std/d)**2
  return num_sample_data

num_sample_data=calculate_number_of_sample_data(z=z,population_std=population_std,d=d)
# print("num_sample_data",num_sample_data)
# 14.9769

# ================================================================================
# credibility: 99%
z_half_alpha=2.58
d=100
sample_std=170

num_sample_data=calculate_number_of_sample_data(z=z_half_alpha,population_std=sample_std,d=d)
# print("num_sample_data",num_sample_data)
# 19.236996

# ================================================================================
