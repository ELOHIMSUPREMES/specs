%define octave_pkg_version 1.3.1
%define octave_pkg_name splines
%define octave_descr_name splines
# BEGIN SourceDeps(oneline):
BuildRequires: makeinfo
# END SourceDeps(oneline)
Serial: 1
Name: octave-%octave_pkg_name
Version: 1.3.1
Release: alt1
Summary: Splines.

Group: Sciences/Mathematics
License: GPLv3+, public domain
URL: http://octave.sf.net

Source0: http://downloads.sourceforge.net/octave/%{octave_pkg_name}-%{octave_pkg_version}.tar.gz

BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel
%else
BuildArch: noarch
%endif
Provides: octave(splines) = %version
Provides: octave(splines) = %version
# Depends: octave (>= 3.6.0)
Requires: octave >= 3.6.0


%description
Octave-Forge - Extra packages for GNU Octave.
This package contains the %octave_descr_name GNU Octave extension.

Extension Description:
Additional spline functions.

%prep
%setup -q -n %{octave_pkg_name}

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
* Tue Sep 27 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.3.1-alt1
- regenerated from template by package builder

* Thu Apr 14 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.2.9-alt1
- regenerated from template by package builder

* Tue Jul 07 2015 Paul Wolneykien <manowar@altlinux.org> 1:1.2.7-alt2
- Rebuild with the next version of Octave: 4.0.0

* Wed Jul 02 2014 Paul Wolneykien <manowar@altlinux.ru> 1:1.2.7-alt1
- updated by octave-package-builder

* Tue Jan 14 2014 Paul Wolneykien <manowar@altlinux.ru> 1:1.2.6-alt1
- updated by octave-package-builder

* Tue Jan 14 2014 Paul Wolneykien <manowar@altlinux.ru> 1:1.2.4-alt2
- Rebuild with the next version of Octave: 3.8.0

* Thu Oct 10 2013 Paul Wolneykien <manowar@altlinux.ru> 1:1.2.4-alt1
- updated by octave-package-builder

* Tue Jan 08 2013 Paul Wolneykien <manowar@altlinux.ru> 1:1.1.2-alt1
- updated by octave-package-builder

* Fri Nov 18 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.7-alt1
- initial import by octave-package-builder

