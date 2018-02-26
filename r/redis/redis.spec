Name: redis
Version: 2.6.10
Release: alt1

Summary: Redis is an advanced key-value store

Group: System/Libraries
License: New BSD License
Url: http://redis.io/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://redis.googlecode.com/files/%name-%version.tar

Source1: %name.conf
Source2: redis-benchmark.1
Source3: redis-cli.1
Source4: redis-server.1
Source5: redis-cli.bash_completion
Source6: redis-server.logrotate
Source7: redis.init
Source8: redis.sysconfig
Source9: redis.service

# for check section
BuildPreReq: tcl >= 8.5

%description
Redis is an advanced key-value store. It is similar to memcached but
the dataset is not volatile, and values can be strings, exactly like in
memcached, but also lists, sets, and ordered sets. All this data types can
be manipulated with atomic operations to push/pop elements, add/remove
elements, perform server side union, intersection, difference between
sets, and so forth. Redis supports different kind of sorting abilities.

In order to be very fast but at the same time persistent the whole dataset
is taken in memory, and from time to time saved on disc asynchronously
(semi persistent mode) or alternatively every change is written into an
append only file (fully persistent mode). Redis is able to rebuild the
append only file in background when it gets too big.

Redis supports trivial to setup master-slave replication, with very
fast non-blocking first synchronization, auto reconnection on net split,
and so forth.

Redis is written in ANSI C and works in most POSIX systems like Linux,
*BSD, Mac OS X, Solaris, and so on. Redis is free software released under
the very liberal BSD license. Redis is reported to compile and work
under WIN32 if compiled with Cygwin, but there is no official support
for Windows currently.

%define redis_user      _redis
%define redis_group     _redis

%prep
%setup
%__subst 's|\$(CCOPT) \$(DEBUG) \$(OBJ)|\$(OBJ) \$(CCOPT) \$(DEBUG)|g' src/Makefile

%build
%make_build CXXFLAGS="%{optflags}" CFLAGS="%{optflags}"

%install
%makeinstall_std PREFIX=%buildroot%prefix
mkdir -p %buildroot%_sbindir/
mkdir -p %buildroot%_sysconfdir/%name
install -m644 %SOURCE1 %buildroot%_sysconfdir/%name/
mv %buildroot%_bindir/redis-server %buildroot%_sbindir/

mkdir -p %buildroot%_localstatedir/%name
mkdir -p %buildroot%_logdir/%name

mkdir -p %buildroot%_man1dir
install -m 644 %SOURCE2 %buildroot%_man1dir/
install -m 644 %SOURCE3 %buildroot%_man1dir/
install -m 644 %SOURCE4 %buildroot%_man1dir/

mkdir -p %buildroot%_sysconfdir/bash_completion.d
install -m 644 %SOURCE5 %buildroot%_sysconfdir/bash_completion.d/redis-cli

mkdir -p %buildroot%_logrotatedir
install -m 640 %SOURCE6 %buildroot%_logrotatedir/redis-server

mkdir -p  %buildroot%_initdir
install -m 0755 %SOURCE7 %buildroot%_initdir/%name

mkdir -p %buildroot%_sysconfdir/sysconfig
install -m 0640 %SOURCE8 %buildroot%_sysconfdir/sysconfig/%name

mkdir -p  %buildroot%_unitdir
install -m 0755 %SOURCE9 %buildroot%_unitdir/%name.service

mkdir -p  %buildroot%_sysconfdir/tmpfiles.d
echo 'd /var/run/%name 0775 root %redis_group' >> %buildroot%_sysconfdir/tmpfiles.d/%name.conf

%pre
# Add the "_redis" user
%_sbindir/groupadd -r -f %redis_group 2>/dev/null ||:
%_sbindir/useradd  -r -g %redis_group -c 'Redis daemon' \
        -s /dev/null -d /var/lib/redis %redis_user 2>/dev/null ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%doc COPYING 00-RELEASENOTES README BUGS

%attr(0750,root,%redis_group) %dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/redis.conf

%config %_logrotatedir/redis-server
%config %_sysconfdir/bash_completion.d/redis-cli
%config %_sysconfdir/tmpfiles.d/%name.conf
%attr(0750,root,%redis_group) %config(noreplace) %_sysconfdir/sysconfig/%name
%config %_initdir/%name
%_unitdir/%name.service

%_bindir/redis-check-aof
%_bindir/redis-check-dump
%_bindir/redis-cli
%_bindir/redis-benchmark
%_sbindir/redis-server

%_man1dir/*

%attr(0770,root,%redis_group) %dir %_localstatedir/%name
%attr(0770,root,%redis_group) %dir %_logdir/%name


%changelog
* Wed Feb 27 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 2.6.10-alt1
- new version (2.6.10) (ALT #28374)
- create temporary dir

* Tue May 15 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4.7-alt2
- add systemd unit file (ALT #27334)

* Mon Feb 13 2012 Nikolay A. Fetisov <naf@altlinux.ru> 2.4.7-alt1
- new version (2.4.7)

* Sun Jan 29 2012 Nikolay A. Fetisov <naf@altlinux.ru> 2.4.6-alt1
- new version (2.4.6) (Closes: #26869)

* Fri Jan 06 2012 Nikolay A. Fetisov <naf@altlinux.ru> 2.4.5-alt1
- new version (2.4.5) (Closes: #26782)

* Mon Oct 24 2011 Nikolay A. Fetisov <naf@altlinux.ru> 2.4.1-alt1
- new version (2.4.1) (Closes: #26496)
- adding init script
- adding logrotate script
- moving default config file to the /etc/redis/

* Fri Sep 02 2011 Vitaly Lipatov <lav@altlinux.ru> 2.2.12-alt1
- new version (2.2.12) with rpmbs script (ALT bug #26131)

* Wed Apr 13 2011 Mykola Grechukh <gns@altlinux.ru> 2.2.4-alt1
- new version 2.2.4

* Tue Nov 09 2010 Vitaly Lipatov <lav@altlinux.ru> 2.0.4-alt1
- new version 2.0.4 (with rpmrb script) (ALT bug #24507)

* Sat Oct 16 2010 Vitaly Lipatov <lav@altlinux.ru> 2.0.3-alt1
- new version 2.0.3 (with rpmrb script) (ALT bug #24322)

* Thu Oct 07 2010 Vitaly Lipatov <lav@altlinux.ru> 2.0.2-alt1
- new version 2.0.2 (with rpmrb script) (ALT bug #24222)

* Mon Sep 13 2010 Nick S. Grechukh <gns@altlinux.ru> 2.0.1-alt1
- new stable version

* Sun Dec 13 2009 Vitaly Lipatov <lav@altlinux.ru> 1.1.91-alt1
- initial build for ALT Linux Sisyphus
