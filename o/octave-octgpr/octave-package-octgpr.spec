%def_with _octave_arch
BuildRequires: gcc-fortran
%define octave_pkg_name octgpr
%define octave_descr_name OctGPR
Name: octave-%octave_pkg_name
Version: 1.2.0
Release: alt2.1
Summary: Package for full dense Gaussian Process Regression

Group: Sciences/Mathematics
License: GPL v3
Url: http://octave.sourceforge.net/

Source0: %octave_pkg_name-%version.tar.gz

BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel octave-devel
%else
BuildArch: noarch
%endif
# Depends: octave (>= 3.2.0)
Requires: octave >= 3.2.0
Provides: octave(octgpr) = 1.2.0


%description
Octave-Forge - Extra packages for GNU Octave.
This package contains the %octave_descr_name GNU Octave extension.

Extension Description:
The package allows interpolating and smoothing scattered

%prep
%setup -n %octave_pkg_name

%build
octave -q -H --no-site-file --eval "pkg build -nodeps . %SOURCE0"

%install
mkdir -p %buildroot%_datadir/octave/packages
mkdir -p %buildroot%_libdir/octave/packages
octave -q -H --no-site-file --eval "pkg prefix %buildroot%_datadir/octave/packages %buildroot%_libdir/octave/packages; pkg install -local -nodeps %octave_pkg_name-%version.tar.gz"

%files
%_datadir/octave/packages/%octave_pkg_name-%version
%if_with _octave_arch
%_libdir/octave/packages/%octave_pkg_name-%version
%endif

%changelog
* Thu Jun 18 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.2.0-alt2.1
- Rebuilt for gcc5 C++11 ABI.

* Tue Jan 14 2014 Paul Wolneykien <manowar@altlinux.ru> 1.2.0-alt2
- Rebuild with the next version of Octave: 3.8.0

* Sun Aug 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1.1
- Built with OpenBLAS instead of GotoBLAS2

* Thu Nov 17 2011 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1
- initial import by octave-package-builder

