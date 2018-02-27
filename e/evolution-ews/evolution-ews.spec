%define ver_major 3.16

Name: evolution-ews
Version: %ver_major.3
Release: alt1

Group: Networking/Mail
Summary: Evolution extension for Exchange Web Services
License: LGPLv2
Url: https://wiki.gnome.org/Apps/Evolution
Source: http://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar


%define ver_base 3.16
%define evo_ver_base %ver_base

%define evolution_ver 3.12.0
# from configure.ac
%define eds_ver 3.16.0
%define libmspack_ver 0.4


Requires: evolution >= %evolution_ver
Requires: evolution-data-server >= %eds_ver
Requires: libmspack >= %libmspack_ver

BuildPreReq: gnome-common rpm-build-gnome gtk-doc
BuildPreReq: evolution-data-server-devel >= %eds_ver
BuildPreReq: evolution-devel >= %evolution_ver
BuildPreReq: libmspack-devel >= %libmspack_ver

BuildPreReq: intltool
BuildRequires: glib2-devel >= 2.40
BuildRequires: libgtk+3-devel >= 3.0
BuildRequires: libsoup-devel >= 2.42
BuildRequires: libsqlite3-devel libical-devel
BuildRequires: gcc-c++
# following unusual reqs needed to link against evolution >= 3.13.6 libraries
BuildRequires: libchamplain-gtk3-devel libgail3-devel gcr-libs-devel libp11-kit-devel
BuildRequires: libgnome-desktop3-devel libdbus-devel libdbus-glib-devel libgeocode-glib-devel
BuildRequires: libgeoclue-devel libgtkspell3-devel libgnome-autoar-devel
BuildRequires: libcanberra-gtk3-devel libcryptui-devel

%description
This package allows Evolution to interact with Microsoft Exchange servers,
versions 2007 and later, through its Exchange Web Services (EWS) interface.

%prep
%setup

%build
#NOCONFIGURE=1 ./autogen.sh
%autoreconf
%configure --disable-static

%make_build

%install
%makeinstall_std

# Remove files we don't want packaged (no devel subpackage).
rm -rf %buildroot%_includedir/evolution-data-server
find %buildroot%_libdir -name '*.la' -exec rm {} \;
rm -f %buildroot%_libdir/evolution-data-server/*.so

%find_lang %name

%files -f %name.lang
%doc COPYING NEWS README
%_libdir/evolution-data-server/*.so.*
%_libdir/evolution-data-server/camel-providers/*
%_libdir/evolution-data-server/addressbook-backends/*.so
%_libdir/evolution-data-server/calendar-backends/*.so
%_libdir/evolution-data-server/registry-modules/*.so
%_libdir/evolution/modules/*.so
%_datadir/evolution/errors/*.error
%_datadir/evolution-data-server/ews/windowsZones.xml
%_datadir/appdata/evolution-ews.metainfo.xml

%changelog
* Tue Jun 09 2015 Alexey Shabalin <shaba@altlinux.ru> 3.16.3-alt1
- 3.16.3

* Wed May 13 2015 Alexey Shabalin <shaba@altlinux.ru> 3.16.2-alt1
- 3.16.2

* Wed Apr 15 2015 Alexey Shabalin <shaba@altlinux.ru> 3.16.1-alt1
- 3.16.1

* Thu Mar 26 2015 Alexey Shabalin <shaba@altlinux.ru> 3.16.0-alt1
- 3.16.0

* Tue Jan 13 2015 Alexey Shabalin <shaba@altlinux.ru> 3.12.10-alt1
- 3.12.10

* Wed Dec 17 2014 Alexey Shabalin <shaba@altlinux.ru> 3.12.9-alt1
- 3.12.9

* Tue Nov 11 2014 Alexey Shabalin <shaba@altlinux.ru> 3.12.8-alt1
- 3.12.8

* Mon Oct 13 2014 Alexey Shabalin <shaba@altlinux.ru> 3.12.7-alt1
- 3.12.7

* Wed Aug 27 2014 Alexey Shabalin <shaba@altlinux.ru> 3.12.5-alt1
- 3.12.5

* Wed Jul 30 2014 Alexey Shabalin <shaba@altlinux.ru> 3.12.4-alt1
- 3.12.4

* Wed Jun 11 2014 Alexey Shabalin <shaba@altlinux.ru> 3.12.3-alt1
- 3.12.3

* Mon May 12 2014 Alexey Shabalin <shaba@altlinux.ru> 3.12.2-alt1
- 3.12.2

* Mon Apr 14 2014 Alexey Shabalin <shaba@altlinux.ru> 3.12.1-alt1
- 3.12.1

* Mon Mar 24 2014 Alexey Shabalin <shaba@altlinux.ru> 3.12.0-alt1
- 3.12.0

* Tue Feb 18 2014 Alexey Shabalin <shaba@altlinux.ru> 3.10.4-alt1
- initial build
