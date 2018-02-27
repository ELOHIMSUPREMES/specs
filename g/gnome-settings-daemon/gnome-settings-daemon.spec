%define ver_major 3.8
%define api_ver 3.0
%def_disable static
%def_enable smartcard
%def_enable systemd
%def_enable ibus
# tests require, as minimum, running colord
%def_disable check

%define _libexecdir %_prefix/libexec

Name: gnome-settings-daemon
Version: %ver_major.0
Release: alt1

Summary: A program that manages general GNOME settings
License: GPLv2+
Group: Graphical desktop/GNOME
Packager: GNOME Maintainers Team <gnome at packages.altlinux.org>

Url: http://gnome.org
Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz
#Source: %name-%version.tar

# From configure.ac
%define glib2_ver 2.35.3
%define gtk_ver 3.7.8
%define gio_ver 2.29.14
%define gnome_desktop_ver 3.5.3
%define notify_ver 0.7.3
%define pulse_ver 0.9.15
%define gsds_ver 3.3.0
%define colord_ver 0.1.9
%define dconf_ver 0.8
%define upower_ver 0.9.1
%define systemd_ver 40
%define wacom_ver 0.7
%define ibus_ver 1.4.99

Requires: dconf >= %dconf_ver
Requires: colord >= %colord_ver
%{?_enable_ibus:Requires:ibus >= %ibus_ver}

# From configure.ac
BuildPreReq: glib2-devel >= %glib2_ver
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: libgio-devel >= %gio_ver
BuildPreReq: libgnome-desktop3-devel >= %gnome_desktop_ver
BuildPreReq: libnotify-devel >= %notify_ver
BuildPreReq: gsettings-desktop-schemas-devel >= %gsds_ver
BuildPreReq: libpulseaudio-devel >= %pulse_ver libcanberra-gtk3-devel
BuildRequires: libdbus-devel libpolkit1-devel
%{?_enable_smartcard:BuildRequires: libnss-devel}
%{?_enable_systemd:BuildRequires: systemd-devel >= %systemd_ver libsystemd-login-devel}
%{?_enable_ibus:BuildRequires: libibus-devel >= %ibus_ver}
BuildRequires: libxkbfile-devel
BuildRequires: rpm-build-gnome intltool docbook-style-xsl xsltproc
BuildRequires: gcc-c++ libcups-devel libgudev-devel libXi-devel libXext-devel libXfixes-devel
BuildRequires: libXrandr-devel xorg-inputproto-devel libICE-devel libSM-devel
BuildRequires: libupower-devel >= %upower_ver
BuildRequires: libcolord-devel >= %colord_ver liblcms2-devel librsvg-devel
BuildRequires: libwacom-devel >= %wacom_ver xorg-drv-wacom-devel libXtst-devel
# for check
%{?_enable_check:BuildRequires: /proc xvfb-run gnome-color-manager}

%description
GNOME Settings Daemon is a program that organizes access to general GNOME
settings. Other GNOME programs may interact with gnome-settings-daemon to
obtain or change some settings. One of the most prominent examples of a g-s-d
client is GNOME Control Center, another one is Evolution.

%package devel
Summary: GNOME Settings Daemon development files
Group: Development/GNOME and GTK+
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package tests
Summary: GSD test programms
Group: Graphical desktop/GNOME
Requires: %name = %version-%release

%description tests
The %name-tests package provides programms for testing GSD plugins.

%prep
%setup -q

%build
%autoreconf
%configure \
	%{subst_enable static} \
	%{?_disable_smartcard:--disable-smartcard-support} \
	%{subst_enable ibus} \
	--disable-schemas-compile

%make_build

%install
%make_install DESTDIR=%buildroot install
%find_lang --with-gnome %name

%check
%{?_enable_check:xvfb-run %make check}

%files -f %name.lang
%dir %_libdir/%name-%api_ver
%_libdir/%name-%api_ver/a11y-keyboard.gnome-settings-plugin
%_libdir/%name-%api_ver/a11y-settings.gnome-settings-plugin
#%_libdir/%name-%api_ver/background.gnome-settings-plugin
%_libdir/%name-%api_ver/clipboard.gnome-settings-plugin
%_libdir/%name-%api_ver/color.gnome-settings-plugin
%_libdir/%name-%api_ver/cursor.gnome-settings-plugin
%_libdir/%name-%api_ver/housekeeping.gnome-settings-plugin
%_libdir/%name-%api_ver/keyboard.gnome-settings-plugin
%_libdir/%name-%api_ver/liba11y-keyboard.so
%_libdir/%name-%api_ver/liba11y-settings.so
%_libdir/%name-%api_ver/libgsd.so
#%_libdir/%name-%api_ver/libbackground.so
%_libdir/%name-%api_ver/libclipboard.so
%_libdir/%name-%api_ver/libcolor.so
%_libdir/%name-%api_ver/libcursor.so
%_libdir/%name-%api_ver/libhousekeeping.so
%_libdir/%name-%api_ver/libkeyboard.so
%_libdir/%name-%api_ver/libmedia-keys.so
%_libdir/%name-%api_ver/libmouse.so
%_libdir/%name-%api_ver/liborientation.so
%_libdir/%name-%api_ver/libpower.so
%_libdir/%name-%api_ver/libprint-notifications.so
%_libdir/%name-%api_ver/libscreensaver-proxy.so
#%_libdir/%name-%api_ver/libsmartcard.so
%_libdir/%name-%api_ver/libsound.so
%_libdir/%name-%api_ver/libgsdwacom.so
%_libdir/%name-%api_ver/libxrandr.so
%_libdir/%name-%api_ver/libxsettings.so
%_libdir/%name-%api_ver/libremote-display.so
%_libdir/%name-%api_ver/media-keys.gnome-settings-plugin
%_libdir/%name-%api_ver/mouse.gnome-settings-plugin
%_libdir/%name-%api_ver/orientation.gnome-settings-plugin
%_libdir/%name-%api_ver/power.gnome-settings-plugin
%_libdir/%name-%api_ver/print-notifications.gnome-settings-plugin
%_libdir/%name-%api_ver/screensaver-proxy.gnome-settings-plugin
#%_libdir/%name-%api_ver/smartcard.gnome-settings-plugin
%_libdir/%name-%api_ver/sound.gnome-settings-plugin
%_libdir/%name-%api_ver/wacom.gnome-settings-plugin
%_libdir/%name-%api_ver/xrandr.gnome-settings-plugin
%_libdir/%name-%api_ver/xsettings.gnome-settings-plugin
%_libdir/%name-%api_ver/remote-display.gnome-settings-plugin
%_libexecdir/%name
%_libexecdir/gsd-list-wacom
%_libexecdir/gsd-locate-pointer
%_libexecdir/gsd-printer
#%_libexecdir/gnome-fallback-mount-helper
%_libexecdir/gsd-backlight-helper
%_libexecdir/gsd-wacom-led-helper
%_libexecdir/gsd-input-sources-switcher
%_datadir/%name
%_iconsdir/hicolor/*/*/*.png
%_iconsdir/hicolor/*/*/*.svg
%_sysconfdir/xdg/autostart/%name.desktop
#%_sysconfdir/xdg/autostart/gnome-fallback-mount-helper.desktop
%config %_datadir/glib-2.0/schemas/*
%_datadir/GConf/gsettings/%name.convert
%_man1dir/%{name}*
%doc AUTHORS NEWS
%_datadir/polkit-1/actions/org.gnome.settings-daemon.plugins.power.policy
%_datadir/polkit-1/actions/org.gnome.settings-daemon.plugins.wacom.policy
%{?_enable_ibus:%_datadir/dbus-1/services/org.freedesktop.IBus.service}

%exclude %_libdir/%name-%api_ver/*.la
%exclude %_datadir/%name-%api_ver/input-device-example.sh


%files devel
%_includedir/*
%_pkgconfigdir/*

%files tests
%_libexecdir/gsd-test-a11y-keyboard
%_libexecdir/gsd-test-a11y-settings
%_libexecdir/gsd-test-cursor
%_libexecdir/gsd-test-housekeeping
%_libexecdir/gsd-test-input-helper
%_libexecdir/gsd-test-keyboard
%_libexecdir/gsd-test-media-keys
%_libexecdir/gsd-test-mouse
%_libexecdir/gsd-test-orientation
%_libexecdir/gsd-test-print-notifications
%_libexecdir/gsd-test-remote-display
%_libexecdir/gsd-test-screensaver-proxy
%_libexecdir/gsd-test-sound
%_libexecdir/gsd-test-wacom
%_libexecdir/gsd-test-wacom-osd
%_libexecdir/gsd-test-xrandr
%_libexecdir/gsd-test-xsettings


%changelog
* Tue Mar 26 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Sat Feb 16 2013 Yuri N. Sedunov <aris@altlinux.org> 3.6.4-alt2
- rebuilt against libcolord.so.2

* Fri Jan 11 2013 Yuri N. Sedunov <aris@altlinux.org> 3.6.4-alt1
- 3.6.4

* Mon Dec 17 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.3-alt2.1
- updated to 87b1afab07
- gnome-settings-daemon-3.6.3-xi-raw-events.patch (see BGO bug #685676)

* Wed Nov 14 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.3-alt1
- 3.6.3

* Thu Nov 08 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.2-alt1
- 3.6.2

* Tue Oct 09 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Wed Oct 03 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt2
- updated to 2184aa5
- built with ibus

* Tue Sep 25 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0
- new -tests subpackage

* Tue May 29 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.2-alt2
- updated from upstream git (4fb45d63a)

* Tue May 15 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.2-alt1
- 3.4.2

* Mon Apr 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Sat Dec 03 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.2-alt2
- updated from upstream git (fixed GNOME bugs ##664418,642489)

* Wed Nov 09 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.2-alt1
- 3.2.2
- removed upstreamed patch
- fixed link

* Mon Oct 17 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Wed Oct 12 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt2
- updated from upstream git

* Mon Sep 26 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Thu Aug 25 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.3-alt1
- 3.0.3

* Mon May 23 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt1
- 3.0.2

* Tue Apr 26 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1

* Wed Apr 06 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0.1-alt1
- 3.0.0.1

* Tue Apr 05 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Thu Mar 31 2011 Yuri N. Sedunov <aris@altlinux.org> 2.91.93-alt2
- added dconf to reqs

* Sun Mar 27 2011 Yuri N. Sedunov <aris@altlinux.org> 2.91.93-alt1
- 2.91.93

* Mon Nov 15 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt1
- 2.32.1

* Tue Oct 05 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1
- 2.32.0

* Wed Aug 04 2010 Yuri N. Sedunov <aris@altlinux.org> 2.31.6-alt1
- 2.31.6

* Wed Jul 07 2010 Yuri N. Sedunov <aris@altlinux.org> 2.31.4.2-alt1
- 2.31.4.2

* Tue Jun 22 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.2-alt1
- 2.30.2

* Mon Apr 26 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.1-alt1
- 2.30.1

* Mon Mar 29 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0
- enabled font plugin disabled by default in this version

* Wed Mar 10 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.92-alt2
- updated buildreqs

* Wed Mar 10 2010 Yuri N. Sedunov <aris@altlinux.org> 2.28.2-alt1
- 2.28.2

* Mon Mar 08 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.92-alt1
- 2.29.92

* Thu Feb 25 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.91.1-alt1
- 2.29.91.1

* Mon Feb 08 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.90-alt1
- 2.29.90

* Tue Jan 26 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.6-alt1
- 2.29.6

* Tue Jan 12 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.5-alt1
- 2.29.5

* Mon Oct 19 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.1-alt1
- 2.28.1

* Mon Sep 28 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt2
- updated buildreqs (shrek@)

* Mon Sep 21 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Wed Sep 09 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.92-alt1
- 2.27.92

* Mon Aug 24 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.91-alt1
- 2.27.91

* Fri Aug 14 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.90-alt1
- 2.27.90

* Tue Apr 14 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt1
- 2.26.1

* Mon Mar 16 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0

* Tue Mar 03 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.92-alt1
- 2.25.92
- removed upstreamed patches

* Fri Feb 06 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.90-alt1
- 2.25.90
- removed upstreamed patches

* Fri Jan 23 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.3-alt1
- 2.25.3
- applied current Fedora patches
- updated buildreqs
- updated schemas list

* Mon Dec 29 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt2
- updated buildreqs

* Tue Nov 25 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt1
- 2.24.1
- updated buildreqs

* Sat Oct 25 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.0-alt4
- rebuild against libgnomekbd.so.3

* Thu Oct 02 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.0-alt3
- add apps_gnome_settings_daemon_xrandr to schemas list

* Wed Oct 01 2008 Alexey Shabalin <shaba@altlinux.ru> 2.24.0-alt2
- define libexec dir as /usr/libexec

* Sun Sep 28 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.0-alt1
- 2.24.0
- new patchset from Fedora

* Wed Aug 13 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.2.1-alt1
- 2.22.2.1
- import patches from fedora
- build with pulseaudio support

* Fri Mar 21 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt2
- check /desktop/gnome/sound/enable_esd for enable/disable esd (patch0)

* Tue Mar 18 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1.1
- build for Sisyphus
- patch2 from RH: don't set keyboard model on startup from gconf if evdev is being used.
  Evdev needs to use its own keyboard model to work right.

* Sun Mar 09 2008 Alexey Shabalin <shaba@altlinux.ru> 2.21.92-alt1
- First build for Sisyphus.

