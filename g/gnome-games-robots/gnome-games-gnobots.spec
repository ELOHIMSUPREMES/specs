%define _unpackaged_files_terminate_build 1

%define _name robots
%define __name gnome-%_name
%define ver_major 3.14
%define _libexecdir %_prefix/libexec

Name: gnome-games-%_name
Version: %ver_major.2
Release: alt1

Summary: Gnome version of robots game for BSD games collection
Group: Games/Boards
License: GPLv3+
Url: http://live.gnome.org/GnomeGames/

Source: ftp://ftp.gnome.org/pub/gnome/sources/%__name/%ver_major/%__name-%version.tar.xz
Patch: %__name-3.7.92-alt-lfs.patch

Provides:  %__name = %version-%release
Obsoletes: gnome-games-gnobots
Provides:  gnome-games-gnobots = %version-%release

%define glib_ver 2.32.0
%define gtk_ver 3.4.0

BuildRequires: gnome-common
BuildRequires: intltool yelp-tools libgio-devel >= %glib_ver libgtk+3-devel >= %gtk_ver librsvg-devel
BuildRequires: libcanberra-gtk3-devel

%description
GNOME Robots is a development of the original Gnome Robots game which
was itself based on the text based robots game which can be found on a
number of UNIX systems, and comes with the BSD games package on Linux
systems.

%prep
%setup -n %__name-%version
%patch -p1 -b .lfs

%build
%autoreconf
%configure \
    --disable-schemas-compile
%make_build

%install
%makeinstall_std

%find_lang --with-gnome %__name

%files -f gnome-%_name.lang
%attr(2711,root,games) %_bindir/%__name
%_desktopdir/%__name.desktop
%_datadir/%__name
%_iconsdir/hicolor/*x*/*/*.png
%_iconsdir/hicolor/scalable/*/*.svg
%_iconsdir/HighContrast/*x*/apps/*.png
%_man6dir/%__name.*
%config %_datadir/glib-2.0/schemas/org.gnome.%_name.gschema.xml
%_datadir/appdata/%__name.appdata.xml

%changelog
* Tue Nov 11 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt1
- 3.14.2

* Fri Oct 10 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Sun Sep 21 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Sun Jun 22 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.3-alt1
- 3.12.3

* Mon May 12 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt1
- 3.12.2

* Mon Apr 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Sun Mar 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Tue Feb 04 2014 Yuri N. Sedunov <aris@altlinux.org> 3.10.2-alt1
- 3.10.2

* Tue Dec 17 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Tue Apr 16 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Wed Mar 27 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Wed Mar 20 2013 Yuri N. Sedunov <aris@altlinux.org> 3.7.92-alt1
- 3.7.92

* Tue Dec 25 2012 Yuri N. Sedunov <aris@altlinux.org> 3.7.2-alt1
- first build for people/gnome



