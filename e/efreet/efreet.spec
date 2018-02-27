%def_disable static

Name: efreet
Version: 1.7.8
%ifdef beta
Release: alt1.%beta
%else
Release: alt1
%endif

Summary: FreeDesktop specifications for E
License: BSD
Group: System/Libraries
Url: http://www.enlightenment.org/pages/efreet.html

Source:  http://download.enlightenment.org/releases/%name-%version.tar.bz2

BuildRequires: libecore-devel >= 1.7.8 libeina-devel >= 1.7.8 libeet-devel >= 1.7.8
BuildRequires: doxygen

%package -n lib%name
Group: System/Libraries
Summary: FreeDesktop specifications for E library.

%description -n lib%name
Implementation of several specifications from freedesktop.org:
 o Base Directory
 o Desktop Entry
 o Icon Theme
 o Menu

%description
Implementation of several specifications from freedesktop.org:
 o Base Directory
 o Desktop Entry
 o Icon Theme
 o Menu

%package -n lib%name-devel
Summary: Efreet headers and development libraries
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
Efreet development files

%prep
%ifdef beta
%setup -q -n %name-%version.%beta
%else
%setup -q
%endif

%build
%autoreconf
%configure %{subst_enable static}
%make_build
%make doc

%install
%make_install DESTDIR=%buildroot install

%find_lang %name

%files -n lib%name -f %name.lang
%_libdir/*.so.*
%dir %_libdir/%name/
%_libdir/%name/efreet_desktop_cache_create
%_libdir/%name/efreet_icon_cache_create
%doc AUTHORS COPYING* README TODO

%files -n lib%name-devel
%_bindir/*
%_libdir/*.so
%_datadir/efreet
%_pkgconfigdir/*
%_includedir/efreet-1

%changelog
* Fri Aug 23 2013 Yuri N. Sedunov <aris@altlinux.org> 1.7.8-alt1
- 1.7.8

* Wed May 15 2013 Yuri N. Sedunov <aris@altlinux.org> 1.7.7-alt1
- 1.7.7

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

* Fri May 11 2012 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Mon Jan 16 2012 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt2
- used %%autoreconf to fix RPATH problem

* Mon Dec 05 2011 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1
- 1.1.0

* Sat May 28 2011 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1

* Tue May 03 2011 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt5
- rebuilt for debuginfo

* Sun Jan 30 2011 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt4
- 1.0.0 release

* Thu Nov 18 2010 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt3.beta2
- 1.0.0.beta2

* Tue Nov 09 2010 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt2.beta
- rebuild for update dependencies

* Fri Oct 29 2010 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1.beta
- 1.0.0.beta

* Mon Jan 04 2010 Yuri N. Sedunov <aris@altlinux.org> 0.5.0.063-alt1
- 0.5.0.063

* Tue Nov 10 2009 Yuri N. Sedunov <aris@altlinux.org> 0.5.0.062-alt1
- new version
- removed obsolete %%post{,un}_ldconfig

* Sat Oct 18 2008 Yuri N. Sedunov <aris@altlinux.org> 0.5.0.050-alt1
- 0.5.0.050

* Mon Sep 17 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.0.3.006-alt1.20070917
- CVS from 20070917.

* Thu Sep 06 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.0.3.006-alt1.20070905
- CVS from 20070905.

* Tue Jul 31 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.0.3.005-alt1.20070731
- CVS from 20070731.

* Wed May 09 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.0.3.002-alt1.20070509
- Initial build for Sisyphus.
- CVS from 20070509.

