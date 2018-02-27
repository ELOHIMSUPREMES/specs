Serial: 1
%def_with _octave_arch
%define octave_pkg_version 1.0.5
%define octave_pkg_name fits
%define octave_descr_name FITS
Name: octave-%octave_pkg_name
Version: 1.0.5
Release: alt3
Summary: Reading and writing FITS (Flexible Image Transport System) files.

Group: Sciences/Mathematics
License: GPLv3+
URL: http://octave.sf.net

Source0: %octave_pkg_name-%version.tar.gz

BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel octave-devel
%else
BuildArch: noarch
%endif
Provides: octave(fits) = %version

# SystemRequirements: libcfitsio
BuildRequires: libcfitsio-devel

# octave module BuildRequires: libcfitsio-dev
BuildRequires: libcfitsio-devel
# Depends: octave (>= 3.0.0)
Requires: octave >= 3.0.0

%description
Octave-Forge - Extra packages for GNU Octave.
This package contains the %octave_descr_name GNU Octave extension.

Extension Description:
The Octave-FITS package provides functions for

%prep
%setup -c -n %name-%version
%define build_flags

%build
%define build_flags CXXFLAGS=-I%_includedir/cfitsio
%define build_flags CXXFLAGS=-I%_includedir/cfitsio
tar czf ../%octave_pkg_name-%version.tar.gz *
rm -rf *
%build_flags octave -q -H --no-site-file --eval "pkg build -nodeps . ../%octave_pkg_name-%version.tar.gz"

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
* Tue Jul 07 2015 Paul Wolneykien <manowar@altlinux.org> 1:1.0.5-alt3
- Rebuild with the next version of Octave: 4.0.0

* Thu Jun 18 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:1.0.5-alt2.1
- Rebuilt for gcc5 C++11 ABI.

* Wed Jul 02 2014 Paul Wolneykien <manowar@altlinux.ru> 1:1.0.5-alt2
- updated by octave-package-builder

* Wed Jul 02 2014 Paul Wolneykien <manowar@altlinux.ru> 1:1.0.5-alt1
- updated by octave-package-builder

* Tue Jan 14 2014 Paul Wolneykien <manowar@altlinux.ru> 1:1.0.3-alt2
- Rebuild with the next version of Octave: 3.8.0

* Thu Oct 10 2013 Paul Wolneykien <manowar@altlinux.ru> 1:1.0.3-alt1
- updated by octave-package-builder

* Tue Jan 08 2013 Paul Wolneykien <manowar@altlinux.ru> 1:1.0.2-alt1
- updated by octave-package-builder

* Fri Nov 18 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1
- initial import by octave-package-builder

