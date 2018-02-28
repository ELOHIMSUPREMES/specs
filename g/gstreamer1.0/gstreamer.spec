%define _name gstreamer
%define ver_major 1.6
%define api_ver 1.0
%define _libexecdir %_prefix/libexec
%define api_ver 1.0

%def_disable gtk-doc

Name: %_name%api_ver
Version: %ver_major.2
Release: alt1

Summary: GStreamer streaming media framework runtime
License: LGPL
Group: System/Libraries
URL: http://gstreamer.freedesktop.org

Requires: lib%name = %version-%release

Source: http://gstreamer.freedesktop.org/src/%_name/%_name-%version.tar.xz
Patch: %_name-0.11.94-alt-intltool.patch

BuildRequires: docbook-utils flex gcc-c++ ghostscript-utils glib2-devel gtk-doc intltool libcheck-devel libxml2-devel
BuildRequires: python-modules sgml-common transfig xml-utils gobject-introspection-devel
BuildRequires: libcap-utils

%description
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plugins.

%package -n lib%name
Summary: Shared libraries of GStreamer
Group: System/Libraries

%description -n lib%name
This package contains the shared libraries of the GStreamer media framework

%package -n lib%name-gir
Summary: GObject introspection data for the GStreamer library
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the GStreamer library

%package devel
Summary: Development files for GStreamer streaming-media framework
Group: Development/C
Requires: lib%name = %version-%release

%description devel
This package contains the libraries and header files necessary to
develop applications and plugins for GStreamer

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the GStreamer library
Group: System/Libraries
BuildArch: noarch
Requires: lib%name-gir = %version-%release %name-devel = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the GStreamer library

%package devel-doc
Summary: Development documentation for GStreamer
Group: Development/C
BuildArch: noarch

%description devel-doc
This package contains development documentation for GStreamer

%package doc
Summary: Documentation for GStreamer
Group: Documentation
BuildArch: noarch

%description doc
This package contains documentation for GStreamer

%package utils
Summary: GStreamer utilities
Group: System/Libraries
Requires: lib%name = %version-%release

%description utils
This package contains some utilities used to register, analyze, and run
Gstreamer plugins.

%prep
%setup -n %_name-%version
%patch -p1

%build
%autoreconf
%configure \
	--with-package-name=GStreamer \
	--with-package-origin=%name \
	--disable-examples \
	--disable-valgrind \
	--enable-docbook \
	%{?_enable_gtk_doc:--enable-gtk-doc} \
	--disable-gtk-doc-pdf \
	--disable-rpath \
	--disable-tests \
	--disable-debug \
	--disable-static \
	--with-bash-completion-dir=no
%make_build

%install
%makeinstall_std

%find_lang %_name-%api_ver

%post
setcap cap_net_bind_service,cap_net_admin+ep %_libexecdir/%_name-%api_ver/gst-ptp-helper 2>/dev/null ||:

%files -f %_name-%api_ver.lang
%dir %_libexecdir/%_name-%api_ver
%_libexecdir/%_name-%api_ver/gst-plugin-scanner
%_libexecdir/%_name-%api_ver/gst-ptp-helper
%dir %_libdir/%_name-%api_ver
%_libdir/%_name-%api_ver/*.so
%exclude %_libdir/%_name-%api_ver/*.la
%doc AUTHORS NEWS README RELEASE

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-gir
%_typelibdir/Gst-%api_ver.typelib
%_typelibdir/GstBase-%api_ver.typelib
%_typelibdir/GstCheck-%api_ver.typelib
%_typelibdir/GstController-%api_ver.typelib
%_typelibdir/GstNet-%api_ver.typelib

%files devel
%_includedir/*
%dir %_libdir/%_name-%api_ver/include/
%dir %_libdir/%_name-%api_ver/include/gst
%_libdir/%_name-%api_ver/include/gst/gstconfig.h
%_libdir/*.so
%_pkgconfigdir/*.pc
%_datadir/aclocal/*

%files -n lib%name-gir-devel
%_girdir/Gst-%api_ver.gir
%_girdir/GstBase-%api_ver.gir
%_girdir/GstCheck-%api_ver.gir
%_girdir/GstController-%api_ver.gir
%_girdir/GstNet-%api_ver.gir

%files devel-doc
%_datadir/gtk-doc/html/*

%files utils
%_bindir/*
%_man1dir/*

%files doc
%_datadir/doc/%_name-%api_ver

%changelog
* Wed Dec 16 2015 Yuri N. Sedunov <aris@altlinux.org> 1.6.2-alt1
- 1.6.2

* Fri Oct 30 2015 Yuri N. Sedunov <aris@altlinux.org> 1.6.1-alt1
- 1.6.1

* Sat Sep 26 2015 Yuri N. Sedunov <aris@altlinux.org> 1.6.0-alt1
- 1.6.0

* Sat Sep 19 2015 Yuri N. Sedunov <aris@altlinux.org> 1.5.91-alt1
- 1.5.91

* Thu Aug 20 2015 Yuri N. Sedunov <aris@altlinux.org> 1.5.90-alt1
- 1.5.90

* Thu Jun 25 2015 Yuri N. Sedunov <aris@altlinux.org> 1.5.2-alt1
- 1.5.2

* Mon Jun 08 2015 Yuri N. Sedunov <aris@altlinux.org> 1.5.1-alt1
- 1.5.1

* Sun Dec 28 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.5-alt1
- 1.4.5

* Mon Nov 10 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.4-alt1
- 1.4.4

* Wed Sep 24 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.3-alt1
- 1.4.3

* Fri Sep 19 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.2-alt1
- 1.4.2

* Thu Aug 28 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.1-alt1
- 1.4.1

* Mon Jul 21 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1
- 1.4.0

* Sun Apr 20 2014 Yuri N. Sedunov <aris@altlinux.org> 1.2.4-alt1
- 1.2.4

* Mon Feb 10 2014 Yuri N. Sedunov <aris@altlinux.org> 1.2.3-alt1
- 1.2.3

* Sun Dec 29 2013 Yuri N. Sedunov <aris@altlinux.org> 1.2.2-alt1
- 1.2.2

* Wed Nov 13 2013 Yuri N. Sedunov <aris@altlinux.org> 1.2.1-alt1
- 1.2.1

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Fri Aug 30 2013 Yuri N. Sedunov <aris@altlinux.org> 1.0.10-alt1
- 1.0.10

* Fri Jul 12 2013 Yuri N. Sedunov <aris@altlinux.org> 1.0.8-alt1
- 1.0.8

* Sat Apr 27 2013 Yuri N. Sedunov <aris@altlinux.org> 1.0.7-alt1
- 1.0.7

* Fri Mar 22 2013 Yuri N. Sedunov <aris@altlinux.org> 1.0.6-alt1
- 1.0.6

* Tue Jan 08 2013 Yuri N. Sedunov <aris@altlinux.org> 1.0.5-alt1
- 1.0.5

* Sat Nov 24 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.3-alt1
- 1.0.3

* Thu Oct 25 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- 1.0.2

* Sun Oct 07 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1

* Mon Sep 24 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0

* Mon Sep 17 2012 Yuri N. Sedunov <aris@altlinux.org> 0.11.99-alt1
- 0.11.99

* Fri Sep 14 2012 Yuri N. Sedunov <aris@altlinux.org> 0.11.94-alt1
- first build for Sisyphus

