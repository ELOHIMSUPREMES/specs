Serial: 4
%def_with _octave_arch
%define octave_pkg_version 1.2.0
%define octave_pkg_name miscellaneous
%define octave_descr_name Miscellaneous
Name: octave-%octave_pkg_name
Version: 1.2.0
Release: alt4
Summary: Miscellaneous functions

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
Provides: octave(miscellaneous) = %version

# SystemRequirements: units
BuildRequires: units

# octave module BuildRequires: libtinfo-devel [Debian] libncurses5-dev
BuildRequires: libtinfo-devel libncurses-devel
# Depends: octave (>= 3.6.0), general (>= 1.3.1)
Requires: octave >= 3.6.0 octave(general) >= 1.3.1


%description
Octave-Forge - Extra packages for GNU Octave.
This package contains the %octave_descr_name GNU Octave extension.

Extension Description:
Miscellaneous tools that don't fit somewhere else.

%prep
%setup -n %octave_pkg_name

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
* Tue Jan 14 2014 Paul Wolneykien <manowar@altlinux.ru> 4:1.2.0-alt4
- Rebuild with the next version of Octave: 3.8.0

* Wed Jan 09 2013 Paul Wolneykien <manowar@altlinux.ru> 4:1.2.0-alt3
- updated by octave-package-builder

* Wed Jan 09 2013 Paul Wolneykien <manowar@altlinux.ru> 3:1.2.0-alt2
- updated by octave-package-builder

* Tue Jan 08 2013 Paul Wolneykien <manowar@altlinux.ru> 2:1.2.0-alt1
- updated by octave-package-builder

* Thu Nov 17 2011 Igor Vlasenko <viy@altlinux.ru> 1:1.0.11-alt1
- initial import by octave-package-builder

