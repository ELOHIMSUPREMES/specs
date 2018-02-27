%def_with _octave_arch
%define octave_pkg_version 1.0.8
%define octave_pkg_name xraylib
%define octave_descr_name Xraylib
Name: octave-%octave_pkg_name
Version: 1.0.8
Release: alt2.1
Summary: GNU Scientific Library

Group: Sciences/Mathematics
License: GPL version 2
URL: http://ftp.esrf.fr/pub/scisoft/xraylib/

Source0: %octave_pkg_name-%version.tar.gz

BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel octave-devel
%else
BuildArch: noarch
%endif
Provides: octave(xraylib) = %version


%description
Octave-Forge - Extra packages for GNU Octave.
This package contains the %octave_descr_name GNU Octave extension.

Extension Description:
Bindings to the Xraylib functions

%prep
%setup -n %octave_pkg_name-%version

%build
octave -q -H --no-site-file --eval "pkg build -nodeps . %SOURCE0"

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
* Thu Jun 18 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.8-alt2.1
- Rebuilt for gcc5 C++11 ABI.

* Tue Jan 14 2014 Paul Wolneykien <manowar@altlinux.ru> 1.0.8-alt2
- Rebuild with the next version of Octave: 3.8.0

* Mon Nov 28 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt1
- initial import by octave-package-builder

