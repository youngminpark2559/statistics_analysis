# conda activate py36gputorch100 && \
# cd /mnt/1T-5e7/mycodehtml/statistics_analysis/Statistical_analysis/KyungSubNoh_py/007_Testing_hypothesis/002_3_Test_hypothesis_on_mean_of_population_by_using_p_value && \
# rm e.l && python main.py \
# 2>&1 | tee -a e.l && code e.l

# ================================================================================
import numpy as np

# ================================================================================
# <./pics/2019_07_16_21:52:23.png>

# So far, to reject or adopt the null hypothesis,
# you saw test_statistic_value_t < p_value
# If it's true, null hypothesis is rejected

# ================================================================================
# <./pics/2019_07_16_21:58:54.png>

# ================================================================================
# <./pics/2019_07_16_21:59:41.png>

# ================================================================================
# <./pics/2019_07_16_21:59:55.png>

# ================================================================================
# H_0: mu=300
# H_1: mu<300

population_mean=300
number_of_sample=300
sample_mean=294.65
sample_std=45
p_value=0.05

def calculate_test_statistic_value(sample_mean,population_mean,sample_std,number_of_sample):
  z_val=(sample_mean-population_mean)/(sample_std-np.sqrt(number_of_sample))
  return z_val

z_val=calculate_test_statistic_value(
  sample_mean=sample_mean,population_mean=population_mean,sample_std=sample_std,number_of_sample=number_of_sample)
# print("z_val",z_val)
# -0.19328389461155732

# p=p(z<-2.059)
#  =0.5-p(0<=z<=2.059)
#  =0.5-p(0<=z<=2.06)
#  =0.5-0.48=0.02

# <./pics/2019_07_16_22:06:42.png>

# ================================================================================
