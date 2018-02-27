%define ver_major 0.2

Name: grilo-plugins
Version: %ver_major.12
Release: alt2
Summary: Plugins for the Grilo framework
Group: Sound
License: LGPLv2+
Url: https://wiki.gnome.org/Projects/Grilo

Source: %name-%version.tar

BuildRequires: gnome-common intltool >= 0.40.0
BuildRequires: gtk-doc yelp-tools
BuildRequires: glib2-devel >= 2.34 libgio-devel
BuildRequires: libgrilo-devel >= 0.2.10
BuildRequires: libxml2-devel
BuildRequires: libgupnp-devel >= 0.13
BuildRequires: libgupnp-av-devel >= 0.5
BuildRequires: libgssdp-devel
BuildRequires: libsqlite3-devel
BuildRequires: libgdata-devel >= 0.7.0
BuildRequires: libquvi-devel >= 0.4.0
BuildRequires: libsoup-devel
BuildRequires: libgcrypt-devel
BuildRequires: libgmime-devel
BuildRequires: tracker-devel
BuildRequires: liboauth-devel
BuildRequires: libgnome-online-accounts-devel >= 3.11.4
BuildRequires: libtotem-pl-parser-devel >= 3.4.1
BuildRequires: libdmapsharing-devel >= 2.9.12
BuildRequires: libjson-glib-devel
BuildRequires: libavahi-gobject-devel libavahi-glib-devel libavahi-devel
BuildRequires: libmediaart-devel
BuildRequires: librest-devel

Requires: grilo-tools
Requires: tracker

%description
Grilo is a framework that provides access to different sources of
multimedia content, using a pluggable system.
This package contains plugins to get information from theses sources:
- Apple Trailers
- Bookmarks
- Filesystem
- Flickr
- Gravatar
- Jamendo
- Last.fm (for album arts)
- Local metadata (album arts and thumbnails)
- Metadata Store
- Podcasts
- Shoutcast
- Tracker
- UPnP
- Vimeo
- Youtube

%prep
%setup

%build
NOCONFIGURE=1 ./autogen.sh
%configure		\
	--disable-static

%make_build

%install
%make_install DESTDIR=%buildroot install

# Remove files that will not be packaged
rm -f %buildroot%_libdir/grilo-%ver_major/*.la

%find_lang --with-gnome %name

%files -f %name.lang
%doc AUTHORS COPYING NEWS README
%_libdir/grilo-%ver_major/*.so*
%_libdir/grilo-%ver_major/*.xml

%changelog
* Fri Aug 22 2014 Yuri N. Sedunov <aris@altlinux.org> 0.2.12-alt2
- rebuilt against libgdata.so.19

* Thu Apr 03 2014 Alexey Shabalin <shaba@altlinux.ru> 0.2.12-alt1
- 0.2.12

* Thu Sep 26 2013 Yuri N. Sedunov <aris@altlinux.org> 0.2.9-alt2
- rebuild against libtotem-plparser.so.18

* Thu Aug 29 2013 Alexey Shabalin <shaba@altlinux.ru> 0.2.9-alt1
- 0.2.9

* Thu Jun 13 2013 Alexey Shabalin <shaba@altlinux.ru> 0.2.8-alt1
- 0.2.8

* Thu May 16 2013 Alexey Shabalin <shaba@altlinux.ru> 0.2.7-alt1
- 0.2.7

* Sun Mar 31 2013 Yuri N. Sedunov <aris@altlinux.org> 0.2.6-alt1
- 0.2.6

* Tue Jan 29 2013 Alexey Shabalin <shaba@altlinux.ru> 0.2.5-alt1
- 0.2.5

* Tue Dec 04 2012 Alexey Shabalin <shaba@altlinux.ru> 0.2.4-alt1
- 0.2.4

* Mon Nov 12 2012 Alexey Shabalin <shaba@altlinux.ru> 0.2.3-alt1
- 0.2.3

* Mon Oct 08 2012 Alexey Shabalin <shaba@altlinux.ru> 0.2.2-alt1
- 0.2.2
- add DMAP plugin
- add TMDb plugin

* Wed Sep 19 2012 Alexey Shabalin <shaba@altlinux.ru> 0.2.0-alt1
- 0.2.0

* Fri May 25 2012 Alexey Shabalin <shaba@altlinux.ru> 0.1.19-alt1
- 0.1.19

* Fri Mar 16 2012 Alexey Shabalin <shaba@altlinux.ru> 0.1.18-alt2.git9e007
- git snapshot 9e00790f40ee498a7359b00e0b11a7523fdd1b3e
- rebuild with tracker-0.14

* Tue Jan 10 2012 Alexey Shabalin <shaba@altlinux.ru> 0.1.18-alt1
- 0.1.18

* Mon Oct 31 2011 Alexey Shabalin <shaba@altlinux.ru> 0.1.17-alt1
- 0.1.17

* Tue Jul 12 2011 Alexey Shabalin <shaba@altlinux.ru> 0.1.16-alt1
- 0.1.16

* Thu Jun 23 2011 Alexey Shabalin <shaba@altlinux.ru> 0.1.15-alt4
- rebuild with new libgupnp

* Wed Jun 01 2011 Alexey Shabalin <shaba@altlinux.ru> 0.1.15-alt3
- build with tracker plugin

* Sun May 29 2011 Alexey Shabalin <shaba@altlinux.ru> 0.1.15-alt2
- rebuild with new libgdata

* Mon May 23 2011 Alexey Shabalin <shaba@altlinux.ru> 0.1.15-alt1
- initial build for ALT Linux Sisyphus
