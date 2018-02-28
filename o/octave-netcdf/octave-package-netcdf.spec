# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/octave /usr/bin/octave-config makeinfo
# END SourceDeps(oneline)
%def_with _octave_arch
%define octave_pkg_version 1.0.11
%define octave_pkg_name netcdf
%define octave_descr_name netcdf
Name: octave-%octave_pkg_name
Version: 1.0.11
Release: alt2
Summary: netcdf

Group: Sciences/Mathematics
License: GPLv2+
URL: http://modb.oce.ulg.ac.be/mediawiki/index.php/Octave-netcdf

Source0: https://downloads.sourceforge.net/project/octave/Octave%%20Forge%%20Packages/Individual%%20Package%%20Releases/%{octave_pkg_name}-%{octave_pkg_version}.tar.gz

BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel
BuildRequires: libGL-devel libGLU-devel libGraphicsMagick-c++-devel libGraphicsMagick-devel fontconfig-devel libfreetype-devel libX11-devel libgl2ps-devel libcurl-devel libsuitesparse-devel libarpack-ng-devel libqrupdate-devel libpcre-devel
%else
BuildArch: noarch
%endif
Provides: octave(netcdf) = %version

# octave module BuildRequires: netcdf-devel [Fedora]
BuildRequires: libnetcdf-devel
# Depends: octave (>= 3.4.0)
Requires: octave >= 3.4.0

%description
Octave-Forge - Extra packages for GNU Octave.
This package contains the %octave_descr_name GNU Octave extension.

Extension Description:
A MATLAB compatible NetCDF interface for Octave

%prep
%setup -q -n %{octave_pkg_name}

%build
%define build_flags CXXFLAGS=$CXXFLAGS
%build_flags octave -H --no-site-file --eval "pkg build -verbose -nodeps . %SOURCE0"

%install
mkdir -p %buildroot%_datadir/octave/packages
mkdir -p %buildroot%_libdir/octave/packages
octave -H --no-site-file --eval "pkg prefix %buildroot%_datadir/octave/packages %buildroot%_libdir/octave/packages; pkg install -verbose -local -nodeps %octave_pkg_name-%octave_pkg_version-$(octave -H --no-site-file --eval "printf([__octave_config_info__(\"canonical_host_type\"), \"-\",  __octave_config_info__(\"api_version\")])").tar.gz"

%files
%_datadir/octave/packages/%octave_pkg_name-%octave_pkg_version
%if_with _octave_arch
%_libdir/octave/packages/%octave_pkg_name-%octave_pkg_version
%endif

%changelog
* Thu May 18 2017 Paul Wolneykien <manowar@altlinux.org> 1.0.11-alt2
- regenerated from template by package builder

* Tue Sep 27 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.11-alt1
- regenerated from template by package builder

* Wed Apr 13 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.9-alt1
- regenerated from template by package builder

* Tue Jul 07 2015 Paul Wolneykien <manowar@altlinux.org> 1.0.5-alt2
- Rebuild with the next version of Octave: 4.0.0

* Thu Jun 18 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.5-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Wed Jul 02 2014 Paul Wolneykien <manowar@altlinux.ru> 1.0.5-alt1
- updated by octave-package-builder

