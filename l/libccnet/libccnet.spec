%define oname ccnet
Name: libccnet
Version: 1.4.2 
Release: alt6

Summary: Networking library for Seafile

Group: Networking/File transfer
License: GPLv3
Url: https://github.com/haiwen/ccnet

Packager: Konstantin Artyushkin <akv@altlinux.org>

# Source-url: https://seafile.googlecode.com/files/seafile-latest.tar.gz
Source: %name-%version.tar

# Automatically added by buildreq on Fri Sep 06 2013
# optimized out: glib2-devel gnu-config libgio-devel pkg-config python-base python-devel python-module-distribute python-module-zope python-modules
BuildRequires: libevent-devel libsearpc-devel >= 1.2.0 libsqlite3-devel libssl-devel libuuid-devel python-module-mwlib python-module-paste python-module-peak
BuildRequires: vala libzdb-devel
%description
Ccnet is a framework for writing networked applications in C

%package devel
Summary: Development files for %name
Requires: %name = %version-%release
Group: Networking/File transfer

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package server
Summary: ccnet server
Requires: %name = %version-%release
Group: Networking/File transfer

%description server
ccnet server files

%prep
%setup
%__subst s/\(DESTDIR\)// libccnet.pc.in

%build
%autoreconf
%configure --disable-static --disable-compile-demo \
	   --enable-server
#%make_build не работает
%make

%install
%makeinstall_std
#find %buildroot -name '*.la' -exec rm -f {} ';'

%files
#%doc AUTHORS README.markdown
%_libdir/*.so.*
%_bindir/%{oname}*
%python_sitelibdir/%oname/

%files server
%_bindir/%oname-server
%_bindir/%oname-servtool

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/%name.pc

%changelog
* Sun Aug 24 2014 Konstantin Artyushkin <akv@altlinux.org> 1.4.2-alt6
- +++ ccnet servre 

* Fri Aug 22 2014 Konstantin Artyushkin <akv@altlinux.org> 1.4.2-alt5
- 1.4.2-alt4

* Mon Aug 04 2014 Konstantin Artyushkin <akv@altlinux.org> 1.4.2-alt4
- new tag

* Mon Aug 04 2014 Konstantin Artyushkin <akv@altlinux.org> 1.4.2-alt3
- new version

* Mon Aug 04 2014 Konstantin Artyushkin <akv@altlinux.org> 1.4.2-alt2
- chabge alt3 for multibuild

* Mon Aug 04 2014 Konstantin Artyushkin <akv@altlinux.org> 1.4.2-alt2
- 1.4.2-alt1
- + vala

* Mon Aug 04 2014 Konstantin Artyushkin <akv@altlinux.org> 1.4.2-alt1
update to 1.4.2

* Sun Nov 10 2013 Denis Baranov <baraka@altlinux.ru> 1.3.6-alt2
- Check repos git

* Fri Nov 08 2013 Denis Baranov <baraka@altlinux.ru> 1.3.6-alt1
- Update to 1.3.6

* Fri Sep 06 2013 Denis Baranov <baraka@altlinux.ru> 1.3.4-alt2
- Rename package to libccnet

* Fri Sep 06 2013 Denis Baranov <baraka@altlinux.ru> 1.3.4-alt1
- initial build for ALT Linux Sisyphus

* Tue Jun 18 2013 Stefan Lohmaier <stefan.lohmaier@stefanlohmaier.de> - 1.3.4-1
- updated for seafile 1.7.0
* Thu May 30 2013 Stefan Lohmaier <stefan.lohmaier@stefanlohmaier.de> - 1.1.0-1
- added description from github
- moved to 1.1.0 from seafile 1.6.1
* Mon Jan 28 2013 Robin Lee <cheeselee@fedoraproject.org> - 1.0.1-1
- Initial package
