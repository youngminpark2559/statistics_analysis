# ================================================================================
# Estimate "population's mean parameter in interval"

# 1. When you know "std parameter of population" (rare case)
# <./pics/2019_07_16_16:43:21.png>

# ================================================================================
# Example
# <./pics/2019_07_16_16:45:58.png>

# A_company
# Estimate "mean lifespan of bulb" of population set

# Extract 200 number of bulbs
# sample_mean_lifespan=30000 hours
# population_std=500 hours

# Estimate mean parameters interval with 95% confidence (z=1.96)

# ================================================================================
# Calculation

# /home/young/Pictures/2019_07_22_08:09:25.png

# ================================================================================
# Standard deviation vs standard error
# <./pics/2019_07_16_16:58:30.png>

# $$$ \text{std} = \sqrt{\text{variance}}$$$

# standard error:
# $$$\dfrac{\text{std from sample}}{\sqrt{n}}$$$

# ================================================================================
# Estimate population's mean parameter in interval

# 2. When you don't know std parameter of population (general case)
# Use sample data's std

# Since you don't know population's std, confidence interval becomes large

# And you use t distribution (when you don't know population's parameters) than z distribution

# <./pics/2019_07_16_17:01:47.png>

# ================================================================================
# Example student heights
# <./pics/2019_07_16_17:02:15.png>

# 12 number students' height values

# with 95% confidence, estimate population's mean parameter in interval

# ================================================================================
# Calculation

# Sample mean and sample std
# /home/young/Pictures/2019_07_22_08:15:52.png

# std error
# /home/young/Pictures/2019_07_22_08:16:54.png

# degree of freedom = 12-1 =11

# Estimate
# /home/young/Pictures/2019_07_22_08:18:58.png
