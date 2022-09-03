#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-fields
Version  : 14.1
Release  : 59
URL      : https://cran.r-project.org/src/contrib/fields_14.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/fields_14.1.tar.gz
Summary  : Tools for Spatial Data
Group    : Development/Tools
License  : GPL-2.0+ GPL-3.0
Requires: R-fields-lib = %{version}-%{release}
Requires: R-fields-license = %{version}-%{release}
Requires: R-maps
Requires: R-spam
Requires: R-viridis
BuildRequires : R-dotCall64
BuildRequires : R-maps
BuildRequires : R-spam
BuildRequires : R-viridis
BuildRequires : buildreq-R

%description
on splines, spatial data, geostatistics,  and spatial statistics. The major methods
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
 source code can be viewed by expanding the source code version
 and looking in the R subdirectory. The reference for fields can be generated

%package lib
Summary: lib components for the R-fields package.
Group: Libraries
Requires: R-fields-license = %{version}-%{release}

%description lib
lib components for the R-fields package.


%package license
Summary: license components for the R-fields package.
Group: Default

%description license
license components for the R-fields package.


%prep
%setup -q -n fields
cd %{_builddir}/fields

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1660317904

%install
export SOURCE_DATE_EPOCH=1660317904
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/R-fields
cp %{_builddir}/fields/LICENSE.note %{buildroot}/usr/share/package-licenses/R-fields/77a3477abadd28c21e911f676ccf9f777297fb6b
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
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


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
/usr/lib64/R/library/fields/data/glacier.rda
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
/usr/lib64/R/library/fields/tests/Krig.Z.test.R
/usr/lib64/R/library/fields/tests/Krig.Z.test.Rout.save
/usr/lib64/R/library/fields/tests/Krig.se.W.R
/usr/lib64/R/library/fields/tests/Krig.se.W.Rout.save
/usr/lib64/R/library/fields/tests/Krig.se.grid.test.R
/usr/lib64/R/library/fields/tests/Krig.se.grid.test.Rout.save
/usr/lib64/R/library/fields/tests/Krig.se.test.R
/usr/lib64/R/library/fields/tests/Krig.se.test.Rout.save
/usr/lib64/R/library/fields/tests/Krig.test.R
/usr/lib64/R/library/fields/tests/Krig.test.Rout.save
/usr/lib64/R/library/fields/tests/Krig.test.W.R
/usr/lib64/R/library/fields/tests/Krig.test.W.Rout.save
/usr/lib64/R/library/fields/tests/KrigGCVREML.test.R
/usr/lib64/R/library/fields/tests/KrigGCVREML.test.Rout.save
/usr/lib64/R/library/fields/tests/Likelihood.test.R
/usr/lib64/R/library/fields/tests/Likelihood.test.Rout.save
/usr/lib64/R/library/fields/tests/SEFixedParameters.R
/usr/lib64/R/library/fields/tests/SEFixedParameters.Rout.save
/usr/lib64/R/library/fields/tests/Tps.test.R
/usr/lib64/R/library/fields/tests/Tps.test.Rout.save
/usr/lib64/R/library/fields/tests/Wend.test.R
/usr/lib64/R/library/fields/tests/Wend.test.Rout.save
/usr/lib64/R/library/fields/tests/cmdfile
/usr/lib64/R/library/fields/tests/cov.test.R
/usr/lib64/R/library/fields/tests/cov.test.Rout.save
/usr/lib64/R/library/fields/tests/cov.test2.R
/usr/lib64/R/library/fields/tests/cov.test2.Rout.save
/usr/lib64/R/library/fields/tests/derivative.test.R
/usr/lib64/R/library/fields/tests/derivative.test.Rout.save
/usr/lib64/R/library/fields/tests/diag.multiply.test.R
/usr/lib64/R/library/fields/tests/diag.multiply.test.Rout.save
/usr/lib64/R/library/fields/tests/evlpoly.test.R
/usr/lib64/R/library/fields/tests/evlpoly.test.Rout.save
/usr/lib64/R/library/fields/tests/fastTpsPredict.test.R
/usr/lib64/R/library/fields/tests/fastTpsPredict.test.Rout.save
/usr/lib64/R/library/fields/tests/mKrig.Z.R
/usr/lib64/R/library/fields/tests/mKrig.Z.Rout.save
/usr/lib64/R/library/fields/tests/mKrig.parameters.test.R
/usr/lib64/R/library/fields/tests/mKrig.parameters.test.Rout.save
/usr/lib64/R/library/fields/tests/mKrig.se.test.R
/usr/lib64/R/library/fields/tests/mKrig.se.test.Rout.save
/usr/lib64/R/library/fields/tests/mKrig.test.R
/usr/lib64/R/library/fields/tests/mKrig.test.Rout.save
/usr/lib64/R/library/fields/tests/mKrigMLETest.R
/usr/lib64/R/library/fields/tests/mKrigMLETest.Rout.save
/usr/lib64/R/library/fields/tests/mKrigREMLTest.R
/usr/lib64/R/library/fields/tests/mKrigREMLTest.Rout.save
/usr/lib64/R/library/fields/tests/misc.test.R
/usr/lib64/R/library/fields/tests/misc.test.Rout.save
/usr/lib64/R/library/fields/tests/offGridWeights.test.R
/usr/lib64/R/library/fields/tests/offGridWeights.test.Rout.save
/usr/lib64/R/library/fields/tests/offGridWeightsNEW.test.Rout.save
/usr/lib64/R/library/fields/tests/offGridWeightsNew.test.R
/usr/lib64/R/library/fields/tests/spam.test.R
/usr/lib64/R/library/fields/tests/spam.test.Rout.save
/usr/lib64/R/library/fields/tests/sreg.test.R
/usr/lib64/R/library/fields/tests/sreg.test.Rout.save
/usr/lib64/R/library/fields/tests/vgram.test.R
/usr/lib64/R/library/fields/tests/vgram.test.Rout.save
/usr/lib64/R/library/fields/tests/vgram2.test.R
/usr/lib64/R/library/fields/tests/vgram2.test.Rout.save

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/fields/libs/fields.so
/usr/lib64/R/library/fields/libs/fields.so.avx2
/usr/lib64/R/library/fields/libs/fields.so.avx512

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/R-fields/77a3477abadd28c21e911f676ccf9f777297fb6b
