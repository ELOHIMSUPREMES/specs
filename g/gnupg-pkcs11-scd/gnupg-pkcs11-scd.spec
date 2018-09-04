%def_disable LibreSSL
%def_enable openssl
%def_disable gnutls

Name: gnupg-pkcs11-scd
Version: 0.9.2
Release: alt1

Summary: A GnuPG PKCS#11 token daemon
Group: System/Configuration/Hardware
License: BSD
Url: https://github.com/alonbl/gnupg-pkcs11-scd

Source: %name-%version.tar

%if_enabled LibreSSL
BuildRequires: LibreSSL-devel
%else %if_enabled openssl
BuildRequires: libssl-devel
%endif
%if_enabled gnutls
BuildRequires: libgnutls-devel
%endif
BuildRequires: libassuan-devel
BuildRequires: libgcrypt-devel
BuildRequires: libgpg-error-devel
BuildRequires: libpkcs11-helper-devel

%description
gnupg-pkcs11 is a project to implement a BSD-licensed smart-card daemon to
enable the use of PKCS#11 tokens with GnuPG.

PKCS#11 is the de-facto standard for accessing cryptographic tokens, and thus
we strongly disagree with WK\'s attitude towards it.

%prep
%setup

%build
%autoreconf
%configure --enable-proxy --localstatedir=%_var
%make_build

%install
%makeinstall_std

%check
#%make check

%files
%_bindir/*
%exclude %_docdir/%name/COPYING
%_docdir/%name/README
%_docdir/%name/*.conf.example
%_man1dir/*.1.*

%changelog
* Tue Sep 04 2018 Paul Wolneykien <manowar@altlinux.org> 0.9.2-alt1
- Switch back to OpenSSL.
- Update to version 0.9.2.

* Sat Mar 24 2018 Paul Wolneykien <manowar@altlinux.org> 0.9.1-alt2
- Build with LibreSSL.

* Fri Mar 23 2018 Paul Wolneykien <manowar@altlinux.org> 0.9.1-alt1
- gnupg-pkcs11-scd-0.9.1 (thx Alon Bar-Lev).
- proxy: systemd: enable user's group using SupplementaryGroups (thx Alon Bar-Lev).
- scdaemon: introduce GNUPG_PKCS11_SOCKETDIR environment (thx Alon Bar-Lev).
- build: support freebsd usock creds (thx Alon Bar-Lev).
- post gnupg-pkcs11-scd-0.9.0 (thx Alon Bar-Lev).

* Wed Feb 07 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.0-alt2
- Fixed localstatedir location.

* Fri Sep 15 2017 Paul Wolneykien <manowar@altlinux.org> 0.9.0-alt1
- Version 0.9.0: Initial build.
