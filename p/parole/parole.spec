Name: parole
Version: 0.5.1
Release: alt1

Summary: Media player for the Xfce desktop
License: %gpl2plus
Group: Video

URL: http://goodies.xfce.org/projects/applications/parole
# git://git.xfce.org/apps/parole
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Packager: XFCE Team <xfce@packages.altlinux.org>

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libxfce4ui-devel libxfce4util-devel libexo-devel libxfconf-devel
BuildRequires: libgtk+2-devel libnotify-devel libtag-devel
BuildRequires: gstreamer1.0-devel gst-plugins1.0-devel
BuildRequires: libdbus-glib-devel libdbus-devel
BuildRequires: intltool gtk-doc

%description
Parole is a modern simple media player based on the GStreamer framework
and written to fit well in the Xfce desktop. Parole features playback of
local media files, DVD/CD and live streams. Parole is extensible via
plugins.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: libgtk+2-devel
BuildArch: noarch

%description devel
This package contains header files and documentation
for developing plugins for %name.

%prep
%setup
%patch -p1
mkdir m4

%build
%xfce4reconf
%configure \
    --disable-static \
    --enable-maintainer-mode \
    --enable-taglib \
	--with-gstreamer=1.0 \
    --enable-gtk-doc \
    --enable-debug=no
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc AUTHORS README THANKS
%_bindir/%name
%_libdir/%name-*/
%exclude %_libdir/%name-*/*.la
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/*
%_datadir/%name/

%files devel
%_includedir/*
%doc %_datadir/gtk-doc/html/*

%changelog
* Tue Jun 04 2013 Mikhail Efremov <sem@altlinux.org> 0.5.1-alt1
- Updated to 0.5.1.

* Fri Mar 08 2013 Mikhail Efremov <sem@altlinux.org> 0.5.0-alt1
- Build with gstreamer1.0.
- Updated to 0.5.0.

* Tue Jan 08 2013 Mikhail Efremov <sem@altlinux.org> 0.4.0-alt1
- Updated to 0.4.0.

* Mon May 21 2012 Mikhail Efremov <sem@altlinux.org> 0.2.0.6-alt3
- Fix DSO linking.
- Updated translations from upstream git.

* Tue Apr 17 2012 Mikhail Efremov <sem@altlinux.org> 0.2.0.6-alt2
- Rebuild against libxfce4util.so.6 (libxfce4util-4.9).
- Updated translations from upstream git.

* Tue Jun 07 2011 Mikhail Efremov <sem@altlinux.org> 0.2.0.6-alt1
- Updated to 0.2.0.6.

* Mon Feb 21 2011 Mikhail Efremov <sem@altlinux.org> 0.2.0.2-alt2
- Package parole-devel as noarch.

* Sun Feb 20 2011 Mikhail Efremov <sem@altlinux.org> 0.2.0.2-alt1
- Fix documentation bulding.
- Initial build (slightly based on FC spec).
