# conda activate py36gputorch100 && \
# cd /mnt/1T-5e7/mycodehtml/statistics_analysis/Statistical_analysis/KyungSubNoh_py/008_Inference_and_testing_between_two_populations/002_003_Test_on_mean_difference_between_2_populations_with_Case3 && \
# rm e.l && python main.py \
# 2>&1 | tee -a e.l && code e.l

# ================================================================================
import numpy as np
import pandas as pd

# ================================================================================
# - Not enough sample
# - Sample populations' variance

# Required assumption
# - 2 populations should be normal distribution or similar normal distribution

# $$$\mathcal{N}(\mu_A,\sigma_A^2)$$$
# $$$\mathcal{N}(\mu_B,\sigma_B^2)$$$

# $$$\sigma_A^2=\sigma_B^2=\sigma^2$$$

# $$$s_A^2=s_B^2=s^2$$$

# ================================================================================
# Pooled variance estimator

# - Populations
# - They are independent
# - Unbiased estimator of comman variance

# ================================================================================
# /home/young/Pictures/2019_07_18_12:42:33.png

# ================================================================================
# /home/young/Pictures/2019_07_18_12:43:56.png

# ================================================================================
# /home/young/Pictures/2019_07_18_12:45:19.png

# ================================================================================
# /home/young/Pictures/2019_07_18_12:51:19.png

# ================================================================================
# /home/young/Pictures/2019_07_18_12:57:03.png

/mnt/1T-5e7/mycodehtml/statistics_analysis/Statistical_analysis/KyungSubNoh_py/008_Inference_and_testing_between_two_populations/002_003_Test_on_mean_difference_between_2_populations_with_Case3/main.py
