%define libgnutls_soname 30
%define libgnutlsxx28_soname 28
%define libgnutls_openssl_soname 27

Name: gnutls%libgnutls_soname
Version: 3.4.17
Release: alt1

Summary: A TLS protocol implementation
# The libgnutls library is LGPLv2.1+, utilities and remaining libraries are GPLv3+
License: LGPLv2.1+ and GPLv3+
Group: System/Libraries
Url: http://gnutls.org/
# ftp://ftp.gnutls.org/pub/gnutls/gnutls-%version.tar.bz2
Source: gnutls-%version.tar

# Skip test-hash-large for overridden CPU flags
Patch1: gnutls-patch-test-hash-large.patch

%define libcxx libgnutlsxx%libgnutlsxx28_soname
%define libssl libgnutls%{libgnutls_openssl_soname}-openssl
%def_disable guile
#set_automake_version 1.11

# Automatically added by buildreq on Thu Dec 08 2011
BuildRequires: gcc-c++ gtk-doc libgcrypt-devel libp11-kit-devel libreadline-devel libtasn1-devel makeinfo zlib-devel
BuildRequires: libnettle-devel autogen libopts-devel libidn-devel
%if_enabled guile
BuildRequires: guile-devel
%endif

# For tests
BuildRequires: net-tools
BuildRequires: /proc
BuildRequires: datefudge-faketime

%description
GnuTLS is a project that aims to develop a library which provides a
secure  layer, over a reliable transport layer.  Currently the GnuTLS
library implements the proposed standards by the IETF's TLS working
group.

%package -n lib%name
Summary: Transport Layer Security library
License: LGPLv2.1+
Group: System/Libraries
Provides: libgnutls = %version
Obsoletes: libgnutls < %version
Obsoletes: libgnutls-new < %version

%description -n lib%name
GnuTLS is a project that aims to develop a library which provides a
secure  layer, over a reliable transport layer.  Currently the GnuTLS
library implements the proposed standards by the IETF's TLS working
group.

This package contains the GnuTLS runtime library.

%package -n libgnutls-devel
Summary: Development files for lib%name
Group: Development/C
Requires: lib%name = %version-%release
Provides: libgnutls-devel = %version
Obsoletes: libgnutls-new-devel < %version

%description -n libgnutls-devel
GnuTLS is a project that aims to develop a library which provides a
secure  layer, over a reliable transport layer.  Currently the GnuTLS
library implements the proposed standards by the IETF's TLS working
group.

This package contains headers and other development files required to
build GnuTLS-based software.

%package -n %libcxx
Summary: Transport Layer Security C++ library
Group: System/Libraries
License: GPLv3+
Requires: lib%name = %version-%release
Provides: libgnutlsxx = %version
Obsoletes: libgnutlsxx < %version
Obsoletes: libgnutls-newxx < %version

%description -n %libcxx
GnuTLS is a project that aims to develop a library which provides a
secure  layer, over a reliable transport layer.  Currently the GnuTLS
library implements the proposed standards by the IETF's TLS working
group.

This package contains the GnuTLS C++ runtime library.

%package -n libgnutlsxx-devel
Summary: Development files for libgnutlsxx
Group: Development/C++
Requires: %libcxx = %version-%release
Requires: libgnutls-devel = %version-%release
Obsoletes: libgnutls-newxx-devel < %version

%description -n libgnutlsxx-devel
GnuTLS is a project that aims to develop a library which provides a
secure  layer, over a reliable transport layer.  Currently the GnuTLS
library implements the proposed standards by the IETF's TLS working
group.

This package contains headers and other development files required to
build GnuTLS-based software using C++.

%package -n %libssl
Summary: OpenSSL compatibility layer for the GnuTLS library
Group: System/Libraries
Requires: lib%name = %version-%release
Provides: libgnutls-openssl = %version
Obsoletes: libgnutls-openssl < %version
Obsoletes: libgnutls-new-openssl < %version

%description -n %libssl
GnuTLS is a project that aims to develop a library which provides a
secure  layer, over a reliable transport layer.  Currently the GnuTLS
library implements the proposed standards by the IETF's TLS working
group.

This package contains the GnuTLS runtime OpenSSL compatibility library.

%package -n libgnutls-openssl-devel
Summary: Development files for %libssl
Group: Development/C
Requires: %libssl = %version-%release
Requires: libgnutls-devel = %version-%release
Obsoletes: libgnutls-new-openssl-devel < %version

%description -n libgnutls-openssl-devel
GnuTLS is a project that aims to develop a library which provides a
secure  layer, over a reliable transport layer.  Currently the GnuTLS
library implements the proposed standards by the IETF's TLS working
group.

This package contains headers and other development files required to
build applications using the GnuTLS compatibility OpenSSL library.

%package -n gnutls-utils
Summary: TLS protocol utilities
Group: Security/Networking
Obsoletes: gnutls-utils26 < %version-%release
Obsoletes: gnutls-utils28 < %version-%release

%description -n gnutls-utils
GnuTLS is a project that aims to develop a library which provides a
secure  layer, over a reliable transport layer.  Currently the GnuTLS
library implements the proposed standards by the IETF's TLS working
group.

This package contains command line TLS client and server, and
certificate manipulation tools.

%package -n libgnutls-guile
Summary: GnuTLS Guile bindings
Group: Development/Other
Requires: lib%name = %version-%release
Obsoletes: libgnutls-new-guile < %version

%description -n libgnutls-guile
GnuTLS is a project that aims to develop a library which provides a
secure  layer, over a reliable transport layer.  Currently the GnuTLS
library implements the proposed standards by the IETF's TLS working
group.

This package contains Guile bindings for the library.

%package devel-doc
Summary: Development documentation for GnuTLS
Group: Development/C
Conflicts: libgnutls-devel < %version
Provides: gnutls-devel-doc = %version
Obsoletes: gnutls-devel-doc < %version
Obsoletes: gnutls-new-devel-doc < %version
BuildArch: noarch

%description devel-doc
GnuTLS is a project that aims to develop a library which provides a
secure  layer, over a reliable transport layer.  Currently the GnuTLS
library implements the proposed standards by the IETF's TLS working
group.

This package contains the GnuTLS API Reference Manual.

%prep
%setup -n gnutls-%version
%patch1 -p2
touch doc/*.texi
rm doc/*.info*
rm aclocal.m4 m4/{libtool,lt*}.m4
# Thanks to USE_POSIX_THREADS_WEAK feature, we have to link
# tests with @LIBMULTITHREAD@ in --no-as-needed mode.
sed -i 's/^\(test_[^ +=]\+\)_LDADD.*@LIBMULTITHREAD@.*/&\n\1_LDFLAGS = -Wl,--no-as-needed/' gl/tests/Makefile.*
# Use soname in the names of locale files
sed -i -r 's/^DOMAIN = [^[:blank:]#]+/&%libgnutls_soname/' po/Makevars

%build
%autoreconf
%def_disable static
%configure \
	--disable-rpath \
	--disable-static \
	--disable-silent-rules \
	--disable-libdane  \
	--without-tpm \
	--with-default-trust-store-file=/usr/share/ca-certificates/ca-bundle.crt \
	%{subst_enable guile} \
	--disable-local-libopts \
	--with-included-libtasn1=no \
	--enable-openssl-compatibility \
	--with-idn
make MAKEINFOFLAGS=--no-split

%install
%makeinstall_std
find %buildroot%_infodir/ -name '*.png' -delete -print
%define docdir %_docdir/gnutls-%version
mkdir -p %buildroot%docdir/{examples,reference}
install -p -m644 AUTHORS NEWS README THANKS %buildroot%docdir/
install -p -m644 doc/*.{cfg,css,html,png} %buildroot%docdir/
install -pm644 doc/examples/*.[hc]* %buildroot%docdir/examples/
install -pm644 doc/reference/html/* %buildroot%docdir/reference/
ln -s %_licensedir/GPL-2 %buildroot%docdir/COPYING
ln -s %_licensedir/LGPL-2.1 %buildroot%docdir/COPYING.LIB

%find_lang gnutls%libgnutls_soname
%set_verify_elf_method strict
%define _unpackaged_files_terminate_build 1

%check
%make_build -k check

%files -n lib%name -f gnutls%libgnutls_soname.lang
%dir %docdir
%docdir/[ACNRT]*
%_libdir/libgnutls.so.*

%files -n %libcxx
%_libdir/libgnutlsxx.so.*

%files -n %libssl
%_libdir/libgnutls-openssl.so.*

%files -n libgnutls-devel
%_includedir/gnutls/
%exclude %_includedir/gnutls/gnutlsxx.h
%exclude %_includedir/gnutls/openssl.h
%_libdir/libgnutls.so
%_pkgconfigdir/gnutls.pc

%files -n libgnutlsxx-devel
%dir %_includedir/gnutls/
%_includedir/gnutls/gnutlsxx.h
%_libdir/libgnutlsxx.so


%files -n libgnutls-openssl-devel
%dir %_includedir/gnutls/
%_includedir/gnutls/openssl.h
%_libdir/libgnutls-openssl.so

%files devel-doc
%dir %docdir
%docdir/*.css
%docdir/*.html
%docdir/*.png
%docdir/examples/
%docdir/reference/
%_man3dir/*
%_infodir/*

%files -n gnutls-utils
%_bindir/*
%_man1dir/*
%dir %docdir
%docdir/*.cfg

%if_enabled guile
# %%_datadir/guile belongs to guile package
# %%_datadir/guile/site may contain not only gnutls guile files.
# therefore %%_datadir/guile and %%_datadir/guile/site are not packaged. 
# is there some package using 'site' directory?
%files -n libgnutls-guile
%_libdir/libguile*
%_datadir/guile/site/gnutls
%_datadir/guile/site/gnutls.scm
%endif

%changelog
* Thu Dec 08 2016 Mikhail Efremov <sem@altlinux.org> 3.4.17-alt1
- Updated to 3.4.17.

* Mon Oct 10 2016 Mikhail Efremov <sem@altlinux.org> 3.4.16-alt1
- Updated to 3.4.16.

* Fri Sep 09 2016 Mikhail Efremov <sem@altlinux.org> 3.4.15-alt1
- Updated to 3.4.15.

* Mon Jul 18 2016 Mikhail Efremov <sem@altlinux.org> 3.4.14-alt1
- Add datefudge-faketime to BR.
- Updated to 3.4.14.

* Tue Jun 07 2016 Mikhail Efremov <sem@altlinux.org> 3.4.13-alt1
- Updated BR for tests.
- Updated to 3.4.13 (CVE-2016-4456).

* Fri May 20 2016 Mikhail Efremov <sem@altlinux.org> 3.4.12-alt1
- Don't package test libraries.
- Updated to 3.4.12.

* Tue Apr 12 2016 Mikhail Efremov <sem@altlinux.org> 3.4.11-alt1
- Updated to 3.4.11.

* Thu Mar 03 2016 Mikhail Efremov <sem@altlinux.org> 3.4.10-alt1
- Skip test-hash-large for overridden CPU flags.
- Updated to 3.4.10.

* Wed Feb 03 2016 Mikhail Efremov <sem@altlinux.org> 3.4.9-alt1
- Updated to 3.4.9.

* Sat Jan 09 2016 Mikhail Efremov <sem@altlinux.org> 3.4.8-alt1
- Updated to 3.4.8.

* Thu Dec 03 2015 Mikhail Efremov <sem@altlinux.org> 3.4.7-alt2
- Use soname in the names of locale files.

* Mon Nov 30 2015 Mikhail Efremov <sem@altlinux.org> 3.4.7-alt1
- Enabled libidn support.
- Updated to 3.4.7.

* Mon Sep 21 2015 Mikhail Efremov <sem@altlinux.org> 3.3.18-alt1
- Updated to 3.3.18.

* Tue Aug 18 2015 Mikhail Efremov <sem@altlinux.org> 3.3.17-alt1
- Updated to 3.3.17.

* Tue Jul 14 2015 Mikhail Efremov <sem@altlinux.org> 3.3.16-alt1
- Updated to 3.3.16.

* Tue May 05 2015 Mikhail Efremov <sem@altlinux.org> 3.3.15-alt1
- Updated to 3.3.15.

* Mon Mar 30 2015 Mikhail Efremov <sem@altlinux.org> 3.3.14-alt1
- Updated to 3.3.14.

* Thu Feb 26 2015 Mikhail Efremov <sem@altlinux.org> 3.3.13-alt1
- Updated to 3.3.13.

* Wed Jan 21 2015 Mikhail Efremov <sem@altlinux.org> 3.3.12-alt1
- Updated to 3.3.12.

* Thu Dec 11 2014 Mikhail Efremov <sem@altlinux.org> 3.3.11-alt1
- Updated to 3.3.11.

* Mon Nov 10 2014 Mikhail Efremov <sem@altlinux.org> 3.3.10-alt1
- Updated to 3.3.10.

* Thu Oct 16 2014 Mikhail Efremov <sem@altlinux.org> 3.3.9-alt1
- Build with external libopts.
- Updated to 3.3.9.

* Wed Sep 24 2014 Mikhail Efremov <sem@altlinux.org> 3.2.18-alt1
- Updated to 3.2.18.

* Tue Sep 02 2014 Mikhail Efremov <sem@altlinux.org> 3.2.17-alt1
- Rename utils subpackage to gnutls-utils.
- Updated to 3.2.17.

* Wed Aug 20 2014 Mikhail Efremov <sem@altlinux.org> 3.2.16-alt1
- Drop obsoleted patches.
- Drop libgnutls-extra.
- Updated to 3.2.16.

* Wed Mar 05 2014 Dmitry V. Levin <ldv@altlinux.org> 2.12.23-alt2
- Applied upstream fixes for CVE-2013-2116, CVE-2014-1959, and CVE-2014-0092.

* Wed Apr 10 2013 Dmitry V. Levin <ldv@altlinux.org> 2.12.23-alt1
- Updated to 2.12.23.

* Sun Dec 16 2012 Dmitry V. Levin <ldv@altlinux.org> 2.12.21-alt1
- Updated to 2.12.21.

* Sat Sep 01 2012 Dmitry V. Levin <ldv@altlinux.org> 2.12.20-alt1
- Updated to 2.12.20.

* Fri Mar 23 2012 Dmitry V. Levin <ldv@altlinux.org> 2.12.18-alt1
- Updated to 2.12.18.

* Thu Dec 08 2011 Dmitry V. Levin <ldv@altlinux.org> 2.12.14-alt1
- Updated to 2.12.14.
- Rewritten specfile.

* Fri Aug 05 2011 Dmitry V. Levin <ldv@altlinux.org> 2.10.5-alt1
- Updated to gnutls_2_10_5-4-g4eeba9b.
- Backported upstream fix for incorrect calls to libgcrypt.

* Fri Mar 04 2011 Alexey Tourbin <at@altlinux.ru> 2.10.4-alt3
- rebuilt for debuginfo
- updated dependencies
- made gnutls26-devel-doc noarch

* Tue Dec 21 2010 Afanasov Dmitry <ender@altlinux.org> 2.10.4-alt2
- build with internal libopencdk.

* Sun Dec 19 2010 Afanasov Dmitry <ender@altlinux.org> 2.10.4-alt1
- 2.10.4 release.

* Tue Oct 19 2010 Afanasov Dmitry <ender@altlinux.org> 2.10.2-alt1
- 2.10.2 release.

* Tue Jun 29 2010 Afanasov Dmitry <ender@altlinux.org> 2.10.0-alt1
- 2.10.0

* Tue Mar 23 2010 Afanasov Dmitry <ender@altlinux.org> 2.8.6-alt1
- 2.8.6 release.

* Tue Nov 17 2009 Afanasov Dmitry <ender@altlinux.org> 2.8.5-alt1
- 2.8.3 release.
- remove deb-fixtimebomb patch (fixed by upstream)

* Fri Nov 06 2009 Afanasov Dmitry <ender@altlinux.org> 2.8.3-alt2
- add deb-fixtimebomb patch that fixes check with expired certificate

* Fri Aug 28 2009 Afanasov Dmitry <ender@altlinux.org> 2.8.3-alt1
- 2.8.3 release.
  + Fix MinGW cross-compiling build error.
  + Fix problem with NUL bytes in X.509 CN and SAN fields.
  + Fix off-by-one size computation error in unknown DN printing.
  + Fix rare failure in gnutls_x509_crt_import.

* Thu Jun 11 2009 Afanasov Dmitry <ender@altlinux.org> 2.8.1-alt1
- 2.8.1 release.
  + Fix crash in gnutls_global_init after earlier init/deinit cycle.
  + Fix PKCS#12 decryption from password.

* Sun May 31 2009 Afanasov Dmitry <ender@altlinux.org> 2.8.0-alt1
- 2.8.0 release.
  + API/ABI changes in GnuTLS 2.8 compared to GnuTLS 2.6.x: The library
    should be completely backwards compatible on both the source and
    binary level.
  + Old libgnutls.m4 and libgnutls-config scripts removed. Please use
    pkg-config instead.
  + use 'libgnutls' as gettext domain
- patch: remove soversion from gettext domain, use offered domain
  (libgnutls) instead.
- don't install pictures in info dorectory
- remove obsolete install_info's invocations

* Mon May 25 2009 Afanasov Dmitry <ender@altlinux.org> 2.6.6-alt2
- %%set_verify_info_method relaxed until info-install filetringger will accept
  pictures used by gnutls in info files.

* Thu Apr 30 2009 Afanasov Dmitry <ender@altlinux.org> 2.6.6-alt1
- 2.6.6 release. 
  + fix Corrected double free on signature verification failure (CVE-2009-1415)
  + fix DSA key generation (CVE-2009-1416)
  + fix gnutls-cli expiration/activation time check (CVE-2009-1417)
- release fixes #19873 also.

* Tue Apr 14 2009 Afanasov Dmitry <ender@altlinux.org> 2.6.5-alt1.1
- build against libtasn1-2.0-alt1.

* Mon Apr 13 2009 Afanasov Dmitry <ender@altlinux.org> 2.6.5-alt1
- 2.6.5 release.
  + GnuTLS no longer uses the libtasn1-config (see NEWS)
- enable lzo by default

* Mon Feb 09 2009 Afanasov Dmitry <ender@altlinux.org> 2.6.4-alt1
- 2.6.4 release. 

* Tue Jan 27 2009 Afanasov Dmitry <ender@altlinux.org> 2.6.3-alt2
- change libgcrypt dependancy (Closes: #18654)

* Sun Dec 21 2008 Afanasov Dmitry <ender@altlinux.org> 2.6.3-alt1
- 2.6.3 release (see NEW for details)
  + Fix chain verification for chains that ends with RSA-MD2 CAs (CVE-2008-4989)
  + Fix memory leak in PSK authentication.
  + gnutls-cli minor updates
- return macroses that updates info's (fix repocop warnings)

* Tue Dec 02 2008 Afanasov Dmitry <ender@altlinux.org> 2.6.2-alt2
- fix unmet with devel packages.

* Wed Nov 26 2008 Afanasov Dmitry <ender@altlinux.org> 2.6.2-alt1
- 2.6.2 release.
- append soname to gettext files (fix conflict with gnutls that 
  has another soname).

* Sat Nov 08 2008 Afanasov Dmitry <ender@altlinux.org> 2.6.0-alt1
- 2.6.0 release.
- update buildreq.
- add support for lzo, guile controlled by --with/--without options.
  disable by default.
- remove obsolete %%post/%%pre actions.

* Fri Jul 11 2008 Pavlov Konstantin <thresh@altlinux.ru> 2.4.1-alt1
- 2.4.1 release.

* Thu Mar 13 2008 Pavlov Konstantin <thresh@altlinux.ru> 2.2.2-alt1
- 2.2.2 release.

* Mon Dec 03 2007 Pavlov Konstantin <thresh@altlinux.ru> 2.0.4-alt1
- 2.0.4 release.

* Fri Sep 21 2007 Pavlov Konstantin <thresh@altlinux.ru> 2.0.1-alt1
- 2.0.1 release.

* Fri Sep 14 2007 Pavlov Konstantin <thresh@altlinux.ru> 2.0.0-alt1
- 2.0.0 release.
- Do not try to use valgrind on non-x86/x86_64 architectures (thx kas@).

* Tue Jun 05 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.6.3-alt1
- 1.6.3 release.

* Thu Apr 19 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.6.2-alt1
- 1.6.2 release.

* Wed Feb 21 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.6.1-alt5
- Reverted -alt4 fixes, introduced a real fix for tasn1.

* Wed Feb 14 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.6.1-alt4
- Fixed #10822: removed .private.

* Sun Jan 21 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.6.1-alt3
- Modified symbol versioning:
  Added GNUTLS_1_6_1 with two new symbols.

* Sun Jan 21 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.6.1-alt2
- Added libgnutlsxx and libgnutlsxx-devel subpackages.
- Spec cleanup.

* Mon Jan 08 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.6.1-alt1
- Release 1.6.1.

* Sun Sep 24 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.4-alt1
- Release 1.4.4

* Sun Sep 10 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.3-alt1
- Release 1.4.3

* Sat Sep 02 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.2-alt1
- Updated to 1.4.2

* Tue May 30 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.0-alt1
- Updated to 1.4.0
- Updated Patch0

* Fri Mar 24 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.2.10-alt2
- Patch0: fixes build problems with ld --as-needed flag

* Sat Feb 11 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.2.10-alt1
- 1.2.10, fixes SA18794
- Correct packaging of examples
- Info install scripts moved to gnutls-devel-doc

* Thu Feb 02 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1.2.9-alt1.1
- Rebuilt for new pkg-config dependencies.

* Sat Dec 03 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.2.9-alt1
- Updated to 1.2.9
- Moved documentation off to gnutls-devel-doc

* Tue Aug 16 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.2.6-alt1.1
- rebuild with libopencdk.

* Sun Aug 14 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.2.6-alt1
- Updated to upstream release 1.2.6

* Fri May 27 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.2.3-alt1
- Updated to upstream release 1.2.3

* Mon Jan 03 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.23-alt1
- Updated to upstream release 1.0.23

* Sat Oct 16 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.21-alt1
- Updated to upstream release 1.0.21

* Tue May 25 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.13-alt1
- Updated to upstream release 1.0.13
- Added /usr/bin/srptool to the utils file list

* Thu Apr 08 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.10-alt1
- Updated to upstream release 1.0.10

* Sat Mar 27 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.8-alt2
- Rebuilt against libgcrypt 1.1.93

* Sat Mar 06 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.8-alt1
- Updated to 1.0.8 upstream release
- Build fixes for new autotools

* Sat Jan 10 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.4-alt1
- Updated to 1.0.4 upstream release
- Renamed the source package to gnutls
- Added openssl subpackage family to pack libgnutls-openssl

* Sat Jan 10 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.8.9-alt3
- Made external libtasn1 linkage optional, disabled per default

* Fri Jan 02 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.8.9-alt2
- Spec cleanup
- Build against libtasn1
- Removed libtool files from the filelist

* Sun Jul 20 2003 Mikhail Zabaluev <mhz@altlinux.ru> 0.8.9-alt1
- Ported the package to ALT Linux
