%define _unpackaged_files_terminate_build 1

%define _name chess
%define __name gnome-%_name
%define ver_major 3.14
%define _libexecdir %_prefix/libexec

Name: gnome-games-%_name
Version: %ver_major.0
Release: alt1

Summary: A chess game for GNOME
Group: Games/Boards
License: GPLv3+
Url: https://live.gnome.org/Chess

Source: ftp://ftp.gnome.org/pub/gnome/sources/%__name/%ver_major/%__name-%version.tar.xz

Provides:  %__name = %version-%release
Obsoletes: gnome-games-glchess
Provides:  gnome-games-glchess = %version-%release

%define glib_ver 2.32.0
%define gtk_ver 3.4.0
%define vala_ver 0.22.0

BuildRequires: gnome-common
BuildRequires: intltool yelp-tools libgio-devel >= %glib_ver libgtk+3-devel >= %gtk_ver librsvg-devel
BuildRequires: libGL-devel libGLU-devel vala-tools >= %vala_ver

%description
A chess game which supports several chess engines, with 2D and optionally
3D support if OpenGL is present.

%prep
%setup -n %__name-%version
[ ! -d m4 ] && mkdir m4

%build
%autoreconf
%configure \
    --disable-schemas-compile

%make_build

%install
%makeinstall_std

%find_lang --with-gnome %__name

%files -f gnome-%_name.lang
%_bindir/%__name
%_desktopdir/%__name.desktop
%_datadir/%__name
%_iconsdir/hicolor/*x*/apps/%__name.png
%_iconsdir/HighContrast/scalable/apps/%__name.svg
%_man6dir/%__name.*
%config %_datadir/glib-2.0/schemas/org.gnome.%_name.gschema.xml
%config(noreplace) %_sysconfdir/%__name/engines.conf
%_datadir/appdata/%__name.appdata.xml

%changelog
* Sun Sep 21 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Fri Jun 27 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.3-alt1
- 3.12.3

* Mon May 12 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt1
- 3.12.2

* Mon Apr 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Sun Mar 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Mon Jan 20 2014 Yuri N. Sedunov <aris@altlinux.org> 3.10.3-alt1
- 3.10.3

* Mon Nov 11 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.2-alt1
- 3.10.2

* Mon Oct 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1.1-alt1
- 3.10.1.1

* Sat Oct 12 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Mon Sep 23 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Tue Aug 20 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.4-alt1
- 3.8.4

* Mon Jun 10 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.3-alt1
- 3.8.3

* Thu May 16 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2.1-alt1
- 3.8.2.1

* Mon May 13 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt1
- 3.8.2

* Mon Apr 15 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Wed Mar 27 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Thu Mar 07 2013 Yuri N. Sedunov <aris@altlinux.org> 3.7.90-alt1
- first build for people/gnome



