%define ver_major 3.20
%define api_ver 1.0
%define _name GPaste
%define xdg_name org.gnome.GPaste
%define _libexecdir %_prefix/libexec

Name: gpaste
Version: %ver_major
Release: alt1

Summary: GPaste is a clipboard management system
Group: Text tools
License: BSD-like
Url: https://github.com/Keruspe/GPaste

Source: http://www.imagination-land.org/files/%name/%name-%version.tar.xz
#Source: %name-%version.tar
# from pkg-config 0.29.1
Source1: pkg.m4
Patch: %name-3.20-alt-link.patch

Requires: lib%name = %version-%release

%define gtk_ver 3.20
%define gi_ver 1.48
%define vala_ver 0.32

BuildRequires: intltool libappstream-glib-devel desktop-file-utils
BuildRequires: libdbus-devel libgtk+3-devel >= %gtk_ver libclutter-devel
BuildRequires: gnome-control-center-devel
BuildRequires: gobject-introspection-devel >= %gi_ver libgtk+3-gir-devel
BuildRequires: vala-tools >= %vala_ver libvala-devel
# since 3.20
BuildRequires: systemd-devel

%description
This package provides gpaste-daemon is a clipboard management daemon with DBus
interface.

%package -n lib%name
Summary: GPaste library
Group: System/Libraries

%description -n lib%name
GPaste is a clipboard management system.
This package provides shared library required for GPaste components to
work.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
The lib%name-devel package contains library and header files for developing
applications that use %name.

%package -n lib%name-gir
Summary: GObject introspection data for the GPaste
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the GPaste library.

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the GPaste
Group: Development/Other
BuildArch: noarch
Requires: lib%name-gir = %version-%release
Requires: lib%name-devel = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the GPaste library.

%package -n gnome-shell-extension-%name
Summary: GNOME Shell extension for GPaste
Group: Graphical desktop/GNOME
BuildArch: noarch
Requires: gnome-shell >= %ver_major
Requires: %name = %version-%release

%description -n gnome-shell-extension-%name
GNOME Shell extension for GPaste clipboard management system.

%package applet
Summary: Tray applet to manage GPaste
Group: Graphical desktop/Other
Requires: %name = %version-%release

%description applet
This package provides GPaste applet which starts the status icon
in notification area.

%prep
%setup
%patch 
# pkg-config-0.27, automake 1.15 required
subst 's/0\.27/0.25/
       s/1\.15/1.14/' configure.ac
cp %SOURCE1 m4/

%build
%autoreconf
%configure \
  --disable-schemas-compile \
  --disable-unity \
  --enable-applet \
  --enable-vala
#  --disable-silent-rules
%make

%install
%makeinstall_std
%find_lang %_name

%files -f %_name.lang
#%_bindir/%name
%_bindir/%name-client
%_libexecdir/%name/
%exclude %_libexecdir/%name/%name-applet
%_desktopdir/%xdg_name.Ui.desktop
%_datadir/appdata/%xdg_name.Ui.appdata.xml
%_prefix/lib/systemd/user/%xdg_name.Ui.service
%_datadir/dbus-1/services/*.service
%_prefix/lib/systemd/user/%xdg_name.service
%_datadir/glib-2.0/schemas/*.xml
%_datadir/gnome-control-center/keybindings/*.xml
%_man1dir/%name-client.1.*

%_datadir/bash-completion/completions/gpaste-client
%exclude %_datadir/zsh/site-functions/_gpaste-client
%doc AUTHORS NEWS README.md THANKS TODO COPYING

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/%name/
%_libdir/*.so
%_libdir/pkgconfig/*.pc
%_vapidir/*

%files -n lib%name-gir
%_typelibdir/%_name-%api_ver.typelib

%files -n lib%name-gir-devel
%_girdir/%_name-%api_ver.gir

%files applet
%_libexecdir/%name/%name-applet
%_datadir/appdata/%xdg_name.Applet.appdata.xml
%_datadir/applications/%xdg_name.Applet.desktop
%_prefix/lib/systemd/user/%xdg_name.Applet.service
%_sysconfdir/xdg/autostart/%xdg_name.Applet.desktop

%files -n gnome-shell-extension-%name
%_datadir/gnome-shell/extensions/GPaste@gnome-shell-extensions.gnome.org/
%_datadir/gnome-shell/search-providers/%xdg_name.search-provider.ini


%changelog
* Tue Mar 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20-alt1
- 3.20

* Wed Jan 20 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.3-alt1
- 3.18.3

* Mon Oct 19 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt1
- 3.18.2

* Wed Sep 30 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1.1-alt1
- 3.18.1.1

* Wed Sep 23 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18-alt1
- 3.18

* Wed Aug 26 2015 Yuri N. Sedunov <aris@altlinux.org> 3.17.90-alt1
- 3.17.90

* Thu May 28 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2.1-alt1
- 3.16.2.1

* Wed May 06 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Sat Mar 28 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16-alt1
- 3.16

* Fri Jan 23 2015 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Tue Nov 18 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14-alt2
- APPSTREAM_XML used instead of APPDATA_XML

* Sun Oct 19 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14-alt1
- 3.14

* Thu Apr 03 2014 Yuri N. Sedunov <aris@altlinux.org> 3.10-alt1
- first build for Sisyphus

