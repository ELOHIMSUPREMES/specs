%define ver_major 3.8
%define _libexecdir %_prefix/libexec
%def_enable kerberos
%def_enable owncloud
%def_enable exchange
%def_enable facebook
%def_enable google
%def_disable flickr
%def_enable imap_smtp
%def_enable windows_live

%def_enable gtk_doc
%define api_ver 1.0

Name: gnome-online-accounts
Version: %ver_major.2
Release: alt2

Summary: Provide online accounts information
Group: Graphical desktop/GNOME
License: LGPLv2+
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

Requires: lib%name = %version-%release

%define glib_ver 2.35
%define gtk_ver 3.5.1
%define oauth_ver 0.9.5
%define rest_ver 0.7.12
%define soup_ver 2.41

BuildPreReq: glib2-devel >= %glib_ver
BuildPreReq: liboauth-devel >= %oauth_ver
BuildPreReq: librest-devel >= %rest_ver
BuildPreReq: libsoup-devel >= %soup_ver
BuildRequires: gnome-common intltool gtk-doc
BuildRequires: libgtk+3-devel >= %gtk_ver libwebkitgtk3-devel libjson-glib-devel
BuildRequires: libgnome-keyring-devel libnotify-devel libsecret-devel
BuildRequires: libkrb5-devel gcr-libs-devel
BuildRequires: gobject-introspection-devel

%description
gnome-online-accounts provides interfaces so applications and
libraries in GNOME can access the user's online accounts.

%package -n lib%name
Summary: %name shared libraries
Group: System/Libraries

%description -n lib%name
This package contains shared %name libraries.

%package -n lib%name-devel
Summary: Development files for %name libraries
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package contains libraries and header files for developing
applications that use %name libraries.

%package -n lib%name-gir
Summary: GObject introspection data for the %name libraries
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the %name libraries

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the %name libraries
Group: Development/Other
BuildArch: noarch
Requires: lib%name-gir = %version-%release
Requires: lib%name-devel = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the %name libraries

%package -n lib%name-devel-doc
Summary: Development documentation for %name
Group: Development/C
Conflicts: lib%name < %version-%release
BuildArch: noarch

%description -n lib%name-devel-doc
This package contains development documentation for the %name libraries.

%prep
%setup -q

%build
%autoreconf
%configure --disable-static \
	--enable-facebook \
	%{subst_enable kerberos} \
	%{subst_enable owncloud} \
	%{?_enable_imap_smtp:--enable-imap-smtp} \
	%{subst_enable exchange} \
	%{subst_enable facebook} \
	%{subst_enable google} \
	%{subst_enable flickr} \
	%{?_enable_windows_live:--enable-windows-live} \
	%{?_enable_gtk_doc:--enable-gtk-doc}

%make_build

%install
%make DESTDIR=%buildroot install

%find_lang %name

%files -f %name.lang
%_libexecdir/goa-daemon
%_datadir/%name/
%_datadir/dbus-1/services/org.gnome.OnlineAccounts.service
%_datadir/icons/hicolor/*/*/*.png
%_man8dir/goa-daemon.*
%doc NEWS

%files -n lib%name
%_libdir/libgoa-%api_ver.so.*
%_libdir/libgoa-backend-%api_ver.so.*

%files -n lib%name-devel
%_includedir/goa-%api_ver/
%dir %_libdir/goa-%api_ver
%dir %_libdir/goa-%api_ver/include
%_libdir/goa-%api_ver/include/goaconfig.h
%_libdir/libgoa-%api_ver.so
%_libdir/libgoa-backend-%api_ver.so
%_libdir/pkgconfig/goa-%api_ver.pc
%_libdir/pkgconfig/goa-backend-%api_ver.pc

%files -n lib%name-gir
%_libdir/girepository-%api_ver/Goa-%api_ver.typelib

%files -n lib%name-gir-devel
%_datadir/gir-%api_ver/Goa-%api_ver.gir

%files -n lib%name-devel-doc
%_datadir/gtk-doc/html/goa/

%changelog
* Thu Jun 13 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt2
- explicitly enabled some providers

* Tue May 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt1
- 3.8.2

* Mon Apr 15 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Tue Mar 26 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Mon Mar 04 2013 Yuri N. Sedunov <aris@altlinux.org> 3.6.3-alt1
- 3.6.3

* Wed Nov 14 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.2-alt1
- 3.6.2

* Mon Oct 15 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Mon Sep 24 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Mon May 14 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.2-alt1
- 3.4.2

* Tue Apr 17 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Sun Dec 04 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Tue Sep 27 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Tue Aug 16 2011 Yuri N. Sedunov <aris@altlinux.org> 3.1.1-alt1
- first build for Sisyphus

