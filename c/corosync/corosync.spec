Name: corosync
Summary: The Corosync Cluster Engine and Application Programming Interfaces
Version: 3.0.1
Release: alt1
License: BSD
Group: System/Base
Url: http://corosync.github.io/corosync/

# https://github.com/corosync/corosync.git
Source0: %name-%version.tar
Source1: corosync-init
Source2: corosync-notifyd-init

#fixed systemd units
Source11: corosync.service

Provides: corosync2 = %version-%release
Obsoletes: corosync2 < %version-%release
Requires: lib%name = %version-%release

BuildRequires: doxygen libqb-devel libstatgrab-devel libnet-snmp-devel libdbus-devel systemd-devel libxslt-devel libaugeas-devel
BuildRequires: augeas graphviz libsocket-devel zlib-devel libknet-devel

%define _localstatedir %_var

%description
This package contains the Corosync Cluster Engine Executive, several
default APIs and libraries, default configuration files, and an init
script.

%package -n lib%name
Summary: The Corosync Cluster Engine Libraries
Group: System/Libraries
Conflicts: libcorosync
Provides: libcorosync2 = %version-%release
Obsoletes: libcorosync2 < %version-%release

%description -n lib%name
This package contains corosync libraries.

%package -n lib%name-devel
Summary: The Corosync Cluster Engine Development Kit
Group: Development/C
Requires: lib%name = %version-%release
Provides: libcorosync2-devel = %version-%release
Obsoletes: libcorosync2-devel < %version-%release

%description -n lib%name-devel
This package contains include files and man pages used to develop using
The Corosync Cluster Engine APIs.

%prep
%setup

echo %version > .version
#if release version (= tarball)
#in checked-out repository it uses git describe
cp .version .tarball-version
mkdir -p m4

%build
%autoreconf

%configure \
	--enable-watchdog \
	--enable-monitoring \
	--enable-snmp \
	--enable-dbus \
	--enable-systemd \
	--enable-xmlconf \
	--enable-augeas \
	--with-systemddir=%_unitdir


%make_build

%install
%makeinstall_std
%makeinstall_std -C init

install -p -D -m644 %buildroot%_sysconfdir/corosync/corosync.conf.example %buildroot%_sysconfdir/corosync/corosync.conf

install -p -D -m644 %_builddir/%name-%version/conf/corosync-signals.conf %buildroot/%_sysconfdir/dbus-1/system.d/corosync-signals.conf

#Initscripts
install -p -D -m755 %SOURCE1 %buildroot%_initdir/corosync
install -p -D -m755 %SOURCE2 %buildroot%_initdir/corosync-notifyd

#fixed native systemd units
install -p -D -m644 %SOURCE11 %buildroot%_unitdir/corosync.service

## tree fixup
# drop static libs
rm -f %buildroot%_libdir/*.a
# drop docs and html docs for now
rm -rf %buildroot%_docdir/*

mkdir -p %buildroot%_sysconfdir/sysconfig

# /etc/sysconfig/corosync-notifyd
install -m 644 tools/corosync-notifyd.sysconfig.example %buildroot%_sysconfdir/sysconfig/corosync-notifyd
# /etc/sysconfig/corosync
install -m 644 init/corosync.sysconfig.example %buildroot%_sysconfdir/sysconfig/corosync

%check
%make check

%post
%post_service corosync
%post_service corosync-notifyd

%preun
%preun_service corosync
%preun_service corosync-notifyd

%files
%doc AUTHORS README* LICENSE
%_bindir/*
%_sbindir/*
%dir %_sysconfdir/corosync
%dir %_sysconfdir/corosync/service.d
%dir %_sysconfdir/corosync/uidgid.d
%config(noreplace) %_sysconfdir/corosync/corosync.conf
%config(noreplace) %_sysconfdir/corosync/corosync.conf.example
%config(noreplace) %_sysconfdir/sysconfig/corosync-notifyd
%config(noreplace) %_sysconfdir/sysconfig/corosync
%config(noreplace) %_sysconfdir/logrotate.d/corosync
%_unitdir/corosync.service
%_unitdir/corosync-notifyd.service
%_sysconfdir/dbus-1/system.d/corosync-signals.conf
%_initrddir/corosync
%_initrddir/corosync-notifyd
%_datadir/corosync
%_datadir/snmp/mibs/COROSYNC-MIB.txt
%_datadir/augeas/lenses/*
%dir %_localstatedir/lib/corosync
%attr(700, root, root) %_localstatedir/log/cluster
%_man5dir/*
%_man7dir/*
%_man8dir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/corosync
%_libdir/*.so
%_pkgconfigdir/*
%_man3dir/*

%changelog
* Tue Mar 05 2019 Alexey Shabalin <shaba@altlinux.org> 3.0.1-alt1
- 3.0.1

* Thu Jun 29 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.4.1-alt2
- Fixed build for new toolchain

* Wed Sep 14 2016 Alexey Shabalin <shaba@altlinux.ru> 2.4.1-alt1
- 2.4.1
- rename to corosync

* Fri Sep 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.4-alt1
- Version 2.3.4

* Mon Nov 11 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 2.3.2-alt1
- New version

* Mon Aug 12 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 2.3.1-alt1
- New version

* Tue Feb 19 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 2.3.0-alt1
- New version

* Sun Sep 20 2011 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.4.1-alt1
- Initial build (using Fedora spec)
