# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/mkoctfile /usr/bin/rpcgen glibc-devel libtirpc-devel
# END SourceDeps(oneline)
%def_with _octave_arch
%define octave_pkg_version 0.2.0
%define octave_pkg_name instrument-control
%define octave_descr_name instrument-control
Name: octave-%octave_pkg_name
Version: 0.2.0
Release: alt3
Summary: Instrument Control Toolbox

Group: Sciences/Mathematics
License: GPLv3+
Url: http://octave.sourceforge.net/

Source0: %octave_pkg_name-%version.tar.gz

BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel octave-devel
%else
BuildArch: noarch
%endif
Provides: octave(instrument-control) = %version
# Depends: octave (>= 3.2.0)
Requires: octave >= 3.2.0


%description
Octave-Forge - Extra packages for GNU Octave.
This package contains the %octave_descr_name GNU Octave extension.

Extension Description:
Low level I/O functions for serial, i2c, parallel, tcp, gpib, vxi11 and usbtmc interfaces.

%prep
%setup -T -c %name-%version

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
* Tue Jul 07 2015 Paul Wolneykien <manowar@altlinux.org> 0.2.0-alt3
- Rebuild with the next version of Octave: 4.0.0

* Thu Jun 18 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.2.0-alt2.1
- Rebuilt for gcc5 C++11 ABI.

* Tue Jan 14 2014 Paul Wolneykien <manowar@altlinux.ru> 0.2.0-alt2
- Rebuild with the next version of Octave: 3.8.0

* Thu Oct 10 2013 Paul Wolneykien <manowar@altlinux.ru> 0.2.0-alt1
- updated by octave-package-builder

* Tue Jan 08 2013 Paul Wolneykien <manowar@altlinux.ru> 0.1.0-alt1
- updated by octave-package-builder

