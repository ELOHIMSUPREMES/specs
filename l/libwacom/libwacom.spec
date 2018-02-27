%define ver_major 0.10
%def_disable static

Name: libwacom
Version: %ver_major
Release: alt1

Summary: A Wacom tablets library
Group: System/Libraries
License: BSD-like
Url: http://linuxwacom.sf.net
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.bz2

Requires: %name-data = %version-%release

BuildRequires: glib2-devel libgudev-devel doxygen
# for check
BuildRequires: /proc

%description
%name is a library to identify Wacom tablets and their model-specific
features. It provides easy access to information such as "is this a
built-in on-screen tablet", "what is the size of this model", etc.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package data
Summary: Tablets data for %name
Group: System/Libraries
BuildArch: noarch

%description data
%name is a library to identify wacom tablets and their model-specific
features.

This package contains tablets/stylus data for %name.

%package devel-doc
Summary: Development documentation for %name
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name-devel < %version-%release

%description devel-doc
The %name-devel-doc package contains documentation for
developing applications that use %name.

%prep
%setup -q

%build
%configure \
    %{subst_enable static}

%make_build

%install
%make_install DESTDIR=%buildroot install

%check
%make check

%files
%_bindir/%name-list-local-devices
%_libdir/*.so.*
%doc NEWS README COPYING

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%files data
%dir %_datadir/%name
%_datadir/%name/*.tablet
%_datadir/%name/*.stylus
%_datadir/%name/layouts/

#%files devel-doc
#%_datadir/gtk-doc/html/*

%changelog
* Sat Aug 23 2014 Yuri N. Sedunov <aris@altlinux.org> 0.10-alt1
- 0.10

* Mon May 05 2014 Yuri N. Sedunov <aris@altlinux.org> 0.9-alt1
- 0.9

* Wed Jan 29 2014 Yuri N. Sedunov <aris@altlinux.org> 0.8-alt1
- 0.8

* Thu May 16 2013 Yuri N. Sedunov <aris@altlinux.org> 0.7.1-alt1
- 0.7.1

* Wed Feb 20 2013 Yuri N. Sedunov <aris@altlinux.org> 0.7-alt1
- 0.7

* Mon Sep 17 2012 Yuri N. Sedunov <aris@altlinux.org> 0.6-alt1
- 0.6

* Mon Jun 25 2012 Yuri N. Sedunov <aris@altlinux.org> 0.5-alt1
- 0.5

* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 0.4-alt1
- 0.4

* Tue Feb 07 2012 Yuri N. Sedunov <aris@altlinux.org> 0.3-alt1
- 0.3

* Tue Jan 17 2012 Yuri N. Sedunov <aris@altlinux.org> 0.2-alt1
- 0.2

* Fri Jan 06 2012 Yuri N. Sedunov <aris@altlinux.org> 0.1-alt1
- first build for Sisyphus

