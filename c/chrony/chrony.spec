Name: chrony
Version: 1.30
Release: alt1

Summary: Chrony clock synchronization program
License: GPLv2 only
Group: System/Configuration/Other

Url: http://chrony.tuxfamily.org
Source0: http://download.tuxfamily.org/chrony/%name-%version.tar
Source1: chronyd.init
Source2: chrony.conf
Source3: chrony.keys
Source4: chrony.logrotate
Source5: chronyd.sysconfig
Source6: chronyd.service
Source7: chrony-wait.service

BuildRequires: libcap-devel libncurses-devel libreadline-devel
BuildRequires: libnss-devel

Conflicts: ntpd openntpd

%define _localstatedir %_var

%description
A pair of programs for keeping computer clocks accurate. chronyd is a daemon
program and chronyc is a command-line interface to it. Time reference sources
for chronyd can be RFC1305 NTP servers, human (via keyboard and chronyc), and
the computer's real-time clock at boot time. chronyd can determine the rate at
which the computer gains or loses time and compensate for it whilst no external
reference is present. chronyd's use of NTP servers can be switched on and off
(through chronyc) to support computers with dial-up/intermittent access to the
Internet. chronyd can also act as an RFC1305-compatible NTP server.

%prep
%setup
# prepare git sources (make_release)
# version in version.txt file
echo %version > version.txt
mandate=$(date +'%B %Y')
for m in chrony.1 chronyc.1.in chrony.conf.5.in chronyd.8.in; do
  sed -e "s|@VERSION@|%version|;s|@MAN_DATE@|${mandate}|" \
    < $m > ${m}_
  mv -f ${m}_ $m
done

%build

%configure \
	--with-user=_chrony \
	--with-sendmail=%_sbindir/sendmail

%make_build getdate all docs

%install
%makeinstall_std
install -pD -m755 %_sourcedir/chronyd.init %buildroot%_initrddir/chronyd
install -pD -m644 %_sourcedir/chrony.conf %buildroot%_sysconfdir/chrony.conf
install -pD -m644 %_sourcedir/chrony.keys %buildroot%_sysconfdir/chrony.keys
install -pD -m644 %_sourcedir/chrony.logrotate %buildroot%_sysconfdir/logrotate.d/chrony
install -pD -m644 %_sourcedir/chronyd.sysconfig %buildroot%_sysconfdir/sysconfig/chronyd
install -pD -m644 %_sourcedir/chronyd.service %buildroot%_unitdir/chronyd.service
install -pD -m644 %_sourcedir/chrony-wait.service %buildroot%_unitdir/chrony-wait.service

install -d %buildroot/lib/systemd/ntp-units.d
echo 'chronyd.service' > \
        %buildroot/lib/systemd/ntp-units.d/50-chronyd.list

rm -rf %buildroot/usr/doc
install -d %buildroot%_localstatedir/{lib,log}/%name
touch %buildroot%_localstatedir/lib/%name/{drift,rtc}

%pre
%_sbindir/groupadd -r -f _chrony 2> /dev/null ||:
%_sbindir/useradd -r -g _chrony -d %_localstatedir/lib/%name -s /dev/null -c "Chrony User" _chrony 2> /dev/null ||:

%post
# Move old configs to /etc
[ -e %_sysconfdir/%name/chrony.conf ] && mv %_sysconfdir/%name/chrony.conf %_sysconfdir/chrony.conf >/dev/null 2>&1 || :
[ -e %_sysconfdir/%name/chrony.keys ] && mv %_sysconfdir/%name/chrony.keys %_sysconfdir/chrony.keys >/dev/null 2>&1 || :

%post_service chronyd

%preun
%preun_service chronyd

%files
%exclude %_docdir/chrony
%doc COPYING NEWS README chrony.txt examples/*
%_initrddir/chronyd
%_unitdir/*.service
/lib/systemd/ntp-units.d/50-chronyd.list
%config(noreplace) %_sysconfdir/sysconfig/chronyd
%config(noreplace) %_sysconfdir/chrony.conf
%config(noreplace) %verify(not md5 size mtime) %attr(640,root,_chrony) %_sysconfdir/chrony.keys
%config(noreplace) %_sysconfdir/logrotate.d/chrony
%_bindir/*
%_sbindir/*
%dir %attr(-,_chrony,_chrony) %_localstatedir/lib/%name
%ghost %attr(-,_chrony,_chrony) %_localstatedir/lib/%name/drift
%ghost %attr(-,_chrony,_chrony) %_localstatedir/lib/%name/rtc
%dir %attr(-,_chrony,adm) %_localstatedir/log/%name
%_man1dir/*
%_man5dir/*
%_man8dir/*

%changelog
* Thu Jul 10 2014 Alexey Shabalin <shaba@altlinux.ru> 1.30-alt1
- 1.30
- moved configs to /etc

* Fri Mar 07 2014 Alexey Shabalin <shaba@altlinux.ru> 1.29.1-alt1
- 1.29.1
- drop root priveleges to user _chrony for chronyd daemon
- add /etc/sysconfig/chronyd
- add systemd support
- update chronyd config
- update chronyd logrotate

* Mon Jul 18 2011 Victor Forsiuk <force@altlinux.org> 1.26-alt1
- 1.26

* Sat Jun 11 2011 Victor Forsiuk <force@altlinux.org> 1.25-alt1
- 1.25

* Mon Feb 08 2010 Victor Forsiuk <force@altlinux.org> 1.24-alt1
- 1.24. Contains security fixes for CVE-2010-0292, CVE-2010-0293, CVE-2010-0294.

* Fri Nov 06 2009 Victor Forsyuk <force@altlinux.org> 1.23-alt2
- Project homepage moved, so fix Url.

* Mon Feb 25 2008 Victor Forsyuk <force@altlinux.org> 1.23-alt1
- Initial build.
