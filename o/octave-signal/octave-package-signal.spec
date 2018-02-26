Serial: 2
%def_with _octave_arch
%define octave_pkg_version 1.2.0
%define octave_pkg_name signal
%define octave_descr_name Signal
Name: octave-%octave_pkg_name
Version: 1.2.0
Release: alt1
Summary: Signal Processing.

Group: Sciences/Mathematics
License: GPLv3+, public domain
URL: http://octave.sf.net

Source0: %octave_pkg_name-%version.tar.gz

BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel octave-devel
%else
BuildArch: noarch
%endif
Provides: octave(signal) = %version
# Depends: octave (>= 3.6.0), optim (>= 1.0.0), specfun, control (>= 2.2.3), general (>= 1.3.2)
Requires: octave >= 3.6.0 octave(optim) >= 1.0.0 octave(specfun) octave(control) >= 2.2.3 octave(general) >= 1.3.2


%description
Octave-Forge - Extra packages for GNU Octave.
This package contains the %octave_descr_name GNU Octave extension.

Extension Description:
Signal processing tools, including filtering, windowing and display functions.

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
* Tue Jan 08 2013 Paul Wolneykien <manowar@altlinux.ru> 2:1.2.0-alt1
- updated by octave-package-builder

* Thu Nov 17 2011 Igor Vlasenko <viy@altlinux.ru> 1:1.1.1-alt1
- initial import by octave-package-builder

