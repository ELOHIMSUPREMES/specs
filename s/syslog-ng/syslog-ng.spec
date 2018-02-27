#!TODO
# systemd support (trivial)
# chroot support
# improve modules packaging (add config examples)

%def_enable	geoip
%def_enable	smtp
%def_enable	json
%def_disable	amqp
%def_enable	mongodb

Name: syslog-ng
Version: 3.4.7
Release: alt1

Summary: syslog-ng daemon
Group: System/Kernel and hardware
License: GPL
URL: http://www.balabit.com/products/syslog_ng/
Provides: syslogd-daemon
Prereq:	syslog-common
Conflicts: klogd < 1.4.1-alt7

Packager: Sergey Alembekov <rt@altlinux.ru>

Source: http://www.balabit.com/downloads/files/syslog-ng/sources/%{version}/source/%{name}_%{version}.tar.gz
Patch1: %name-%version-%release.patch

# Automatically added by buildreq on Fri Apr 19 2013 (-bi)
# optimized out: elfutils libcom_err-devel libkrb5-devel pkg-config python-base python-modules
# base config:
# + SSL/TLS
# + PCRE
# + SQL
BuildRequires: flex glib2-devel libcap-devel libdbi-devel libeventlog-devel >= 0.2.13 libnet2-devel libpcre-devel libpopt-devel libssl-devel libuuid-devel libwrap-devel libivykis-devel xsltproc docbook-style-xsl

%if_enabled geoip
BuildRequires: libGeoIP-devel
%endif
%if_enabled json
BuildRequires: libjson-devel
%endif
%if_enabled smtp
BuildRequires: libesmtp-devel
%endif
%if_enabled amqp
BuildRequires: librabbitmq-c-devel
%endif
%if_enabled mongodb
BuildRequires: libmongo-client-devel
%endif


%description
syslog-ng, as the name shows, is a syslogd replacement, but with new
functionality for the new generation. The original syslogd allows
messages only to be sorted based on priority/facility pairs; syslog-ng
adds the possibility to filter based on message contents using regular
expressions. The new configuration scheme is intuitive and powerful.
Forwarding logs over TCP and remembering all forwarding hops makes it
ideal for firewalled environments.

%package libdbi
Summary: libdbi support for %{name}
Group: System/Libraries

%description libdbi
This module supports a large number of database systems via libdbi.

%if_enabled geoip
%package geoip
Summary: GeoIP support for %{name}
Group: System/Libraries

%description geoip
This module provides a function to get GeoIP info from an IPv4 address.
%endif

%if_enabled smtp
%package smtp
Summary: SMTP destination support for %{name}
Group: System/Libraries

%description smtp
This module provides SMTP destination support for %{name}.
%endif

%if_enabled json
%package json
Summary: JSON support for %{name}
Group: System/Libraries

%description json
This module provides JSON parsing & formatting support for %{name}.
%endif

%if_enabled amqp
%package amqp
Summary: AMQP support for %{name}
Group: System/Libraries

%description amqp
This module provides AMQP destination support for %{name}.
%endif

%if_enabled mongodb
%package mongodb
Summary: mongodb support for %{name}
Group: System/Libraries

%description mongodb
This module supports the mongodb database via libmongo-client.
%endif

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release libeventlog-devel libivykis-devel

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.


%prep
%setup -q -n %{name}_%{version}
%patch1 -p1
%if_enabled amqp
pushd modules/afamqp/rabbitmq-c
tar -xf ../../../altlinux/rabbitmq-c-v0.3.0-80-gc9f6312.tar.gz
autoreconf -i
popd
%endif

# fix perl path
%{__sed} -i 's|^#!/usr/local/bin/perl|#!%{__perl}|' contrib/relogger.pl

%build
skip_submodules=1 ./autogen.sh
%configure \
 --sbindir=/sbin \
 --sysconfdir=%_sysconfdir/%name \
 --localstatedir=/var/lib/syslog-ng \
 --datadir=%_datadir/%name \
 --mandir=%_mandir \
 --with-ivykis=system \
 --with-pidfile-dir=/var/run \
 --with-module-dir=%_libdir/%name \
 --enable-ipv6 \
 --enable-dynamic-linking \
 --enable-tcp-wrapper \
 --enable-spoof-source \
 --with-embedded-crypto \
 %{subst_enable geoip} \
 %{subst_enable smtp} \
 %{subst_enable json} \
 %{subst_enable amqp} \
%if_enabled mongodb
 %{subst_enable mongodb} \
 --with-libmongo-client=system
%endif

# fixed libraries path in RPATH
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build XSL_STYLESHEET=/usr/share/xml/docbook/xsl-stylesheets/manpages/docbook.xsl

%install
mkdir -p %buildroot%_initdir
make DESTDIR=%buildroot sbindir=/sbin sysconfdir=%_sysconfdir/%name \
  mandir=%_mandir prefix=%prefix install

install -m755 -D -p altlinux/%name.init %buildroot%_initdir/%name
install -m640 -D -p altlinux/%name.conf %buildroot%_sysconfdir/%name/%name.conf
install -m640 -D -p altlinux/%name.sysconfig %buildroot%_sysconfdir/sysconfig/%name

install -m644 -p config.h %buildroot%_includedir/%name

mkdir -p %buildroot%_localstatedir/%name
mkdir -p %buildroot%_sysconfdir/%name/conf.d 

find %buildroot -name "*.la" -exec rm -f {} +

%post
%post_service %name
if [ $1 = 1 ]; then
    [ -x /sbin/syslogd ] && /sbin/chkconfig --level 2345 syslogd off ||:
fi

%triggerpostun -- %name <= 3.0.10-alt1
if [ -f %_sysconfdir/%name.conf.rpmsave ]; then
	echo "legacy configuration detected, new config moved to %_sysconfdir/%name"
	echo "please review and apply local changes from %_sysconfdir/%name.conf.rpmsave config!"
fi

%preun
%preun_service %name
if [ $1 = 0 ]; then
    [ -x /sbin/syslogd ] && /sbin/chkconfig --level 2345 syslogd on ||:
fi

%files
%doc AUTHORS NEWS COPYING
%doc doc/security/*.txt
%doc contrib/{syslog2ng,syslog-ng.vim,relogger.pl,syslog-ng.conf.doc}

%dir %_sysconfdir/%name
%dir %_sysconfdir/%name/patterndb.d
%dir %_sysconfdir/%name/conf.d
%config(noreplace) %_sysconfdir/%name/%name.conf
%config(noreplace) %_sysconfdir/%name/scl.conf
%config(noreplace) %_sysconfdir/sysconfig/%name
%_initdir/syslog-ng*

/sbin/syslog-ng
/sbin/syslog-ng-ctl
%_bindir/loggen
%_bindir/pdbtool
%_bindir/update-patterndb

%dir %_libdir/%name
# basic plugin set
%_libdir/%name/libaffile.so
%_libdir/%name/libafprog.so
%_libdir/%name/libafsocket-notls.so
%_libdir/%name/libafsocket-tls.so
%_libdir/%name/libafsocket.so
%_libdir/%name/libafuser.so
%_libdir/%name/libbasicfuncs.so
%_libdir/%name/libconfgen.so
%_libdir/%name/libcryptofuncs.so
%_libdir/%name/libcsvparser.so
%_libdir/%name/libdbparser.so
%_libdir/%name/libsyslogformat.so
%_libdir/%name/libsystem-source.so
%_libdir/lib%name-%version.so

%dir %_datadir/%name
%dir %_datadir/%name/include
%dir %_datadir/%name/xsd
%_datadir/%name/include/*
%_datadir/%name/xsd/*

%_man1dir/*
%_man5dir/*
%_man8dir/*

%dir %_localstatedir/%name

%files libdbi
%_libdir/%name/libafsql.so

%if_enabled geoip
%files geoip
%_libdir/%name/libtfgeoip.so
%endif

%if_enabled smtp
%files smtp
%_libdir/%name/libafsmtp.so
%endif

%if_enabled json
%files json
%_libdir/%name/libjson-plugin.so
%endif

%if_enabled amqp
%files amqp
%_libdir/%name/libafamqp.so
%endif

%if_enabled mongodb
%files mongodb
%_libdir/%name/libafmongodb.so
%endif

%files devel
%dir %_includedir/%name
%_includedir/%name/*.h
%dir %_datadir/%name/tools
%_datadir/%name/tools/*

%_libdir/lib%name.so
%_libdir/pkgconfig/%name.pc

%changelog
* Thu Dec 26 2013 Sergey Y. Afonin <asy@altlinux.ru> 3.4.7-alt1
- 3.4.7 (git20131225)

* Thu Dec 05 2013 Sergey Y. Afonin <asy@altlinux.ru> 3.4.6-alt1.git20131204
- 3.4.6 (git20131204)

* Wed Sep 11 2013 Sergey Y. Afonin <asy@altlinux.ru> 3.4.3-alt2.git20130813
- changed default permissions (ALT #29312)

* Thu Aug 15 2013 L.A. Kostis <lakostis@altlinux.ru> 3.4.3-alt1.git20130813
- Updated to v3.0.10-1507-g64d670f GIT.

* Sun Jun 02 2013 L.A. Kostis <lakostis@altlinux.ru> 3.4.1-alt1.git20130528
- packaging changes (see TODO for full list):
  + .conf: sync config file with RedHat/upstream changes.
  + .spec: notify about configuration changes.
  + .spec: enhance doc section.
  + .spec: split plugins to separate packages.
  + .spec: fix rpath issue..
  + .spec: fix module_dir.

* Tue May 28 2013 L.A. Kostis <lakostis@altlinux.ru> 3.4.1-alt0.git20130528
- Prepare for first build.
- Use GIT 20130528 snapshot.

* Mon Apr 15 2013 Sergey Y. Afonin <asy@altlinux.ru> 3.4.1-alt0
- 3.4.1 (some parts of 3.4.1-1.fc19 spec used)

* Mon Jan 31 2011 Sergey Alembekov <rt@altlinux.ru> 3.0.10-alt1
- 3.0.10

* Tue Dec 07 2010 Igor Vlasenko <viy@altlinux.ru> 3.0.5-alt2.1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Tue Mar 09 2010 Sergey Alembekov <rt@altlinux.ru> 3.0.5-alt2.1
- #23070 again :)

* Mon Mar 08 2010 Sergey Alembekov <rt@altlinux.ru> 3.0.5-alt2
- new syntax for default configuration; (#23070)
- fix pid creation (#23071)

* Thu Jan 28 2010 Sergey Alembekov <rt@altlinux.ru> 3.0.5-alt1
- 3.0.5

* Mon Jan 12 2009 Dmitry Lebkov <dlebkov@altlinux.ru> 2.1.3-alt1
- 2.1.3

* Sun Apr 06 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 2.0.9-alt1
- 2.0.9
- init-script changes:
  + add 'check' action -- validate syslog-ng.conf syntax;
  + validate syslog-ng.conf syntax before start|restart|reload;
- change default configuration:
  + 'MARK' message every 5 min.;
  + 'STATS' message every 1 hour (#14686)

* Fri Feb 01 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 2.0.8-alt1
- 2.0.8

* Thu Jan 10 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 2.0.7-alt1
- 2.0.7

* Fri Jul 27 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 2.0.5-alt1
- 2.0.5
- add '--enable-tcp-wrapper' and '--enable-spoof-source'
  configure flags


* Sun Apr 01 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 2.0.3-alt1
- fix path for syslog-ng.persist

* Tue Mar 27 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 2.0.3-alt0
- 2.0.3

* Sat Feb 03 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 2.0.2-alt0
- 2.0.2

* Tue Jan 09 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 2.0.1-alt0
- 2.0.1

* Tue Apr 13 2004 Stanislav Ievlev <inger@altlinux.org> 1.6.2-alt2
- require resent libol (#3823)

* Wed Mar 10 2004 Stanislav Ievlev <inger@altlinux.org> 1.6.2-alt1
- 1.6.2

* Tue Sep 30 2003 Stanislav Ievlev <inger@altlinux.ru> 1.4.17-alt1.1
- don't made static link with libol
- update init-script
- fix building in hasher

* Thu Oct 31 2002 Nikita Gergel <fc@altlinux.ru> 1.4.17-alt1
- 1.4.17

* Sun Oct 27 2002 Nikita Gergel <fc@altlinux.ru> 1.4.16-alt2
- syslog-ng.conf patch

* Fri Oct 25 2002 Nikita Gergel <fc@altlinux.ru> 1.4.16-alt1
- 1.4.16

* Fri Oct 11 2002 Stanislav Ievlev <inger@altlinux.ru> 1.4.15-alt3
- security fix

* Thu Sep 19 2002 Stanislav Ievlev <inger@altlinux.ru> 1.4.15-alt2
- rebuild with gcc3

* Sat May 18 2002 Stanislav Ievlev <inger@altlinux.ru> 1.4.15-alt1
- 1.4.15

* Tue Feb 05 2002 Stanislav Ievlev <inger@altlinux.ru> 1.4.14-alt2
- sync with chrooted klogd

* Thu Dec 20 2001 Stanislav Ievlev <inger@altlinux.ru> 1.4.14-alt1
- 1.4.14

* Tue Sep 25 2001 Stanislav Ievlev <inger@altlinux.ru> 1.4.12-alt2
- added PreReq for syslog-common - general package for all syslogs.
- added some documentation

* Fri Jul 27 2001 Stanislav Ievlev <inger@altlinux.ru> 1.4.12-alt1
- 1.4.12

* Tue Jul 24 2001 Stanislav Ievlev <inger@altlinux.ru> 1.4.10-alt1
- Initial release for ALT Linux.

* Wed Jan 17 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.4.10-1mdk
- used srpm from John Johnson <jjohnson@linux-mandrake.com> :
	- Updated syslog-ng to version 1.4.

* Mon Nov 13 2000 Vincent Danen <vdanen@mandrakesoft.com> 1.4.8-2mdk
- specfile cleaning, use macros
- rewrote init file
- wrote proper syslog-ng.conf file based on syslog.conf
- patch so config goes in /etc not /etc/syslog-ng
- syslog-ng goes in /sbin not /usr/sbin

* Wed Nov 8 2000 John Johnson <jjohnson@linux-mandrake.com> 1.4.8-1mdk
- Made Mandrake rpm
