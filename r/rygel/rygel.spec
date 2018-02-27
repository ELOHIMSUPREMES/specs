%set_automake_version 1.11

%define ver_major 0.26
%def_enable external_plugin
%def_enable mpris_plugin
%def_enable mediathek_plugin
%def_enable tracker_plugin
%def_with ui
%define media_engine gstreamer

%if %media_engine == gstreamer
%def_enable playbin_plugin
%def_enable media_export_plugin
%def_enable gst_launch_plugin
%else
%def_disable playbin_plugin
%def_disable media_export_plugin
%def_disable gst_launch_plugin
%endif

Name: rygel
Version: %ver_major.1
Release: alt1

Summary: A UPnP v2 Media Server
Group: System/Servers
License: LGPLv2+
Url: https://wiki.gnome.org/Projects/Rygel

#Source: %name-%version.tar
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

%define libxml_ver 2.7
%define vala_ver 0.22.0
%define gssdp_ver 0.13.0
%define gupnp_ver 0.19.0
%define gupnp_av_ver 0.12.4
%define gupnp_dlna_ver 0.9.4
%define gstreamer_ver 1.0
%define gst_pbu_ver 1.0
%define gst_tag_ver 1.0
%define gst_app_ver 1.0
%define gst_audio_ver 1.0
%define gio_ver 2.34
%define gee_ver 0.8.0
%define uuid_ver 1.41.3
%define libsoup_ver 2.44.0
%define gtk_ver 3.0
%define libsqlite3_ver 3.5
%define mediaart_ver 1.9
%define tracker_ver 1.4.0

BuildRequires: intltool gnome-common gtk-doc
BuildRequires: gobject-introspection-devel >= 1.33.4
BuildRequires: pkgconfig(gssdp-1.0) >= %gssdp_ver
BuildRequires: pkgconfig(gupnp-1.0) >= %gupnp_ver
BuildRequires: pkgconfig(gupnp-av-1.0) >= %gupnp_av_ver
BuildRequires: pkgconfig(gio-2.0) >= %gio_ver
BuildRequires: pkgconfig(gmodule-2.0)
BuildRequires: pkgconfig(gee-0.8) >= %gee_ver
BuildRequires: pkgconfig(uuid) >= %uuid_ver
BuildRequires: pkgconfig(libsoup-2.4) >= %libsoup_ver
BuildRequires: pkgconfig(libxml-2.0) >= %libxml_ver
BuildRequires: pkgconfig(gstreamer-1.0) >= %gstreamer_ver
BuildRequires: pkgconfig(gstreamer-base-1.0) >= %gstreamer_ver
BuildRequires: pkgconfig(libmediaart-2.0) >= %mediaart_ver
%if %media_engine == gstreamer
BuildRequires: pkgconfig(gstreamer-pbutils-1.0) >= %gst_pbu_ver
BuildRequires: pkgconfig(gstreamer-app-1.0) >= %gst_app_ver
BuildRequires: pkgconfig(gstreamer-audio-1.0) >= %gst_audio_ver
BuildRequires: pkgconfig(gupnp-dlna-2.0) >= %gupnp_dlna_ver
BuildRequires: pkgconfig(gio-2.0) >= %gio_ver
BuildRequires: gir(Gst) = 1.0
%endif
BuildRequires: tracker-devel >= %tracker_ver
%{?_enable_media_export_plugin:BuildRequires: pkgconfig(sqlite3) >= %libsqlite3_ver pkgconfig(gstreamer-tag-1.0) >= %gst_tag_ver pkgconfig(gstreamer-app-1.0) >= %gst_app_ver pkgconfig(gupnp-dlna-2.0) >= %gupnp_dlna_ver pkgconfig(gupnp-dlna-gst-2.0) >= %gupnp_dlna_ver }
BuildRequires: libvala-devel >= %vala_ver vala >= %vala_ver
BuildRequires: vapi(gupnp-1.0) vapi(gupnp-av-1.0) vapi(gio-2.0) vapi(gee-0.8) vapi(posix)
BuildRequires: gir(GUPnP) = 1.0 gir(GUPnPAV) = 1.0 gir(GObject) = 2.0 gir(Gee) = 0.8 gir(Gio) = 2.0 gir(GLib) = 2.0
%{?_with_ui:BuildRequires: pkgconfig(gtk+-3.0) >= %gtk_ver}
BuildRequires: xsltproc docbook-style-xsl docbook-dtds

%description
Rygel is an implementation of the UPnP MediaServer V 2.0 specification that is
specifically designed for GNOME. It is based on GUPnP and is written (mostly)
in Vala language. The project was previously known as gupnp-media-server.

%package devel
Summary: Development package for %name
Group: Development/Other
Requires: %name = %version-%release

%description devel
Files for development with %name.

%package tracker
Summary: Tracker plugin for %name
Group: System/Servers
Requires: %name = %version-%release
Requires: tracker

%description tracker
A plugin for rygel to use tracker to locate media on the local machine.

%package gir
Summary: GObject introspection data for the %name
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the %name

%package gir-devel
Summary: GObject introspection devel data for the %name
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the %name

%prep
%setup
echo %version > .tarball-version

%build
%autoreconf
# glib-gettextize --force --copy
# ./autogen.sh
%configure \
	%{subst_enable vala} \
	%{subst_with ui} \
	%{?_enable_tracker_plugin:--enable-tracker-plugin} \
	%{?_enable_media_export_plugin:--enable-media-export-plugin} \
	%{?_enable_external_plugin:--enable-external-plugin} \
	%{?_enable_mpris_plugin:--enable-mpris-plugin} \
	%{subst_enable playbin_plugin} \
	%{?_enable_mediathek_plugin:--enable-mediathek-plugin} \
	%{?_enable_gst_launch_plugin:--enable-gst-launch-plugin}

%make_build

%install

%makeinstall_std

%find_lang --with-gnome %name

%files -f %name.lang
%config(noreplace) %_sysconfdir/%name.conf
%_bindir/*
%_libdir/librygel-*.so.*
%_libdir/%name-*
%exclude %_libdir/%name-*/plugins/librygel-tracker.so
%_datadir/%name
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*
%_datadir/dbus-1/services/*.service
%_man1dir/*
%_man5dir/*
%exclude %_libdir/%name-*/*/*.la
%doc AUTHORS COPYING README TODO NEWS

%files tracker
%_libdir/%name-*/plugins/librygel-tracker.so

%files devel
%_libdir/librygel-*.so
%_includedir/%name-*
%_pkgconfigdir/*.pc
%_datadir/vala/vapi/*

%files gir
%_typelibdir/*.typelib

%files gir-devel
%_girdir/*.gir

%changelog
* Sun May 10 2015 Yuri N. Sedunov <aris@altlinux.org> 0.26.1-alt1
- 0.26.1

* Sun Mar 29 2015 Yuri N. Sedunov <aris@altlinux.org> 0.26.0-alt1
- 0.26.0

* Sat Jan 24 2015 Yuri N. Sedunov <aris@altlinux.org> 0.24.3-alt1
- 0.24.3

* Mon Nov 10 2014 Yuri N. Sedunov <aris@altlinux.org> 0.24.2-alt1
- 0.24.2

* Wed Nov 05 2014 Yuri N. Sedunov <aris@altlinux.org> 0.24.1-alt1
- 0.24.1

* Tue Sep 23 2014 Alexey Shabalin <shaba@altlinux.ru> 0.24.0-alt1
- 0.24.0

* Mon Jul 28 2014 Alexey Shabalin <shaba@altlinux.ru> 0.22.3-alt1
- 0.22.3

* Fri Jun 06 2014 Alexey Shabalin <shaba@altlinux.ru> 0.22.2-alt1
- 0.22.2

* Fri Apr 25 2014 Alexey Shabalin <shaba@altlinux.ru> 0.22.1-alt1
- 0.22.1

* Tue Mar 25 2014 Alexey Shabalin <shaba@altlinux.ru> 0.22.0-alt1
- 0.22.0

* Wed Jan 15 2014 Alexey Shabalin <shaba@altlinux.ru> 0.20.3-alt1
- 0.20.3

* Thu Nov 14 2013 Alexey Shabalin <shaba@altlinux.ru> 0.20.2-alt1
- 0.20.2

* Thu Oct 17 2013 Alexey Shabalin <shaba@altlinux.ru> 0.20.1-alt1
- 0.20.1

* Wed Sep 25 2013 Alexey Shabalin <shaba@altlinux.ru> 0.20.0-alt1
- 0.20.0

* Mon Aug 12 2013 Alexey Shabalin <shaba@altlinux.ru> 0.18.4-alt1
- 0.18.4

* Tue Jul 30 2013 Alexey Shabalin <shaba@altlinux.ru> 0.18.3-alt1
- 0.18.3

* Mon May 13 2013 Alexey Shabalin <shaba@altlinux.ru> 0.18.2-alt1
- 0.18.2

* Fri Apr 19 2013 Alexey Shabalin <shaba@altlinux.ru> 0.18.1-alt1
- 0.18.1

* Wed Mar 27 2013 Alexey Shabalin <shaba@altlinux.ru> 0.18.0-alt1
- 0.18.0

* Thu Mar 07 2013 Alexey Shabalin <shaba@altlinux.ru> 0.17.9-alt1
- 0.17.9

* Mon Feb 25 2013 Alexey Shabalin <shaba@altlinux.ru> 0.17.8-alt1
- 0.17.8

* Mon Dec 17 2012 Alexey Shabalin <shaba@altlinux.ru> 0.17.5.1-alt1
- 0.17.5.1

* Tue Dec 11 2012 Alexey Shabalin <shaba@altlinux.ru> 0.17.4-alt1
- 0.17.4

* Wed Nov 14 2012 Alexey Shabalin <shaba@altlinux.ru> 0.16.3-alt1
- 0.16.3

* Tue Nov 13 2012 Alexey Shabalin <shaba@altlinux.ru> 0.16.2-alt1
- 0.16.2

* Fri Oct 12 2012 Alexey Shabalin <shaba@altlinux.ru> 0.16.1-alt1
- 0.16.1

* Tue Sep 11 2012 Alexey Shabalin <shaba@altlinux.ru> 0.14.3-alt1
- 0.14.3

* Mon Jul 30 2012 Alexey Shabalin <shaba@altlinux.ru> 0.14.2-alt1
- 0.14.2

* Tue May 22 2012 Alexey Shabalin <shaba@altlinux.ru> 0.14.1-alt1
- 0.14.1

* Tue Mar 13 2012 Alexey Shabalin <shaba@altlinux.ru> 0.13.3-alt1
- 0.13.3

* Wed Feb 08 2012 Alexey Shabalin <shaba@altlinux.ru> 0.12.7-alt1
- 0.12.7

* Wed Dec 21 2011 Alexey Shabalin <shaba@altlinux.ru> 0.12.6-alt1
- 0.12.6

* Mon Nov 07 2011 Alexey Shabalin <shaba@altlinux.ru> 0.12.5-alt1
- 0.12.5

* Mon Oct 17 2011 Alexey Shabalin <shaba@altlinux.ru> 0.12.4-alt1
- 0.12.4

* Thu Oct 06 2011 Alexey Shabalin <shaba@altlinux.ru> 0.12.3-alt1
- 0.12.3

* Wed Sep 21 2011 Alexey Shabalin <shaba@altlinux.ru> 0.12.2-alt1
- 0.12.2

* Tue Jul 12 2011 Alexey Shabalin <shaba@altlinux.ru> 0.11.2-alt1
- 0.11.2

* Thu Jun 23 2011 Alexey Shabalin <shaba@altlinux.ru> 0.11.1-alt1
- 0.11.1

* Thu Jun 23 2011 Alexey Shabalin <shaba@altlinux.ru> 0.10.2-alt1
- 0.10.2

* Mon May 30 2011 Alexey Shabalin <shaba@altlinux.ru> 0.10.1-alt1
- 0.10.1

* Thu Oct 21 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8.2-alt1
- 0.8.2

* Mon Oct 04 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8.1-alt1
- 0.8.1

* Sun May 16 2010 Alexey Shabalin <shaba@altlinux.ru> 0.6.0-alt1
- 0.6.0

* Fri Mar 12 2010 Alexey Shabalin <shaba@altlinux.ru> 0.5.0-alt1
- 0.5.0

* Tue Dec 15 2009 Alexey Shabalin <shaba@altlinux.ru> 0.4.6-alt1.ba17eba
- git version with port to tracker 0.7 API

* Fri Dec 04 2009 Alexey Shabalin <shaba@altlinux.ru> 0.4.6-alt1
- Initial release
