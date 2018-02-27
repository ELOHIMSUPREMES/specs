
%def_enable static
%def_disable pth
%define req_gpgerror_ver 1.0
%define info_nogen 1
%define soversion 11

Name: libgcrypt%{soversion}
Version: 1.5.4
Release: alt2

Group: System/Legacy libraries
Summary: The GNU crypto library
License: LGPL
URL: http://www.gnupg.org/

Requires: libgpg-error >= %req_gpgerror_ver
Provides: libgcrypt = %version-%release
Obsoletes: libgcrypt < %version-%release

BuildRequires: libgpg-error-devel >= %req_gpgerror_ver
%if_enabled static
BuildRequires: glibc-devel-static
%endif
%if_enabled pth
BuildRequires: libpth-devel
%endif

Source: libgcrypt-%version.tar.bz2
Source1: version-script-gcrypt-1.4.map
# PLD
Patch0:	libgcrypt-1.3.1-no_libnsl.patch
Patch1:	libgcrypt-info.patch
Patch2:	libgcrypt-am18.patch
# ALT
Patch3: libgcrypt-1.4.0-alt-autotools-version.patch

%package pth
Summary: GNU Crypto library with GNU Pth user-space thread support
Group: System/Legacy libraries
Requires: libgpg-error >= %req_gpgerror_ver
Provides: libgcrypt-pth = %version-%release
Obsoletes: libgcrypt-pth < %version-%release

%description
Libgcrypt is a general purpose cryptographic library
based on the code from GNU Privacy Guard.  It provides functions for all
cryptograhic building blocks: symmetric ciphers
(AES,DES,Blowfish,CAST5,Twofish,Arcfour), hash algorithms (MD5,
RIPE-MD160, SHA-1, TIGER-192), MACs (HMAC for all hash algorithms),
public key algorithms (RSA, ElGamal, DSA), large integer functions,
random numbers and a lot of supporting functions.


%description pth
This is a portion of Libgcrypt supporting user-space
threads provided by the GNU Pth library.

%prep
%setup -q -n libgcrypt-%version
cat %SOURCE1 >> src/libgcrypt.vers
%if %info_nogen
sed -i "s|^info_TEXINFOS|#info_TEXINFOS|" doc/Makefile.am
%endif
%patch0 -p1
%patch1 -p1
#%patch2 -p1
#%patch3 -p1

%__rm -f COPYING.LIB
%__ln_s %_licensedir/LGPL-2.1 COPYING.LIB


%build
%autoreconf

%add_optflags %optflags_shared
%configure %{subst_enable static} \
    --enable-shared \
    --enable-noexecstack \
    --enable-ld-version-script \
    --disable-dev-random

%make_build -C doc ||:
%make_build

%check
%make check

%install
%makeinstall
%if %info_nogen
mkdir %buildroot/%_infodir/
install -m 0644 doc/*.info %buildroot/%_infodir/
%endif


%files
%_libdir/libgcrypt.so.*
#%_libdir/libgcrypt-pthread.so.*
%doc AUTHORS ChangeLog NEWS README THANKS TODO

%if_enabled pth
%files pth
%_libdir/libgcrypt-pth.so.*
%endif

%changelog
* Mon Jun 15 2015 Alexey Shabalin <shaba@altlinux.ru> 1.5.4-alt2
- build only library package as libgcrypt11 for compat

* Mon Aug 11 2014 Sergey V Turchin <zerg@altlinux.org> 1.5.4-alt1
- new version

* Thu Jul 25 2013 Sergey V Turchin <zerg@altlinux.org> 1.5.3-alt1
- new version

* Fri Apr 19 2013 Sergey V Turchin <zerg@altlinux.org> 1.5.2-alt1
- new version

* Tue Mar 19 2013 Sergey V Turchin <zerg@altlinux.org> 1.5.1-alt1
- new version

* Wed Jun 29 2011 Sergey V Turchin <zerg@altlinux.org> 1.5.0-alt1
- new version

* Fri Feb 25 2011 Sergey V Turchin <zerg@altlinux.org> 1.4.6-alt3
- clean version script

* Mon Oct 25 2010 Sergey V Turchin <zerg@altlinux.org> 1.4.6-alt2
- rebuilt

* Wed Jul 14 2010 Sergey V Turchin <zerg@altlinux.org> 1.4.6-alt0.M51.1
- built for M51

* Wed Jul 14 2010 Sergey V Turchin <zerg@altlinux.org> 1.4.6-alt1
- new version

* Mon Dec 14 2009 Sergey V Turchin <zerg@altlinux.org> 1.4.5-alt1
- new version

* Mon Apr 27 2009 Sergey V Turchin <zerg@altlinux.org> 1.4.4-alt2
- built static library

* Mon Jan 26 2009 Sergey V Turchin <zerg at altlinux dot org> 1.4.4-alt1
- new version
- removed deprecated macroses from specfile

* Tue Oct 07 2008 Sergey V Turchin <zerg at altlinux dot org> 1.4.3-alt1
- new version
- update version script
- split utils to separate package

* Tue Sep 09 2008 Sergey V Turchin <zerg at altlinux dot org> 1.4.2-alt1
- new version

* Wed Apr 30 2008 Sergey V Turchin <zerg at altlinux dot org> 1.4.1-alt1
- new version

* Fri Dec 14 2007 Sergey V Turchin <zerg at altlinux dot org> 1.4.0-alt2
- built without libcap

* Tue Dec 11 2007 Sergey V Turchin <zerg at altlinux dot org> 1.4.0-alt1
- new version

* Mon Dec 03 2007 Sergey V Turchin <zerg at altlinux dot org> 1.3.2-alt1
- new version

* Fri Oct 26 2007 Sergey V Turchin <zerg at altlinux dot org> 1.3.1-alt1
- new version

* Mon Feb 05 2007 Sergey V Turchin <zerg at altlinux dot org> 1.2.4-alt1
- new version

* Tue Aug 29 2006 Sergey V Turchin <zerg at altlinux dot org> 1.2.3-alt1
- new version

* Wed Nov 30 2005 Sergey V Turchin <zerg at altlinux dot org> 1.2.2-alt1
- new version
- using /dev/urandom only (not /dev/random)

* Tue Jan 11 2005 Sergey V Turchin <zerg at altlinux dot org> 1.2.1-alt1
- new version

* Mon Oct 11 2004 Sergey V Turchin <zerg at altlinux dot org> 1.2.0-alt1
- new version

* Mon Apr 05 2004 Sergey V Turchin <zerg at altlinux dot org> 1.1.94-alt1
- new version
- sync patches with PLD

* Thu Mar 25 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.1.93-alt0.1
- Updated to the latest upstream release
- Spec cleanup

* Thu Feb 05 2004 Sergey V Turchin <zerg at altlinux dot org> 1.1.91-alt2
- rebuild

* Mon Feb 02 2004 Sergey V Turchin <zerg at altlinux dot org> 1.1.91-alt1
- new version

* Mon Jan 12 2004 Sergey V Turchin <zerg at altlinux dot org> 1.1.12-alt3
- remove *.la

* Tue Sep 30 2003 Sergey V Turchin <zerg at altlinux dot org> 1.1.12-alt2
- fix build

* Wed Sep 03 2003 Sergey V Turchin <zerg at altlinux dot org> 1.1.12-alt1
- new version

* Fri Feb 07 2003 Sergey V Turchin <zerg@altlinux.ru> 1.1.10-alt2
- fix requires

* Fri Feb 07 2003 Sergey V Turchin <zerg@altlinux.ru> 1.1.10-alt1
- build for ALT

* Sat Nov 23 2002 Per �yvind Karlsen <peroyvind@sintrax.net> 1.1.10-6mdk
- Better fix for binary name(Patch #0)
- Follow mdk lib policy
- Removed non-existing libgcrypt.txt file from filelist
- bzip2'ed the source
- Remove tests from doc (rpmlint says so)
- Move *.so to -devel package, only *.so.* stays
- Cleanups

* Sat Nov 23 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.1.10-5mdk
- fix binary name for arch != i586

* Mon Nov 04 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 1.1.10-4mdk
- Rebuild

* Sat Oct 19 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 1.1.10-3mdk
- Fix bin name

* Sat Oct 19 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 1.1.10-2mdk
- Fix postun/post

* Sat Oct 19 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 1.1.10-1mdk
- Initial package
