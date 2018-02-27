%define _libexecdir %_prefix/libexec
%def_enable epdf

Name: ethumb
Version: 1.7.5
Release: alt3

Summary: Ethumb - Thumbnail generation library
Group: Graphical desktop/Enlightenment
License: LGPLv2+
Url: http://www.enlightenment.org

Source: http://download.enlightenment.org/releases/%name-%version.tar.bz2

Requires: lib%name = %version-%release

BuildRequires: doxygen edje libedbus-devel libedje-devel libeet-devel libemotion-devel libexif-devel
%{?_enable_epdf:BuildRequires: libepdf-devel}
BuildRequires: doxygen

%description
Ethumb is a EFL thumbnail generation library that
 * create thumbnails with a predefined frame (possibly an edje frame);
 * have an option to create fdo-like thumbnails;
 * have a client/server utility.

%package -n lib%name
Summary: Libraries for %name
Group: System/Libraries
Requires: %name = %version-%release

%description -n lib%name
Ethumb is a EFL thumbnail generation library that
 * create thumbnails with a predefined frame (possibly an edje frame);
 * have an option to create fdo-like thumbnails;
 * have a client/server utility.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
The lib%name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup -q

%build
%autoreconf
%configure --disable-static
%make_build
%make doc

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%_bindir/%name
%_bindir/%{name}d
%_bindir/%{name}d_client
%_libexecdir/%{name}d_slave
%_libdir/%name/
%exclude %_libdir/%name/*/*.la
%_datadir/dbus-1/services/org.enlightenment.Ethumb.service
%_datadir/%name/

%files -n lib%name
%_libdir/lib%{name}*.so.*
%doc COPYING README

%files -n lib%name-devel
%_includedir/%{name}*/
%_libdir/lib%{name}*.so
%_pkgconfigdir/%{name}*.pc

%changelog
* Sun Apr 07 2013 Yuri N. Sedunov <aris@altlinux.org> 1.7.5-alt3
rebuilt against libpoppler.so.35

* Sun Jan 20 2013 Yuri N. Sedunov <aris@altlinux.org> 1.7.5-alt2
- epdf support

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

* Mon Jan 16 2012 Yuri N. Sedunov <aris@altlinux.org> 0.1.1.65643-alt2
- used %%autoreconf to fix RPATH problem

* Tue Dec 06 2011 Yuri N. Sedunov <aris@altlinux.org> 0.1.1.65643-alt1
- first build for Sisyphus

