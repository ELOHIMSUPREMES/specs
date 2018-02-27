%define oldname octave-
%def_with _octave_arch
%define octave_pkg_version 1.0.9
%define octave_pkg_name engine
%define octave_descr_name Engine
Name: octave-engine
Version: 1.0.9
Release: alt2
Summary: Engine

Group: Sciences/Mathematics
License: GPL version 2 or later
URL: http://octave.sf.net

Source0: in/%octave_pkg_name-%version.tar.gz

BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel octave-devel
%else
BuildArch: noarch
%endif
Provides: octave(engine) = %version
# Depends: octave (>= 2.9.7)
Requires: octave >= 2.9.7


%description
Octave-Forge - Extra packages for GNU Octave.
This package contains the %octave_descr_name GNU Octave extension.

Extension Description:
An external interface library for Octave

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
* Tue Jan 14 2014 Paul Wolneykien <manowar@altlinux.ru> 1.0.9-alt2
- Rebuild with the next version of Octave: 3.8.0

* Mon Nov 28 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.9-alt1
- initial import by octave-package-builder

