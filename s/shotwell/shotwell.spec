%define ver_major 0.23
%define gst_api_ver 1.0

Name: shotwell
Version: %ver_major.0
Release: alt1

Summary: digital photo organizer designed for the GNOME desktop environment
Group: Graphics
License: LGPL
Url: http://www.yorba.org/shotwell/

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
#Source: %name-%version.tar

Requires: dconf
# for video-thumbnailer
Requires: gst-plugins-base%gst_api_ver gst-plugins-good%gst_api_ver gst-libav

BuildRequires: gstreamer%gst_api_ver-devel gst-plugins%gst_api_ver-devel libGConf-devel
BuildRequires: libdconf-devel libdbus-glib-devel libgexiv2-devel >= 0.10.3
BuildRequires: libgphoto2-devel libgudev-devel libjson-glib-devel
BuildRequires: libraw-devel libgomp-devel
BuildRequires: libsqlite3-devel libstdc++-devel libunique3-devel libwebkit2gtk-devel
BuildRequires: vala librest-devel libgee0.8-devel desktop-file-utils gnome-doc-utils

%description
Shotwell is a digital photo organizer designed for the GNOME desktop
environment.  It allows you to import photos from disk or camera,
organize them in various ways, view them in full-window or fullscreen
mode, and export them to share with others.

%define _libexecdir %_prefix/libexec/%name

%prep
%setup

%build
./configure --disable-icon-update --prefix=%_prefix --lib=%_lib
%make_build

%install
%makeinstall_std
%find_lang --with-gnome --output=%name.lang %name %name-extras

%files -f %name.lang
%_bindir/%name
%_libexecdir/%name-video-thumbnailer
%_prefix/libexec/%name/%name-settings-migrator
%_libdir/%name
%_desktopdir/%{name}*
%_iconsdir/hicolor/*x*/apps/%name.svg
%_iconsdir/hicolor/scalable/apps/%name.svg
%_datadir/%name
%_datadir/GConf/gsettings/*
%_datadir/glib-2.0/schemas/*
%_datadir/appdata/%name.appdata.xml
%doc AUTHORS COPYING NEWS README THANKS

%changelog
* Tue Apr 26 2016 Yuri N. Sedunov <aris@altlinux.org> 0.23.0-alt1
- 0.23.0

* Sat Apr 16 2016 Yuri N. Sedunov <aris@altlinux.org> 0.22.1-alt1
- 0.22.1

* Tue Sep 15 2015 Yuri N. Sedunov <aris@altlinux.org> 0.22.0-alt2
- rebuilt against libraw.so.15

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 0.22.0-alt1
- 0.22.0

* Tue Feb 03 2015 Yuri N. Sedunov <aris@altlinux.org> 0.21.0-alt2
- rebuilt against libgphoto2_port.so.12

* Tue Feb 03 2015 Yuri N. Sedunov <aris@altlinux.org> 0.21.0-alt1
- 0.21.0

* Sat Nov 01 2014 Yuri N. Sedunov <aris@altlinux.org> 0.20.2-alt1
- 0.20.2

* Fri Oct 03 2014 Yuri N. Sedunov <aris@altlinux.org> 0.20.1-alt1
- 0.20.1

* Sat Sep 20 2014 Yuri N. Sedunov <aris@altlinux.org> 0.20.0-alt1
- 0.20.0

* Fri Aug 22 2014 Yuri N. Sedunov <aris@altlinux.org> 0.19.0-alt1
- 0.19.0

* Wed Jul 02 2014 Yuri N. Sedunov <aris@altlinux.org> 0.18.1-alt1
- 0.18.1

* Wed Mar 19 2014 Yuri N. Sedunov <aris@altlinux.org> 0.18.0-alt1
- 0.18.0

* Wed Mar 05 2014 Yuri N. Sedunov <aris@altlinux.org> 0.17.2-alt1
- 0.17.2

* Tue Feb 18 2014 Yuri N. Sedunov <aris@altlinux.org> 0.17.1-alt1
- 0.17.1

* Wed Feb 05 2014 Yuri N. Sedunov <aris@altlinux.org> 0.17.0-alt1
- 0.17.0 snapshot (6321cbf4)

* Tue Jan 21 2014 Vladimir Lettiev <crux@altlinux.ru> 0.15.1-alt2
- rebuilt with libraw 0.16.0

* Sat Dec 07 2013 Yuri N. Sedunov <aris@altlinux.org> 0.15.1-alt1
- 0.15.1

* Tue Apr 09 2013 Vladimir Lettiev <crux@altlinux.ru> 0.14.1-alt1
- 0.14.1

* Fri Jan 25 2013 Vladimir Lettiev <crux@altlinux.ru> 0.13.1-alt2
- rebuilt with libgexiv2 0.5.0

* Tue Oct 09 2012 Vladimir Lettiev <crux@altlinux.ru> 0.13.1-alt1
- 0.13.1

* Thu Sep 20 2012 Vladimir Lettiev <crux@altlinux.ru> 0.13.0-alt1
- 0.13.0

* Wed Jun 13 2012 Vladimir Lettiev <crux@altlinux.ru> 0.12.3-alt1
- 0.12.3
- build with new shared libraw

* Thu Apr 12 2012 Vladimir Lettiev <crux@altlinux.ru> 0.12.2-alt1
- 0.12.2

* Mon Apr 09 2012 Vladimir Lettiev <crux@altlinux.ru> 0.12.1-alt1
- 0.12.1

* Wed Jan 25 2012 Vladimir Lettiev <crux@altlinux.ru> 0.11.99-alt2
- git snapshot d867f19

* Thu Nov 03 2011 Vladimir Lettiev <crux@altlinux.ru> 0.11.99-alt1
- git snapshot c1f9e00

* Wed Oct 19 2011 Vladimir Lettiev <crux@altlinux.ru> 0.11.5-alt1
- 0.11.5

* Fri Oct 14 2011 Vladimir Lettiev <crux@altlinux.ru> 0.11.4-alt1
- 0.11.4

* Wed Oct 12 2011 Vladimir Lettiev <crux@altlinux.ru> 0.11.3-alt1
- 0.11.3

* Fri Oct 07 2011 Vladimir Lettiev <crux@altlinux.ru> 0.11.2-alt1
- 0.11.2
- Source cloned from upstream git
- No longer need to install or compile GConf schemas (b3d5985d)

* Wed Sep 07 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.11.0-alt2
- Dependance on dconf added.

* Wed Aug 24 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.11.0-alt1
- New version 0.11.0
- shotwell-plugins-mk.patch deleted

* Sat Jul 30 2011 Vladimir Lettiev <crux@altlinux.ru> 0.10.1-alt1
- New version 0.10.1
- Fixed plugins linking
- Dropped shotwell-0.9.1-vala.patch

* Thu May 05 2011 Yuri N. Sedunov <aris@altlinux.org> 0.8.1-alt3
- fixed build with vala-0.10.4 (4c74b5c)

* Fri Feb 18 2011 Vladimir Lettiev <crux@altlinux.ru> 0.8.1-alt2
- Rebuilt with libraw 0.13.1

* Wed Jan 12 2011 Vladimir Lettiev <crux@altlinux.ru> 0.8.1-alt1
- New version 0.8.1

* Fri Dec 24 2010 Vladimir Lettiev <crux@altlinux.ru> 0.8.0-alt1
- New version 0.8.0
- Updated buildrequires

* Fri Dec 03 2010 Vladimir Lettiev <crux@altlinux.ru> 0.7.2-alt2
- Rebuilt with libraw 0.11.3

* Mon Oct 18 2010 Vladimir Lettiev <crux@altlinux.ru> 0.7.2-alt1
- New version 0.7.2

* Tue Jul 27 2010 Vladimir Lettiev <crux@altlinux.ru> 0.6.1-alt1
- New version 0.6.1

* Thu Jun 03 2010 Vladimir Lettiev <crux@altlinux.ru> 0.5.2-alt1
- New version 0.5.2

* Wed Mar 17 2010 Vladimir Lettiev <crux@altlinux.ru> 0.5.0-alt1
- new version 0.5.0

* Tue Mar 16 2010 Vladimir Lettiev <crux@altlinux.ru> 0.4.3-alt1
- initial build

