%define _name enlightenment
%define cvs_date zero
%undefine cvs_date
%define snapshot 2012-10-12
%define rel alt3

%def_disable static
%def_with pam_helper

# TODO: pam CoreFoundation

Name: e17
Version: 0.17.1

%ifdef cvs_date
Release: %rel.%cvs_date
%else
Release: %rel
%endif
Serial: 1

Summary: The Enlightenment window manager
License: BSD
Group: Graphical desktop/Enlightenment
URL: http://www.enlightenment.org/

Source: http://download.enlightenment.org/releases/%_name-%version.tar.bz2

Source1: E-17.xpm
Source2: start%name
Source3: %name.wmsession
Source6: %name.xpm
Source7: %name-32.xpm
Source8: %_name.desktop
Source9: %_name-wm.desktop

# Some missing source files from the SVN tree
Source10: %_name.missing-%version.tar
Source11: e17-alt-sysactions.conf

Patch0: fix-systray-height.patch
Patch1: add-systray-mobile.patch
Patch2: add-systray-standard.patch
Patch3: illume-keyboard-bigfont.patch
Patch4: e17-0.17.0-alt-g-s-d_path.patch
Patch5: e17-0.17.1-alt-e_sys_nosuid.patch
Patch6: auto-ptrace-disable.patch
Patch11: enlightenment-0.17.1-pam-helper.patch

Provides: e17-default
# default terminal
Requires: terminology
Requires: evas_generic_loaders dbus-tools-gui edbus eeze
Requires: empower
Requires: pm-utils
# for menu
Requires: gnome-icon-theme
Requires: wm-common-freedesktop
Requires: altlinux-freedesktop-menu-%_name >= 0.55
%{?_with_pam_helper:Requires: chkpwd-pam}

BuildPreReq: libeet-devel >= 1.7.4
BuildPreReq: libecore-devel >= 1.7.4
BuildPreReq: libeio-devel >= 1.7.4
BuildRequires: libpam-devel libX11-devel libevas-devel libecore-devel
BuildRequires: edje libedje-devel libeet-devel libeet-utils libembryo-devel libefreet-devel
BuildRequires: libXext-devel embryo_cc libdbus-devel libedbus-devel
BuildRequires: libalsa-devel libeina-devel eeze libeeze-devel libemotion-devel libelementary-devel
BuildRequires: libudev-devel libxcbutil-keysyms-devel pm-utils
BuildRequires: doxygen
BuildRequires: libp11-kit-devel

%description
Enlightenment is a window manager.
E-17 is a non-stable Enlightenment version from CVS.
	
%package devel
Summary: Development headers for Enlightenment.
Group: Development/C
Requires: %name = %serial:%version-%release

%description devel
Development headers for Enlightenment.

%package gnome
Summary: GNOME-specific parts of Enlightenment
Group: Graphical desktop/GNOME
BuildArch: noarch
Provides: gnome-wm
Requires: %name = %serial:%version-%release
Requires: gnome-session >= 2.24

%description gnome
Install this package and run:
"gconftool-2 --set --type string /desktop/gnome/session/required_components/windowmanager enlightenment"
to use Enlightenment as windowmanager in GNOME 2 session

%prep
%ifdef cvs_date
%setup -q -n %_name-%version-%cvs_date -a10
%else
%setup -q -n %_name-%version -a10
%endif
%patch0 -p2
%patch1 -p2
%patch2 -p2
%patch3 -p2
%patch4 -p1 -b .gsd
%patch5 -p1 -b .nosuid
%patch6 -p2
%patch11 -p1

%build
%autoreconf
export CFLAGS="$CFLAGS `pkg-config --cflags dbus-1` -g -ggdb3"
%configure \
	--with-profile=FAST_PC \
	--enable-files \
	%{subst_enable static} \
	--enable-shared \
	--enable-mount-eeze \
	--enable-pam \
%if_with pam_helper
	--with-pam-helper=%prefix/libexec/chkpwd-pam/chkpwd-pam \
%endif
	--disable-mount-hal

%make_build
%make doc
%install
%make_install DESTDIR=%buildroot install

%find_lang enlightenment

mkdir -p %buildroot%_sysconfdir/X11/wmsession.d
mkdir -p %buildroot%_bindir/
install -p -m755 %SOURCE2 %buildroot%_bindir/
install -D -pm 644 %SOURCE3 %buildroot%_sysconfdir/X11/wmsession.d/05E-17

# Install icons
install -pD -m644 %SOURCE6 %buildroot%_miconsdir/%name.xpm
install -pD -m644 %SOURCE7 %buildroot%_niconsdir/%name.xpm
install -p -m644 %SOURCE1 %buildroot%_niconsdir/

# desktop file
install -pD -m 644 %SOURCE8 %buildroot%_datadir/applications/enlightenment.desktop
# be gnome-wm
install -pD -m 644 %SOURCE9 %buildroot%_datadir/gnome/wm-properties/enlightenment-wm.desktop

# PAM-config
mkdir -p %buildroot%_sysconfdir/pam.d
cat > %buildroot%_sysconfdir/pam.d/enlightenment << _PAM_
#%%PAM-1.0

auth		include		system-auth
account		required	pam_deny.so
password	required	pam_deny.so
session		required	pam_deny.so
_PAM_

# replace original sysaction.conf
cp %SOURCE11 %buildroot%_sysconfdir/enlightenment/sysactions.conf

%find_lang enlightenment

%files -f enlightenment.lang
%config %_sysconfdir/X11/wmsession.d/*
%config %_sysconfdir/enlightenment/sysactions.conf
%config(noreplace) %_sysconfdir/pam.d/enlightenment
%dir %_libdir/enlightenment/
%_libdir/enlightenment/*
%_niconsdir/*.xpm
%_miconsdir/*.xpm
%_bindir/*
%_datadir/enlightenment/
%_datadir/xsessions/enlightenment.desktop
%_datadir/applications/*.desktop
%doc AUTHORS COPYING README

%files devel
%dir %_includedir/enlightenment/
%_includedir/enlightenment/*.h
%_libdir/pkgconfig/enlightenment.pc
%_libdir/pkgconfig/everything.pc

%files gnome
%_datadir/gnome/wm-properties/*.desktop

%changelog
* Thu Apr 04 2013 Yuri N. Sedunov <aris@altlinux.org> 1:0.17.1-alt3
- applied e17-0.17.1-alt-e_sys_nosuid.patch,
  applied custom sysactions.conf, added empower to rqs (ALT #28291)

* Wed Apr 03 2013 Led <led@altlinux.ru> 1:0.17.1-alt2
- with pam helper (ALT#28277)

* Mon Feb 04 2013 Paul Wolneykien <manowar@altlinux.ru> 1:0.17.1-alt1
- Fresh up to v0.17.1.

* Fri Feb 01 2013 Paul Wolneykien <manowar@altlinux.ru> 1:0.17.0-alt6
- Disable tracing automatically if enlightenment has suid/sgid
  bit set.

* Fri Jan 18 2013 Yuri N. Sedunov <aris@altlinux.org> 1:0.17.0-alt5
- required evas_generic_loaders (especially for .svg)
- required gnome-icon-theme for menus (ALT #28311)
- required terminology as a default terminal
- fixed path to gnome-settings-daemon
- prepared pam-config for screenlock
- prepared (not applied) e17-0.17.0-alt-e_sys_nosuid.patch
- prepared (not applied) a draft of custom sysactions.conf

* Fri Jan 18 2013 Paul Wolneykien <manowar@altlinux.ru> 1:0.17.0-alt4
- Make the keylabels bigger, 14 pt (patch).
- Add missing SVN files as the separate tar source.
- Patch the default configuration placing systray gadget on the
  panel/shelf by default.

* Wed Jan 16 2013 Paul Wolneykien <manowar@altlinux.ru> 1:0.17.0-alt3
- Do not assume systray must be on a shelf (patch).
- Build with additional debugging flags (-g -ggdb3).

* Sat Dec 22 2012 Yuri N. Sedunov <aris@altlinux.org> 1:0.17.0-alt2
- 0.17.0 final release (zero)
- provides e17-default

* Tue Dec 18 2012 Yuri N. Sedunov <aris@altlinux.org> 1:0.17.0-alt1.omega
- - 0.17.0 beta (omega)

* Sat Dec 15 2012 Yuri N. Sedunov <aris@altlinux.org> 1:0.17.0-alt1.lucky
- 0.17.0 beta (lucky)

* Wed Nov 28 2012 Yuri N. Sedunov <aris@altlinux.org> 1:0.17.0-alt1.alpha6
- 0.17.0 alpha6

* Sat Nov 24 2012 Yuri N. Sedunov <aris@altlinux.org> 1:0.17.0-alt1.alpha5
- 0.17.0 alpha5
- requires altlinux-freedesktop-menu-enlightenment >= 0.55

* Fri Nov 16 2012 Yuri N. Sedunov <aris@altlinux.org> 1:0.17.0-alt1.alpha3
- 0.17.0 alpha3

* Tue Nov 13 2012 Yuri N. Sedunov <aris@altlinux.org> 1:0.17.0-alt1.alpha2
- 0.17.0 alpha2

* Mon Oct 22 2012 Yuri N. Sedunov <aris@altlinux.org> 1:0.16.999.77927-alt1
- 0.16.999.77927

* Tue Sep 04 2012 Yuri N. Sedunov <aris@altlinux.org> 1:0.16.999.76015-alt1
- 0.16.999.76015

* Fri May 11 2012 Yuri N. Sedunov <aris@altlinux.org> 1:0.16.999.70492-alt1
- 0.16.999.70492

* Mon Dec 05 2011 Yuri N. Sedunov <aris@altlinux.org> 1:0.16.999.65643-alt1
- 0.16.999.65643

* Sun May 01 2011 Yuri N. Sedunov <aris@altlinux.org> 1:0.16.999.55225-alt2
- set default_system_menu to enlightenment-applications.menu,
  requires wm-common-freedesktop and altlinux-freedesktop-menu-enlightenment (ALT #16132)

* Sun Jan 30 2011 Yuri N. Sedunov <aris@altlinux.org> 1:0.16.999.55225-alt1
- 0.16.999.55225

* Thu Nov 18 2010 Yuri N. Sedunov <aris@altlinux.org> 1:0.16.999.54504-alt1
- 0.16.999.54504

* Fri Oct 29 2010 Yuri N. Sedunov <aris@altlinux.org> 1:0.16.999.52995-alt1
- new snapshot

* Mon Jan 04 2010 Yuri N. Sedunov <aris@altlinux.org> 1:0.16.999.063-alt1
- new version

* Tue Nov 10 2009 Yuri N. Sedunov <aris@altlinux.org> 1:0.16.999.062-alt1
- new version
- removed obsolete %%update_wms calls
- icons moved in proper location

* Thu Nov 13 2008 Yuri N. Sedunov <aris@altlinux.org> 1:0.16.999.050-alt2
- new e17-gnome package to be gnome-wm as metacity or sawfish. Install this package and do
  "gconftool-2 --set --type string /desktop/gnome/session/required_components/windowmanager enlightenment" to take effect
- install desktop-file instead old menu-file
- remove post{,un}_ldconfig, {update,clean}_menus calls

* Sat Oct 18 2008 Yuri N. Sedunov <aris@altlinux.org> 1:0.16.999.050-alt1
- 0.16.999.050
- added serial due to version downgrade
- don't use bundled vera font, it doesn't support national glyphs

* Wed Sep 19 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.17.0.pre10-alt1.20070918
- CVS from 20070918.

* Tue Jul 31 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.17.0.pre10-alt1.20070731
- CVS from 20070731.

* Wed May 16 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.17.0.pre10-alt1.20070516
- CVS from 20070516.

* Thu May 10 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.17.0.pre10-alt1.20070509
- CVS from 20070509.
- Fix BuildRequires.
- Fix --as-needed problems.

* Wed Sep 20 2006 Igor Zubkov <icesik@altlinux.org> 0.17.0.pre10-alt1.20060920
- 20060910 -> 20060920

* Tue Sep 12 2006 Igor Zubkov <icesik@altlinux.org> 0.17.0.pre10-alt1.20060910
- update from cvs (20060327 -> 20060910)
- buildreq

* Mon Apr 10 2006 Igor Zubkov <icesik@altlinux.ru> 0.17.0.pre10-alt1.20060327
- update from cvs

* Mon May 30 2005 Denis Klykvin <nikon@altlinux.ru> 0.17.0.pre10-alt1.20050530
- updated from cvs.

* Mon May 16 2005 Denis Klykvin <nikon@altlinux.ru> 0.17.0.pre10-alt1.20050516
- updated from cvs.


* Mon May 16 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.17.0.pre10-alt1.1.20050428
-  small fixes in the spec (wmsession.d path corrected).
-  %_menudir filesystem intersections repaired.

* Sat May 14 2005 Denis Klykvin <nikon@altlinux.ru> 0.17.0.pre10-alt1.20050514
- updated from cvs.

* Thu Apr 28 2005 Denis Klykvin <nikon@altlinux.ru> 0.17.0.pre10-alt1.20050428
- updated from cvs.

* Mon Apr 25 2005 Denis Klykvin <nikon@altlinux.ru> 0.17.0.pre10-alt1.20050425
- updated from cvs.

* Thu Apr 21 2005 Denis Klykvin <nikon@altlinux.ru> 0.17.0.pre10-alt1.20050421
- updated from cvs.

* Mon Apr 11 2005 Denis Klykvin <nikon@altlinux.ru> 0.17.0_pre10-alt1.cvs20050420
- Initial build from CVS

* Tue Mar 29 2005 Alex Murygin <murygin@altlinux.ru> 1:0.16.999-alt0.1_003_20050329
- updated from cvs.
- added serial due to version downgrade
- added lib%name and lib%name-devel packages

* Sat Jan 22 2005 Alex Murygin <murygin@altlinux.ru> 0.17.0-alt0.1_pre10_20050122
- updated from cvs.

* Fri Jun 13 2003 Alex Murygin <murygin@altlinux.ru> 0.17.0-alt0.1_20030613
- Updated from cvs.
- Moved to /usr/X11 dir
- added check to fam

* Sat Mar 15 2003 Alex Murygin <murygin@altlinux.ru> 0.17.0-alt0.1_20030530
- Updated from cvs.
- Fix borders
- Fix font link
- Add menu-method support
- Change standart font borzoib.ttf for n019003l.ttf (val-ttf)
- Added requires to efsd, imlib2_loaders

* Sat Nov 23 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.17.0-alt0.1_20021123
- First build for Sisyphus.
