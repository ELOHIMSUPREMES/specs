%define _name gupnp-dlna

Name: libgupnp-dlna
Version: 0.10.2
Release: alt1
Summary: A collection of helpers for building UPnP AV applications

Group: System/Libraries
License: LGPLv2+
Url: http://www.gupnp.org/
Source: http://ftp.gnome.org/pub/GNOME/sources/gupnp-dlna/0.6/%name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libgio-devel
BuildRequires: pkgconfig(glib-2.0) >= 2.32 pkgconfig(gobject-2.0) pkgconfig(gmodule-2.0)
BuildRequires: pkgconfig(gstreamer-1.0) >= 1.0 pkgconfig(gstreamer-pbutils-1.0) >= 1.0
BuildRequires: gir(GObject) = 2.0 gir(Gst) = 1.0 gir(GstPbutils) = 1.0
BuildRequires: vala-tools >= 0.18 rpm-build-vala libvala-devel
BuildRequires: pkgconfig(gobject-introspection-1.0) >= 1.36.0
BuildRequires: vapi(gupnp-1.0) vapi(libxml-2.0) vapi(gstreamer-pbutils-1.0) vapi(gstreamer-1.0) vapi(gstreamer-base-1.0) vapi(gstreamer-video-1.0)
BuildRequires: pkgconfig(libxml-2.0) >= 2.5.0
BuildRequires: gtk-doc xml-utils

%description
GUPnP is an object-oriented open source framework for creating UPnP
devices and control points, written in C using GObject and libsoup.
The GUPnP API is intended to be easy to use, efficient and flexible.

GUPnP-dlna is a collection of helpers for building DLNA (Digital
Living Network Alliance) compliant applications using GUPnP.

%package devel
Summary: Development package for %_name
Group: Development/Other
Requires: %name = %version-%release

%description devel
Contains libraries and header files for developing applications that
use %_name.

%package gir
Summary: GObject introspection data for the %_name
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the %_name

%package gir-devel
Summary: GObject introspection devel data for the %_name
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the %_name

%package devel-doc
Summary: Development package for %_name
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %version

%description devel-doc
Contains developer documentation for %_name.

%prep
%setup
%patch -p1

%build
NOCONFIGURE=1 ./autogen.sh
%configure --disable-static --enable-gtk-doc
%make_build

%install

%makeinstall_std

%files
%doc AUTHORS COPYING README TODO
%_bindir/*
%_libdir/lib*.so.*
%_datadir/%{_name}*
%_libdir/%{_name}/*.so

%files devel
%_libdir/lib*.so
%_pkgconfigdir/*.pc
%_includedir/*
%_vapidir/*.deps
%_vapidir/*.vapi

%files gir
%_typelibdir/*.typelib

%files gir-devel
%_girdir/*.gir

%files devel-doc
%_datadir/gtk-doc/html/*

%changelog
* Thu Jun 13 2013 Alexey Shabalin <shaba@altlinux.ru> 0.10.2-alt1
- 0.10.2

* Fri Apr 19 2013 Alexey Shabalin <shaba@altlinux.ru> 0.10.1-alt1
- 0.10.1

* Fri Mar 29 2013 Alexey Shabalin <shaba@altlinux.ru> 0.10.0-alt1
- 0.10.0

* Mon Feb 25 2013 Alexey Shabalin <shaba@altlinux.ru> 0.9.5-alt1
- 0.9.5

* Wed Dec 12 2012 Alexey Shabalin <shaba@altlinux.ru> 0.7.0-alt1
- 0.7.0

* Fri Apr 06 2012 Alexey Shabalin <shaba@altlinux.ru> 0.6.6-alt1
- 0.6.6

* Tue Mar 13 2012 Alexey Shabalin <shaba@altlinux.ru> 0.6.5-alt1
- 0.6.5

* Wed Sep 21 2011 Alexey Shabalin <shaba@altlinux.ru> 0.6.3-alt1
- upstream snapshot (990d1bec2d39f42dfef04527464b784f57120837)
- add GObject packages

* Tue May 17 2011 Alexey Shabalin <shaba@altlinux.ru> 0.6.1-alt1
- 0.6.1

* Tue Oct 19 2010 Alexey Shabalin <shaba@altlinux.ru> 0.4.2-alt1
- initial build for ALT Linux Sisyphus
