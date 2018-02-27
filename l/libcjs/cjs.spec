%define ver_major 2.6
%define _name cjs
%define api_ver 1.0

Name: lib%_name
Version: %ver_major.2
Release: alt1

Summary: Javascript Bindings for Cinnamon
Group: System/Libraries
# The following files contain code from Mozilla which
# is triple licensed under MPL1.1/LGPLv2+/GPLv2+:
# The console module (modules/console.c)
# Stack printer (cjs/stack.c)
License: MIT and (MPLv1.1 or GPLv2+ or LGPLv2+)
Url: https://github.com/linuxmint/cjs

Source: %_name-%version.tar

%define glib_ver 2.33.14
%define gi_ver 1.33.14

BuildRequires: gcc-c++ libmozjs-devel >= 1.8.5 libcairo-devel
BuildRequires: glib2-devel >= %glib_ver gobject-introspection-devel >= %gi_ver
BuildRequires: libdbus-glib-devel libreadline-devel libcairo-gobject-devel
BuildRequires: gnome-common
BuildRequires: libmozjs24-devel

# for check
BuildRequires: /proc dbus-tools-gui

%description
Cjs allows using GNOME/Cinnamon libraries from Javascript. It's based on the
Spidermonkey Javascript engine from Mozilla and the GObject introspection
framework.

%package devel
Summary: Development package for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
Files for development with %name.

%set_typelibdir %_libdir/%_name/girepository-1.0


%prep
%setup -q -n %_name-%version

%build
%autoreconf
%configure \
    --disable-static

%make_build

%install
%make DESTDIR=%buildroot install

#%check
#%make check

%files
%_bindir/%_name
%_bindir/%_name-console
%_libdir/*.so.*
%dir %_libdir/%_name/
%dir %_libdir/%_name/girepository-1.0
%_libdir/%_name/girepository-1.0/CjsPrivate-%api_ver.typelib
%doc COPYING NEWS README

%files devel
%_includedir/%_name-%api_ver/
%_libdir/*.so
%_libdir/pkgconfig/%_name-%api_ver.pc
%_libdir/pkgconfig/%_name-internals-%api_ver.pc

%doc examples/*

%changelog
* Tue Jun 23 2015 Vladimir Didenko <cow@altlinux.org> 2.6.2-alt1
- 2.6.2

* Tue May 19 2015 Vladimir Didenko <cow@altlinux.org> 2.6.0-alt1
- 2.6.0

* Tue Apr 14 2015 Vladimir Didenko <cow@altlinux.org> 2.5.0-alt1
- 2.5.0

* Fri Oct 31 2014 Vladimir Didenko <cow@altlinux.org> 2.4.0-alt1
- 2.4.0

* Mon Apr 14 2014 Vladimir Didenko <cow@altlinux.org> 2.3.1-alt1
- git 20141014

* Mon Apr 14 2014 Vladimir Didenko <cow@altlinux.org> 2.2.0-alt1
- 2.2.0

* Mon Apr 7 2014 Vladimir Didenko <cow@altlinux.org> 2.0.0-alt2
- git20140405

* Thu Oct 10 2013 Vladimir Didenko <cow@altlinux.org> 2.0.0-alt1
- 2.0.0

* Wed Sep 25 2013 Yuri N. Sedunov <aris@altlinux.org> 0.0.1-alt2
- rebuild for GNOME-3.10

* Wed Jul 31 2013 Vladimir Didenko <cow@altlinux.org> 0.0.1-alt1
- Initial build - git20130721
