Name: LibreSSL
Version: 2.4.2
Release: alt1

%define oname libressl

Summary: OpenBSD fork of OpenSSL library

License: ISC
Group: Security/Networking
Url: http://www.libressl.org/

Packager: Vladimir D. Seleznev <vseleznv@altlinux.org>
Source: %oname-%version.tar.gz
Patch4: netcat-1.159-alt-usage.patch
Patch8: netcat-1.159-alt-execcmd.patch
Patch9: netcat-1.159-alt-proxy_pass.patch
Patch10: LibreSSL-2.4.2-alt-openssl-manpage.patch

%define common_descr \
LibreSSL is a version of the TLS/crypto stack forked from OpenSSL in \
2014, with goals of modernizing the codebase, improving security, and \
applying best practice development processes.

%description
%common_descr

%package -n openssl-LibreSSL
Summary: LibreSSL openssl utility, which provides tools for managing keys, certificates, etc
Group: Security/Networking
Obsoletes: LibreSSL-openssl
Conflicts: openssl

%description -n openssl-LibreSSL
%common_descr

This package contains openssl(1) utility.

%package devel
Summary: Headers for %name
Group: Development/C
Conflicts: libcrypto-devel libssl-devel

%description devel
%common_descr

Headers for building software that uses %name

%package doc
Summary: Documantation pages for %name
Group: Documentation
BuildArch: noarch
Conflicts: openssl-doc

%description doc
%common_descr

This package contains documantation pages for %name

%package -n libcrypto-LibreSSL
Summary: LibreSSL libcrypto shared library
Group: Security/Networking

%description -n libcrypto-LibreSSL
%common_descr

LibreSSL libcrypto shared library

%package -n libssl-LibreSSL
Summary: LibreSSL libssl shared library
Group: Security/Networking

%description -n libssl-LibreSSL
%common_descr

LibreSSL libssl shared library

%package -n libtls
Summary: TLS library from LibreSSL
Group: Security/Networking

%description -n libtls
%common_descr

A new TLS library, designed to make it easier to write foolproof
applications.

%package -n libtls-devel
Summary: Headers for libtls
Group: Development/C
Requires: libtls = %version-%release
Requires: %name-devel = %version-%release

%description -n libtls-devel
%common_descr

A new TLS library, designed to make it easier to write foolproof
applications.

Headers for building software that uses libtls

%package -n libtls-doc
Summary: Manpages for libtls
Group: Documentation
BuildArch: noarch

%description -n libtls-doc

%common_descr

A new TLS library, designed to make it easier to write foolproof
applications.

Thins package contains manual pages for libtls

%package -n netcat-tls
Summary: Reads and writes data across network connections using TCP or UDP
Group: Networking/Other
License: BSD
Obsoletes: netcat-openbsd
Conflicts: netcat
Provides: netcat
Provides: netcat-ssl

%description -n netcat-tls
The nc (or netcat) utility is used for just about anything under the sun
involving TCP, UDP, or UNIX-domain sockets.  It can open TCP connections,
send UDP packets, listen on arbitrary TCP and UDP ports, do port scanning,
and deal with both IPv4 and IPv6.  Unlike telnet(1), nc scripts nicely, and
separates error messages onto standard error instead of sending them to
standard output, as telnet(1) does with some.

Common uses include:

      o   simple TCP proxies
      o   shell-script based HTTP clients and servers
      o   network daemon testing
      o   a SOCKS or HTTP ProxyCommand for ssh(1)
      o   and much, much more

%prep
%setup -n %oname-%version
%patch8 -p2
%patch9 -p2
%patch4 -p2
%patch10 -p2

%build
%autoreconf
%configure \
	--disable-static \
	--enable-nc \
	--with-openssldir='%_sysconfdir/%oname/' \
	#
%make check

%install
%makeinstall_std

pushd %buildroot%_bindir
	mv openssl{,-LibreSSL}
	ln -s nc netcat
popd

install -m 0644 apps/nc/nc.1 %buildroot%_man1dir

pushd %buildroot%_man1dir
	for nc_manpage in nc.*; do
		netcat_manpage=$(echo $nc_manpage | sed -e 's/nc/netcat/')
		cp $nc_manpage $netcat_manpage
	done

	for openssl_manpage in openssl.*; do
		openssl_LibreSSL_manpage=$(echo $openssl_manpage | sed -e 's/\(openssl\)/\1-LibreSSL/')
		mv $openssl_manpage $openssl_LibreSSL_manpage
	done
popd

%files -n openssl-LibreSSL
%_bindir/openssl-LibreSSL
%_man1dir/openssl-LibreSSL.*

%files devel
%_includedir/openssl
%_libdir/*.so
%_pkgconfigdir/*.pc
%exclude %_libdir/libtls.so
%exclude %_pkgconfigdir/libtls.pc

%files doc
%_man3dir/*
%exclude %_man3dir/tls_*

%files -n libcrypto-LibreSSL
%dir %_sysconfdir/%oname/
%_sysconfdir/%oname/*
%_libdir/libcrypto.so.*

%files -n libssl-LibreSSL
%_libdir/libssl.so.*

%files -n libtls
%_libdir/libtls.so.*

%files -n libtls-devel
%_includedir/tls.h
%_libdir/libtls.so
%_pkgconfigdir/libtls.pc

%files -n libtls-doc
%_man3dir/tls_*

%files -n netcat-tls
%_bindir/nc
%_bindir/netcat
%_man1dir/nc.*
%_man1dir/netcat.*

%changelog
* Wed Aug 03 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.4.2-alt1
- 2.4.2
- LibreSSL
  + Bug fixes and improvements:
    - Fixed loading default certificate locations with openssl s_client.
    - Ensured OSCP only uses and compares GENERALIZEDTIME values as per
      RFC6960. Also added fixes for OCSP to work with intermediate
      certificates provided in responses.
    - Improved behavior of arc4random on Windows to not appear to leak
      memory in debug tools, reduced privileges of allocated memory.
    - Fixed incorrect results from BN_mod_word() when the modulus is too
      large, thanks to Brian Smith from BoringSSL.
    - Correctly handle an EOF prior to completing the TLS handshake in
      libtls.
    - Improved libtls ceritificate loading and cipher string validation.
    - Updated libtls cipher group suites into four categories:
      - "secure"   (TLSv1.2+AEAD+PFS)
      - "compat"   (HIGH:!aNULL)
      - "legacy"   (HIGH:MEDIUM:!aNULL)
      - "insecure" (ALL:!aNULL:!eNULL)
      This allows for flexibility and finer grained control, rather than
      having two extremes.
    - Limited support for 'backward com
- openssl-LibreSSL:
  + rename package from LibreSSL-openssl
  + remove conflict with openssl
  + rename binary and manpages fro openssl to openssl-LibreSSL
  + move some man pages to LibreSSL-doc package
- netcat-tls:
  + rename package from netcat-openbsd
  + adopt many of original netcat alt and owl patches

* Sun Jun 19 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.3.6-alt1
- 2.3.6
- Correct a problem that prevents the DSA signing algorithm from running
  in constant time even if the flag BN_FLG_CONSTTIME is set.

* Wed Jun 01 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.3.5-alt1
- 2.3.5

* Tue May 03 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.3.4-alt1
- 2.3.4
- Fix multiple vulnerabilities in libcrypto relating to ASN.1 and encoding
  (From OpenSSL):
  + Memory corruption in the ASN.1 encoder (CVE-2016-2108)
  + Padding oracle in AES-NI CBC MAC check (CVE-2016-2107)
  + EVP_EncodeUpdate overflow (CVE-2016-2105)
  + EVP_EncryptUpdate overflow (CVE-2016-2106)
  + ASN.1 BIO excessive memory allocation (CVE-2016-2109)
- Minor build fixes.
- LibreSSL-openssl
  + Added conflict to openssl-doc

* Tue May 3 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.3.3-alt2
- LibreSSL-doc
  + Add conflict: openssl-doc.
- libtls-doc
  + Build as noarch
- libcrypto-LibreSSL
  + "/etc/libressl" directory is owned by package now.

* Thu Apr 21 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.3.3-alt1
- Initial build.
