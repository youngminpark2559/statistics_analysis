# conda activate py36gputorch100 && \
# cd /home/young && \
# rm e.l && python T_test_in_Python.py \
# 2>&1 | tee -a e.l && code e.l

# ================================================================================
# Python에서 t-검정을 하는 방법에 대해 알아보자.

# ================================================================================
# 1-Sample T-test(단일 표본 t-검정)

# ================================================================================
# 20 number of studuents: sample from single population

# ================================================================================
# 전체 학생들 중 20명의 학생들을 추려 키를 재서 전체 학생들의 평균 키가 175cm인지 아닌지 알아보고 싶다.

# ================================================================================
#  귀무 가설: 학생들의 평균 키가 175cm이다.
#  대립 가설: 학생들의 평균 키가 175cm가 아니다.

# ================================================================================
# scipy.stats의 ttest_1samp 메소드를 이용한다. 

import numpy as np
from scipy import stats
 
# to get consistent result
np.random.seed(1)
 
# generate 20 random heights 
# mean: 180
# standard deviation: 5
# variance: 25
heights = [180 + np.random.normal(0, 5) for _ in range(20)]

# ================================================================================

# perform 1-sample t-test
tTestResult = stats.ttest_1samp(heights, 175)

# ================================================================================
print("The T-statistic is %.3f and the p-value is %.3f" % tTestResult)
# The T-statistic is 3.435 and the p-value is 0.003

# p-value 가 0.003으로, 기각역을 p < 0.05로 설정했을 때 귀무 가설을 기각한다. 

# 즉, 귀무 가설이 참일때 (학생들의 실제 평균 키가 175cm일때) 위와 같은 표본을 얻을 확률이 0.003으로, 학생들의 평균 키는 175cm가 아니라고 할 수 있다.

# ================================================================================
# Unpaired T-test(독립 표본 t-검정)

# Population: 1 and 2
# Extract 20 students from each population

# 2 populations have same height?

# ================================================================================
# 집단 1과 집단 2에서 각각 20명의 학생들을 추려, 각 집단의 키가 같은지, 다른지 알아보고 싶다.

# ================================================================================
#  귀무 가설: 두 집단의 평균 키는 같다.
#  대립 가설: 두 집단의 평균 키는 같지 않다.(양측 검정)

# ================================================================================
# scipy.stats 의 ttest_ind 메소드를 이용한다. (two INDependent sample이라 해서 ttest_ind )

# to get consistent result
np.random.seed(1)
 
# group 1 
# 20 heights
# mean 170
# standard deviation 5
group1Heights = [170 + np.random.normal(0, 5) for _ in range(20)]

# group 2
# 20 heights
# mean 180
# standard deviation 10
group2Heights = [175 + np.random.normal(0, 10) for _ in range(20)]
 
# perform t-test assuming "equal variances"
tTestResult = stats.ttest_ind(group1Heights, group2Heights)

print("The t-statistic and p-value assuming equal variances is %.3f and %.3f." % tTestResult)
# The t-statistic and p-value assuming equal variances is -2.329 and 0.025.

# perform t-test assuming "unequal variances"
tTestResultDiffVar = stats.ttest_ind(group1Heights, group2Heights, equal_var=False)

print("The t-statistic and p-value not assuming equal variances is %.3f and %.3f" % tTestResultDiffVar)
# The t-statistic and p-value not assuming equal variances is -2.329 and 0.026

# ================================================================================
# 기각역이 p < 0.05일때 귀무 가설을 기각한다. 

# 즉, 두 집단의 평균 키는 같지 않다. 

# 두 집단의 분산이 같다고 가정했을 때보다 같지 않다고 가정했을 때 p-value가 높게 나타난다. 

# 실제로 분산이 같지 않을 때 등분산을 가정하면 p-value가 낮게 나타나 실제로 그 차이가 유의미하지 않음에도 유의미하다고 해석할 수 있다. 주의하자.

# 참고) 등분산을 가정하지 않으면 Welch's T-test를 수행한다.

# ================================================================================
# Paired T-test(대응 표본 t-검정)

# group:
# people took diet drug

# Extract 20 people

# They show difference in weight?

# ================================================================================
# 다이어트 약을 복용한 사람들 중 20명을 추려 복용 전/후의 체중 차이가 유의미한지 알아보고 싶다.

# ================================================================================
#  귀무 가설: 복용 전/후의 체중 차이가 없다.
#  대립 가설: 복용 전/후의 체중 차이가 있다.

# ================================================================================
# scipy.stats 의 ttest_rel 메소드를 이용한다. (two RELated samples)

# to get consistent result
np.random.seed(1)
 
# before treatment
# 20 people case
# mean of weight: 60
# standard deviation of weight: 5
beforeWeights = [60 + np.random.normal(0, 5) for _ in range(20)]

# after treatment
# mean 0.99-fold decrease
# standard deviation 0.02
afterWeights = [w * np.random.normal(0.99, 0.02) for w in beforeWeights]

# perform paired t-test
tTestResult = stats.ttest_rel(beforeWeights, afterWeights)
 
print("The T-statistic is %.3f and the p-value is %.3f" % tTestResult)
# The T-statistic is 2.915 and the p-value is 0.009

# ================================================================================
# 기각역 p < 0.05에서 귀무 가설을 기각한다. 즉, 다이어트 약 복용 전/후에 체중 차이는 유의미하다고 할 수 있다.  

# ================================================================================
# 단측 검정은?

# T-분포는 0을 중심으로 대칭이므로,  기각역을 \alpha, T-statistic을 t라고 하면,

# t < 0, p/2 < \alpha
# 이면 less-than test의 귀무 가설을 기각하며,

# t > 0, p/2 < \alpha
# 이면 greater-than test의 귀무 가설을 기각한다.

# ================================================================================
# 참고
# http://stackoverflow.com/questions/15984221/how-to-perform-two-sample-one-tailed-t-test-with-numpy-scipy

# http://iaingallagher.tumblr.com/post/50980987285/t-tests-in-python


# 출처: https://thenotes.tistory.com/entry/Ttest-in-python [NOTES]