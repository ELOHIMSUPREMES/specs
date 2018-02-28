Serial: 1
%def_with _octave_arch
%define octave_pkg_version 3.0.0
%define octave_pkg_name control
%define octave_descr_name Control
Name: octave-%octave_pkg_name
Version: 3.0.0
Release: alt1
Summary: Control Systems

Group: Sciences/Mathematics
License: GPLv3+
URL: http://octave.sf.net

Source0: %octave_pkg_name-%version.tar.gz

BuildRequires: octave-devel texinfo
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel
%else
BuildArch: noarch
%endif
Provides: octave(control) = %version
# Depends: octave (>= 3.6.0)
Requires: octave >= 3.6.0


%description
Octave-Forge - Extra packages for GNU Octave.
This package contains the %octave_descr_name GNU Octave extension.

Extension Description:
Computer-Aided Control System Design (CACSD) Tools for GNU Octave, based on the proven SLICOT Library

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
* Sun Mar 27 2016 Anton Midyukov <antohami@altlinux.org> 1:3.0.0-alt1
- New version
- Added missing buildrequires.

* Thu Jun 18 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:2.6.5-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Wed Jul 02 2014 Paul Wolneykien <manowar@altlinux.ru> 1:2.6.5-alt1
- updated by octave-package-builder

* Tue Jan 14 2014 Paul Wolneykien <manowar@altlinux.ru> 1:2.6.1-alt1
- updated by octave-package-builder

* Tue Jan 14 2014 Paul Wolneykien <manowar@altlinux.ru> 1:2.4.5-alt2
- Rebuild with the next version of Octave: 3.8.0

* Thu Oct 10 2013 Paul Wolneykien <manowar@altlinux.ru> 1:2.4.5-alt1
- updated by octave-package-builder

* Tue Jan 08 2013 Paul Wolneykien <manowar@altlinux.ru> 1:2.4.1-alt1
- updated by octave-package-builder

* Sun Aug 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.1-alt1.1
- Built with OpenBLAS instead of GotoBLAS2

* Thu Nov 17 2011 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1
- initial import by octave-package-builder

