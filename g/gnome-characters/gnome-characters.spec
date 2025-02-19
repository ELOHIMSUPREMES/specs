%def_disable snapshot

%define xdg_name org.gnome.Characters
%define ver_major 3.32
%define _libexecdir %_prefix/libexec
%def_without included_libunistring

Name: gnome-characters
Version: %ver_major.1
Release: alt1

Summary: Character map application for GNOME
Group: Text tools
License: BSD and GPLv2+
Url: https://wiki.gnome.org/Design/Apps/CharacterMap

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
#VCS: https://gitlab.gnome.org/GNOME/gnome-characters
Source: %name-%version.tar
%endif

%set_typelibdir %_libdir/%xdg_name/girepository-1.0

%define gjs_ver 1.44.0
%define unistring_ver 0.9.5

Requires: libgjs >= %gjs_ver
# find ./ -name "*.js" |/usr/lib/rpm/gir-js.req |sort|uniq|sed -e 's/^/Requires: /'
Requires: typelib(Gc)
Requires: typelib(Gdk)
Requires: typelib(Gio)
Requires: typelib(GLib)
Requires: typelib(GnomeDesktop)
Requires: typelib(GObject)
Requires: typelib(Gtk)
Requires: typelib(IBus)
Requires: typelib(Pango)
Requires: typelib(PangoCairo)

BuildRequires(pre): meson rpm-build-gir
BuildRequires: libappstream-glib-devel
BuildRequires: libgtk+3-devel libgjs-devel >= %gjs_ver libdbus-devel
BuildRequires: gobject-introspection-devel libgtk+3-gir-devel
%{?_without_included_libunistring:BuildRequires: libunistring-devel >= %unistring_ver}
BuildRequires: gperf

%description
Characters is a simple utility application to find and insert unusual
characters.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang %xdg_name

%files -f %xdg_name.lang
%_bindir/%name
%_libdir/%xdg_name/
%_datadir/%xdg_name/
%_desktopdir/%xdg_name.desktop
%_datadir/dbus-1/services/%xdg_name.service
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_datadir/dbus-1/services/%xdg_name.BackgroundService.service
%_datadir/gnome-shell/search-providers/%xdg_name.search-provider.ini
%_iconsdir/*/*/*/*.svg
%_datadir/metainfo/%xdg_name.appdata.xml
%doc NEWS COPYING
#%doc README


%changelog
* Mon Apr 08 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.1-alt1
- 3.32.1

* Fri Mar 15 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Tue Oct 09 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Sat Aug 18 2018 Yuri N. Sedunov <aris@altlinux.org> 3.29.91-alt1
- 3.29.91

* Tue May 08 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.2-alt1
- 3.28.2

* Mon Mar 12 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Wed Jan 31 2018 Yuri N. Sedunov <aris@altlinux.org> 3.26.2-alt2
- updated to v3.26.2-8-gc1b4f79
- build with system libunistring2-0.9.8

* Mon Oct 30 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.2-alt1
- 3.26.2

* Wed Oct 04 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt1
- 3.26.1

* Mon Sep 04 2017 Yuri N. Sedunov <aris@altlinux.org> 3.25.92-alt1
- 3.25.92

* Tue Jul 04 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Tue Sep 20 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Sun Apr 10 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Mon Mar 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Sun Oct 11 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Tue Sep 22 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Mon May 11 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Mon Apr 13 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Fri Feb 13 2015 Yuri N. Sedunov <aris@altlinux.org> 3.15.2-alt1
- first build for people/gnome

