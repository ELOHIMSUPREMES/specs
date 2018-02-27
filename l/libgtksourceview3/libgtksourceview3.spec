%define _name gtksourceview
%define api_ver 3.0
%define ver_major 3.14
%def_disable static
%def_disable gtk_doc
%def_enable introspection
%def_enable vala

Name: lib%{_name}3
Version: %ver_major.2
Release: alt1

Summary: GtkSourceView text widget library
License: LGPLv2+
Group: System/Libraries
Url: https://wiki.gnome.org/Projects/GtkSourceView

Source: %gnome_ftp/%_name/%ver_major/%_name-%version.tar.xz

# From configure.ac
%define intltool_ver 0.40
%define gtk_ver 3.13.7
%define libxml2_ver 2.6.0

BuildPreReq: rpm-build-gnome

# From configure.ac
BuildPreReq: gnome-common
BuildPreReq: intltool >= %intltool_ver
BuildPreReq: gtk-doc >= 1.11
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: libxml2-devel >= %libxml2_ver

BuildRequires: gcc-c++ perl-XML-Parser zlib-devel libgio-devel
%{?_enable_introspection:BuildRequires: gobject-introspection-devel >= 0.9.5 libgtk+3-gir-devel}
%{?_enable_vala:BuildRequires: vala-tools libvala-devel}
# for check
BuildRequires: xvfb-run

%description
GtkSourceView is a text widget that extends the standard gtk+ 2.x text
widget GtkTextView. It improves GtkTextView by implementing syntax
highlighting and other features typical of a source editor.

This package contains shared GtkSourceView library.

%package devel
Summary: Files to compile applications that use GtkSourceView
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains the files required to develop applications against
the GtkSourceView library.

%package devel-doc
Summary: Development documentation for %_name
Group: Development/Documentation
Conflicts: %name < %version-%release
BuildArch: noarch

%description devel-doc
GtkSourceView is a text widget that extends the standard gtk+ 3.x text
widget GtkTextView. It improves GtkTextView by implementing syntax
highlighting and other features typical of a source editor.

This package provides development documentation for %_name.

%package gir
Summary: GObject introspection data for the GtkSourceView library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the GtkSourceView library

%package gir-devel
Summary: GObject introspection devel data for the GtkSourceView library
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the GtkSourceView library

%define _gtk_docdir %_datadir/gtk-doc/html

%prep
%setup -n %_name-%version

%build
%configure \
	%{subst_enable static} \
	%{?_enable_gtk_doc:--enable-gtk-doc} \
	%{subst_enable introspection}

%make_build

%check
#xvfb-run %make check

%install
%makeinstall_std

%find_lang %_name-%api_ver

%files -f %_name-%api_ver.lang
%_libdir/*.so.*
%_datadir/%_name-%api_ver
%doc AUTHORS NEWS README

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*
%if_enabled vala
%_vapidir/%_name-%api_ver.deps
%_vapidir/%_name-%api_ver.vapi
%endif
%doc HACKING MAINTAINERS

%files devel-doc
%_gtk_docdir/*

%if_enabled introspection
%files gir
%_typelibdir/*

%files gir-devel
%_girdir/*
%endif

%changelog
* Mon Nov 10 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt1
- 3.14.2

* Mon Oct 13 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Mon Sep 22 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Fri Aug 22 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.3-alt1
- 3.12.3

* Mon May 12 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt1
- 3.12.2

* Tue Apr 15 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Mon Mar 24 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Mon Jan 27 2014 Yuri N. Sedunov <aris@altlinux.org> 3.10.2-alt1
- 3.10.2

* Mon Oct 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Mon Sep 23 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Sun Jul 07 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt1
- 3.8.2

* Mon Apr 15 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Mon Mar 25 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Mon Mar 18 2013 Yuri N. Sedunov <aris@altlinux.org> 3.7.92-alt1
- 3.7.92

* Sat Jan 26 2013 Yuri N. Sedunov <aris@altlinux.org> 3.6.3-alt1
- 3.6.3

* Wed Jan 23 2013 Yuri N. Sedunov <aris@altlinux.org> 3.6.2-alt1
- 3.6.2

* Sun Nov 04 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Tue Sep 25 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Tue May 15 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.2-alt1
- 3.4.2

* Tue Apr 17 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Tue Nov 08 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.3-alt1
- 3.2.3

* Sun Oct 16 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.2-alt1
- 3.2.2

* Fri Jul 01 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.5-alt1
- 3.0.5

* Mon Jun 20 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.4-alt1
- 3.0.4

* Wed May 25 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.3-alt1
- 3.0.3

* Wed May 25 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt1
- 3.0.2

* Tue Apr 26 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1

* Tue Apr 05 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Tue Mar 22 2011 Yuri N. Sedunov <aris@altlinux.org> 2.91.9-alt1
- 2.91.9

* Sat Jun 26 2010 Yuri N. Sedunov <aris@altlinux.org> 2.90.3-alt1
- first build for Sisyphus.

