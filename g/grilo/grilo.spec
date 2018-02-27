%define ver_major 0.2

Name: grilo
Version: %ver_major.7
Release: alt1
Summary: Content discovery framework
Group: Sound
License: LGPLv2+
Url: http://live.gnome.org/Grilo

Source: %name-%version.tar
#Patch1: %name-%version-%release.patch

BuildRequires: gnome-common intltool >= 0.40.0
BuildRequires: glib2-devel >= 2.29.10 libgio-devel
BuildRequires: libxml2-devel
BuildRequires: libgtk+3-devel >= 3.0
BuildRequires: libsoup-devel >= 2.39.0 libsoup-gir-devel
BuildRequires: liboauth-devel
BuildRequires: vala-tools libvala-devel
BuildRequires: gtk-doc >= 1.10
BuildRequires: gobject-introspection-devel >= 0.9.0

%description
Grilo is a framework that provides access to different sources of
multimedia content, using a pluggable system.
This package contains the core library and elements.

%package -n lib%name
Summary: Libraries files for Grilo framework
Group: System/Libraries

%description -n lib%name
Grilo is a framework that provides access to different sources of
multimedia content, using a pluggable system.
This package contains the core library.

%package -n lib%name-devel
Summary: Development files for Grilo framework
Group: Development/Other
Requires: lib%name = %version-%release

%description -n lib%name-devel
Grilo is a framework that provides access to different sources of
multimedia content, using a pluggable system.
This package contains the core library and elements, as well as
general and API documentation.

%package devel-doc
Summary: Development documentation for %name
Group: Development/GNOME and GTK+
Conflicts: lib%name < %version-%release
BuildArch: noarch

%description devel-doc
This package provides development documentation for %name.

%package -n lib%name-gir
Summary: GObject introspection data for the %name library
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the %name library

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the %name library
Group: System/Libraries
BuildArch: noarch
Requires: lib%name-gir = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the %name library

%package tools
Summary: Tools for the %name library
Group: Sound
Requires: lib%name = %version-%release

%description tools
Tools for the %name library

%define _gtk_docdir %_datadir/gtk-doc/html

%prep
%setup
#%%patch1 -p1

# Fix vala detection for version 0.16
# sed -i.vala 's/libvala-0.14/libvala-0.16/g' configure*

%build
NOCONFIGURE=1 ./autogen.sh
%configure			\
	--disable-static	\
	--enable-vala		\
	--enable-gtk-doc	\
	--enable-introspection	\
	--enable-grl-net	\
	--disable-tests

%make_build

%install
%make_install DESTDIR=%buildroot install
mkdir -p %buildroot%_libdir/grilo-%ver_major %buildroot%_datadir/grilo-%ver_major/plugins

%find_lang %name

# Remove files that will not be packaged
rm -f %buildroot%_bindir/grilo-simple-playlist

%files tools
%doc AUTHORS COPYING NEWS README TODO
%_bindir/grl-inspect*
%_bindir/grilo-test-ui*
%_man1dir/*

%files -n lib%name -f %name.lang
%_libdir/*.so.*
%dir %_libdir/grilo-%ver_major
%dir %_datadir/grilo-%ver_major/plugins

%files -n lib%name-gir
%_typelibdir/*.typelib

%files -n lib%name-gir-devel
%_girdir/*.gir

%files -n lib%name-devel
%_includedir/%name-%ver_major
%_libdir/*.so
%_pkgconfigdir/*.pc
%_vapidir/*

%files devel-doc
%_gtk_docdir/*

%changelog
* Thu Sep 19 2013 Alexey Shabalin <shaba@altlinux.ru> 0.2.7-alt1
- 0.2.7

* Thu May 16 2013 Alexey Shabalin <shaba@altlinux.ru> 0.2.6-alt1
- 0.2.6

* Mon Apr 08 2013 Alexey Shabalin <shaba@altlinux.ru> 0.2.5-alt1
- 0.2.5

* Tue Dec 04 2012 Alexey Shabalin <shaba@altlinux.ru> 0.2.4-alt1
- 0.2.4

* Mon Nov 12 2012 Alexey Shabalin <shaba@altlinux.ru> 0.2.3-alt1
- 0.2.3

* Mon Oct 08 2012 Alexey Shabalin <shaba@altlinux.ru> 0.2.2-alt1
- 0.2.2

* Wed Sep 19 2012 Alexey Shabalin <shaba@altlinux.ru> 0.2.0-alt1
- 0.2.0

* Fri May 25 2012 Alexey Shabalin <shaba@altlinux.ru> 0.1.19-alt1
- 0.1.19

* Thu Mar 29 2012 Alexey Shabalin <shaba@altlinux.ru> 0.1.18-alt2
- rebuild with vala-0.16

* Tue Jan 10 2012 Alexey Shabalin <shaba@altlinux.ru> 0.1.18-alt1
- 0.1.18

* Wed Oct 26 2011 Alexey Shabalin <shaba@altlinux.ru> 0.1.17-alt2
- rebuild with vala-0.14

* Wed Sep 14 2011 Alexey Shabalin <shaba@altlinux.ru> 0.1.17-alt1
- 0.1.17

* Tue Jul 12 2011 Alexey Shabalin <shaba@altlinux.ru> 0.1.16-alt1
- 0.1.16

* Mon May 23 2011 Alexey Shabalin <shaba@altlinux.ru> 0.1.15-alt1
- initial build for ALT Linux Sisyphus
