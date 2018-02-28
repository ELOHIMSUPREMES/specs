%set_automake_version 1.11

%define upstreamname lxdm
%define theme_name Industrial
%define gtkver 2
Name: lxde-%upstreamname
Version: 0.5.3
Release: alt1.20160321.1

Summary: Lightweight X11 Display Manager
License: GPL
Group: Graphical desktop/Other
Url: http://lxde.sf.net
#Url: git://git.lxde.org/lxde/lxdm.git

Packager: LXDE Development Team <lxde@packages.altlinux.org>

Source: %upstreamname-%version.tar
Patch3: lxdm-alt-session-name.patch
Patch4: lxdm-nonolisten.patch
Patch5: lxdm-buildfix_syswait.patch
Patch6: lxdm-0.4.1-old-plymouth.patch
Patch7: lxdm-alt-cpuhog.patch

Source1: alt.lxdm.pam
Source2: alt.lxdm.conf
Source3: alt.Xsession

BuildPreReq: imake intltool libConsoleKit-devel libXmu-devel libgtk+%gtkver-devel libpam-devel xinitrc xorg-cf-files

%add_findreq_skiplist %_sbindir/%upstreamname

%description
LXDM is the future display manager of LXDE, the Lightweight X11 Desktop
environment. It is designed as a lightweight alternative to replace GDM or
KDM in LXDE distros. It's still in very early stage of development.

%prep
%setup -n %upstreamname-%version
#%%patch3 -p2
#%%patch4 -p2
#%%patch5 -p2
#%%patch6 -p1
#%%patch7 -p2

%build
%autoreconf
%if %gtkver==3
    %configure --enable-gtk3
%else
    %configure
%endif
#touch -r po/Makefile po/stamp-it
%make_build

%install
%makeinstall_std
%find_lang %upstreamname

touch %buildroot%_sysconfdir/%upstreamname/xinitrc

mkdir -p %buildroot/%_altdir
cat > %buildroot/%_altdir/lxdm-theme-%theme_name << __EOF__
%_datadir/%upstreamname/themes/default %_datadir/%upstreamname/themes/%theme_name 10
__EOF__

mkdir -p %buildroot%_sysconfdir/pam.d
install -m644 %SOURCE1 %buildroot%_sysconfdir/pam.d/lxdm

install -m644 %SOURCE2 %buildroot%_sysconfdir/%upstreamname/lxdm.conf
install -m755 %SOURCE3 %buildroot%_sysconfdir/%upstreamname/Xsession

mkdir -p %buildroot%_unitdir
install -m644 systemd/lxdm.service %buildroot%_unitdir

%files -f %upstreamname.lang
%doc ChangeLog INSTALL README
%_sysconfdir/%upstreamname
%config(noreplace) %_altdir/lxdm-theme-%theme_name
%config(noreplace) %_sysconfdir/pam.d/%upstreamname
%_sbindir/*
%_libexecdir/lxdm-greeter-gdk
%_libexecdir/lxdm-greeter-gtk
%_libexecdir/lxdm-numlock
%_libexecdir/lxdm-session
%_sysconfdir/lxdm/Xsession
%config %_sysconfdir/lxdm/lxdm.conf
%_bindir/*
%_datadir/%upstreamname
%_unitdir/lxdm.service

%changelog
* Sat May 21 2016 Anton Midyukov <antohami@altlinux.org> 0.5.3-alt1.20160321.1
- New snapshot 20160321.

* Mon Feb 02 2015 Michael Shigorin <mike@altlinux.org> 0.3.0-alt3
- added patch by Alex Moskalenko to fix CPU hogging (closes: #28778)

* Fri Apr 11 2014 Sergey V Turchin <zerg@altlinux.org> 0.3.0-alt2.2
- fix plymouth support

* Thu Nov 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt2.1
- Fixed build

* Mon Feb 14 2011 Lenar Shakirov <snejok@altlinux.ru> 0.3.0-alt2
- Packaging fixed: new rpm not prevent glob patter for libdir

* Thu Sep 30 2010 Mykola Grechukh <gns@altlinux.ru> 0.3.0-alt1
- new version
- X started with parameters from /etc/sysconfig/xserver

* Fri Sep 10 2010 Mykola Grechukh <gns@altlinux.ru> 0.2.0-alt6
- new snapshot from upstream (mostly i18n)
- rebuilt with new ConsoleKit

* Fri Jun 25 2010 Mykola Grechukh <gns@altlinux.ru> 0.2.0-alt5
- updated from upstream GIT. GEAR layout revisited.

* Wed May 26 2010 Mykola Grechukh <gns@altlinux.ru> 0.2.0-alt4
- latest upstream updates. Improved session handling (ALT-specific)

* Sun May 02 2010 Mykola Grechukh <gns@altlinux.ru> 0.2.0-alt0.M51.3
- build for branch 5.1

* Sun May 02 2010 Mykola Grechukh <gns@altlinux.ru> 0.2.0-alt3
- requires fixed

* Mon Jan 11 2010 Mykola Grechukh <gns@altlinux.ru> 0.1.0-alt1
- initial build, based on F12 spec
