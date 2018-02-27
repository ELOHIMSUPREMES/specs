%define ver_major 2.6
%define _libexecdir %_prefix/libexec
%def_enable systemd
%define _name cinnamon

Name: %{_name}-session
Version: %ver_major.0
Release: alt1

Summary: The cinnamon session programs for the Cinnamon GUI desktop environment
License: GPLv2+
Group: Graphical desktop/GNOME
URL: https://github.com/linuxmint/cinnamon-session
Packager: Vladimir Didenko <cow@altlinux.org>

Source: %name-%version.tar
Source1: %{_name}.session
Source2: %{_name}2d.session
Source3: start%{_name}-common
Source4: start%{_name}
Source5: start%{_name}2d
Source6: 02Cinnamon
Source7: 02Cinnamon2D
Patch: %name-%version-%release.patch

# From configure.in
%define glib_ver 2.33.4
%define gtk_ver 3.0.0
%define dbus_glib_ver 0.76
%define polkit_ver 0.91
%define upower_ver 0.9
%define systemd_ver 40

PreReq: xinitrc libcanberra-gnome libcanberra-gtk3
Requires: altlinux-freedesktop-menu-cinnamon
Requires: gstreamer dbus-tools-gui
Requires: gnome-filesystem
Requires: cinnamon-settings-daemon
Requires: nemo
Requires: upower polkit-gnome gcr
Requires: %name-translations

BuildPreReq: rpm-build-gnome >= 0.5
BuildPreReq: gnome-common

# From configure.in
BuildPreReq: intltool >= 0.35.0 libGConf-devel
BuildPreReq: libgio-devel glib2-devel >= %glib_ver
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: libdbus-glib-devel >= %dbus_glib_ver
BuildPreReq: libupower-devel >= %upower_ver
BuildRequires: libpangox-compat-devel librsvg-devel libjson-glib-devel
BuildRequires: libX11-devel libXau-devel libXrandr-devel libXrender-devel libXt-devel
BuildRequires: libSM-devel libXext-devel libXtst-devel libXi-devel libXcomposite-devel libGL-devel
BuildRequires: GConf browser-plugins-npapi-devel perl-XML-Parser xorg-xtrans-devel
BuildRequires: libcanberra-devel
BuildRequires: libcinnamon-desktop-devel
%{?_enable_systemd:BuildRequires: systemd-devel >= %systemd_ver libsystemd-login-devel libsystemd-daemon-devel libpolkit-devel}

%description
Cinnamon is a Linux desktop which provides advanced innovative features
and a traditional user experience. The desktop layout is similar to Gnome 2.
The underlying technology is forked from Gnome Shell. The emphasis is put on
making users feel at home and providing them with an easy to use and comfortable 
desktop experience.

This package provides the Cinnamon session manager.

%prep
%setup -q
%patch0 -p1

[ ! -d m4 ] && mkdir m4

%build
%autoreconf
%configure PATH=$PATH:/sbin \
    %{subst_enable systemd} \
    --enable-ipv6 \
    --disable-schemas-compile

%make_build

%install
%make_install install DESTDIR=%buildroot

install -pD -m655 %SOURCE1 %buildroot%_datadir/%name/sessions/%{_name}.session
install -pD -m655 %SOURCE2 %buildroot%_datadir/%name/sessions/%{_name}2d.session
install -pD -m755 %SOURCE3 %buildroot%_datadir/%name/start%{_name}-common
install -pD -m755 %SOURCE4 %buildroot%_bindir/start%{_name}
install -pD -m755 %SOURCE5 %buildroot%_bindir/start%{_name}2d

mkdir -p %buildroot%_x11sysconfdir/wmsession.d
install -pD -m655 %SOURCE6 %buildroot%_x11sysconfdir/wmsession.d
install -pD -m655 %SOURCE7 %buildroot%_x11sysconfdir/wmsession.d

rm -f %buildroot%_docdir/%name/dbus/cinnamon-session.html

%find_lang --with-gnome --output=%name.lang %name-3.0

%check
%make check

%files -f %name.lang
%_bindir/*
%_libexecdir/cinnamon-session-check-accelerated
%_libexecdir/cinnamon-session-check-accelerated-helper
%dir %_datadir/%name
%_datadir/%name/*.glade
%_datadir/%name/hardware-compatibility
%_datadir/%name/start%{_name}-common
%dir %_datadir/%name/sessions
%_datadir/%name/sessions/%{_name}.session
%_datadir/%name/sessions/%{_name}2d.session
%_iconsdir/hicolor/*/apps/cinnamon-session-properties.*
%config %_datadir/glib-2.0/schemas/org.cinnamon.SessionManager.gschema.xml
%_mandir/man?/*
%_x11sysconfdir/wmsession.d/*
%doc AUTHORS NEWS README

%changelog
* Tue May 19 2015 Vladimir Didenko <cow@altlinux.org> 2.6.0-alt1
- 2.6.0

* Fri May 8 2015 Vladimir Didenko <cow@altlinux.org> 2.5.1-alt2
- git20150506

* Tue Apr 14 2015 Vladimir Didenko <cow@altlinux.org> 2.5.1-alt1
- 2.5.1

* Mon Mar 30 2015 Vladimir Didenko <cow@altlinux.org> 2.4.3-alt1
- 2.4.3

* Wed Feb 18 2015 Vladimir Didenko <cow@altlinux.org> 2.4.2-alt2
- explicitly set clutter backend

* Thu Nov 27 2014 Vladimir Didenko <cow@altlinux.org> 2.4.2-alt1
- 2.4.2

* Mon Nov 10 2014 Vladimir Didenko <cow@altlinux.org> 2.4.1-alt1
- 2.4.1

* Fri Oct 31 2014 Vladimir Didenko <cow@altlinux.org> 2.4.0-alt1
- 2.4.0

* Tue Sep 2 2014 Vladimir Didenko <cow@altlinux.org> 2.3.0-alt1
- git20141006

* Tue Sep 2 2014 Vladimir Didenko <cow@altlinux.org> 2.2.2-alt2
- rebuild with new gnome

* Tue Jul 22 2014 Vladimir Didenko <cow@altlinux.org> 2.2.2-alt1
- 2.2.2

* Mon May 12 2014 Vladimir Didenko <cow@altlinux.org> 2.2.1-alt1
- 2.2.1

* Mon May 5 2014 Vladimir Didenko <cow@altlinux.org> 2.2.0-alt2
- add dependence on translations package

* Mon Apr 14 2014 Vladimir Didenko <cow@altlinux.org> 2.2.0-alt1
- 2.2.0-1-g6a4aeb2

* Mon Apr 7 2014 Vladimir Didenko <cow@altlinux.org> 2.0.6-alt4
- git20140402

* Tue Mar 4 2014 Vladimir Didenko <cow@altlinux.org> 2.0.6-alt3
- build with gnome-3.12

* Tue Nov 26 2013 Vladimir Didenko <cow@altlinux.org> 2.0.6-alt2
- add cinnamon polkit agent to required components

* Mon Nov 25 2013 Vladimir Didenko <cow@altlinux.org> 2.0.6-alt1
- 2.0.6

* Tue Nov 5 2013 Vladimir Didenko <cow@altlinux.org> 2.0.4-alt1
- 2.0.4

* Tue Oct 29 2013 Vladimir Didenko <cow@altlinux.org> 2.0.3-alt1
- 2.0.3

* Mon Oct 21 2013 Vladimir Didenko <cow@altlinux.org> 2.0.1-alt2
- add nemo and fallback-mount-helper as required components

* Thu Oct 10 2013 Vladimir Didenko <cow@altlinux.org> 2.0.1-alt1
- 2.0.1

* Wed Sep 25 2013 Yuri N. Sedunov <aris@altlinux.org> 1.9.0-alt3
- rebuild for GNOME-3.10

* Thu Sep 5 2013 Vladimir Didenko <cow@altlinux.org> 1.9.0-alt2
- load cinnamon-settings-daemon2d.desktop in 2d session

* Thu Aug 29 2013 Vladimir Didenko <cow@altlinux.org> 1.9.0-alt1
- git20130824
- bump version

* Fri Aug 2 2013 Vladimir Didenko <cow@altlinux.org> 0.0.1-alt1
- Initial build - git20130723
