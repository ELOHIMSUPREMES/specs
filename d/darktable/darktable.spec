%define ver_major 1.6

Name: darktable
Version: %ver_major.0
Release: alt1

Summary: Darktable is a virtual lighttable and darkroom for photographer
License: GPLv3
Group: Graphics

Url: http://%name.sourceforge.net/
#VCS: https://github.com/darktable-org/darktable.git
#Source: %name-%version.tar
Source: http://downloads.sourceforge.net/%name/%name-%version.tar.xz

BuildPreReq: rpm-build-gnome
BuildRequires: libgio-devel >= 2.30 libgtk+2-devel >= 2.24
BuildRequires: cmake gcc-c++ intltool libSDL-devel libXScrnSaver-devel libXcomposite-devel libXcursor-devel
BuildRequires: libXdamage-devel libXdmcp-devel libXinerama-devel libXpm-devel libXrandr-devel
BuildRequires: libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel
BuildRequires: libdbus-glib-devel libexiv2-devel libflickcurl-devel libsecret-devel
BuildRequires: libgomp-devel libgphoto2-devel libjpeg-devel liblcms2-devel liblensfun-devel
BuildRequires: libpng-devel librsvg-devel libsqlite3-devel libtiff-devel libxkbfile-devel lsb-release
BuildRequires: openexr-devel perl-Pod-Parser
BuildRequires: libjson-glib-devel libsoup-devel xsltproc libpixman-devel libexpat-devel
BuildRequires: libcolord-gtk-devel libudev-devel
BuildRequires: libGraphicsMagick-c++-devel libopenjpeg-devel
BuildRequires: libharfbuzz-devel libwebp-devel libxshmfence-devel
# for build from git tree
#BuildRequires: gnome-doc-utils fop saxon ...

%description
darktable is a virtual light table and darkroom for photographers. It manages
your digital negatives in a database and lets you view them through a zoomable
light table. It also enables you to develop raw images and enhance them.

%prep
%setup

%build
%cmake -DCMAKE_SKIP_RPATH:BOOL=OFF \
-DCMAKE_BUILD_TYPE=Release
%cmake_build VERBOSE=1

%install
%cmakeinstall_std

ln -s %name/lib%name.so %buildroot%_libdir/lib%name.so

install -pD -m644 data/pixmaps/16x16/darktable.png %buildroot%_miconsdir/darktable.png
install -pD -m644 data/pixmaps/32x32/darktable.png %buildroot%_niconsdir/darktable.png
install -pD -m644 data/pixmaps/48x48/darktable.png %buildroot%_liconsdir/darktable.png

%find_lang %name

%files -f %name.lang
%_bindir/*
%_datadir/%name/
%_libdir/lib%name.so
%_libdir/%name/
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*
%_man1dir/*
%_datadir/appdata/%name.appdata.xml
%exclude /usr/share/doc/%name/

%changelog
* Tue Dec 09 2014 Yuri N. Sedunov <aris@altlinux.org> 1.6.0-alt1
- 1.6.0

* Sun Jun 08 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.2-alt2
- rebuilt against libcolord.so.2

* Thu May 15 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.2-alt1
- 1.4.2

* Fri Feb 21 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.1-alt1
- 1.4.1

* Sat Dec 28 2013 Yuri N. Sedunov <aris@altlinux.org> 1.4-alt1
- 1.4 release

* Tue Dec 03 2013 Yuri N. Sedunov <aris@altlinux.org> 1.4-alt0.1.rc1
- 1.4-rc1
- built against libexiv2.so.13

* Wed Sep 18 2013 Yuri N. Sedunov <aris@altlinux.org> 1.2.3-alt1
- 1.2.3, fixed (ALT #29371)

* Sun Aug 25 2013 Yuri N. Sedunov <aris@altlinux.org> 1.2.2-alt1
- 1.2.2
- GraphicsMagick, libopenjpeg support

* Thu Jan 24 2013 Yuri N. Sedunov <aris@altlinux.org> 1.1.2-alt1
- 1.1.2

* Thu Oct 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.4-alt1.1
- Rebuilt with libpng15

* Sat Jun 16 2012 Victor Forsiuk <force@altlinux.org> 1.0.4-alt1
- 1.0.4

* Tue May 15 2012 Victor Forsiuk <force@altlinux.org> 1.0.3-alt1
- 1.0.3

* Thu Mar 15 2012 Victor Forsiuk <force@altlinux.org> 1.0-alt1
- 1.0

* Sat Nov 12 2011 Victor Forsiuk <force@altlinux.org> 0.9.3-alt1
- 0.9.3

* Wed Nov 02 2011 Yuri N. Sedunov <aris@altlinux.org> 0.9.2-alt2
- rebuilt against libexiv2.so.11

* Sun Aug 28 2011 Victor Forsiuk <force@altlinux.org> 0.9.2-alt1
- 0.9.2

* Wed Jul 27 2011 Victor Forsiuk <force@altlinux.org> 0.9.1-alt1
- 0.9.1

* Sun Jul 03 2011 Victor Forsiuk <force@altlinux.org> 0.9-alt1
- 0.9

* Wed Mar 09 2011 Victor Forsiuk <force@altlinux.org> 0.8-alt3
- Refresh BuildRequires.

* Thu Feb 17 2011 Victor Forsiuk <force@altlinux.org> 0.8-alt2
- Fix build mistake, now darktable will work correctly (closes: #25102).

* Wed Feb 16 2011 Victor Forsiuk <force@altlinux.org> 0.8-alt1
- 0.8

* Tue Dec 14 2010 Victor Forsiuk <force@altlinux.org> 0.7.1-alt1
- 0.7.1

* Fri Dec 03 2010 Victor Forsiuk <force@altlinux.org> 0.7-alt1
- 0.7

* Wed Sep 08 2010 Victor Forsiuk <force@altlinux.org> 0.6-alt1
- 0.6

* Tue Jun 01 2010 Victor Forsiuk <force@altlinux.org> 0.5-alt2
- Rebuild with libexiv2.so.9.

* Wed Mar 31 2010 Victor Forsiuk <force@altlinux.org> 0.5-alt1
- 0.5

* Wed Feb 10 2010 Victor Forsiuk <force@altlinux.org> 0.4-alt1.git20100210
- Git snapshot from 2010-02-10.

* Tue Aug 18 2009 Victor Forsyuk <force@altlinux.org> 0.2-alt1
- Initial build.
