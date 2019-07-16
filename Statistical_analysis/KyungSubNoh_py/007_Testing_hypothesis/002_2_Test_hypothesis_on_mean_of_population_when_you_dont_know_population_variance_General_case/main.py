# conda activate py36gputorch100 && \
# cd /mnt/1T-5e7/mycodehtml/statistics_analysis/Statistical_analysis/KyungSubNoh_py/007_Testing_hypothesis/002_2_Test_hypothesis_on_mean_of_population_when_you_dont_know_population_variance_General_case && \
# rm e.l && python main.py \
# 2>&1 | tee -a e.l && code e.l

# ================================================================================
import numpy as np

# ================================================================================
# /home/young/Pictures/2019_07_16_21:33:36.png

# /home/young/Pictures/2019_07_16_21:34:05.png

# /home/young/Pictures/2019_07_16_21:34:46.png

# ================================================================================
# /home/young/Pictures/2019_07_16_21:35:02.png

def calculate_test_statistic_value_t(sample_mean,population_mean,sample_std,number_of_sample):
  test_statistic_value_t=(sample_mean-population_mean)/(sample_std/np.sqrt(number_of_sample))
  return test_statistic_value_t

number_of_sample=15

test_statistic_value_t=calculate_test_statistic_value_t(sample_mean=302.1,population_mean=300,sample_std=14.54,number_of_sample=15)
# print("test_statistic_value_t",test_statistic_value_t)
# 0.5593717350093305

DOF=number_of_sample-1

p_value=0.05

# /home/young/Pictures/2019_07_16_21:40:18.png
