%define oldname octave-
%define octave_pkg_version 1.1.1
%define octave_pkg_name benchmark
%define octave_descr_name benchmark
Name: octave-benchmark
Version: 1.1.1
Release: alt3
Summary: Benchmarks for Octave

Group: Sciences/Mathematics
License: GPL v2
Url: http://octave.sourceforge.net/

Source0: in/%octave_pkg_name-%version.tar.gz

BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel octave-devel
%else
BuildArch: noarch
%endif
Provides: octave(benchmark) = %version
# Depends: octave (>= 2.9.7)
Requires: octave >= 2.9.7


%description
Octave-Forge - Extra packages for GNU Octave.
This package contains the %octave_descr_name GNU Octave extension.

Extension Description:
The package contains code used to benchmark speed of Octave.

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
* Tue Jul 07 2015 Paul Wolneykien <manowar@altlinux.org> 1.1.1-alt3
- Rebuild with the next version of Octave: 4.0.0

* Tue Jan 14 2014 Paul Wolneykien <manowar@altlinux.ru> 1.1.1-alt2
- Rebuild with the next version of Octave: 3.8.0

* Mon Nov 28 2011 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1
- initial import by octave-package-builder

