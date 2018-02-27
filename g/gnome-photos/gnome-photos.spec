%define _unpackaged_files_terminate_build 1
%define _name org.gnome.Photos
%define ver_major 3.14
%define _libexecdir %_prefix/libexec

Name: gnome-photos
Version: %ver_major.0
Release: alt1

Summary: Photos - access, organize and share your photos on GNOME
License: %gpl2plus
Group: Graphics
Url: https://wiki.gnome.org/Apps/Photos

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz

BuildPreReq: rpm-build-gnome rpm-build-licenses

# From configure.ac
BuildRequires: gnome-common intltool yelp-tools desktop-file-utils
BuildPreReq: libgio-devel >= 2.40.0
BuildPreReq: libgtk+3-devel >= 3.13.2
BuildPreReq: libexif-devel >= 0.6.14
BuildPreReq: tracker-devel >= 0.17.5
BuildPreReq: libgdata-devel >= 0.15.2
BuildRequires: libbabl-devel libgegl-devel libexempi-devel
BuildRequires: liblcms2-devel librsvg-devel libgfbgraph-devel
BuildRequires: libgnome-desktop3-devel libgnome-online-accounts-devel
BuildRequires: libgrilo-devel zlib-devel
BuildRequires: gobject-introspection-devel libgtk+3-gir-devel

%description
Photos, like Documents, Music and Videos, is one of the core GNOME
applications meant for find and reminding the user about her content.
The internal architecture Photos is based on Documents -- the document
manager application for GNOME, because they share similar UI/UX
patterns and objectives.

%prep
%setup

%build
%autoreconf
%configure \
    --disable-schemas-compile

%make_build

%install
%makeinstall_std
rm -rf %buildroot/%_datadir/doc/%name
%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_desktopdir/%_name.desktop
%_iconsdir/hicolor/*/apps/%name.*
%_iconsdir/HighContrast/*/apps/%name.*
%_datadir/appdata/%_name.appdata.xml
%_datadir/gnome-shell/search-providers/%_name.search-provider.ini
%_datadir/dbus-1/services/%_name.service
%config %_datadir/glib-2.0/schemas/org.gnome.photos.gschema.xml
%doc ARTISTS AUTHORS NEWS README

%changelog
* Wed Sep 24 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Tue Apr 15 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Mon Mar 24 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Mon Mar 17 2014 Yuri N. Sedunov <aris@altlinux.org> 3.11.92-alt1
- 3.11.92

* Wed Nov 13 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.2-alt1
- 3.10.2

* Mon Oct 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Mon Sep 23 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Tue May 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt1
- 3.8.2

* Mon Apr 15 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Sun Mar 24 2013 Yuri N. Sedunov <aris@altlinux.org> 3.7.3-alt1
- first build for people/gnome

