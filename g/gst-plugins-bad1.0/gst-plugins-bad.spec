%define _name gst-plugins
%define api_ver 1.0
%define ver_major 1.2

%define _gst_libdir %_libdir/gstreamer-%api_ver
%define _gtk_docdir %_datadir/gtk-doc/html

%def_enable gtk_doc

Name: %_name-bad%api_ver
Version: %ver_major.3
Release: alt2

Summary: A set of GStreamer plugins that need more quality
Group: System/Libraries
License: LGPL
URL: http://gstreamer.freedesktop.org/

Requires: lib%_name%api_ver >= 1.0.5
Requires: gstreamer%api_ver >= 1.0.5

Source: http://gstreamer.freedesktop.org/src/gst-plugins-bad/%_name-bad-%version.tar.xz
Patch: gst-plugins-bad-0.11.94-alt-intltool.patch

BuildRequires: gst-plugins%api_ver-devel
BuildRequires: bzlib-devel gcc-c++ gtk-doc intltool libSDL-devel libX11-devel
BuildRequires: libalsa-devel libcdaudio-devel libdca-devel libdirac-devel libdvdnav-devel libexif-devel
BuildRequires: libfaad-devel libgio-devel libgsm-devel libjasper-devel libmjpegtools-devel libmms-devel
BuildRequires: libmpcdec-devel libneon-devel liboil-devel libsoundtouch-devel libssl-devel libmodplug-devel
BuildRequires: libtimidity-devel libxvid-devel python-module-PyXML python-modules-email python-modules-encodings
BuildRequires: timidity-instruments libcelt-devel libdc1394-devel libkate-devel libtiger-devel
BuildRequires: libvpx-devel librtmp-devel liborc-devel orc libofa-devel libmusicbrainz-devel libass-devel
BuildRequires: libzbar-devel libwayland-client-devel libwebp-devel libopenjpeg-devel libbluez-devel
BuildRequires: libfluidsynth-devel libdbus-devel libxml2-devel libgnutls-devel libvdpau-devel
BuildRequires: libsbc-devel libschroedinger-devel libusb-devel libgudev-devel libopus-devel libcurl-devel
BuildRequires: libvo-amrwbenc-devel librsvg-devel libvo-aacenc-devel
BuildRequires: gobject-introspection-devel libgstreamer1.0-gir-devel

%description
GStreamer Bad Plug-ins is a set of plug-ins that aren't up to par
compared to the rest.  They might be close to being good quality, but
they're missing something - be it a good code review, some
documentation, a set of tests, a real live maintainer, or some actual
wide use.  If the blanks are filled in they might be upgraded to
become part of either gst-plugins-good or gst-plugins-ugly, depending
on the other factors.

%package devel
Summary: Development files for GStreamer plugins
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains the libraries, headers and other files necessary
to develop GStreamer Bad Plug-ins.

%package doc
Summary: Documentation for %name
Group: Documentation
BuildArch: noarch

%description doc
This package contains documentation for GStreamer Bad Plug-ins.

%prep
%setup -n %_name-bad-%version
%patch -p1

%build
%autoreconf
%configure \
    --disable-examples \
    --enable-experimental \
    %{subst_enable gtk_doc} \
    --disable-static \
    --with-html-dir=%_gtk_docdir

%make_build

%install
%make DESTDIR=%buildroot install

%find_lang %_name-bad-%api_ver

%files -f %_name-bad-%api_ver.lang
%doc AUTHORS NEWS README RELEASE
%_libdir/*.so.*
%dir %_gst_libdir
%_gst_libdir/*.so
%exclude %_gst_libdir/*.la
%_typelibdir/GstEGL-%api_ver.typelib
%_typelibdir/GstInsertBin-%api_ver.typelib
%_typelibdir/GstMpegts-%api_ver.typelib
%_datadir/gstreamer-%api_ver/presets/GstVoAmrwbEnc.prs
#%_datadir/gstreamer-%api_ver/presets/GstVP8Enc.prs
#%_datadir/glib-2.0/schemas/*.xml

%files devel
%_includedir/gstreamer-%api_ver/*
%_libdir/*.so
%_pkgconfigdir/*.pc
%_girdir/GstEGL-%api_ver.gir
%_girdir/GstInsertBin-%api_ver.gir
%_girdir/GstMpegts-%api_ver.gir

%if_enabled gtk_doc
%files doc
%_gtk_docdir/gst-plugins-bad-plugins-%api_ver
%_gtk_docdir/gst-plugins-bad-libs-%api_ver
%endif

%changelog
* Thu Feb 27 2014 Yuri N. Sedunov <aris@altlinux.org> 1.2.3-alt2
- enabled VisualOn AAC support via libvo-aacenc (ALT #29852)

* Mon Feb 10 2014 Yuri N. Sedunov <aris@altlinux.org> 1.2.3-alt1
- 1.2.3

* Sat Jan 04 2014 Yuri N. Sedunov <aris@altlinux.org> 1.2.2-alt2
- rebuilt against libwebp.so.5

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

* Sat Sep 15 2012 Yuri N. Sedunov <aris@altlinux.org> 0.11.94-alt1
- first build for Sisyphus

