%define xdg_name org.gnome.Calendar
%define ver_major 3.20
%define _libexecdir %_prefix/libexec

Name: gnome-calendar
Version: %ver_major.1
Release: alt1

Summary: Calendar application for GNOME
License: %gpl2plus
Group: Graphical desktop/GNOME
Url: https://wiki.gnome.org/Apps/Calendar

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz

BuildPreReq: rpm-build-licenses rpm-build-gnome

%define glib_ver 2.44.0
%define gtk_ver 3.20.0
%define ical_ver 1.0.1
%define eds_ver 3.18.0

BuildPreReq: intltool yelp-tools itstool libappstream-glib-devel
BuildPreReq: libgio-devel >= %glib_ver libgtk+3-devel >= %gtk_ver
BuildPreReq: libical-devel >= %ical_ver libicu-devel
BuildRequires: libgnome-online-accounts-devel vala-tools
BuildRequires: evolution-data-server-devel >= %eds_ver

%description
Calendar is a calendar application for GNOME.

%prep
%setup

%build
%configure \
    --disable-schemas-compile
%make_build

%install
%makeinstall_std

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_datadir/dbus-1/services/%xdg_name.service
%_datadir/gnome-shell/search-providers/%xdg_name.search-provider.ini
%_desktopdir/%xdg_name.desktop
#%_man1dir/*
%_datadir/glib-2.0/schemas/org.gnome.calendar.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.calendar.enums.xml
%_iconsdir/hicolor/*x*/apps/%xdg_name.png
%_iconsdir/hicolor/symbolic/apps/%xdg_name-symbolic.svg
%_datadir/appdata/%xdg_name.appdata.xml
%doc NEWS README

%changelog
* Thu Apr 14 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Tue Mar 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Thu Mar 17 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.3-alt1
- 3.18.3

* Fri Jan 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.2.1-alt2
- rebuilt against libical.so.2

* Thu Dec 24 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.2.1-alt1
- 3.18.2.1

* Wed Dec 23 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt1
- 3.18.2

* Sat Oct 17 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Tue May 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Thu Apr 16 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Fri Dec 26 2014 Yuri N. Sedunov <aris@altlinux.org> 3.15.3.1-alt1
- first build for people/gnome


