#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-janitor
Version  : 2.1.0
Release  : 35
URL      : https://cran.r-project.org/src/contrib/janitor_2.1.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/janitor_2.1.0.tar.gz
Summary  : Simple Tools for Examining and Cleaning Dirty Data
Group    : Development/Tools
License  : MIT
Requires: R-dplyr
Requires: R-lifecycle
Requires: R-lubridate
Requires: R-magrittr
Requires: R-purrr
Requires: R-rlang
Requires: R-snakecase
Requires: R-stringi
Requires: R-stringr
Requires: R-tidyr
Requires: R-tidyselect
BuildRequires : R-dplyr
BuildRequires : R-lifecycle
BuildRequires : R-lubridate
BuildRequires : R-magrittr
BuildRequires : R-purrr
BuildRequires : R-rlang
BuildRequires : R-snakecase
BuildRequires : R-stringi
BuildRequires : R-stringr
BuildRequires : R-tidyr
BuildRequires : R-tidyselect
BuildRequires : buildreq-R

%description
names; provide quick counts of variable combinations (i.e., frequency
    tables and crosstabs); and isolate duplicate records. Other janitor functions
    nicely format the tabulation results. These tabulate-and-report functions
    approximate popular features of SPSS and Microsoft Excel. This package
    follows the principles of the "tidyverse" and works well with the pipe function
    %>%. janitor was built with beginning-to-intermediate R users in mind and is
    optimized for user-friendliness. Advanced R users can already do everything
    covered here, but with janitor they can do it faster and save their thinking for
    the fun stuff.

%prep
%setup -q -c -n janitor
cd %{_builddir}/janitor

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1609888517

%install
export SOURCE_DATE_EPOCH=1609888517
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library janitor
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library janitor
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library janitor
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc janitor || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/janitor/DESCRIPTION
/usr/lib64/R/library/janitor/INDEX
/usr/lib64/R/library/janitor/LICENSE
/usr/lib64/R/library/janitor/Meta/Rd.rds
/usr/lib64/R/library/janitor/Meta/features.rds
/usr/lib64/R/library/janitor/Meta/hsearch.rds
/usr/lib64/R/library/janitor/Meta/links.rds
/usr/lib64/R/library/janitor/Meta/nsInfo.rds
/usr/lib64/R/library/janitor/Meta/package.rds
/usr/lib64/R/library/janitor/Meta/vignette.rds
/usr/lib64/R/library/janitor/NAMESPACE
/usr/lib64/R/library/janitor/NEWS.md
/usr/lib64/R/library/janitor/R/janitor
/usr/lib64/R/library/janitor/R/janitor.rdb
/usr/lib64/R/library/janitor/R/janitor.rdx
/usr/lib64/R/library/janitor/doc/index.html
/usr/lib64/R/library/janitor/doc/janitor.R
/usr/lib64/R/library/janitor/doc/janitor.Rmd
/usr/lib64/R/library/janitor/doc/janitor.html
/usr/lib64/R/library/janitor/doc/tabyls.R
/usr/lib64/R/library/janitor/doc/tabyls.Rmd
/usr/lib64/R/library/janitor/doc/tabyls.html
/usr/lib64/R/library/janitor/help/AnIndex
/usr/lib64/R/library/janitor/help/aliases.rds
/usr/lib64/R/library/janitor/help/figures/logo_small.png
/usr/lib64/R/library/janitor/help/janitor.rdb
/usr/lib64/R/library/janitor/help/janitor.rdx
/usr/lib64/R/library/janitor/help/paths.rds
/usr/lib64/R/library/janitor/html/00Index.html
/usr/lib64/R/library/janitor/html/R.css
/usr/lib64/R/library/janitor/tests/testthat.R
/usr/lib64/R/library/janitor/tests/testthat/test-adorn-ns.R
/usr/lib64/R/library/janitor/tests/testthat/test-adorn-pct-formatting.R
/usr/lib64/R/library/janitor/tests/testthat/test-adorn-percentages.R
/usr/lib64/R/library/janitor/tests/testthat/test-adorn-rounding.R
/usr/lib64/R/library/janitor/tests/testthat/test-adorn-title.R
/usr/lib64/R/library/janitor/tests/testthat/test-adorn-totals.R
/usr/lib64/R/library/janitor/tests/testthat/test-adorn_totals.R
/usr/lib64/R/library/janitor/tests/testthat/test-clean-names.R
/usr/lib64/R/library/janitor/tests/testthat/test-compare_df_cols.R
/usr/lib64/R/library/janitor/tests/testthat/test-convert_to_date.R
/usr/lib64/R/library/janitor/tests/testthat/test-date-conversion.R
/usr/lib64/R/library/janitor/tests/testthat/test-get-dupes.R
/usr/lib64/R/library/janitor/tests/testthat/test-get-level-groups.R
/usr/lib64/R/library/janitor/tests/testthat/test-remove-empties.R
/usr/lib64/R/library/janitor/tests/testthat/test-round_to_fraction.R
/usr/lib64/R/library/janitor/tests/testthat/test-row-to-names.R
/usr/lib64/R/library/janitor/tests/testthat/test-signif_half_up.R
/usr/lib64/R/library/janitor/tests/testthat/test-statistical-tests.R
/usr/lib64/R/library/janitor/tests/testthat/test-tabyl-classifiers.R
/usr/lib64/R/library/janitor/tests/testthat/test-tabyl.R
/usr/lib64/R/library/janitor/tests/testthat/test-top-levels.R
/usr/lib64/R/library/janitor/tests/testthat/test-utilities.R
