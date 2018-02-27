%def_disable snapshot
%define _libexecdir %_prefix/libexec
%define ver_major 3.16

Name: gnome-tweak-tool
Version: %ver_major.2
Release: alt1

Summary: A tool to customize advanced GNOME 3 options
Group: Graphical desktop/GNOME
License: GPLv3
Url: https://live.gnome.org/GnomeTweakTool
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

%if_enabled snapshot
Source: %name-%version.tar
%else
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%endif
Patch: gnome-tweak-tool-3.8.0-alt-desktop.patch

BuildArch: noarch
Requires: gnome-shell >= %ver_major

BuildRequires: GConf gnome-common intltool libgio-devel libgtk+3-devel >= 3.12.0
BuildRequires: gsettings-desktop-schemas-devel >= 3.4.0
BuildRequires: python-module-pygobject3-devel >= 3.2.1

%description
GNOME Tweak Tool is an application for changing the advanced settings
of GNOME 3.

Features:
* Install and switch gnome-shell themes
* Switch GTK+ themes
* Switch icon themes
* Change
  - The user-interface and title bar fonts
  - Icons in menus and buttons
  - Behavior on laptop lid close
  - Shell font size
  - File manager desktop icons
  - Title bar click action
  - Shell clock to show date
  - Font hinting
  - Font anti-aliasing

%prep
%setup
%patch -b .desktop

%build
%{?_enable_snapshot:NOCONFIGURE=1 ./autogen.sh}
%configure --disable-schemas-compile
%make_build

%install
%make_install install DESTDIR=%buildroot

%find_lang %name

%files -f %name.lang
%_bindir/%name
%_libexecdir/%name-lid-inhibitor
%python_sitelibdir/gtweak
%_datadir/applications/%name.desktop
%_datadir/%name
%_iconsdir/hicolor/*/*/*.png
%_iconsdir/hicolor/*/*/*.svg
%_datadir/appdata/%name.appdata.xml
%doc AUTHORS NEWS README

%changelog
* Mon May 11 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Thu Apr 16 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Fri Nov 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt1
- 3.14.2

* Tue Sep 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Thu Mar 27 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Wed Nov 13 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Sat Nov 02 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt3
- updated to 3.10_5dce590 (fixed extension update checks)
- fixed BGO #710275

* Sun Sep 29 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt2
- updated to 3.10_a8f0982 (fixed BGO #708900)

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Wed Jul 17 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Mon Apr 08 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Thu Feb 28 2013 Yuri N. Sedunov <aris@altlinux.org> 3.7.4-alt1
- 3.7.4

* Mon Dec 17 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt2
- updated to 600e101a
- moved to System menu (ALT #27896)

* Tue Oct 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Wed Oct 03 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Mon May 14 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0.1-alt1
- 3.4.0.1

* Mon May 14 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Thu Mar 22 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.5-alt1
- 3.3.5 snapshot

* Sat Nov 19 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.2-alt1
- 3.2.2

* Mon Oct 31 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.2.0-alt1.1
- Rebuild with Python-2.7

* Wed Sep 28 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Wed Jun 22 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.5-alt1
- 3.0.5

* Sun May 22 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.4-alt1
- 3.0.4

* Thu Apr 28 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.3-alt1
- 3.0.3

* Wed Apr 27 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt1
- 3.0.2

* Thu Apr 07 2011 Alexey Shabalin <shaba@altlinux.ru> 3.0.0-alt1
- Initial package
