%define _libexecdir %_prefix/libexec
%define ver_major 3.18
%define _name org.gnome.Todo

Name: gnome-todo
Version: %ver_major.0
Release: alt1

Summary: Todo manager for GNOME
Group: Graphical desktop/GNOME
License: GPLv3+
Url: https://wiki.gnome.org/Apps/Todo

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
#Source: %name-%version.tar

%define gtk_ver 3.16.0
%define eds_ver 3.17.1

BuildRequires: intltool yelp-tools libappstream-glib-devel
BuildRequires: libgtk+3-devel >= %gtk_ver evolution-data-server-devel >= %eds_ver
BuildRequires: libgnome-online-accounts-devel libical-devel

%description
GNOME Todo is a simple task management application designed to integrate
with GNOME.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%_bindir/%name
%_desktopdir/%_name.desktop
%_datadir/glib-2.0/schemas/org.gnome.todo.gschema.xml
%_iconsdir/hicolor/*x*/apps/*.png
%_datadir/appdata/%_name.appdata.xml
%doc NEWS README

%changelog
* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Fri Jun 26 2015 Yuri N. Sedunov <aris@altlinux.org> 3.17.3.1-alt1
- first build for people/gnome

