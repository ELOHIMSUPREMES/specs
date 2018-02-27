%def_disable static

Name: eio
Version: 1.7.8
%ifdef beta
Release: alt1.%beta
%else
Release: alt1
%endif

Summary: Enlightenment Input Output Library
License: LGPLv2.1+
Group: System/Libraries
Url: http://www.enlightenment.org/

# http://svn.enlightenment.org/svn/e/trunk/%name
Source: http://download.enlightenment.org/releases/%name-%version.tar.bz2

BuildRequires: libeina-devel >= 1.7.8
BuildRequires: libecore-devel >= 1.7.8
BuildRequires: libeet-devel >= 1.7.8
%{?_enable_static:BuildPreReq: glibc-devel-static}
BuildRequires: doxygen

%description
EIO is a library that intended to provide non blocking IO by using
thread for all operation that may block. It depends only on eina and
ecore right now. It should integrate all the features/functions of
Ecore_File that could block.

%package -n lib%name
Summary: Enlightenment Input Output Library
Group: System/Libraries

%description -n lib%name
Eio is a library that intended to provide non blocking IO by using
thread for all operation that may block. It depends only on eina and
ecore right now. It should integrate all the features/functions of
Ecore_File that could block.

This package contains shared Eio library.

%package -n lib%name-devel
Summary: Enlightenment Input Output Library development files
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
Eio is a library that intended to provide non blocking IO by using
thread for all operation that may block. It depends only on eina and
ecore right now. It should integrate all the features/functions of
Ecore_File that could block.

This package contains headers, development libraries, test programs and
documentation for Eio.

%prep
%setup -q -n %name-%version

%build
%configure \
	%{subst_enable static}

%make_build
%make doc

%check
%make check

%install
%make DESTDIR=%buildroot install

%files -n lib%name
%_libdir/*.so.*
%doc AUTHORS README

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*

%changelog
* Fri Aug 23 2013 Yuri N. Sedunov <aris@altlinux.org> 1.7.8-alt1
- 1.7.8

* Wed May 15 2013 Yuri N. Sedunov <aris@altlinux.org> 1.7.7-alt1
- 1.7.7

* Wed Apr 10 2013 Yuri N. Sedunov <aris@altlinux.org> 1.7.6.1-alt1
- 1.7.6.1

* Tue Apr 09 2013 Yuri N. Sedunov <aris@altlinux.org> 1.7.6-alt1
- 1.7.6

* Sat Jan 05 2013 Yuri N. Sedunov <aris@altlinux.org> 1.7.5-alt1
- 1.7.5

* Sat Dec 22 2012 Yuri N. Sedunov <aris@altlinux.org> 1.7.4-alt1
- 1.7.4

* Sat Dec 15 2012 Yuri N. Sedunov <aris@altlinux.org> 1.7.3-alt1
- 1.7.3

* Sat Nov 24 2012 Yuri N. Sedunov <aris@altlinux.org> 1.7.2-alt1
- 1.7.2

* Mon Oct 22 2012 Yuri N. Sedunov <aris@altlinux.org> 1.7.1-alt1
- 1.7.1

* Tue Sep 04 2012 Yuri N. Sedunov <aris@altlinux.org> 1.7.0-alt1
- 1.7.0

* Mon Jun 11 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1

* Fri May 11 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0

* Tue Dec 06 2011 Yuri N. Sedunov <aris@altlinux.org> 0.1.0.65643-alt1
- first build for Sisyphus

