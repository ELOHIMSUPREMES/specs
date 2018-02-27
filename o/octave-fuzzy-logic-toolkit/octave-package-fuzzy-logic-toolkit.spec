Serial: 1
%define octave_pkg_version 0.4.4
%define octave_pkg_name fuzzy-logic-toolkit
%define octave_descr_name fuzzy-logic-toolkit
Name: octave-%octave_pkg_name
Version: 0.4.4
Release: alt2
Summary: Octave Fuzzy Logic Toolkit

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
Provides: octave(fuzzy-logic-toolkit) = %version
# Depends: octave (>= 3.2.4)
Requires: octave >= 3.2.4


%description
Octave-Forge - Extra packages for GNU Octave.
This package contains the %octave_descr_name GNU Octave extension.

Extension Description:
A mostly MATLAB-compatible fuzzy logic toolkit for Octave.

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
* Tue Jul 07 2015 Paul Wolneykien <manowar@altlinux.org> 1:0.4.4-alt2
- Rebuild with the next version of Octave: 4.0.0

* Wed Jul 02 2014 Paul Wolneykien <manowar@altlinux.ru> 1:0.4.4-alt1
- updated by octave-package-builder

* Tue Jan 14 2014 Paul Wolneykien <manowar@altlinux.ru> 1:0.4.2-alt2
- Rebuild with the next version of Octave: 3.8.0

* Tue Jan 08 2013 Paul Wolneykien <manowar@altlinux.ru> 1:0.4.2-alt1
- updated by octave-package-builder

* Thu Nov 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1
- initial import by octave-package-builder

