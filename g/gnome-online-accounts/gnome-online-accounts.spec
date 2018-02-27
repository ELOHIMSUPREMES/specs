%def_disable snapshot

%define ver_major 3.16
%define _libexecdir %_prefix/libexec
%def_enable kerberos
%def_enable owncloud
%def_enable exchange
%def_enable facebook
%def_enable google
%def_enable flickr
%def_enable imap_smtp
%def_enable windows_live
%def_enable telepathy
%def_enable pocket
%def_enable media_server
%def_enable foursquare

%def_enable gtk_doc
%define api_ver 1.0

Name: gnome-online-accounts
Version: %ver_major.2
Release: alt1

Summary: Provide online accounts information
Group: Graphical desktop/GNOME
License: LGPLv2+
Url: https://live.gnome.org/GnomeOnlineAccounts

%if_enabled snapshot
Source: %name-%version.tar
%else
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%endif

Requires: lib%name = %version-%release

%{?_enable_kerberos:Requires: realmd}

%define glib_ver 2.36
%define gtk_ver 3.11.1
%define oauth_ver 0.9.5
%define rest_ver 0.7.12
%define soup_ver 2.42
%define webkit_ver 2.6.0

BuildPreReq: glib2-devel >= %glib_ver
BuildPreReq: liboauth-devel >= %oauth_ver
BuildPreReq: librest-devel >= %rest_ver
BuildPreReq: libsoup-devel >= %soup_ver
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: libwebkit2gtk-devel >= %webkit_ver
BuildRequires: libtelepathy-glib-devel
BuildRequires: gnome-common intltool gtk-doc
BuildRequires: libjson-glib-devel libgnome-keyring-devel libnotify-devel libsecret-devel
BuildRequires: libkrb5-devel gcr-libs-devel gobject-introspection-devel

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
%setup

%build
%if_enabled snapshot
NOCONFIGURE=1 ./autogen.sh
%else
%autoreconf
%endif
%configure --disable-static \
	--enable-facebook \
	%{subst_enable kerberos} \
	%{subst_enable owncloud} \
	%{?_enable_imap_smtp:--enable-imap-smtp} \
	%{subst_enable exchange} \
	%{subst_enable facebook} \
	%{subst_enable google} \
	%{subst_enable flickr} \
	%{subst_enable telepathy} \
	%{subst_enable pocket} \
	%{?_enable_windows_live:--enable-windows-live} \
	%{?_enable_media_server:--enable-media-server} \
	%{subst_enable foursquare} \
	%{?_enable_gtk_doc:--enable-gtk-doc}

%make_build

%install
%make DESTDIR=%buildroot install

%find_lang --output=%name.lang %name %{?_enable_telepathy:%name-tpaw}

%files -f %name.lang
%_libexecdir/goa-daemon
%_datadir/%name/
%_datadir/dbus-1/services/org.gnome.OnlineAccounts.service
%_datadir/glib-2.0/schemas/org.gnome.online-accounts.gschema.xml
%_datadir/icons/hicolor/*/*/*.png
%_man8dir/goa-daemon.*
%doc NEWS

%if_enabled telepathy
#%_datadir/glib-2.0/schemas/org.gnome.telepathy-account-widgets.gschema.xml
%_iconsdir/hicolor/scalable/apps/im-*.svg
%endif

%files -n lib%name
%_libdir/libgoa-%api_ver.so.*
%_libdir/libgoa-backend-%api_ver.so.*
%dir %_libdir/goa-%api_ver
%dir %_libdir/goa-%api_ver/web-extensions
%_libdir/goa-%api_ver/web-extensions/libgoawebextension.so
%exclude %_libdir/goa-%api_ver/web-extensions/*.la

%files -n lib%name-devel
%_includedir/goa-%api_ver/
%dir %_libdir/goa-%api_ver/include
%_libdir/goa-%api_ver/include/goaconfig.h
%_libdir/libgoa-%api_ver.so
%_libdir/libgoa-backend-%api_ver.so
%_pkgconfigdir/goa-%api_ver.pc
%_pkgconfigdir/goa-backend-%api_ver.pc

%files -n lib%name-gir
%_typelibdir/Goa-%api_ver.typelib

%files -n lib%name-gir-devel
%_girdir/Goa-%api_ver.gir

%files -n lib%name-devel-doc
%_datadir/gtk-doc/html/goa/

%changelog
* Mon May 11 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Fri Jan 16 2015 Yuri N. Sedunov <aris@altlinux.org> 3.14.3-alt1
- 3.14.3

* Wed Nov 12 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt1
- 3.14.2

* Thu Oct 16 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Tue Sep 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Wed Jul 16 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.4-alt1
- 3.12.4

* Thu Jun 05 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.3-alt1
- 3.12.3

* Tue May 13 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt1
- 3.12.2

* Wed Apr 30 2014 Alexey Shabalin <shaba@altlinux.ru> 3.12.1-alt2
- Requires realmd if enabled kerberos support

* Tue Apr 15 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Tue Mar 18 2014 Yuri N. Sedunov <aris@altlinux.org> 3.10.3-alt1
- 3.10.3

* Tue Nov 12 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.2-alt1
- 3.10.2

* Tue Oct 15 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Fri Aug 30 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.3-alt1
- 3.8.3

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

