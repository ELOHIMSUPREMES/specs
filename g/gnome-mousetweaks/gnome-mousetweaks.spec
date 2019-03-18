%define ver_major 3.32
%define _name mousetweaks

Name: gnome-%_name
Version: %ver_major.0
Release: alt1

Summary: Mouse accessibility enhancements
License: %gpl3plus
Group: Graphical desktop/GNOME
Url: https://wiki.gnome.org/Projects/Mousetweaks

Source: %gnome_ftp/%_name/%ver_major/%_name-%version.tar.xz

Provides: %_name = %version-%release
Requires: dconf

BuildRequires: rpm-build-gnome rpm-build-licenses

# From configure.ac
BuildRequires: gnome-common
BuildRequires: libgio-devel >= 2.28.5
BuildRequires: libgtk+3-devel >= 3.0.7
BuildRequires: libX11-devel libXfixes-devel libXcursor-devel libXtst-devel
BuildRequires: gsettings-desktop-schemas-devel

%description
The Mousetweaks package provides mouse accessibility enhancements for
the GNOME desktop. These enhancements are: 1. It offers a way to perform
the various clicks without using any hardware button. (hover click)

2. It allows users to perform a secondary click by keeping the primary
mousebutton pressed for a determined amount of time. (simulated
secondary click)

3. For desktops using the gnome-panel, it provides two panel applets
that the user can install on the gnome-panels. - The first applet
provides an alternative way to control the hover click. - The second
applet creates an area on the panel into which the pointer can be
captured until the user releases it with a predefined button and
modifier combination.

The hover click and the simulated secondary click can be accessed
through the Universal Access control panel in the GNOME Control Center.
The applets however can only be accessed on desktops using the
gnome-panel.

%prep
%setup -n %_name-%version

%build
%configure \
	--disable-schemas-compile
%make_build

%install
%makeinstall_std
%find_lang --with-gnome %_name

%define schemas  %_name pointer-capture-applet

%files -f %_name.lang
%_bindir/*
%_datadir/%_name
%_man1dir/*
%config %_datadir/glib-2.0/schemas/*
%_datadir/GConf/gsettings/*
%doc AUTHORS ChangeLog NEWS README

%changelog
* Mon Mar 11 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Mon Mar 24 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Tue Mar 26 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Wed Mar 06 2013 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Sun Sep 09 2012 Yuri N. Sedunov <aris@altlinux.org> 3.5.91-alt1
- 3.5.91

* Tue May 15 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.2-alt1
- 3.4.2

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Mon Sep 26 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Tue May 24 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt1
- 3.0.2

* Mon Nov 15 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt1
- 2.32.1

* Tue Oct 19 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1
- 2.32.0

* Tue Sep 14 2010 Yuri N. Sedunov <aris@altlinux.org> 2.31.92-alt1
- 2.31.92

* Wed Sep 08 2010 Yuri N. Sedunov <aris@altlinux.org> 2.31.91-alt1
- 2.31.91

* Mon Jun 21 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.2-alt1
- 2.30.2

* Sun May 02 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.1-alt1
- 2.30.1

* Sun Apr 04 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt2
- updated buildreqs

* Sun Mar 28 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0

* Mon Feb 08 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.90-alt1
- 2.29.90

* Tue Jan 26 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.6-alt1
- 2.29.6

* Tue Jan 12 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.5-alt1
- 2.29.5

* Mon Dec 14 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.2-alt1
- 2.28.2

* Mon Oct 19 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.1-alt1
- 2.28.1

* Tue Sep 22 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Mon Aug 24 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.91-alt1
- 2.27.91

* Thu Aug 20 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.90-alt1
- 2.27.90

* Mon Jun 29 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.3-alt1
- 2.26.3

* Mon May 18 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.2-alt1
- 2.26.2

* Sat Mar 21 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0
- updated buildreqs

* Tue Jan 13 2009 Yuri N. Sedunov <aris@altlinux.org> 2.24.3-alt1
- 2.24.3

* Mon Nov 24 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.2-alt1
- 2.24.2
- remove obsolete %%post{,un} scripts
- updated buildreqs

* Tue Jul 01 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.3-alt1
- 2.22.3 

* Thu Jun 19 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.2-alt1
- First build for Sisyphus
