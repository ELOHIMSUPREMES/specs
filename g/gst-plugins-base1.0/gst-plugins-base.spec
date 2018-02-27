%define _name gst-plugins
%define ver_major 1.0
%define api_ver 1.0

%define _gst_libdir %_libdir/gstreamer-%api_ver
%define _gtk_docdir %_datadir/gtk-doc/html

%def_disable gtk_doc

Name: %_name-base%api_ver
Version: %ver_major.7
Release: alt1

Summary: An essential set of GStreamer plugins
Group: System/Libraries
License: LGPL
URL: http://gstreamer.freedesktop.org/

Requires: lib%_name%api_ver = %version-%release
Requires: gstreamer%api_ver

Provides: gstreamer%api_ver(audio-hardware-sink) = %version
Provides: gstreamer%api_ver(audio-hardware-source) = %version

Source: http://download.gnome.org/sources/%_name-base/%ver_major/%_name-base-%version.tar.xz
Patch: gst-plugins-base-0.11.94-alt-intltool.patch

BuildRequires: gstreamer%api_ver-devel libgstreamer%api_ver-gir-devel gtk-doc intltool libSM-devel
BuildRequires: libXext-devel libXv-devel libalsa-devel libgtk+3-devel libvisual0.4-devel iso-codes-devel
BuildRequires: libcdparanoia-devel liboil-devel libtheora-devel libvorbis-devel orc liborc-test-devel
BuildRequires: python-module-PyXML python-modules-encodings gobject-introspection-devel

%description
GStreamer Base Plug-ins is a well-groomed and well-maintained
collection of GStreamer plug-ins and elements, spanning the range of
possible types of elements one would want to write for GStreamer. A
wide range of video and audio decoders, encoders, and filters are
included.

%package -n lib%_name%api_ver
Summary: GStreamer plugin libraries
Group: System/Libraries

%description -n lib%_name%api_ver
Helper libraries for GStreamer plugins, containing base classes useful for elements

%package -n lib%_name%api_ver-gir
Summary: GObject introspection data for the GStreamer library
Group: System/Libraries
Requires: lib%_name%api_ver = %version-%release

%description -n lib%_name%api_ver-gir
GObject introspection data for the GStreamer library

%package -n %_name%api_ver-tools
Summary: GStreamer plugin tools
Group: Development/Other
Requires: %name = %version-%release

%description -n %_name%api_ver-tools
This package contains a few test tools from the
GStreamer Base Plugins distribution.

%package -n %_name%api_ver-devel
Summary: Development files for GStreamer plugins
Group: Development/C
Requires: lib%_name%api_ver = %version-%release
Requires: gstreamer%api_ver-devel

%description -n %_name%api_ver-devel
This package contains the libraries, headers and other files necessary
to develop GStreamer plugins.

%package -n %_name%api_ver-gir-devel
Summary: GObject introspection devel data for the GStreamer library
Group: System/Libraries
BuildArch: noarch
Requires: lib%_name%api_ver-gir = %version-%release
Requires: %_name%api_ver-devel = %version-%release

%description -n %_name%api_ver-gir-devel
GObject introspection devel data for the GStreamer library

%prep
%setup -n %_name-base-%version
%patch -p1

%build
%autoreconf
%configure \
	--with-default-audiosrc=pulsesrc \
	--with-default-audiosink=pulsesink \
	--with-default-videosrc=v4l2src \
	--with-default-videosink=xvimagesink \
	--disable-examples \
	--disable-valgrind \
	--enable-experimental \
	--enable-gio \
	--disable-debug \
	--disable-static \
	--with-html-dir=%_gtk_docdir \
	%{?_enable_gtk_doc:--enable-gtk-doc}

%make_build

%install
%make DESTDIR=%buildroot install

%find_lang %_name-base-%api_ver

%files -f %_name-base-%api_ver.lang
%dir %_gst_libdir
%_gst_libdir/*.so
%_datadir/%_name-base/%api_ver/*.dict
%exclude %_gst_libdir/*.la

%files -n lib%_name%api_ver
%_libdir/*.so.*
%dir %_gst_libdir

%files -n lib%_name%api_ver-gir
%_typelibdir/GstApp-%api_ver.typelib
%_typelibdir/GstAudio-%api_ver.typelib
%_typelibdir/GstFft-%api_ver.typelib
%_typelibdir/GstPbutils-%api_ver.typelib
%_typelibdir/GstRiff-%api_ver.typelib
%_typelibdir/GstRtp-%api_ver.typelib
%_typelibdir/GstRtsp-%api_ver.typelib
%_typelibdir/GstSdp-%api_ver.typelib
%_typelibdir/GstTag-%api_ver.typelib
%_typelibdir/GstVideo-%api_ver.typelib

%files -n %_name%api_ver-tools
%_bindir/*-%api_ver
%_man1dir/*

%files -n %_name%api_ver-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc
%_gtk_docdir/%_name-base-*-%api_ver

%files -n %_name%api_ver-gir-devel
%_girdir/GstApp-%api_ver.gir
%_girdir/GstAudio-%api_ver.gir
%_girdir/GstFft-%api_ver.gir
%_girdir/GstPbutils-%api_ver.gir
%_girdir/GstRiff-%api_ver.gir
%_girdir/GstRtp-%api_ver.gir
%_girdir/GstRtsp-%api_ver.gir
%_girdir/GstSdp-%api_ver.gir
%_girdir/GstTag-%api_ver.gir
%_girdir/GstVideo-%api_ver.gir

%changelog
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

