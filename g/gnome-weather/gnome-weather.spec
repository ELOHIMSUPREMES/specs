%define xdg_name org.gnome.Weather
%define ver_major 3.32
%define _libexecdir %_prefix/libexec

Name: gnome-weather
Version: %ver_major.2
Release: alt1

Summary: Access current weather conditions and forecasts
Group: Graphical desktop/GNOME
License: GPLv3+
Url: https://wiki.gnome.org/Apps/Weather

#Source: %name-%version.tar
Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz

BuildArch: noarch

Obsoletes: %name-data
Provides:  %name-data = %version-%release

%define gtk_ver 3.12
%define gi_ver 1.36.0
%define gjs_ver 1.40.0
%define gweather_ver 3.26.0

Requires: libgweather-gir >= %gweather_ver
Requires: geoclue2

# find ./ -name "*.js" |/usr/lib/rpm/gir-js.req |sort|uniq|sed -e 's/^/Requires: /'
Requires: typelib(GLib)
Requires: typelib(GObject)
Requires: typelib(GWeather)
Requires: typelib(Gdk)
Requires: typelib(Geoclue)
Requires: typelib(Gio)
Requires: typelib(GnomeDesktop)
Requires: typelib(Gtk)

BuildRequires(pre): meson rpm-build-gnome rpm-build-gir
BuildRequires: yelp-tools libappstream-glib-devel desktop-file-utils
BuildRequires: libgtk+3-devel >= %gtk_ver libgjs-devel >= %gjs_ver
BuildRequires: libgweather-devel >= %gweather_ver pkgconfig(geoclue-2.0)
BuildRequires: gobject-introspection-devel >= %gi_ver libgtk+3-gir-devel libgweather-gir-devel

%description
%name is a small application that allows you to monitor the current
weather conditions for your city, or anywhere in the world, and to
access updated forecasts provided by various internet services.


%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome --output=%name.lang %name %xdg_name

%files -f %name.lang
%_bindir/%name
%_desktopdir/%xdg_name.desktop
%_datadir/%xdg_name/
%_datadir/dbus-1/services/%xdg_name.service
%_datadir/dbus-1/services/%xdg_name.BackgroundService.service
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_iconsdir/hicolor/scalable/apps/%xdg_name.svg
%_iconsdir/hicolor/symbolic/apps/%xdg_name-symbolic.svg
%_datadir/gnome-shell/search-providers/%xdg_name.search-provider.ini
%_datadir/metainfo/%xdg_name.appdata.xml
%doc NEWS

%changelog
* Sun Apr 21 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.2-alt1
- 3.32.2

* Fri Apr 05 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.1-alt1
- 3.32.1

* Mon Mar 11 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Mon Sep 11 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Mon Mar 20 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Tue Aug 16 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.2-alt1
- 3.20.2

* Mon May 09 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Tue Mar 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Mon Oct 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Mon Apr 27 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2.1-alt1
- 3.16.2.1

* Mon Apr 27 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Tue Apr 14 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Mon Oct 13 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Mon Sep 22 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Tue May 13 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Tue Oct 15 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Tue May 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt1
- 3.8.2

* Wed Apr 17 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Tue Mar 26 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Fri Mar 08 2013 Yuri N. Sedunov <aris@altlinux.org> 0.2-alt1
- first preview for people/gnome

