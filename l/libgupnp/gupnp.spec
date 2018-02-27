%define _name gupnp
%def_disable static
%def_disable gtk_doc
%def_enable introspection

Name: libgupnp
Version: 0.20.4
Release: alt1

Summary: A framework for creating UPnP devices and control points
Group: System/Libraries
License: LGPLv2+
Url: http://www.gupnp.org/

Source: http://www.gupnp.org/sources/%_name/%_name-%version.tar.xz

BuildPreReq: gnome-common libgssdp-devel >= 0.14.4 glib2-devel >= 2.24.0 libgio-devel
BuildRequires: libxml2-devel libsoup-devel >= 2.28.2 libuuid-devel gtk-doc
BuildRequires: vala-tools rpm-build-vala libvala-devel
%{?_enable_introspection:BuildPreReq: gobject-introspection-devel libsoup-gir-devel libgssdp-gir-devel}

%description
gUPnP is an object-oriented open source framework for creating UPnP
devices and control points, written in C using GObject and libsoup.
The gUPnP API is intended to be easy to use, efficient and flexible.

%package devel
Summary: Development files and libraries for gUPnP
Group: Development/C
Requires: %name = %version-%release

%description devel
gUPnP is an object-oriented open source framework for creating UPnP
devices and control points, written in C using GObject and libsoup.
The gUPnP API is intended to be easy to use, efficient and flexible.

This package provides files for development with gUPnP.

%package devel-doc
Summary: Development documentaion for gUPnP
Group: Development/C
BuildArch: noarch
Conflicts: %name < %version

%description devel-doc
gUPnP is an object-oriented open source framework for creating UPnP
devices and control points, written in C using GObject and libsoup.
The gUPnP API is intended to be easy to use, efficient and flexible.

This package provides development documentations for gUPnP.

%package gir
Summary: GObject introspection data for the gUPnP library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the gUPnP library

%package gir-devel
Summary: GObject introspection devel data for the gUPnP library
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the gUPnP library


%prep
%setup -q -n %_name-%version

%build
%configure --disable-static \
%{?_enable_gtk_doc:--enable-gtk-doc} \
%{subst_enable introspection}

%make_build

%install
%make DESTDIR=%buildroot install

%check
%make check

%files
%_libdir/*.so.*
%_bindir/gupnp-binding-tool
%doc AUTHORS README ChangeLog

%files devel
%_pkgconfigdir/*.pc
%_libdir/*.so
%_includedir/*
%_vapidir/*.deps
%_vapidir/*.vapi

%files devel-doc
%_datadir/gtk-doc/html/*

%if_enabled introspection
%files gir
%_typelibdir/*.typelib

%files gir-devel
%_girdir/*.gir
%endif


%changelog
* Tue Jul 30 2013 Yuri N. Sedunov <aris@altlinux.org> 0.20.4-alt1
- 0.20.4

* Sun Jun 02 2013 Yuri N. Sedunov <aris@altlinux.org> 0.20.3-alt1
- 0.20.3

* Wed Mar 06 2013 Yuri N. Sedunov <aris@altlinux.org> 0.20.1-alt1
- 0.20.1

* Fri Feb 22 2013 Yuri N. Sedunov <aris@altlinux.org> 0.20.0-alt1
- 0.20.0

* Tue Dec 11 2012 Alexey Shabalin <shaba@altlinux.ru> 0.19.3-alt1
- 0.19.3

* Thu Sep 06 2012 Yuri N. Sedunov <aris@altlinux.org> 0.18.4-alt1
- 0.18.4

* Thu May 10 2012 Yuri N. Sedunov <aris@altlinux.org> 0.18.3-alt1
- 0.18.3

* Sat Mar 17 2012 Yuri N. Sedunov <aris@altlinux.org> 0.18.2-alt1
- 0.18.2

* Fri Dec 09 2011 Yuri N. Sedunov <aris@altlinux.org> 0.18.1-alt1
- 0.18.1

* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.18.0-alt1.1
- Rebuild with Python-2.7

* Wed Aug 31 2011 Yuri N. Sedunov <aris@altlinux.org> 0.18.0-alt1
- 0.18.0

* Tue Aug 09 2011 Yuri N. Sedunov <aris@altlinux.org> 0.17.2-alt1
- 0.17.2

* Thu Jun 16 2011 Yuri N. Sedunov <aris@altlinux.org> 0.17.0-alt1
- 0.17.0

* Tue May 31 2011 Yuri N. Sedunov <aris@altlinux.org> 0.16.1-alt1
- 0.16.1

* Sun Mar 13 2011 Yuri N. Sedunov <aris@altlinux.org> 0.14.1-alt1
- 0.14.1

* Sun Nov 07 2010 Yuri N. Sedunov <aris@altlinux.org> 0.14.0-alt2
- rebuild for update dependencies

* Mon Oct 18 2010 Yuri N. Sedunov <aris@altlinux.org> 0.14.0-alt1
- 0.14.0

* Tue Jun 22 2010 Yuri N. Sedunov <aris@altlinux.org> 0.13.4-alt1
- 0.13.4

* Fri Apr 16 2010 Yuri N. Sedunov <aris@altlinux.org> 0.13.3-alt1
- 0.13.3
- introspection support

* Sun Jan 03 2010 Yuri N. Sedunov <aris@altlinux.org> 0.13.2-alt1
- 0.13.2

* Tue Nov 03 2009 Yuri N. Sedunov <aris@altlinux.org> 0.13.1-alt1
- 0.13.1

* Mon Sep 21 2009 Yuri N. Sedunov <aris@altlinux.org> 0.13.0-alt1
- 0.13.0

* Wed Jun 24 2009 Yuri N. Sedunov <aris@altlinux.org> 0.12.8-alt1
- new version (closes #20468)

* Mon Apr 27 2009 Yuri N. Sedunov <aris@altlinux.org> 0.12.7-alt1
- 0.12.7

* Sun Jan 18 2009 Yuri N. Sedunov <aris@altlinux.org> 0.12.5-alt1
- new version

* Fri Nov 28 2008 Yuri N. Sedunov <aris@altlinux.org> 0.12.4-alt1
- first build for Sisyphus

