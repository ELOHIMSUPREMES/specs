%define oname STLport
Name: libstlport

Version: 5.2.1
Release: alt1

Summary: C++ standard library

License: distributable (see README)
Group: System/Libraries
Url: http://stlport.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sf.net/stlport/%oname-%version.tar

BuildRequires: gcc-c++
# libstdc++-devel

%description
STLport is a multiplatform implementation of C++ Standard Template
Library based on SGI STL. It's used by e.g. OpenOffice.

%package devel
Summary: STLport heades files, documentation
Group: Development/Other
Requires: %name = %version-%release
Provides: %oname-devel = %version-%release

%description devel
Header files and development documentation for STLport.

%package static
Summary: Static STLport libraries
Group: Development/Other
Requires: %name-devel = %version-%release

%description static
Static STLport libraries.

%prep
%setup -q -n %oname-%version

%build
./configure --prefix=%prefix --includedir=%_includedir --libdir=%_libdir
%make_build
# -C build/lib -f gcc.mak

%install
%makeinstall_std

%files
%doc README
%_libdir/*.so.*

%files devel
%doc doc/*
%_includedir/stlport/
%_libdir/*.so

#%files static
#%_libdir/*.a

%changelog
* Wed Sep 05 2012 Vitaly Lipatov <lav@altlinux.ru> 5.2.1-alt1
- new version 5.2.1 (with rpmrb script)

* Tue Nov 24 2009 Repocop Q. A. Robot <repocop@altlinux.org> 5.1.4-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libstlport
  * postun_ldconfig for libstlport
  * postclean-05-filetriggers for spec file

* Mon Jan 07 2008 Vitaly Lipatov <lav@altlinux.ru> 5.1.4-alt1
- new version 5.1.4 (with rpmrb script)

* Sat Nov 05 2005 Vitaly Lipatov <lav@altlinux.ru> 5.0.0-alt0.2
- initial build for ALT Linux Sisyphus
- spec from PLD Team <feedback@pld-linux.org>
