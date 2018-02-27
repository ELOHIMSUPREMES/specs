# BEGIN SourceDeps(oneline):
BuildRequires: glibc-devel libgnustep-corebase-devel zlib-devel
# END SourceDeps(oneline)
%def_with _octave_arch
%define octave_pkg_version 2.5.9
%define octave_pkg_name nan
%define octave_descr_name NaN
Name: octave-%octave_pkg_name
Version: 2.5.9
Release: alt1
Summary: The NaN-toolbox

Group: Sciences/Mathematics
License: GPLv3+
URL: http://pub.ist.ac.at/~schloegl/matlab/NaN

Source0: %octave_pkg_name-%version.tar.gz

BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel octave-devel
%else
BuildArch: noarch
%endif
Provides: octave(nan) = %version
# Depends: octave (> 3.2.0)
Requires: octave > 3.2.0


%description
Octave-Forge - Extra packages for GNU Octave.
This package contains the %octave_descr_name GNU Octave extension.

Extension Description:
A statistics and machine learning toolbox for Octave and Matlab for data with and w/o missing values.

%prep
%setup -c -n %name-%version

%build
tar czf ../%octave_pkg_name-%version.tar.gz *
rm -rf *
octave -q -H --no-site-file --eval "pkg build -nodeps . ../%octave_pkg_name-%version.tar.gz"

%install
mkdir -p %buildroot%_datadir/octave/packages
mkdir -p %buildroot%_libdir/octave/packages
octave -q -H --no-site-file --eval "pkg prefix %buildroot%_datadir/octave/packages %buildroot%_libdir/octave/packages; pkg install -local -nodeps %octave_pkg_name-%octave_pkg_version.tar.gz"

%files
%_datadir/octave/packages/%octave_pkg_name-%octave_pkg_version
%if_with _octave_arch
%_libdir/octave/packages/%octave_pkg_name-%octave_pkg_version
%endif

%changelog
* Wed Jul 02 2014 Paul Wolneykien <manowar@altlinux.ru> 2.5.9-alt1
- updated by octave-package-builder

