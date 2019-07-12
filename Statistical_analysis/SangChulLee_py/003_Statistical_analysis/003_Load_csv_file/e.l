Installing package into ‘/home/young/R/x86_64-pc-linux-gnu-library/3.6’
(as ‘lib’ is unspecified)
trying URL 'https://cloud.r-project.org/src/contrib/readxl_1.3.1.tar.gz'
Content type 'application/x-gzip' length 2056165 bytes (2.0 MB)
==================================================
downloaded 2.0 MB

* installing *source* package ‘readxl’ ...
** package ‘readxl’ successfully unpacked and MD5 sums checked
** using staged installation
** libs
g++ -std=gnu++11 -I"/usr/share/R/include" -DNDEBUG -Iunix -I. -DRCPP_DEFAULT_INCLUDE_CALL=false -I"/home/young/R/x86_64-pc-linux-gnu-library/3.6/progress/include" -I"/home/young/R/x86_64-pc-linux-gnu-library/3.6/Rcpp/include"  -fvisibility=hidden -fpic  -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -c RcppExports.cpp -o RcppExports.o
g++ -std=gnu++11 -I"/usr/share/R/include" -DNDEBUG -Iunix -I. -DRCPP_DEFAULT_INCLUDE_CALL=false -I"/home/young/R/x86_64-pc-linux-gnu-library/3.6/progress/include" -I"/home/young/R/x86_64-pc-linux-gnu-library/3.6/Rcpp/include"  -fvisibility=hidden -fpic  -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -c XlsWorkBook.cpp -o XlsWorkBook.o
g++ -std=gnu++11 -I"/usr/share/R/include" -DNDEBUG -Iunix -I. -DRCPP_DEFAULT_INCLUDE_CALL=false -I"/home/young/R/x86_64-pc-linux-gnu-library/3.6/progress/include" -I"/home/young/R/x86_64-pc-linux-gnu-library/3.6/Rcpp/include"  -fvisibility=hidden -fpic  -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -c XlsWorkSheet.cpp -o XlsWorkSheet.o
g++ -std=gnu++11 -I"/usr/share/R/include" -DNDEBUG -Iunix -I. -DRCPP_DEFAULT_INCLUDE_CALL=false -I"/home/young/R/x86_64-pc-linux-gnu-library/3.6/progress/include" -I"/home/young/R/x86_64-pc-linux-gnu-library/3.6/Rcpp/include"  -fvisibility=hidden -fpic  -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -c XlsxWorkBook.cpp -o XlsxWorkBook.o
g++ -std=gnu++11 -I"/usr/share/R/include" -DNDEBUG -Iunix -I. -DRCPP_DEFAULT_INCLUDE_CALL=false -I"/home/young/R/x86_64-pc-linux-gnu-library/3.6/progress/include" -I"/home/young/R/x86_64-pc-linux-gnu-library/3.6/Rcpp/include"  -fvisibility=hidden -fpic  -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -c XlsxWorkSheet.cpp -o XlsxWorkSheet.o
gcc -std=gnu99 -I"/usr/share/R/include" -DNDEBUG -Iunix -I. -DRCPP_DEFAULT_INCLUDE_CALL=false -I"/home/young/R/x86_64-pc-linux-gnu-library/3.6/progress/include" -I"/home/young/R/x86_64-pc-linux-gnu-library/3.6/Rcpp/include"  -fvisibility=hidden -fpic  -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -c cran.c -o cran.o
gcc -std=gnu99 -I"/usr/share/R/include" -DNDEBUG -Iunix -I. -DRCPP_DEFAULT_INCLUDE_CALL=false -I"/home/young/R/x86_64-pc-linux-gnu-library/3.6/progress/include" -I"/home/young/R/x86_64-pc-linux-gnu-library/3.6/Rcpp/include"  -fvisibility=hidden -fpic  -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -c endian.c -o endian.o
gcc -std=gnu99 -I"/usr/share/R/include" -DNDEBUG -Iunix -I. -DRCPP_DEFAULT_INCLUDE_CALL=false -I"/home/young/R/x86_64-pc-linux-gnu-library/3.6/progress/include" -I"/home/young/R/x86_64-pc-linux-gnu-library/3.6/Rcpp/include"  -fvisibility=hidden -fpic  -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -c ole.c -o ole.o
gcc -std=gnu99 -I"/usr/share/R/include" -DNDEBUG -Iunix -I. -DRCPP_DEFAULT_INCLUDE_CALL=false -I"/home/young/R/x86_64-pc-linux-gnu-library/3.6/progress/include" -I"/home/young/R/x86_64-pc-linux-gnu-library/3.6/Rcpp/include"  -fvisibility=hidden -fpic  -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -c xls.c -o xls.o
gcc -std=gnu99 -I"/usr/share/R/include" -DNDEBUG -Iunix -I. -DRCPP_DEFAULT_INCLUDE_CALL=false -I"/home/young/R/x86_64-pc-linux-gnu-library/3.6/progress/include" -I"/home/young/R/x86_64-pc-linux-gnu-library/3.6/Rcpp/include"  -fvisibility=hidden -fpic  -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -c xlstool.c -o xlstool.o
g++ -std=gnu++11 -I"/usr/share/R/include" -DNDEBUG -Iunix -I. -DRCPP_DEFAULT_INCLUDE_CALL=false -I"/home/young/R/x86_64-pc-linux-gnu-library/3.6/progress/include" -I"/home/young/R/x86_64-pc-linux-gnu-library/3.6/Rcpp/include"  -fvisibility=hidden -fpic  -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -c zip.cpp -o zip.o
g++ -std=gnu++11 -shared -L/usr/lib/R/lib -Wl,-Bsymbolic-functions -Wl,-z,relro -o readxl.so RcppExports.o XlsWorkBook.o XlsWorkSheet.o XlsxWorkBook.o XlsxWorkSheet.o cran.o endian.o ole.o xls.o xlstool.o zip.o -L/usr/lib/R/lib -lR
installing to /home/young/R/x86_64-pc-linux-gnu-library/3.6/00LOCK-readxl/00new/readxl/libs
** R
** inst
** byte-compile and prepare package for lazy loading
** help
*** installing help indices
*** copying figures
** building package indices
** installing vignettes
** testing if installed package can be loaded from temporary location
** checking absolute paths in shared objects and dynamic libraries
** testing if installed package can be loaded from final location
** testing if installed package keeps a record of temporary installation path
* DONE (readxl)

The downloaded source packages are in
	‘/tmp/RtmpUyGcRn/downloaded_packages’

# A tibble: 5 x 4
     id msex   csex grade
  <dbl> <chr> <dbl> <dbl>
1     1 Male      1     3
2     2 Male      1     4
3     3 Male      1     5
4     4 Male      1     3
5     5 Male      1     2

Classes ‘tbl_df’, ‘tbl’ and 'data.frame':	5 obs. of  4 variables:
 $ id   : num  1 2 3 4 5
 $ msex : chr  "Male" "Male" "Male" "Male" ...
 $ csex : num  1 1 1 1 1
 $ grade: num  3 4 5 3 2
Error: unexpected '=' in "="
Execution halted
