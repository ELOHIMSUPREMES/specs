%define api_ver 1.0

Name: libevdev
Version: 1.2.2
Release: alt1

Summary: kernel evdev device wrapper library
Group: System/Libraries
License: MIT
Url: http://www.freedesktop.org/wiki/Software/libevdev

Source: http://www.freedesktop.org/software/%name/%name-%version.tar.xz

BuildRequires: glibc-kernheaders libcheck-devel python-modules python-module-setuptools doxygen

%description
%name is a wrapper library for evdev devices.

%package devel
Summary: kernel evdev device wrapper library development package
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains development libraries and header files
that are needed to write applications that use %name.

%prep
%setup

%build
%autoreconf
%configure --disable-static \
	--disable-gcov

%make_build

%install
%makeinstall_std

%check
#%make check

%files
%_bindir/touchpad-edge-detector
%_libdir/libevdev.so.*
%doc COPYING

%files devel
%_includedir/%name-%api_ver/
%_libdir/%name.so
%_pkgconfigdir/%name.pc
%_man3dir/%name.3.*

%changelog
* Thu Jun 05 2014 Yuri N. Sedunov <aris@altlinux.org> 1.2.2-alt1
- 1.2.2

* Wed Apr 30 2014 Yuri N. Sedunov <aris@altlinux.org> 1.2-alt1
- 1.2

* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 1.1-alt1
- 1.1

* Tue Feb 18 2014 Yuri N. Sedunov <aris@altlinux.org> 1.0-alt1
- 1.0

* Tue Nov 12 2013 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt1
- 0.4.1

* Fri Sep 20 2013 Yuri N. Sedunov <aris@altlinux.org> 0.4-alt1.1
- disable coverage testing

* Fri Sep 20 2013 Yuri N. Sedunov <aris@altlinux.org> 0.4-alt1
- first build for Sisyphus


