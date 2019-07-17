# conda activate py36gputorch100 && \
# cd /mnt/1T-5e7/mycodehtml/statistics_analysis/Statistical_analysis/KyungSubNoh_py/006_Estimation/003_Decide_number_of_sample_data && \
# rm e.l && python main.py \
# 2>&1 | tee -a e.l && code e.l

# ================================================================================
import numpy as np

# ================================================================================
# Large sample data: good, credibility increases

# $$$\bar{X} \pm z_{\frac{\alpha}{2}} \times \text{standard error} \\ $$$
# $$$= \bar{X} \pm z_{\frac{\alpha}{2}} \times \frac{\sigma}{\sqrt{n}}$$$

# ================================================================================
# Simpify above one wrt n

# ================================================================================
# c n: proper size of sample from the population
# $$$ n = \dfrac{z_{\frac{\alpha}{2} \times \sigma}}{d} $$$
# $$$ n = \left \dfrac{z_{\frac{\alpha}{2} \times \sigma}}{d} \right^2 $$$
# d: allowed error

# ================================================================================
# <./pics/2019_07_16_19:16:53.png>

# confidence: 99%
z=2.58

# allowed error += 100ml
d=100

# population_std: 150ml
population_std=150

def calculate_proper_sample_size(z,population_std,d):
  num_sample_data=(z*population_std/d)**2
  return num_sample_data

num_sample_data=calculate_proper_sample_size(z=z,population_std=population_std,d=d)
# print("num_sample_data",num_sample_data)
# 14.9769

# ================================================================================
# confidence: 99%
z_half_alpha=2.58

d=100

# When you don't know population std, you extract 10 number of samples to calculate sample_std
sample_std=170

num_sample_data=calculate_proper_sample_size(z=z_half_alpha,population_std=sample_std,d=d)
# print("num_sample_data",num_sample_data)
# 19.236996

# ================================================================================
