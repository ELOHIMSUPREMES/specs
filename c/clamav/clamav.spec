%def_without milter

%def_with ownconfdir

%if_with ownconfdir
%define clamconfdir /etc/clamav
%else
%define clamconfdir /etc
%endif

%define rctag %nil

Name: clamav
Version: 0.97.8
Release: alt1

Packager: Victor Forsiuk <force@altlinux.org>

Summary: Clam Antivirus scanner
License: GPLv2 only
Group: File tools

URL: http://www.clamav.net/
%ifdef snap
Source0: http://www.clamav.net/snapshot/clamav-devel-%snap.tar.gz
%else
Source0: http://downloads.sourceforge.net/clamav/clamav-%{version}%{rctag}.tar.gz
%endif

Source1: clamav.init
Source2: clamav.sysconfig

Source4: freshclam.cron
Source5: freshclam.logrotate
Source6: clamav.logrotate

Source10: clamav-milter.init
Source11: clamav-milter.sysconfig
Source12: clamav-milter.msg
Source13: clamav-milter.whitelist
Source14: clamav-milter.conf

Source20: virusstat-perIP
Source21: virusstat-perIP-PrevHour
Source22: virusstat-total
Source23: virusstat.cron.example

Patch1: clamav-0.96-config.patch
Patch2: freshclam-0.96.1-config.patch

Patch20: clamav-0.97.2-libs.private.patch

# Package with clamd should require libclamav, not vice versa.
# Corresponding libclamav version need to be updated before, or clamd restart may fail!
Requires: lib%{name} = %version-%release

# Database updater moved to separated package.
Requires: clamav-freshclam = %version-%release

# postinstall uses subst utility
Requires(post): sed >= 1:3.02-alt1

# sed used by configure script
BuildRequires: sed
# Automatically added by buildreq on Sat Oct 31 2009
BuildRequires: gcc-c++ bzlib-devel git-core libcheck-devel libncurses-devel subversion zlib-devel

# ...and edited manually to separate conditional buildreqs
%{?_with_milter:BuildRequires: sendmail-devel}

# for snapshots
%{?snap: BuildRequires: automake}

%description
Clam AntiVirus is an anti-virus toolkit for Unix. The main purpose of this
software is the integration with mail servers (attachment scanning). The package
provides a flexible and scalable multi-threaded daemon, a commandline scanner,
and a tool for automatic updating via Internet. The programs are based on a
shared library distributed with the Clam AntiVirus package, which you can use in
your own software.

%package -n lib%{name}
Summary: Shared libraries for clamav
Group: Development/C

%description -n lib%{name}
Shared libraries for clamav.

%package -n lib%{name}-devel
Summary: Development header files and libraries for clamav
Group: Development/C
Requires: %name = %version

%description -n lib%{name}-devel
This package contains the development header files and libraries
necessary to develop clamav client applications.

%package milter
Summary: clamav-milter for sendmail
Group: File tools
Requires: clamav = %version, /usr/sbin/sendmail

%description milter
This package contains the filter for Sendmail necessary to
integrate clamav with Sendmail MTA.

%package manual
Summary: ClamAV User Manual
Group: Books/Howtos
BuildArch: noarch

%description manual
This package contains user manual for clamav in HTML format.

%package freshclam
Summary: Auto-updater for the Clam Antivirus scanner virus signature files
Group: File tools

%description freshclam
This package contains programs which can be used to update the clamav anti-virus
database automatically. It uses the freshclam(1) utility for this task.

%prep
%setup %{?snap: -n clamav-devel-%snap} %{?rctag: -n clamav-%{version}%{rctag}}
%patch1 -p1
%patch2 -p2

%patch20 -p1

%build
%{?snap: aclocal}

# See http://www.gossamer-threads.com/lists/clamav/users/41630
#rm -f configure.in

# fixed RPATH issue (0.97.3 tarball built with wrong libtool)
%{!?snap: %autoreconf}

# --disable-clamav: Disable test for clamav user/group
%configure \
	--sysconfdir=%clamconfdir \
	--enable-experimental \
	--enable-clamdtop \
	--disable-clamav \
	--with-user=mail \
	--with-group=mail \
	--with-dbdir=/var/lib/%name %{?_with_milter: --enable-milter}

# Safety belt for IPv6 enabling. We want to build clamav with IPv6 support,
# but can not rely on configure check as it can fail if build host set up
# as IPv4 only system.
echo >> clamav-config.h
echo "#ifndef SUPPORT_IPv6" >> clamav-config.h
echo "#define SUPPORT_IPv6 1" >> clamav-config.h
echo "#endif" >> clamav-config.h

%make_build

install -m644 %_sourcedir/virusstat* .

%install
%makeinstall_std

# fix config
subst 's|@@CLAMAVCONFDIR@@|%clamconfdir|' %buildroot%clamconfdir/freshclam.conf

%{!?_with_milter:rm -f %buildroot%_man1dir/clamav-milter*}

install -pD -m755 %_sourcedir/clamav.init %buildroot/etc/rc.d/init.d/clamd

install -pD %_sourcedir/clamav.sysconfig %buildroot/etc/sysconfig/clamd

%if_with milter
sed -e 's|@@CLAMAVCONFDIR@@|%clamconfdir|' < %_sourcedir/clamav-milter.sysconfig > %buildroot/etc/sysconfig/clamav-milter
install -m644 %_sourcedir/clamav-milter.conf %buildroot%clamconfdir/
install -m755 %_sourcedir/clamav-milter.init %buildroot/etc/rc.d/init.d/clamav-milter
#install -m644 %_sourcedir/clamav-milter.whitelist %buildroot%clamconfdir/
#install -m644 %_sourcedir/clamav-milter.msg %buildroot%clamconfdir/
%endif

install -d %buildroot%_logdir/clamav
touch %buildroot%_logdir/clamav/clamd.log
touch %buildroot%_logdir/clamav/freshclam.log

# install the logrotate stuff
install -pD -m644 %_sourcedir/freshclam.logrotate %buildroot%_sysconfdir/logrotate.d/freshclam
install -m644 %_sourcedir/clamav.logrotate %buildroot%_sysconfdir/logrotate.d/clamav

# pid file dir
install -d %buildroot/var/run/clamav

# install html docs
mkdir -p %buildroot%_defaultdocdir/clamav-manual
rm -rf docs/html/CVS
install -m644 docs/html/* %buildroot%_defaultdocdir/clamav-manual

# remove non-packaged files
rm -f %buildroot%_libdir/*.la
rm -f %buildroot%_libdir/*.a
# databases is not installing in 0.97.5
if [ -d %buildroot/var/lib/clamav ] ; then
    rm -f %buildroot/var/lib/clamav/*.cvd
else
    mkdir -p %buildroot/var/lib/clamav
fi


install -d %buildroot%_sysconfdir/cron.d
cat <<EOF >%buildroot%_sysconfdir/cron.d/freshclam
30 * * * *       root    %_bindir/freshclam --quiet --daemon-notify
EOF

%if_without milter
rm -f %buildroot/%_man8dir/clamav-milter.*
%endif

%post
# Format of database changing occasionally. So removing database.
for FNAME in `ls --ignore=*.socket /var/lib/clamav`; do
    [ -h /var/lib/clamav/$FNAME ] && continue
    [ -d /var/lib/clamav/$FNAME ] && rm -rf /var/lib/clamav/$FNAME
    [ -f /var/lib/clamav/$FNAME ] && rm -f /var/lib/clamav/$FNAME
done

# randomize time of database updating (in order to distribute load on servers evenly)
RNDM=$[$RANDOM/555]
subst s/^[0-9]*/$RNDM/ %_sysconfdir/cron.d/freshclam

%post_service clamd

%preun
%preun_service clamd

%post milter
%post_service clamav-milter

%preun milter
%preun_service clamav-milter

%files
%doc docs/signatures.*
%doc virusstat*

%_bindir/clamdscan
%_bindir/clamscan
%_bindir/sigtool
%_bindir/clamdtop
%_bindir/clambc
%_sbindir/clamd
%config %_initdir/clamd
%{?_with_ownconfdir: %dir %clamconfdir}
%config(noreplace) %verify(not md5 size mtime) %clamconfdir/clamd.conf
%config(noreplace) %_sysconfdir/logrotate.d/clamav
%attr(640,root,root) %config(noreplace) %verify(not md5 size mtime) /etc/sysconfig/clamd
%_man1dir/clamdscan*
%_man1dir/clamscan*
%_man1dir/sigtool*
%_man1dir/clamdtop*
%_man1dir/clambc*
%_man5dir/*
%_man8dir/clamd*
%attr(3775,root,mail) %dir /var/lib/clamav
%attr(3775,root,mail) %ghost %dir /var/run/clamav
%attr(3771,root,mail) %dir %_logdir/clamav
%attr(640,mail,root) %ghost %_logdir/clamav/clamd.log

%files -n lib%{name}
%_libdir/lib*.so.*

%files freshclam
%{?_with_ownconfdir: %dir %clamconfdir}
%attr(3775,root,mail) %dir /var/lib/clamav
%attr(3775,root,mail) %ghost %dir /var/run/clamav
%attr(3771,root,mail) %dir %_logdir/clamav
%_bindir/freshclam
%_man1dir/freshclam*
%_bindir/clamconf
%_man1dir/clamconf*
%config(noreplace) %verify(not md5 size mtime) %clamconfdir/freshclam.conf
%config(noreplace) %_sysconfdir/cron.d/freshclam
%config(noreplace) %_sysconfdir/logrotate.d/freshclam
%attr(644,mail,mail) %ghost %_logdir/clamav/freshclam.log

%files -n lib%{name}-devel
%_bindir/clamav-config
%_libdir/lib*.so
%_libdir/pkgconfig/*
%_includedir/*.h

%files manual
%_defaultdocdir/clamav-manual

%if_with milter
%files milter
%_sbindir/clamav-milter
%config %_initdir/clamav-milter
%config(noreplace) %verify(not md5 size mtime) /etc/sysconfig/clamav-milter
%config(noreplace) %verify(not md5 size mtime) %clamconfdir/clamav-milter.conf
%_man8dir/clamav-milter.*
#config(noreplace) #verify(not md5 size mtime) %clamconfdir/clamav-milter.whitelist
#config(noreplace) #verify(not md5 size mtime) %clamconfdir/*.msg
%endif

%changelog
* Thu Apr 25 2013 Sergey Y. Afonin <asy@altlinux.ru> 0.97.8-alt1
- 0.97.8 (Security update)

* Fri Mar 22 2013 Sergey Y. Afonin <asy@altlinux.ru> 0.97.7-alt1
- 0.97.7

* Thu Oct 04 2012 Sergey Y. Afonin <asy@altlinux.ru> 0.97.6-alt1
- 0.97.6

* Mon Jun 25 2012 Sergey Y. Afonin <asy@altlinux.ru> 0.97.5-alt1
- 0.97.5 (CVE-2012-1457, CVE-2012-1458, CVE-2012-1459)
- added check of database to "restart" and "reload" functions of
  init script

* Fri Mar 30 2012 Sergey Y. Afonin <asy@altlinux.ru> 0.97.4-alt1
- 0.97.4

* Thu Dec 22 2011 Sergey Y. Afonin <asy@altlinux.ru> 0.97.3-alt2
- fixed RPATH issue
- more neatly hack for enable IPv6

* Thu Oct 20 2011 Sergey Y. Afonin <asy@altlinux.ru> 0.97.3-alt1
- 0.97.3 (CVE-2011-3627)

* Thu Aug 04 2011 Sergey Y. Afonin <asy@altlinux.ru> 0.97.2-alt1
- 0.97.2

* Tue Jun 21 2011 Sergey Y. Afonin <asy@altlinux.ru> 0.97.1-alt2
- added lsb init header to init scripts
- added check for /var/run/clamav directory in scripts

* Tue Jun 21 2011 Sergey Y. Afonin <asy@altlinux.ru> 0.97.1-alt1
- 0.97.1

* Fri Mar 11 2011 Sergey Y. Afonin <asy@altlinux.ru> 0.97-alt1
- 0.97
- disabled building clamav-milter subpackage
  (mailfromd encouraged to use as an alternative)

* Thu Dec 02 2010 Sergey Y. Afonin <asy@altlinux.ru> 0.96.5-alt1
- 0.96.5
- changed "sendmail" to "/usr/sbin/sendmail" in "Requires" of clamav-milter
- recreated clamav-milter's configuration (incompatible changes
  in clamav-milter since ClamAV 0.95)
- removed old patches for old clamav-milter

* Tue Nov 02 2010 Sergey Y. Afonin <asy@altlinux.ru> 0.96.4-alt1
- NMU
- 0.96.4

* Thu Sep 23 2010 Sergey Y. Afonin <asy@altlinux.ru> 0.96.3-alt1
- NMU
- 0.96.3

* Thu Aug 26 2010 Sergey Y. Afonin <asy@altlinux.ru> 0.96.2-alt2
- NMU
- fixed segfault when starting on SELinux
  (https://wwws.clamav.net/bugzilla/show_bug.cgi?id=2200)
- added 1 second delay when restart (in init script)

* Fri Aug 13 2010 Sergey Y. Afonin <asy@altlinux.ru> 0.96.2-alt1
- NMU
- 0.96.2

* Thu Jun 24 2010 Sergey Y. Afonin <asy@altlinux.ru> 0.96.1-alt1
- NMU
- 0.96.1
- added gcc-c++ to BuildRequires (needed for compile LLVM for bytecode compiler)
- enabled SubmitDetectionStats in freshclam.conf

* Sun Apr 11 2010 Sergey Y. Afonin <asy at altlinux.ru> 0.96-alt1.1
- NMU
- uploading in Sisyphus only

* Thu Apr 01 2010 Victor Forsiuk <force@altlinux.org> 0.96-alt1
- 0.96
- Build with IPv6 support.

* Sun Dec 13 2009 Sergey Y. Afonin <asy@altlinux.ru> 0.95.3-alt1.1
- NMU
- uploading in Sisyphus only

* Thu Nov 05 2009 Victor Forsyuk <force@altlinux.org> 0.95.3-alt1
- 0.95.3
- Package clamdtop.

* Mon Jun 22 2009 Sergey Y. Afonin <asy@altlinux.ru> 0.95.2-alt1
- NMU
- 0.95.2 (fixes: ALT#19770)
  (contains security fixes for CVE-2008-6680, CVE-2009-1241, CVE-2009-1270, CVE-2009-1371, CVE-2009-1372)

* Wed Nov 26 2008 Victor Forsyuk <force@altlinux.org> 0.94.2-alt1
- 0.94.2

* Wed Nov 05 2008 Victor Forsyuk <force@altlinux.org> 0.94.1-alt1
- 0.94.1

* Wed Sep 03 2008 Victor Forsyuk <force@altlinux.org> 0.94-alt1
- 0.94
- Package manual as noarch.

* Wed Jul 23 2008 Victor Forsyuk <force@altlinux.org> 0.93.3-alt1
- 0.93.3
- Fix initscript to run freshclam only when no virus databases available
  (fixes: ALT#16365).

* Tue Jun 10 2008 Victor Forsyuk <force@altlinux.org> 0.93.1-alt1
- 0.93.1
- clamdmon is gone.

* Tue Apr 15 2008 Victor Forsyuk <force@altlinux.org> 0.93-alt1
- 0.93 (contains security fixes: CVE-2008-1100, CVE-2008-1387)

* Tue Feb 12 2008 Victor Forsyuk <force@altlinux.org> 0.92.1-alt1
- 0.92.1
- Security fix for CVE-2008-0318.

* Mon Dec 17 2007 Victor Forsyuk <force@altlinux.org> 0.92-alt1
- 0.92

* Wed Oct 10 2007 Victor Forsyuk <force@altlinux.org> 0.92-alt0.rc2
- 0.92rc2

* Mon Sep 03 2007 Victor Forsyuk <force@altlinux.org> 0.91.2-alt1
- 0.91.2 (fixes for CVE-2007-4510, CVE-2007-4560).

* Tue Jul 17 2007 Victor Forsyuk <force@altlinux.org> 0.91.1-alt1
- 0.91.1 (fixes for CVE-2007-3726).

* Fri Jul 13 2007 Victor Forsyuk <force@altlinux.org> 0.91-alt1
- Fixes security bug: https://wwws.clamav.net/bugzilla/show_bug.cgi?id=555
  (CVE-2007-3725).
- Use of libcurl removed (should improve stability).

* Thu May 31 2007 Victor Forsyuk <force@altlinux.org> 0.90.3-alt1
- 0.90.3 (contains security related fixes).

* Fri Apr 13 2007 Victor Forsyuk <force@altlinux.org> 0.90.2-alt1
- 0.90.2 (contains security related fixes).

* Mon Mar 05 2007 Victor Forsyuk <force@altlinux.org> 0.90.1-alt1
- 0.90.1

* Thu Mar 01 2007 Victor Forsyuk <force@altlinux.org> 0.90-alt2
- Fix not expanded variable in freshclam config (ALT#10958).

* Wed Feb 14 2007 Victor Forsyuk <force@altlinux.org> 0.90-alt1
- 0.90
- Move clamconf to clamav-freshclam package.
- Cleaned up pkgconfig and clamav-config.

* Fri Feb 09 2007 Victor Forsyuk <force@altlinux.org> 0.90-alt0.2.rc3
- Rebuilt with libmilter.so.3.

* Fri Feb 02 2007 Victor Forsyuk <force@altlinux.org> 0.90-alt0.1.rc3
- 0.90 RC3.
- Fix ALT#10486: clamav-freshclam package should contain /var/lib/clamav.

* Tue Oct 31 2006 Victor Forsyuk <force@altlinux.org> 0.90-alt0.0.rc2
- 0.90 RC2
- Move post_service call to end of post-install script (thnx to Sergey Afonin).
- Move freshclam to separate package as it just updates signature databases that
  used by all software built around libclamav (such as havp, clement etc).
- Apply patch that fixes RH#202043.

* Thu Aug 10 2006 Victor Forsyuk <force@altlinux.ru> 0.88.4-alt1
- 0.88.4, fixed CVE-2006-4018.

* Wed Jul 26 2006 Victor Forsyuk <force@altlinux.ru> 0.88.3-alt1
- 0.88.3

* Thu May 04 2006 Victor Forsyuk <force@altlinux.ru> 0.88.2-alt1
- Fixes security issue in freshclam.

* Thu Apr 06 2006 Victor Forsyuk <force@altlinux.ru> 0.88.1-alt1
- 0.88.1
- Fixed CVE-2006-1614, CVE-2006-1615 and CVE-2006-1630.
- Patches for clamav-milter from Sergey Y. Afonin.

* Fri Jan 13 2006 Victor Forsyuk <force@altlinux.ru> 0.88-alt1
- 0.88

* Tue Nov 08 2005 Victor Forsyuk <force@altlinux.ru> 0.87.1-alt1
- 0.87.1
- Create clamd.log in postinstall script with correct owner and mode.
  Otherwise clamav-milter will be very unhappy :) (reported by asy@).

* Wed Sep 28 2005 Victor Forsyuk <force@altlinux.ru> 0.87-alt1
- 0.87

* Tue Jul 26 2005 Victor Forsyuk <force@altlinux.ru> 0.86.2-alt1
- 0.86.2

* Mon Jul 11 2005 Victor Forsyuk <force@altlinux.ru> 0.86.1-alt1
- 0.86.1.
- Enable scanning RAR archives in default config.
- Hack to define sendmail version used in clamav-milter code when
  building on boxes without sendmail installed.

* Tue May 17 2005 Victor Forsyuk <force@altlinux.ru> 0.85.1-alt1
- 0.85.1.

* Wed May 04 2005 Victor Forsyuk <force@altlinux.ru> 0.84-alt1
- 0.84 release.
- Allow replacement of rc.d service script during upgrades
  (i.e., remove "noreplace" in spec).

* Fri Apr 08 2005 Victor Forsyuk <force@altlinux.ru> 0.84-alt0.rc1
- Add clamdmon to package.
- Move HTML docs to separate package.

* Thu Feb 17 2005 Victor Forsyuk <force@altlinux.ru> 0.83-alt2
- clamav-milter tweaks from Sergey Afonin.

* Mon Feb 14 2005 Victor Forsyuk <force@altlinux.ru> 0.83-alt1
- 0.83.

* Mon Feb 07 2005 Victor Forsyuk <force@altlinux.ru> 0.82-alt1
- 0.82.

* Thu Jan 27 2005 Victor Forsyuk <force@altlinux.ru> 0.81-alt2
- 0.81.
- Fix from Sergey Afonin: add `bc' to BuildRequires.
- Patch to fix freshclam error with buggy proxy servers (that answers
  in HTTP/1.0 when we requested HTTP/1.1).

* Fri Jan 21 2005 Victor Forsyuk <force@altlinux.ru> 0.81-alt1.rc1
- 0.81rc1.
- Address BTS #5377.

* Fri Oct 29 2004 Victor Forsyuk <force@altlinux.ru> 0.80-alt4
- Check for database updates hourly.
- Fix path to config file in NotifyClamd.

* Mon Oct 18 2004 Victor Forsyuk <force@altlinux.ru> 0.80-alt3
- 0.80.
- Patches from Sergey Afonin.

* Tue Oct 12 2004 Victor Forsyuk <force@altlinux.ru> 0.80-alt2.rc4
- Mark clamav-milter startup script as noreplaced config.
- Small fix in database updating time randomizer.
- Modify clamav-milter sysconfig file.
- Move config files to /etc/clamav.
- Tweak initscripts priorities to start clamd before clamav-milter
  and both of them before MTA.

* Wed Sep 29 2004 Victor Forsyuk <force@altlinux.ru> 0.80-alt1.rc3
- 0.80rc3.

* Mon Aug 30 2004 Victor Forsyuk <force@altlinux.ru> 0.75.1-alt2
- Build --without-tcpwrappers to fix bug #5064.

* Mon Aug 02 2004 Victor Forsyuk <force@altlinux.ru> 0.75.1-alt1
- 0.75.1

* Fri Jun 25 2004 Victor Forsyuk <force@altlinux.ru> 0.73-alt1
- 0.73.
- Add pkgconfig file and clamav-config to -devel package.

* Wed May 19 2004 Victor Forsyuk <force@altlinux.ru> 0.71-alt1
- New version.

* Wed Apr 21 2004 Victor Forsyuk <force@altlinux.ru> 0.70-alt2
- New version.
- Freshclam launching time randomized at package installation.
  Thanks to Sergey Afonin <asy <at> kraft-s.ru> for idea.

* Wed Apr 14 2004 Victor Forsyuk <force@altlinux.ru> 0.70-alt1.20040414
- Build (post-0.70rc) snapshot from 2004/04/14.

* Mon Mar 01 2004 Victor Forsyuk <force@altlinux.ru> 0.67-alt2.20040301
- Build snapshot from 2004/03/01.
- Fix logrotate for clamd logs.
- Add --daemon-notify to options freshclam run with.
- Add build with milter and create clamav-milter subpackage.

* Sun Feb 15 2004 Victor Forsyuk <force@altlinux.ru> 0.67-alt1
- New version.
- Checks for new database every two hours (suggested by clamav authors).
- Rotate logs weekly (was monthly).

* Thu Dec 18 2003 Victor Forsyuk <force@altlinux.ru> 0.65-alt0.1
- New version.
- Removed *.la files.
- Do not build devel-static subpackage by default.

* Fri Jun 27 2003 Victor Forsyuk <force@altlinux.ru> 0.60-alt1
- Initial build for Sisyphus.
