%define ver_major 0.3
%define gst_api_ver 1.0
%def_with recording

Name: gnome-internet-radio-locator
Version: %ver_major.0
Release: alt1

Summary: GNOME Internet Radio Locator
License: GPLv2+
Group: Sound
Url: https://wiki.gnome.org/Apps/Girl

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

Requires: gst-plugins-base%gst_api_ver
Requires: gst-plugins-bad%gst_api_ver
Requires: gst-plugins-ugly%gst_api_ver

%define gtk_ver 3.0

BuildRequires: gnome-common intltool yelp-tools gtk-doc
BuildRequires: libgtk+3-devel >= %gtk_ver libxml2-devel libchamplain-gtk3-devel
BuildRequires: gst-plugins%gst_api_ver-devel gst-plugins-bad1.0-devel

%description
GNOME Internet Radio Locator is a Free Software program that allows
you to easily locate radio programs by broadcasters on the Internet
with the help of a map.

%prep
%setup

%build
%autoreconf
%configure \
	%{subst_with recording}
%make_build

%install
%makeinstall_std

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_datadir/applications/%name.desktop
%_datadir/%name/
%_iconsdir/hicolor/*x*/apps/%name.png
%_datadir/appdata/%name.appdata.xml
%_man1dir/%name.1.*
%doc AUTHORS NEWS README TODO HACKING


%changelog
* Tue Jun 20 2017 Yuri N. Sedunov <aris@altlinux.org> 0.3.0-alt1
- 0.3.0

* Fri Jun 16 2017 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt1
- first build for Sisyphus

