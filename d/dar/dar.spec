Name: dar
Version: 2.4.14
Release: alt1

Summary: DAR - Disk ARchive tool

License: LGPL
Group: File tools
Url: http://dar.linux.free.fr/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sf.net/%name/%name-%version.tar
Patch: %name-2.4.2.patch

Requires: lib%name = %version-%release

# manually removed: glibc-devel-static
# Automatically added by buildreq on Wed Sep 11 2013
# optimized out: groff-base libgpg-error libgpg-error-devel libstdc++-devel python3-base xz
BuildRequires: bzlib-devel doxygen gcc-c++ libattr-devel libe2fs-devel libgcrypt-devel liblzo2-devel zlib-devel

BuildRequires: perl-devel groff-base man

%description
dar is a shell command, that makes backup of a directory tree and files.
It has been tested under Linux, Windows (95, 2000, NT, XP), Solaris 8,
FreeBSD and NetBSD, it has been reported as working under Mac OS X 10.3.

%package -n lib%name
Summary: Library for %name
Group: Development/C

%description -n lib%name
This package contains library for %name.

%package -n lib%name-devel
Summary: Devel files for lib%name
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package contains header files for %name.

%package doc
Summary: Documentation files for %name
Group: File tools

%description doc
This package contains documentation files for %name.

%prep
%setup
%patch -p2
# for autopoint
#__subst "s|AM_GNU_GETTEXT_VERSION|AM_GNU_GETTEXT_VERSION(0.18.2)|g" configure.ac

%build
#autoreconf #for disable rpath
%configure --disable-static --disable-upx --enable-examples --disable-rpath
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build

%install
%makeinstall_std pkgdatadir=%_docdir/%name-%version
%find_lang %name

%files -f %name.lang
%config(noreplace) %_sysconfdir/darrc
%_bindir/*
%_man1dir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%files doc
%_docdir/%name-%version/

#%files -n lib%name-devel-static
#%_libdir/*.a

%changelog
* Tue Sep 02 2014 Vitaly Lipatov <lav@altlinux.ru> 2.4.14-alt1
- new version 2.4.14 (with rpmrb script)

* Mon Feb 17 2014 Vitaly Lipatov <lav@altlinux.ru> 2.4.12-alt1
- new version 2.4.12 (with rpmrb script)

* Wed Sep 11 2013 Vitaly Lipatov <lav@altlinux.ru> 2.4.10-alt1
- new version 2.4.10 (with rpmrb script)
- update buildreqs

* Thu Feb 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.11-alt1.1
- Removed bad RPATH

* Fri May 13 2011 Vitaly Lipatov <lav@altlinux.ru> 2.3.11-alt1
- new version 2.3.11 (with rpmrb script)
- update buildreqs

* Tue Dec 07 2010 Igor Vlasenko <viy@altlinux.ru> 2.3.8-alt1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Tue Nov 04 2008 Vitaly Lipatov <lav@altlinux.ru> 2.3.8-alt1
- new version 2.3.8 (with rpmrb script)
- fix build with gcc 4.3, on x86_64

* Tue Jan 01 2008 Vitaly Lipatov <lav@altlinux.ru> 2.3.6-alt1
- new version 2.3.6 (with rpmrb script)

* Fri Jul 06 2007 Vitaly Lipatov <lav@altlinux.ru> 2.3.4-alt1
- new version 2.3.4 (with rpmrb script)

* Wed Feb 28 2007 Vitaly Lipatov <lav@altlinux.ru> 2.3.3-alt1
- new version 2.3.3 (fix bug #10947), update buildreq
- split doc package, move doc to right place (fix bug #10948)

* Mon Nov 20 2006 Vitaly Lipatov <lav@altlinux.ru> 2.3.2-alt0.1
- new version 2.3.2 (with rpmrb script)

* Mon May 22 2006 Vitaly Lipatov <lav@altlinux.ru> 2.3.0-alt0.1
- new version 2.3.0 (with rpmrb script)

* Sun Feb 19 2006 Vitaly Lipatov <lav@altlinux.ru> 2.2.6-alt1
- new version (2.2.6)
- disable upx build requires

* Sun Sep 04 2005 Vitaly Lipatov <lav@altlinux.ru> 2.2.2-alt1
- new version
- disable static, upx

* Fri Mar 04 2005 Vitaly Lipatov <lav@altlinux.ru> 2.2.1-alt1
- first build for ALT Linux Sisyphus

