%define ver_major 0.22
%define api_ver 1.0

Name: libgit2-glib
Version: %ver_major.4
Release: alt1

Summary: Git library for GLib
Group: System/Libraries
License: LGPLv2+
Url: https://live.gnome.org/Libgit2-glib

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

%define libgit2_ver 0.22.0
%define glib_ver 2.28

BuildRequires: gnome-common gtk-doc
BuildRequires: libgio-devel >= %glib_ver libgit2-devel >= %libgit2_ver
BuildRequires: libssh2-devel gobject-introspection-devel
BuildRequires: rpm-build-python3 python3-devel python3-module-pygobject3-devel
BuildRequires: vala-tools

%description
Libgit2-glib is a glib wrapper library around the libgit2 git access library.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
Libgit2-glib is a glib wrapper library around the libgit2 git access library.

The %name-devel package contains libraries and header files for
developing applications that use %name.

%package gir
Summary: GObject introspection data for the Libgit2-glib library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
Libgit2-glib is a glib wrapper library around the libgit2 git access library.

This package provides GObject introspection data for the Libgit2-glib library.

%package gir-devel
Summary: GObject introspection devel data for the Libgit2-glib library
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %version-%release

%description gir-devel
Libgit2-glib is a glib wrapper library around the libgit2 git access library.

This package provides GObject introspection devel data for the Libgit2-glib library .

%package devel-doc
Summary: Development documentation for Libgit2-glib
Group: Development/Documentation
Conflicts: %name < %version, %name > %version
BuildArch: noarch

%description devel-doc
Libgit2-glib is a glib wrapper library around the libgit2 git access library.

This package contains documentation needed for developing Libgit2-glib applications.


%prep
%setup

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%_libdir/%name-%api_ver.so.*
%python3_sitelibdir/gi/overrides/*
%doc AUTHORS COPYING NEWS

%files devel
%_includedir/%name-%api_ver/
%_libdir/%name-%api_ver.so
%_libdir/pkgconfig/%name-%api_ver.pc
%_vapidir/ggit-%api_ver.vapi
%_vapidir/ggit-%api_ver.deps

%files gir
%_typelibdir/Ggit-%api_ver.typelib

%files gir-devel
%_girdir/Ggit-%api_ver.gir

%files devel-doc
%_datadir/gtk-doc/*

%changelog
* Tue Apr 07 2015 Yuri N. Sedunov <aris@altlinux.org> 0.22.4-alt1
- 0.22.4

* Sun Mar 29 2015 Yuri N. Sedunov <aris@altlinux.org> 0.22.2-alt1
- 0.22.2

* Sun Jan 18 2015 Yuri N. Sedunov <aris@altlinux.org> 0.22.0-alt1
- 0.22.0

* Wed Nov 05 2014 Yuri N. Sedunov <aris@altlinux.org> 0.0.24-alt1
- 0.0.24

* Tue Sep 16 2014 Yuri N. Sedunov <aris@altlinux.org> 0.0.22-alt1
- 0.0.22

* Fri Jul 25 2014 Yuri N. Sedunov <aris@altlinux.org> 0.0.20-alt1
- 0.0.20

* Mon Jun 30 2014 Yuri N. Sedunov <aris@altlinux.org> 0.0.18-alt1
- 0.0.18

* Wed Mar 05 2014 Yuri N. Sedunov <aris@altlinux.org> 0.0.12-alt1
- 0.0.12

* Tue Jul 02 2013 Yuri N. Sedunov <aris@altlinux.org> 0.0.6-alt1
- 0.0.6

* Sat Jun 22 2013 Yuri N. Sedunov <aris@altlinux.org> 0.0.2-alt1
- first build for Sisyphus

