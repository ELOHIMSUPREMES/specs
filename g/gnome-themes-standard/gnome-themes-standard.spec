%define ver_major 3.6

Name: gnome-themes-standard
Version: %ver_major.2
Release: alt1

Summary: A set of standard themes for GNOME desktop
License: LGPLv2.1+
Group: Graphical desktop/GNOME
Url: http://www.gnome.org
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

Obsoletes: gtk2-themes-accessibility
Provides: gtk2-themes-accessibility = %version-%release
Obsoletes: icon-themes-accessibility
Provides: icon-themes-accessibility = %version-%release
Obsoletes: gnome-themes-accessibility
Provides: gnome-themes-accessibility = %version-%release

Requires: %name-data = %version-%release

%define theme_prefix gnome-theme
BuildPreReq: intltool >= 0.35.0
BuildRequires: libgtk+3-devel >= 3.5.17 libgtk+2-devel librsvg-devel

%description
This package provides a set of standard GTK+-(2/3) themes, engines,
metacity themes, cursors, backgrounds for GNOME 3 desktop.

%package data
Summary: Arch-independent data for %name
Group: Graphical desktop/GNOME
BuildArch: noarch
Requires: libgtk3-engine-adwaita = %version-%release
Requires: gnome-icon-theme >= 3.0.0
# for gtk2 themes
Requires: libgtk-engine-hc
Requires: gtk2-theme-clearlooks

%description data
This package provides an Arch-independent part of %name.

%package -n libgtk3-engine-adwaita
Summary: GTK+3 theme engine Adwaita
Group: Graphical desktop/GNOME

%description -n libgtk3-engine-adwaita
This package provides a GTK+3 theme engine Adwaita.

%package -n libgtk2-engine-adwaita
Summary: GTK+2 theme engine Adwaita
Group: Graphical desktop/GNOME

%description -n libgtk2-engine-adwaita
This package provides a GTK+2 theme engine Adwaita.

%prep
%setup -q

%build
%configure
%make_build

%install
%make DESTDIR=%buildroot install

%find_lang %name

%files
%files data -f %name.lang
%_datadir/gnome-background-properties/adwaita.xml
%dir %_datadir/themes/Adwaita
%_datadir/themes/Adwaita/index.theme
%_datadir/themes/Adwaita/metacity-1/
%_datadir/themes/Adwaita/backgrounds/
%_datadir/icons/Adwaita/cursors/
%dir %_datadir/themes/Adwaita/gtk-2.0
%_datadir/themes/Adwaita/gtk-2.0/gtkrc
%_datadir/themes/Adwaita/gtk-2.0/Arrows/
%_datadir/themes/Adwaita/gtk-2.0/Buttons/
%_datadir/themes/Adwaita/gtk-2.0/Check-Radio/
%_datadir/themes/Adwaita/gtk-2.0/Entry/
%_datadir/themes/Adwaita/gtk-2.0/Expanders/
%_datadir/themes/Adwaita/gtk-2.0/Handles/
%_datadir/themes/Adwaita/gtk-2.0/Lines/
%_datadir/themes/Adwaita/gtk-2.0/Menu-Menubar/
%_datadir/themes/Adwaita/gtk-2.0/Others/
%_datadir/themes/Adwaita/gtk-2.0/ProgressBar/
%_datadir/themes/Adwaita/gtk-2.0/Range/
%_datadir/themes/Adwaita/gtk-2.0/Scrollbars/
%_datadir/themes/Adwaita/gtk-2.0/Shadows/
%_datadir/themes/Adwaita/gtk-2.0/Spin/
%_datadir/themes/Adwaita/gtk-2.0/Tabs/
%_datadir/themes/Adwaita/gtk-2.0/Toolbar/

%dir %_datadir/themes/Adwaita/gtk-3.0
%_datadir/themes/Adwaita/gtk-3.0/gtk.css
%_datadir/themes/Adwaita/gtk-3.0/settings.ini
%_datadir/themes/Adwaita/gtk-3.0/gtk-dark.css
%_datadir/themes/Adwaita/gtk-3.0/gtk.gresource

# Accessibility themes from ghome-temes(-default)
%_datadir/themes/HighContrast/gtk-2.0/gtkrc
%_datadir/themes/HighContrast/gtk-3.0/gtk.css
%_datadir/themes/HighContrast/gtk-3.0/gtk.gresource
%_datadir/themes/HighContrast/index.theme
%_datadir/themes/HighContrast/gtk-3.0/settings.ini
%_iconsdir/HighContrast/
# metacity theme
%_datadir/themes/HighContrast/metacity-1/metacity-theme-3.xml
%doc NEWS README

%files -n libgtk3-engine-adwaita
%_libdir/gtk-3.0/3.0.0/theming-engines/libadwaita.so
%exclude %_libdir/gtk-3.0/3.0.0/theming-engines/libadwaita.la

%files -n libgtk2-engine-adwaita
%_libdir/gtk-2.0/2.10.0/engines/libadwaita.so
%exclude %_libdir/gtk-2.0/2.10.0/engines/libadwaita.la

%changelog
* Tue Nov 13 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.2-alt1
- 3.6.2

* Tue Oct 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1
- new libgtk2-engine-adwaita subpackage

* Tue Sep 25 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0.2-alt1
- 3.6.0.2

* Tue May 15 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.2-alt1
- 3.4.2

* Sat Apr 14 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Tue Mar 20 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.92-alt1
- 3.3.92

* Tue Oct 18 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Mon Sep 26 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Mon May 23 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt1
- 3.0.2

* Mon Apr 25 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1

* Fri Apr 08 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Mon Mar 28 2011 Yuri N. Sedunov <aris@altlinux.org> 2.91.93-alt1
- 2.91.93

* Wed Jan 19 2011 Yuri N. Sedunov <aris@altlinux.org> 2.91.5-alt1
- 2.91.5

* Fri Dec 17 2010 Yuri N. Sedunov <aris@altlinux.org> 2.91.4-alt1
- first build for Sisyphus

