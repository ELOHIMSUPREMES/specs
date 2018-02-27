%def_with _octave_arch
%define octave_pkg_name fenv
%define octave_descr_name fenv
Name: octave-%octave_pkg_name
Version: 0.1.0
Release: alt2.1
Summary: Floating point environment

Group: Sciences/Mathematics
License: GPL version 3
URL: http://octave.sf.net

Source0: %octave_pkg_name-%version.tar.gz

BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel octave-devel
%else
BuildArch: noarch
%endif
# Depends: octave (>= 3.0.0)
Requires: octave >= 3.0.0
Provides: octave(fenv) = 0.1.0


%description
Octave-Forge - Extra packages for GNU Octave.
This package contains the %octave_descr_name GNU Octave extension.

Extension Description:
On supported architectures, change the rounding mode of the floating point arithmetics (to nearest, up, down, to zero) or change the precision of the arithmetical operations (single, double, double extended). Experimentally test the properties of the floating point arithmetics.

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
* Thu Jun 18 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.1.0-alt2.1
- Rebuilt for gcc5 C++11 ABI.

* Tue Jan 14 2014 Paul Wolneykien <manowar@altlinux.ru> 0.1.0-alt2
- Rebuild with the next version of Octave: 3.8.0

* Thu Nov 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.1.0-alt1
- initial import by octave-package-builder

