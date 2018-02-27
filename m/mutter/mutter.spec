%define ver_major 3.10
%def_enable privatelib
%def_enable gtk_doc

Name: mutter
Version: %ver_major.3
Release: alt1
Epoch: 1

Summary: Clutter based compositing GTK3 Window Manager
Group: Graphical desktop/GNOME
License: GPLv2+
Url: http://ftp.gnome.org/pub/gnome/sources/%name
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Requires: lib%name = %epoch:%version-%release
Requires: zenity

#Source: %name-%version.tar
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

BuildPreReq: rpm-build-gnome gnome-common
BuildPreReq: intltool >= 0.34.90
BuildPreReq: gobject-introspection-devel >= 0.9.5
BuildRequires: libgtk+3-devel >= 3.3.7
BuildRequires: glib2-devel  libgio-devel >= 2.25.10
BuildRequires: libpango-devel >= 1.2.0
BuildRequires: libcairo-devel >= 1.10.0
BuildRequires: gsettings-desktop-schemas-devel >= 3.7.3
BuildRequires: libXcomposite-devel libXfixes-devel libXrender-devel libXdamage-devel libXi-devel >= 1.6.0
BuildRequires: libXcursor-devel libX11-devel libXinerama-devel libXext-devel libXrandr-devel libSM-devel libICE-devel
BuildRequires: libclutter-devel >= 1.14.3 libcogl-devel >= 1.15.8
BuildRequires: libgdk-pixbuf-devel
BuildRequires: gtk-doc
BuildRequires: libstartup-notification-devel zenity libcanberra-gtk3-devel
BuildRequires: libclutter-gir-devel libpango-gir-devel libgtk+3-gir-devel gsettings-desktop-schemas-gir-devel
BuildRequires: libgnome-desktop3-devel libupower-devel

%set_typelibdir %_libdir/%name
%set_girdir %_libdir/%name

%description
mutter is a minimal X window manager aimed at nontechnical users and is
designed  to  integrate well with the GNOME desktop.  mutter lacks some
features that may be expected by traditional UNIX  or  other  technical
users;  these users may want to investigate other available window man-
agers for use with GNOME or standalone.

%package -n lib%name
Summary: Shared library for Mutter
Group: System/Libraries

%description -n lib%name
This package contains shared library needed to run Mutter.

%package -n lib%name-devel
Summary: Development files for lib%name
Group: Development/C
Requires: lib%name = %epoch:%version-%release

%description -n lib%name-devel
This package contains headers and development libraries for lib%name

%package -n lib%name-gir
Summary: GObject introspection data for the Mutter library
Group: System/Libraries
Requires: lib%name = %epoch:%version-%release

%description -n lib%name-gir
GObject introspection data for the Mutter library

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the Mutter library
Group: System/Libraries
Requires: lib%name-devel = %epoch:%version-%release lib%name-gir = %epoch:%version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the Mutter library

%package gnome
Summary: GNOME-specific parts of Mutter
Group: Graphical desktop/GNOME
BuildArch: noarch
Provides: gnome-wm
Requires: %name = %epoch:%version-%release

%description gnome
This package contains everything necessary to use Mutter in GNOME desktop
environment.

%package devel-doc
Summary: Development docs package for mutter
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %version

%description devel-doc
Development docs package for mutter

%prep
%setup -q

%build
%autoreconf
DATADIRNAME=share %configure \
	--enable-introspection \
	%{?_enable_gtk_doc:--enable-gtk-doc} \
	--disable-static \
	--disable-schemas-compile

%make_build

%install
%make DESTDIR=%buildroot DATADIRNAME=share install

%find_lang --with-gnome %name creating-%name-themes

%files -f %name.lang
%doc README AUTHORS NEWS
%_bindir/*
%dir %_libdir/%name
%dir %_libdir/%name/plugins
%_libdir/%name/plugins/*.so
%_desktopdir/%name.desktop
%_man1dir/*

%if_enabled privatelib
%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%doc doc/*.txt HACKING
%_includedir/%name
%_libdir/*.so
%_pkgconfigdir/*.pc
%endif

%files -n lib%name-gir
%_libdir/%name/*.typelib

%files -n lib%name-gir-devel
%_libdir/%name/*.gir

%files gnome
%_datadir/glib-2.0/schemas/org.gnome.mutter.gschema.xml
%_datadir/GConf/gsettings/mutter-schemas.convert
%_datadir/gnome-control-center/keybindings/*.xml
%_datadir/gnome/wm-properties/%name-wm.desktop

%if_enabled gtk_doc
%files devel-doc
%_datadir/gtk-doc/html/*
%endif


%changelog
* Thu Jan 16 2014 Yuri N. Sedunov <aris@altlinux.org> 1:3.10.3-alt1
- 3.10.3

* Wed Dec 25 2013 Yuri N. Sedunov <aris@altlinux.org> 1:3.10.2-alt2
- updated to 7278f9b (fixed BGO #710296, 711618, 719669, 720545)

* Thu Nov 14 2013 Yuri N. Sedunov <aris@altlinux.org> 1:3.10.2-alt1
- 3.10.2

* Wed Oct 16 2013 Yuri N. Sedunov <aris@altlinux.org> 1:3.10.1.1-alt1
- 3.10.1.1

* Tue Oct 15 2013 Yuri N. Sedunov <aris@altlinux.org> 1:3.10.1-alt1
- 3.10.1

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 1:3.10.0.1-alt1
- 3.10.0.1

* Wed Jul 31 2013 Yuri N. Sedunov <aris@altlinux.org> 1:3.8.4-alt1
- 3.8.4

* Sat Jun 08 2013 Yuri N. Sedunov <aris@altlinux.org> 1:3.8.3-alt1
- 3.8.3

* Tue May 14 2013 Yuri N. Sedunov <aris@altlinux.org> 1:3.8.2-alt1
- 3.8.2

* Thu May 09 2013 Yuri N. Sedunov <aris@altlinux.org> 1:3.8.1-alt2
- updated to 2c210e0

* Tue Apr 16 2013 Yuri N. Sedunov <aris@altlinux.org> 1:3.8.1-alt1
- 3.8.1

* Wed Mar 27 2013 Alexey Shabalin <shaba@altlinux.ru> 1:3.8.0-alt1
- 3.8.0

* Tue Mar 19 2013 Alexey Shabalin <shaba@altlinux.ru> 1:3.7.92-alt1
- 3.7.92

* Thu Mar 07 2013 Alexey Shabalin <shaba@altlinux.ru> 1:3.7.91-alt1
- 3.7.91

* Fri Feb 22 2013 Alexey Shabalin <shaba@altlinux.ru> 1:3.7.90-alt1
- 3.7.90

* Mon Feb 18 2013 Alexey Shabalin <shaba@altlinux.ru> 1:3.6.3-alt1
- 3.6.3

* Tue Nov 13 2012 Alexey Shabalin <shaba@altlinux.ru> 1:3.6.2-alt1
- 3.6.2

* Tue Oct 16 2012 Alexey Shabalin <shaba@altlinux.ru> 1:3.6.1-alt1
- 3.6.1

* Mon Oct 08 2012 Alexey Shabalin <shaba@altlinux.ru> 1:3.6.0-alt2
- mutter-gnome as noarch

* Tue Sep 25 2012 Alexey Shabalin <shaba@altlinux.ru> 1:3.6.0-alt1
- 3.6.0

* Wed Sep 19 2012 Alexey Shabalin <shaba@altlinux.ru> 1:3.5.92-alt1
- 3.5.92

* Thu Sep 06 2012 Alexey Shabalin <shaba@altlinux.ru> 1:3.5.91-alt1
- 3.5.91

* Wed Apr 18 2012 Alexey Shabalin <shaba@altlinux.ru> 1:3.4.1-alt1
- 3.4.1

* Wed Mar 28 2012 Alexey Shabalin <shaba@altlinux.ru> 1:3.4.0-alt1
- 3.4.0

* Wed Jan 18 2012 Alexey Shabalin <shaba@altlinux.ru> 1:3.2.2-alt1
- 3.2.2

* Tue Oct 25 2011 Alexey Shabalin <shaba@altlinux.ru> 1:3.2.1-alt1
- 3.2.1

* Thu May 26 2011 Alexey Shabalin <shaba@altlinux.ru> 1:3.0.2.1-alt1
- 3.0.2.1

* Wed Apr 06 2011 Alexey Shabalin <shaba@altlinux.ru> 1:3.0.0-alt1
- 3.0.0

* Wed Mar 30 2011 Alexey Shabalin <shaba@altlinux.ru> 1:2.91.93-alt1
- 2.91.93

* Wed Mar 23 2011 Alexey Shabalin <shaba@altlinux.ru> 1:2.91.92-alt1
- 2.91.92

* Wed Mar 09 2011 Alexey Shabalin <shaba@altlinux.ru> 1:2.91.91-alt1
- 2.91.91

* Thu Mar 03 2011 Alexey Shabalin <shaba@altlinux.ru> 1:2.91.90-alt1.git20110302
- snapshot 20110302

* Fri Feb 25 2011 Alexey Shabalin <shaba@altlinux.ru> 1:2.91.90-alt1
- 2.91.90

* Fri Feb 04 2011 Alexey Shabalin <shaba@altlinux.ru> 1:2.91.6-alt1
- 2.91.6

* Thu Jan 20 2011 Alexey Shabalin <shaba@altlinux.ru> 1:2.91.5-alt1
- 2.91.5

* Mon Oct 11 2010 Alexey Shabalin <shaba@altlinux.ru> 1:2.91.0-alt2
- add serial to requires

* Wed Oct 06 2010 Alexey Shabalin <shaba@altlinux.ru> 1:2.91.0-alt1
- 2.91.0

* Tue Mar 23 2010 Alexey Shabalin <shaba@altlinux.ru> 1:2.29.1-alt1
- 2.29.1

* Sat Mar 13 2010 Alexey Shabalin <shaba@altlinux.ru> 1:2.29.0-alt2
- git snaphot ff4f096f1d9ec3d8113286ade9e9aa53da84b198
- install gir files to standart path

* Wed Mar 03 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:2.29.0-alt1
- 2.29.0

* Wed Feb 10 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:2.28.0-alt3
- fixed build with clutter 1.1.6

* Tue Dec 15 2009 Alexey Shabalin <shaba@altlinux.ru> 2.28.0-alt2
- enabled gobject-introspection

* Thu Oct 08 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.28.0-alt1
- 2.28.0

* Wed Sep 16 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.27.5-alt1
- 2.27.5

* Mon Sep 07 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.27.4-alt1
- 2.27.4

* Sat Aug 29 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.27.3-alt1
- 2.27.3

* Wed Aug 12 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.27.2-alt1
- 2.27.2

* Wed Aug 05 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.27.1-alt1
- initial release

