#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-fields
Version  : 9.6
Release  : 11
URL      : https://cran.r-project.org/src/contrib/fields_9.6.tar.gz
Source0  : https://cran.r-project.org/src/contrib/fields_9.6.tar.gz
Summary  : Tools for Spatial Data
Group    : Development/Tools
License  : GPL-2.0+ GPL-3.0
Requires: R-fields-lib
Requires: R-maps
Requires: R-spam
BuildRequires : R-maps
BuildRequires : R-spam
BuildRequires : clr-R-helpers

%description
on splines, spatial data and spatial statistics. The major methods
 include cubic, and thin plate splines, Kriging, and compactly supported
 covariance functions for large data sets. The splines and Kriging methods are
 supported by functions that can determine the smoothing parameter
 (nugget and sill variance) and other covariance function parameters by cross
 validation and also by restricted maximum likelihood. For Kriging
 there is an easy to use function that also estimates the correlation
 scale (range parameter).  A major feature is that any covariance function
 implemented in R and following a simple format can be used for
 spatial prediction. There are also many useful functions for plotting
 and working with spatial data as images. This package also contains
 an implementation of sparse matrix methods for large spatial data
 sets and currently requires the sparse matrix (spam) package. Use
 help(fields) to get started and for an overview.  The fields source
 code is deliberately commented and provides useful explanations of
 numerical details as a companion to the manual pages. The commented
 source code can be viewed by expanding  source code version
 and looking in the R subdirectory. The reference for fields can be generated

%package lib
Summary: lib components for the R-fields package.
Group: Libraries

%description lib
lib components for the R-fields package.


%prep
%setup -q -c -n fields

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1521169642

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1521169642
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fields
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fields
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fields
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library fields|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/fields/CITATION
/usr/lib64/R/library/fields/DESCRIPTION
/usr/lib64/R/library/fields/INDEX
/usr/lib64/R/library/fields/Meta/Rd.rds
/usr/lib64/R/library/fields/Meta/data.rds
/usr/lib64/R/library/fields/Meta/features.rds
/usr/lib64/R/library/fields/Meta/hsearch.rds
/usr/lib64/R/library/fields/Meta/links.rds
/usr/lib64/R/library/fields/Meta/nsInfo.rds
/usr/lib64/R/library/fields/Meta/package.rds
/usr/lib64/R/library/fields/NAMESPACE
/usr/lib64/R/library/fields/R/fields
/usr/lib64/R/library/fields/R/fields.rdb
/usr/lib64/R/library/fields/R/fields.rdx
/usr/lib64/R/library/fields/data/CO2.rda
/usr/lib64/R/library/fields/data/COmonthlyMet.rda
/usr/lib64/R/library/fields/data/NorthAmericanRainfall.rda
/usr/lib64/R/library/fields/data/PRISMelevation.rda
/usr/lib64/R/library/fields/data/RCMexample.rda
/usr/lib64/R/library/fields/data/RMelevation.rda
/usr/lib64/R/library/fields/data/US.dat.rda
/usr/lib64/R/library/fields/data/WorldBankCO2.rda
/usr/lib64/R/library/fields/data/datalist
/usr/lib64/R/library/fields/data/lennon.rda
/usr/lib64/R/library/fields/data/ozone2.rda
/usr/lib64/R/library/fields/data/rat.diet.rda
/usr/lib64/R/library/fields/data/world.dat.rda
/usr/lib64/R/library/fields/help/AnIndex
/usr/lib64/R/library/fields/help/aliases.rds
/usr/lib64/R/library/fields/help/fields.rdb
/usr/lib64/R/library/fields/help/fields.rdx
/usr/lib64/R/library/fields/help/paths.rds
/usr/lib64/R/library/fields/html/00Index.html
/usr/lib64/R/library/fields/html/R.css
/usr/lib64/R/library/fields/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/fields/libs/fields.so
/usr/lib64/R/library/fields/libs/fields.so.avx2
/usr/lib64/R/library/fields/libs/fields.so.avx512
