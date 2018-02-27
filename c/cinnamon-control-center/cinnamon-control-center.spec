%define ver_major 1.8
%define api_ver 1.0

%def_disable debug
%def_disable static
%def_with libsocialweb
%def_with cheese
%def_enable systemd
%def_enable ibus

Name: cinnamon-control-center
Version: %ver_major.1
Release: alt1

Summary: Cinnamon Control Center
License: GPLv2+
Group: Graphical desktop/GNOME
Url: https://github.com/linuxmint/cinnamon-control-center

Source: %name-%version.tar
Patch: %name-%version-%release.patch

# From configure.ac
%define gtk_ver 3.5.13
%define glib_ver 2.31.0
%define desktop_ver 3.5.91
#%define clutter_ver 1.11.3
%define fontconfig_ver 1.0.0
%define xft_ver 2.1.2
%define libmetacity_ver 2.30.0
%define gsds_ver 3.6.0
%define notify_ver 0.7.3
%define nm_ver 0.9.1.90
%define gnome_menus_ver 3.5.5
%define goa_ver 3.5.90
%define sett_daemon_ver 3.6.3
%define cheese_ver 3.5.92
%define bt_ver 3.5.92
%define systemd_ver 40
%define wacom_ver 0.6
%define ibus_ver 1.4.99

Requires: %name-data = %version-%release

# For /usr/share/gnome
Requires: gnome-filesystem
Requires: gnome-settings-daemon >= %sett_daemon_ver
# for graphical passwd changing apps
Requires: accountsservice
#Requires: userpasswd
Requires: gnome-online-accounts >= %goa_ver
%{?_with_cheese:Requires: cheese >= %cheese_ver}
BuildPreReq: rpm-build-gnome >= 0.9

# From configure.in
BuildPreReq: intltool >= 0.50 gnome-common desktop-file-utils gnome-doc-utils gtk-doc xsltproc
BuildPreReq: fontconfig-devel >= %fontconfig_ver
BuildPreReq: libXft-devel >= %xft_ver
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: glib2-devel >= %glib_ver
BuildPreReq: libgnome-desktop3-devel >= %desktop_ver
BuildPreReq: gsettings-desktop-schemas-devel >= %gsds_ver
BuildPreReq: libnotify-devel >= %notify_ver
BuildPreReq: gnome-settings-daemon-devel >= %sett_daemon_ver
BuildPreReq: libgnome-menus-devel >= %gnome_menus_ver
%{?_with_cheese:BuildPreReq: libcheese-devel >= %cheese_ver}
BuildRequires: libxkbfile-devel
%{?_enable_ibus:BuildPreReq: libibus-devel >= %ibus_ver}
BuildRequires: libGConf-devel libdbus-glib-devel libupower-devel libpolkit1-devel
BuildRequires: libgio-devel librsvg-devel libxml2-devel libcanberra-gtk3-devel
BuildRequires: libX11-devel libXext-devel libSM-devel libXScrnSaver-devel libXt-devel
BuildRequires: libXft-devel libXi-devel libXrandr-devel libXrender-devel libXcursor-devel libXcomposite-devel
BuildRequires: libgtop-devel libcups-devel libpulseaudio-devel iso-codes-devel
BuildRequires: libpwquality-devel libkrb5-devel
BuildRequires: libgnomekbd-devel libxklavier-devel

# for test-endianess
BuildRequires: glibc-i18ndata
BuildRequires: libnm-gtk-devel >= %nm_ver
BuildRequires: libgnome-online-accounts-devel >= %goa_ver colord-devel
BuildRequires: libgnome-bluetooth-devel >= %bt_ver
BuildRequires: libwacom-devel >= %wacom_ver
BuildRequires: libclutter-gtk3-devel
%{?_with_libsocialweb:BuildRequires: libsocialweb-devel}
%{?_enable_systemd:BuildRequires: systemd-devel >= %systemd_ver libsystemd-login-devel}

%description
Cinnamon is an attractive and easy-to-use GUI desktop environment. The control-center package
provides the Cinnamon Control Center utilities that allow you to setup
and configure your Cinnamon environment (things like the desktop
background and theme, the screensaver, the window manager, system
sounds, and mouse behavior).

If you install Cinnamon, you need to install control-center.

%package data
Summary: Arch independent files for Cinnamon Control Center
Group: Networking/Instant messaging
BuildArch: noarch

%description data
This package provides noarch data needed for Cinnamon Control Center to work.

%package devel
Summary: Cinnamon Control Center development files
Group: Development/GNOME and GTK+
Requires: %name = %version-%release

%description devel
If you're interested in developing panels for the Cinnamon control center,
you'll want to install this package.

%name-devel helps you create the panels for the control center.

%prep
%setup
%patch0 -p1

%build
#NOCONFIGURE=1 ./autogen.sh
%autoreconf
%configure \
	%{subst_enable debug} \
	%{subst_enable static} \
	--disable-update-mimedb \
	%{subst_with libsocialweb} \
	%{subst_with cheese} \
	%{subst_enable systemd} \
	%{subst_enable ibus}

%make_build

%install
%make_install DESTDIR=%buildroot install

%find_lang --with-gnome --output=%name.lang %name-%api_ver %name-%api_ver-timezones %name


%files
#cinnamon-control-center binary doesn't work at x64 so temporary disable it. 
%exclude %_bindir/*
%dir %_libdir/%{name}-1/panels
%_libdir/%{name}-1/panels/libbluetooth.so
%_libdir/%{name}-1/panels/libcolor.so
%_libdir/%{name}-1/panels/libdisplay.so
%_libdir/%{name}-1/panels/libnetwork.so
%_libdir/%{name}-1/panels/libpower.so
# region panel doesn't work correctly with Gnome-3.8 so temporary disable it. 
%exclude %_libdir/%{name}-1/panels/libregion.so
%_libdir/%{name}-1/panels/libscreen.so
%_libdir/%{name}-1/panels/libsoundnua.so
%_libdir/%{name}-1/panels/libuniversal-access.so
%_libdir/%{name}-1/panels/libuser-accounts.so
%_libdir/*.so.*

%exclude %_libdir/%{name}-1/panels/*.la

%files data -f %name.lang
%dir %_datadir/%name
%_datadir/%name/ui
# need to move to ui subdir
%_datadir/%name/bluetooth.ui
%_datadir/%name/pixmaps
%dir %_datadir/%name/sounds
%_datadir/%name/sounds/cinnamon-sounds-default.xml
%_datadir/%name/icons/
%_desktopdir/*.desktop
%_sysconfdir/xdg/menus/cinnamoncc.menu
%_datadir/desktop-directories/*
%_sysconfdir/xdg/autostart/cinnamon-sound-applet.desktop
%_datadir/pixmaps/cinnamon/faces/
%_iconsdir/hicolor/*/*/*
%_datadir/sounds/cinnamon/default/alerts/*.ogg
%_datadir/polkit-1/actions/org.cinnamon.controlcenter.user-accounts.policy
%_datadir/polkit-1/rules.d/cinnamon-control-center.rules
%doc AUTHORS NEWS README

%files devel
%_pkgconfigdir/*.pc
%dir %_includedir/%name-1/lib%{name}/
%_includedir/%name-1/lib%{name}/*
%_libdir/*.so


%changelog
* Tue May 21 2013 Vladimir Didenko <cow@altlinux.org> 1.8.1-alt1
- 1.8.1

* Thu May 16 2013 Vladimir Didenko <cow@altlinux.org> 1.8.0-alt2
- Replace gnome_rr_labeler calls by cc_rr_labeler
- Fix bluetooth panel

* Thu May 16 2013 Vladimir Didenko <cow@altlinux.org> 1.8.0-alt1
- 1.8.0

* Fri Apr 26 2013 Vladimir Didenko <cow@altlinux.org> 1.7.3-alt1
- 1.7.3-9-g3526e0d

* Fri Feb 22 2013 Vladimir Didenko <cow@altlinux.org> 1.7.1-alt1
- Initial build for Alt Linux
