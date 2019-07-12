# cd /mnt/1T-5e7/mycodehtml/statistics_analysis/Statistical_analysis/SangChulLee/003_Statistical_analysis/004_Load_xslx_file && \
# rm e.l && Rscript main.r \
# 2>&1 | tee -a e.l && code e.l

# ================================================================================
# Load xls file 

# It requires package

# install.packages("readxl")

library(readxl)

# ================================================================================
# Load txt file

gradexls<-read_excel(
  "./data/0203.grade.xlsx",
  sheet="grade",
  col_names=TRUE,
  na="NA")
gradexls
# # A tibble: 5 x 4
#      id msex   csex grade
#   <dbl> <chr> <dbl> <dbl>
# 1     1 Male      1     3
# 2     2 Male      1     4
# 3     3 Male      1     5
# 4     4 Male      1     3
# 5     5 Male      1     2

# ================================================================================
# See structure of data
str(gradexls)
# Classes ‘tbl_df’, ‘tbl’ and 'data.frame':	5 obs. of  4 variables:
#  $ id   : num  1 2 3 4 5
#  $ msex : chr  "Male" "Male" "Male" "Male" ...
#  $ csex : num  1 1 1 1 1
#  $ grade: num  3 4 5 3 2

# ================================================================================
