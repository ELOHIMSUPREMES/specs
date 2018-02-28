%define _name gmime
%define ver_major 3.0
%define api_ver 3.0

%def_disable static

Name: lib%_name%api_ver
Version: %ver_major.2
Release: alt1

Summary: Glorious MIME Utility Library
License: LGPLv2+
Group: System/Libraries
Url: https://github.com/jstedfast/gmime

# VCS: git://git.gnome.org/gmime
# https://github.com/jstedfast/gmime.git
Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz

%define glib_ver 2.32.0
%define gi_ver 1.30.0

BuildRequires: /proc
BuildPreReq: rpm-build-gnome
BuildRequires: gcc-c++ libgio-devel >= %glib_ver
BuildRequires: libgpgme-devel libidn-devel zlib-devel
BuildRequires: gtk-doc docbook-utils
BuildRequires: gobject-introspection-devel >= %gi_ver
BuildRequires: libvala-devel vala vala-tools

%description

GMime is a C/C++ library for the creation and parsing of messages using
the Multipurpose Internet Mail Extension (MIME) as defined by numerous
IETF specifications.

%package devel
Summary: Development files for GMime
Group: Development/C
PreReq: %name = %version-%release

%description devel
This package contains development files required for packaging
GMime-based software.

%package gir
Summary: GObject introspection data for the GMime library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the GMime library.

%package gir-devel
Summary: GObject introspection devel data for the GMime library
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: %name-devel = %version-%release

%description gir-devel
GObject introspection devel data for the GMime library.

%package devel-doc
Summary: Development documentation for GMime
Group: Development/Documentation
Conflicts: %name < %version-%release
BuildArch: noarch

%description devel-doc
This package provides development documentation for the GMime library.

%package devel-static
Summary: Static GMime libraries
Group: Development/C
PreReq: %name-devel = %version-%release

%description devel-static
This package contains development libraries required for packaging
statically linked GMime-based software.

%define _gtk_docdir %_datadir/gtk-doc/html

%prep
%setup -n %_name-%version

%build
%autoreconf
%configure  %{subst_enable static} \
	    --enable-introspection \
	    --enable-vala \
	    --enable-largefile \
	    --enable-gtk-doc
%make_build

%install
%makeinstall_std

%files
%_libdir/lib%_name-%api_ver.so.*
%doc AUTHORS ChangeLog README

%files devel
%_includedir/*
%_libdir/lib%_name-%api_ver.so
%_pkgconfigdir/%_name-%ver_major.pc
%_vapidir/%_name-%api_ver.vapi
%_vapidir/%_name-%api_ver.deps

%files gir
%_typelibdir/GMime-%api_ver.typelib

%files gir-devel
%_girdir/GMime-%api_ver.gir

%files devel-doc
%_gtk_docdir/%_name-%api_ver/

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Sat Sep 02 2017 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt1
- 3.0.2

* Mon May 22 2017 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1

* Sun Apr 23 2017 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- first build for Sisyphus

