Name: 	 xrdp
Version: 0.9.3
Release: alt1

Summary: An open source remote desktop protocol (RDP) server

License: GPLv2+ with exceptions
Group: 	 System/Servers
Url: 	 http://xrdp.sourceforge.net/

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:  %name-%version.tar
# VCS:   https://github.com/neutrinolabs/xrdp
Source1: %name.sysconfig
Source2: %name.logrotate
Source3: %name-init-alt
Source4: libpainter.tar
Source5: librfxcodec.tar
Source6: xorgxrdp.tar

# patches from Debian
Patch1: asm-librfxcodec.diff
Patch2: asm-xorgxrdp.diff
Patch3: make-fixes.diff
Patch4: config.diff
Patch5: misc-fixes.diff
Patch7: shutup-daemon.diff
Patch10: lfs.diff

# Other patches
Patch12: xrdp-alt-startwm.patch

BuildPreReq: rpm-build-intro
BuildRequires: libjpeg-devel
BuildRequires: libpam-devel
BuildRequires: libssl-devel
BuildRequires: libX11-devel
BuildRequires: libXfixes-devel
BuildRequires: libXrandr-devel
BuildRequires: xorg-resourceproto-devel
BuildRequires: xorg-scrnsaverproto-devel
BuildRequires: libXfont2-devel
BuildRequires: libfuse-devel
BuildRequires: libfreerdp-devel
BuildRequires: libopus-devel
BuildRequires: openssl
BuildRequires: xorg-sdk
BuildRequires: nasm

Requires: xorg-drv-xrdp = %EVR

Provides: librfxcodec = %EVR
Obsoletes: librfxcodec < %EVR
Provides: librfxcodec-devel = %EVR
Obsoletes: librfxcodec-devel < %EVR

%description
xrdp offers a graphical login to a remote client using
RDP (the Remote Desktop Protocol). xrdp can connect to
a locally created X.org session with the xorgxrdp drivers,
to a VNC X11 server, and forward to another RDP server.

xrdp accepts connections from freerdp, rdesktop, and the
built-in terminal server / remote desktop clients of
Microsoft Windows operating systems.
In the xorgxrdp (which replaces X11RDP) and VNC modes,
it provides a fully functional Linux terminal server,
offering an X-Window desktop to the user. In the RDP
or VNC forwarding mode, any sort of desktop can be used.

%package -n xorg-drv-%name
Summary: Remote Desktop Protocol (RDP) modules for X.org
Group: System/X11
Provides: xorgxrdp = %EVR

%description -n xorg-drv-xrdp
xorgxrdp is a set of drivers (screen device, keyboard, and mouse)
for X.org enabling use through an RDP session with xrdp. For full
operation, most standard X11 fonts and tools need to be installed.

%prep
%setup
tar xf %SOURCE4
tar xf %SOURCE5
tar xf %SOURCE6
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch7 -p1
%patch10 -p1
%patch12 -p1

cp %SOURCE3 %name-init

subst "s|/usr/lib|%_libdir|g" %name-init
find . -type f -name Makefile.am -exec subst "s|\${localstatedir}\/run|/var/run|g" {} \;

# remove unused modules from xrdp login combobox
subst '/^\[Xvnc\]/,$s/^\([a-z[]\)/#\1/' xrdp/xrdp.ini

# Low is 40 bit key and everything from client to server is encrypted.
# Medium is 40 bit key, everything both ways is encrypted.
# High is 128 bit key everything both ways is encrypted.
# increase encryption to 128 bit's
subst 's/crypt_level=low/crypt_level=high/g' xrdp/xrdp.ini

# create 'bash -l' based startwm, to pick up PATH etc.
echo '#!/bin/bash -l
. %_sysconfdir/xrdp/startwm.sh' > sesman/startwm-bash.sh

%build
./bootstrap
for dir in xorgxrdp librfxcodec libpainter; do
	pushd $dir
	./bootstrap
	popd
done
#autoreconf
%configure \ #--disable-static \
	   --enable-jpeg \
	   --enable-fuse \
	   --enable-rfxcodec \
	   --enable-opus \
	   --enable-painter \
	   --with-systemdsystemunitdir=%systemd_unitdir
pushd xorgxrdp
PKG_CONFIG_PATH=../pkgconfig ./configure
popd
pushd librfxcodec
./configure \
	    --disable-shared \
	    --enable-static
popd
pushd libpainter
./configure \
	    --disable-shared \
	    --enable-static
popd
%make_build

%install
%makeinstall_std

mkdir -p %buildroot%_sysconfdir/xrdp

rm -f %buildroot/%_libdir/xrdp/startwm.sh
rm -f %buildroot/%_libdir/xrdp/xrdp_control.sh
install -D -m755 %name-init %buildroot%_initdir/%name
rm -rf %buildroot%_sysconfdir/init.d

# install sesman pam config /etc/pam.d/xrdp-sesman.unix
install -Dp -m 644 instfiles/pam.d/xrdp-sesman.unix %buildroot%_sysconfdir/pam.d/xrdp-sesman

# install xrdp systemd units
install -Dp -m 644 instfiles/xrdp.service %buildroot/lib/systemd/system/xrdp.service
install -Dp -m 644 instfiles/xrdp-sesman.service %buildroot/lib/systemd/system/xrdp-sesman.service

# install xrdp sysconfig /etc/sysconfig/xrdp
install -Dp -m 644 %SOURCE1 %buildroot%_sysconfdir/sysconfig/xrdp

# install logrotate /etc/logrotate.d/xrdp
install -Dp -m 644 %SOURCE2 %buildroot%_sysconfdir/logrotate.d/xrdp

# install log file /var/log/xrdp-sesman.log
mkdir -p %buildroot%_localstatedir/log/
touch %buildroot%_localstatedir/log/xrdp-sesman.log

# rsakeys.ini
touch %buildroot%_sysconfdir/xrdp/rsakeys.ini
chmod 0600 %buildroot%_sysconfdir/xrdp/rsakeys.ini

# install 'bash -l' startwm script
install -Dp -m 755 sesman/startwm-bash.sh %buildroot%_sysconfdir/xrdp/startwm-bash.sh

# Clean unnecessary files
find %buildroot -name *.a -delete -o -name *.la -delete
rm -rf %buildroot{/usr/local,%_includedir,%_pkgconfigdir}

%pre
/usr/sbin/groupadd -r -f tsusers ||:
/usr/sbin/groupadd -r -f tsadmins ||:

%post
%post_service %name
# Generate keys if they are missing
if [ ! -s %_sysconfdir/xrdp/rsakeys.ini ]; then
  (umask 377; %_bindir/xrdp-keygen xrdp %_sysconfdir/xrdp/rsakeys.ini >/dev/null)
fi
chmod 400 %_sysconfdir/xrdp/rsakeys.ini

if [ ! -s %_sysconfdir/xrdp/cert.pem ]; then
  (umask 377; openssl req -x509 -newkey rsa:2048 -sha256 -nodes -days 3652 \
    -keyout %_sysconfdir/xrdp/key.pem \
    -out %_sysconfdir/xrdp/cert.pem \
    -config %_sysconfdir/xrdp/openssl.conf >/dev/null 2>&1)
fi
chmod 400 %_sysconfdir/xrdp/cert.pem
chmod 400 %_sysconfdir/xrdp/key.pem

%preun
%preun_service %name

%files
%config %_sysconfdir/pam.d/xrdp-sesman
%dir %_sysconfdir/xrdp/
%_sysconfdir/xrdp/km*.ini
%_sysconfdir/xrdp/*.sh
%_sysconfdir/xrdp/xrdp.sh
%dir %_sysconfdir/xrdp/pulse
%_sysconfdir/xrdp/pulse/default.pa
%_sysconfdir/xrdp/xrdp_keyboard.ini
%_initdir/%name
%config(noreplace) %_sysconfdir/sysconfig/xrdp
/lib/systemd/system/*.service
%ghost %_localstatedir/log/xrdp-sesman.log
%attr(0600,root,root) %verify(not size md5 mtime) %_sysconfdir/xrdp/rsakeys.ini
%config %_sysconfdir/xrdp/sesman.ini
%config %_sysconfdir/xrdp/xrdp.ini
%_sysconfdir/xrdp/*.pem
%_bindir/xrdp*
%_sbindir/xrdp*
%_libdir/%name
%_logrotatedir/%name
%dir %_datadir/xrdp/
%_datadir/xrdp/*
%_man1dir/*
%_man5dir/*
%_man8dir/*

%files -n xorg-drv-xrdp
%_sysconfdir/X11/%name/xorg.conf
%_x11modulesdir/*.so
%_x11modulesdir/drivers/*.so
%_x11modulesdir/input/*.so

%changelog
* Wed Jul 26 2017 Andrey Cherepanov <cas@altlinux.org> 0.9.3-alt1
- New version (ALT #33674)
- xrdp requires xorg-drv-xrdp
- Create keys if they do not exist

* Fri Mar 31 2017 Andrey Cherepanov <cas@altlinux.org> 0.9.2-alt1
- New version

* Wed Mar 29 2017 Andrey Cherepanov <cas@altlinux.org> 0.9.1-alt1
- New version

* Tue Mar 15 2016 Andrey Cherepanov <cas@altlinux.org> 0.9.0-alt1.gitf422461
- New version from Git repository
- Enable fuse for drive redirection or clipboard file transfer

* Mon Sep 21 2015 L.A. Kostis <lakostis@altlinux.ru> 0.6.1-alt1.1
- fix pidfile path and sysv init script.

* Fri Feb 07 2014 Andrey Cherepanov <cas@altlinux.org> 0.6.1-alt1
- New version (ALT #19193)
- Use patches and init scripts from Fedora and Debian (ALT #27853)

* Sun Aug 04 2013 Vitaly Lipatov <lav@altlinux.ru> 0.6.0-alt1
- new version 0.6.0 (with rpmrb script)

* Thu Aug 18 2011 Denis Baranov <baraka@altlinux.ru> 0.4.2-alt1
- new version (0.4.2) with rpmbs script

* Mon Oct 11 2010 Vitaly Lipatov <lav@altlinux.ru> 0.4.1-alt2
- fix build, cleanup spec

* Tue Oct 07 2008 Vitaly Lipatov <lav@altlinux.ru> 0.4.1-alt1
- new version 0.4.1 (with rpmrb script)

* Sun Nov 04 2007 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt4
- provide internal lib
- install generic init script, add ALT init script
- use config mark for ini files

* Mon Sep 24 2007 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt3
- NMU build
- fix source tarball url
- set all destination pathes from spec
- add rpath to fix linking
- use /etc/X11/xdm/Xsession instead sessionwm.sh

* Wed Sep 12 2007 Lunar Child <luch@altlinux.ru> 0.4.0-alt2
- added patch by Nickolay <sn@m2.sta.gov.ua>
- fixing bug this documentation.

* Mon Aug 27 2007 Lunar Child <luch@altlinux.ru> 0.4.0-alt1
- new version

* Wed Jan 17 2007 Lunar Child <luch@altlinux.ru> 0.3.2-alt1
- First Build for ALT Linux Sisyphus
