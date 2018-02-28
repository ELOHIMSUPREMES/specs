%define ver_major 0.2

Name: pantheon-files
Version: %ver_major.4
Release: alt1

Summary: The file manager of the Pantheon desktop
License: GPLv3
Group: File tools
Url: https://launchpad.net/pantheon-files

Source: https://launchpad.net/%name/%{ver_major}.x/%version/+download/%name-%version.tar.xz

Packager: Igor Zubkov <icesik@altlinux.org>

#Depends: tumbler
#Recommends: contractor
#Suggests: tumbler-plugins-extra
Requires: polkit zeitgeist

BuildRequires: cmake gcc-c++ vala libsqlite3-devel libgtk+3-devel
BuildRequires: libgee0.8-devel libpixman-devel libgranite-devel
BuildRequires: libgail3-devel libdbus-glib-devel libnotify-devel
BuildRequires: libXdmcp-devel libGConf-devel libXdamage-devel
BuildRequires: libXxf86vm-devel libharfbuzz-devel libpng-devel
BuildRequires: libXinerama-devel libXi-devel libXrandr-devel
BuildRequires: libXcursor-devel libXcomposite-devel
BuildRequires: libxkbcommon-devel libwayland-cursor-devel
BuildRequires: at-spi2-atk-devel libgranite-vala
BuildRequires: libzeitgeist2.0-devel libplank-devel libplank-vala
BuildRequires: libpolkit-devel

%description
The simple, powerful, and sexy file manager from elementary.

%package devel
Summary: Development files for pantheon-files
Group: Development/C
Requires: %name = %version-%release

%description devel
Development files for pantheon-files.

%package vala
Summary: Vala language bindings for the pantheon-files
Group: Development/Other
BuildArch: noarch
Requires: %name-devel = %version-%release

%description vala
This package provides Vala language bindings for the pantheon-files.

%prep
%setup
# fix libdir
find ./ -name "CMakeLists.txt" -print0 | xargs -r0 subst 's|lib\/|${LIB_DESTINATION}/|g' --

%build
%cmake -DCMAKE_BUILD_TYPE:STRING="Release" \
		-DWITH_UNITY:BOOL=OFF
%cmake_build VERBOSE=1

%install
%cmakeinstall_std

%find_lang %name

%files -f %name.lang
%doc AUTHORS HACKING INSTALL README
%_bindir/*
%_libdir/*.so.*
%_libdir/gtk-3.0/modules/libpantheon-filechooser-module.so
%_libdir/%name/
%_desktopdir/%name.desktop
%_datadir/dbus-1/services/%name.service
%_datadir/glib-2.0/schemas/org.pantheon.files.gschema.xml
%_datadir/polkit-1/actions/net.launchpad.%name.policy
%_datadir/%name/
%dir %_datadir/pixmaps/%name
%_datadir/pixmaps/%name/*.png

%files devel
%_libdir/*.so
%_includedir/%name-core/
%_pkgconfigdir/%name-core.pc

%if 0
%files vala
%_vapidir/%name-core-C.vapi
%_vapidir/%name-core.deps
%_vapidir/%name-core.vapi
%endif

%changelog
* Wed Mar 30 2016 Yuri N. Sedunov <aris@altlinux.org> 0.2.4-alt1
- 0.2.4

* Wed Sep 09 2015 Yuri N. Sedunov <aris@altlinux.org> 0.2.3-alt1
- 0.2.3

* Wed Nov 20 2013 Igor Zubkov <icesik@altlinux.org> 0.1.5.1-alt1
- 0.1.5.1

* Mon Nov 11 2013 Igor Zubkov <icesik@altlinux.org> 0.1.5-alt2
- Make build more verbose

* Sat Oct 12 2013 Igor Zubkov <icesik@altlinux.org> 0.1.5-alt1
- 0.1.4 -> 0.1.5

* Sat Sep 14 2013 Igor Zubkov <icesik@altlinux.org> 0.1.4-alt2
- Fix pkgconfig file

* Mon Sep 09 2013 Igor Zubkov <icesik@altlinux.org> 0.1.4-alt1
- 0.1.3 -> 0.1.4

* Sat Aug 24 2013 Igor Zubkov <icesik@altlinux.org> 0.1.3-alt1
- build for Sisyphus

