# cd /mnt/1T-5e7/mycodehtml/statistics_analysis/Statistical_analysis/SangChulLee/003_Statistical_analysis/001_Load_txt_file && \
# rm e.l && Rscript main.r \
# 2>&1 | tee -a e.l && code e.l

# ================================================================================
# Load txt file

gradetxt<-read.table(
  "./data/0201.grade.txt",header=FALSE,sep=",",stringsAsFactors=FALSE,na.strings=".")
gradetxt
#      V1   V2      V3    V4
# 1 index  sex subject grade
# 2     1 Male       1     3
# 3     1 Male       1     4
# 4     1 Male       1     5
# 5     1 Male       1     3

gradetxt<-read.table(
  "./data/0201.grade.txt",header=TRUE,sep=",",stringsAsFactors=FALSE,na.strings=".")
gradetxt
#   index  sex subject grade
# 1     1 Male       1     3
# 2     1 Male       1     4
# 3     1 Male       1     5
# 4     1 Male       1     3

str(gradetxt)
# 'data.frame':	4 obs. of  4 variables:
#  $ index  : int  1 1 1 1
#  $ sex    : chr  "Male" "Male" "Male" "Male"
#  $ subject: int  1 1 1 1
#  $ grade  : int  3 4 5 3

