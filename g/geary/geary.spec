%define ver_major 0.10
%def_disable contractor

Name: geary
Version: %ver_major.0
Release: alt1

Summary: Email client
License: LGPLv2.1+
Group: Networking/Mail
Url: https://wiki.gnome.org/Apps/Geary

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

Packager: Igor Zubkov <icesik@altlinux.org>

%define vala_ver 0.22.1
%define gtk_ver 3.10.0
%define sqlite_ver 3.7.4
%define gcr_ver 3.10.1

BuildPreReq: vala-tools >= %vala_ver libvala-devel
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: libsqlite3-devel >= %sqlite_ver
BuildRequires: cmake intltool desktop-file-utils gnome-doc-utils
BuildRequires: libnotify-devel libcanberra-devel libgee0.8-devel
BuildRequires: libgmime-devel libgnome-keyring-devel libexpat-devel
BuildRequires: libpixman-devel libharfbuzz-devel libwebkitgtk3-devel
BuildRequires: libpng-devel libsecret-devel at-spi2-atk-devel libxml2-devel
BuildRequires: libXdmcp-devel libXdamage-devel libxshmfence-devel
BuildRequires: libXxf86vm-devel libXinerama-devel libXrandr-devel libXi-devel
BuildRequires: libXcursor-devel libXcomposite-devel libxkbcommon-devel
BuildRequires: libwayland-cursor-devel
BuildRequires: libat-spi2-core-devel at-spi2-atk-devel
BuildRequires: gobject-introspection-devel libgtk+3-gir-devel
BuildRequires: libsoup-gir-devel libwebkitgtk3-gir-devel libcanberra-vala
BuildRequires: gcr-libs-devel >= %gcr_ver gcr-libs-vala

# TODO:
# -- Unity indicate support: OFF
# -- Unity messaging menu support: OFF
# -- Unity launcher support: OFF
# -- Reference tracking: OFF

%description
Geary is an email client built for the GNOME desktop environment.  It
allows you to read and send email with a simple, modern interface.

Visit http://www.yorba.org to read about the current state of.
Geary's development.

%prep
%setup

%build
#%%configure --disable-schemas-compile \
#	--disable-desktop-update \
#	--disable-icon-update \
#	%{subst_enable contractor}
%cmake -DGSETTINGS_COMPILE:BOOL=OFF \
	-DICON_UPDATE:BOOL=OFF \
	-DDESKTOP_UPDATE:BOOL=OFF \
%cmake_build VERBOSE=1

%install
%cmakeinstall_std

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%{?_enable_contractor:%_bindir/%name-attach}
%_datadir/%name/
%_desktopdir/%name.desktop
%_desktopdir/%name-autostart.desktop
%_datadir/glib-2.0/schemas/org.yorba.%name.gschema.xml
%_iconsdir/*/*/apps/*
%_iconsdir/hicolor/scalable/actions/*.svg
%_datadir/appdata/%name.appdata.xml
%{?_enable_contractor:%_datadir/contractor/geary-attach.contract}
%doc AUTHORS MAINTAINERS NEWS README THANKS

%changelog
* Tue Mar 31 2015 Yuri N. Sedunov <aris@altlinux.org> 0.10.0-alt1
- 0.10.0

* Tue Feb 03 2015 Yuri N. Sedunov <aris@altlinux.org> 0.9.1-alt1
- 0.9.1

* Sat Dec 20 2014 Yuri N. Sedunov <aris@altlinux.org> 0.8.3-alt1
- 0.8.3

* Wed Nov 05 2014 Yuri N. Sedunov <aris@altlinux.org> 0.8.2-alt1
- 0.8.2

* Wed Oct 08 2014 Yuri N. Sedunov <aris@altlinux.org> 0.8.1-alt1
- 0.8.1

* Sat Sep 20 2014 Yuri N. Sedunov <aris@altlinux.org> 0.8.0-alt1
- 0.8.0

* Wed Sep 03 2014 Yuri N. Sedunov <aris@altlinux.org> 0.7.2-alt1
- 0.7.2

* Thu Aug 21 2014 Yuri N. Sedunov <aris@altlinux.org> 0.7.1-alt1
- 0.7.1

* Sat Jul 19 2014 Yuri N. Sedunov <aris@altlinux.org> 0.7.0-alt1
- 0.7.0

* Wed Jul 02 2014 Yuri N. Sedunov <aris@altlinux.org> 0.6.1-alt1
- 0.6.1

* Mon Mar 03 2014 Igor Zubkov <icesik@altlinux.org> 0.4.3-alt1
- 0.4.3

* Sat Nov 23 2013 Igor Zubkov <icesik@altlinux.org> 0.4.2-alt1
- 0.4.2

* Wed Nov 20 2013 Igor Zubkov <icesik@altlinux.org> 0.4.1-alt1
- 0.4.1 trunk (r1119)

* Mon Aug 26 2013 Igor Zubkov <icesik@altlinux.org> 0.3.1-alt3
- Cleanup build requires

* Sat Jun 22 2013 Igor Zubkov <icesik@altlinux.org> 0.3.1-alt2
- Fix desktop file

* Sat Apr 13 2013 Igor Zubkov <icesik@altlinux.org> 0.3.1-alt1
- 0.3.0 -> 0.3.1

* Fri Mar 29 2013 Igor Zubkov <icesik@altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus

