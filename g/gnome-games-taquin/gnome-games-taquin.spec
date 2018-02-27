%define _unpackaged_files_terminate_build 1

%define _name org.gnome.taquin
%define __name gnome-taquin
%define ver_major 3.16
%define _libexecdir %_prefix/libexec

Name: gnome-games-taquin
Version: %ver_major.0
Release: alt1

Summary: Gnome tiles game
Group: Games/Boards
License: GPLv3+
Url: http://live.gnome.org/Apps/Taquin

Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%__name-%version.tar.xz

Provides:  %_name = %version-%release

%define glib_ver 2.40.0
%define gtk_ver 3.15.0

BuildRequires: gnome-common intltool yelp-tools libappstream-glib-devel
BuildRequires: libgio-devel >= %glib_ver libgtk+3-devel >= %gtk_ver librsvg-devel
BuildRequires: libcanberra-gtk3-devel

%description
Move tiles so that they reach their places.

%prep
%setup -n %__name-%version

%build
%autoreconf
%configure --disable-schemas-compile
%make_build

%install
%makeinstall_std

%find_lang --with-gnome %__name

%files -f %__name.lang
%_bindir/%__name
%_desktopdir/%_name.desktop
%_datadir/%__name/
%_iconsdir/hicolor/*x*/apps/%__name.png
%_iconsdir/hicolor/scalable/apps/%__name-symbolic.svg
%_iconsdir/HighContrast/*x*/apps/%__name.png
%_man6dir/%__name.*
%_datadir/dbus-1/services/%_name.service
%config %_datadir/glib-2.0/schemas/%_name.gschema.xml
%_datadir/appdata/%_name.appdata.xml
%doc AUTHORS NEWS

%changelog
* Thu Mar 26 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Fri Dec 26 2014 Yuri N. Sedunov <aris@altlinux.org> 3.15.3-alt1
- first build for people/gnome

