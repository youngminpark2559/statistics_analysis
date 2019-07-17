# conda activate py36gputorch100 && \
# cd /mnt/1T-5e7/mycodehtml/statistics_analysis/Statistical_analysis/KyungSubNoh_py/007_Testing_hypothesis/002_1_Test_hypothesis_on_mean_of_population_when_you_know_population_variance && \
# rm e.l && python main.py \
# 2>&1 | tee -a e.l && code e.l

# ================================================================================
import numpy as np

# ================================================================================
# <./pics/2019_07_16_20:42:28.png>

# <./pics/2019_07_16_20:43:58.png>

# <./pics/2019_07_16_20:45:03.png>

# <./pics/2019_07_16_20:45:20.png>

# ================================================================================
# null hypothesis: 
mu=300

# research hypothesis: mu<300
p_value=0.05

# -z_{0.05}=-1.64 (so, if -z<-1.64, H_0 is rejected)
number_of_sample=300

sample_mean=244.65

sample_std=20

# ================================================================================
def calculate_z_for_left_testing_hypothesis(sample_mean,mu,sample_std,number_of_sample):
  z=(sample_mean-mu)/(sample_std/np.sqrt(number_of_sample))
  return z

# ================================================================================
z_value=calculate_z_for_left_testing_hypothesis(
  sample_mean=sample_mean,mu=mu,sample_std=sample_std,number_of_sample=number_of_sample)
# print("z_value",z_value)
# -47.93450609946868

# -47.93450609946868<-1.64
# True

# H_0 is rejected

# ================================================================================
