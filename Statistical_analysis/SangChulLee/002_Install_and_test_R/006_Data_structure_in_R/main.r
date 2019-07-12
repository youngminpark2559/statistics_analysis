# cd /mnt/1T-5e7/mycodehtml/statistics_analysis/Statistical_analysis/SangChulLee/002_Install_and_test_R/006_Data_structure_in_R && \
# rm e.l && Rscript main.r \
# 2>&1 | tee -a e.l && code e.l

# ================================================================================
# https://github.com/youngminpark2559/statistics_analysis/blob/master/Statistical_analysis/SangChulLee/002_Install_and_test_R/006_Data_structure_in_R/pics/2019_07_12_11:48:48.png

# ================================================================================
# Vector and Dataframe is most used

# ================================================================================
# https://github.com/youngminpark2559/statistics_analysis/blob/master/Statistical_analysis/SangChulLee/002_Install_and_test_R/006_Data_structure_in_R/pics/2019_07_12_11:49:45.png

# https://github.com/youngminpark2559/statistics_analysis/blob/master/Statistical_analysis/SangChulLee/002_Install_and_test_R/006_Data_structure_in_R/pics/2019_07_12_11:50:07.png

# ================================================================================
# generate numbers from 1 to 12
m<-1:12
m
# 1  2  3  4  5  6  7  8  9 10 11 12

# ================================================================================
# Create matrix, number of rows 4, format remains automatically
outMatrix <- matrix(data = m, nrow = 4)
outMatrix
#      [,1] [,2] [,3]
# [1,]    1    5    9
# [2,]    2    6   10
# [3,]    3    7   11
# [4,]    4    8   12

# ================================================================================
# Create array, width: 2, height:3, depth: 4
outArray=array(m,c(2,3,4))
outArray
#      [,1] [,2] [,3]
# [1,]    1    3    5
# [2,]    2    4    6

# , , 2

#      [,1] [,2] [,3]
# [1,]    7    9   11
# [2,]    8   10   12

# , , 3

#      [,1] [,2] [,3]
# [1,]    1    3    5
# [2,]    2    4    6

# , , 4

#      [,1] [,2] [,3]
# [1,]    7    9   11
# [2,]    8   10   12

# ================================================================================
