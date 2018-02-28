Name: seafile-client
Version: 5.1.1
Release: alt1

Summary: Seafile gui client on QT bassed

Group: Networking/File transfer
License: GPLv3
Url: https://github.com/haiwen/seafile-client

Packager: Denis Baranov <baraka@altlinux.ru>

# Source-url: https://github.com/haiwen/seafile-client/archive/v%version.tar.gz
Source: %name-%version.tar

Requires: seafile >= %version

# manually removed: git-core i586-libxcb libfreetype-infinality python-module-mwlib ruby ruby-stdlibs python-module-google python3-dev python3-module-yieldfrom python3-module-zope 
# Automatically added by buildreq on Tue May 17 2016
# optimized out: cmake cmake-modules gcc-c++ glib2-devel libEGL-devel libGL-devel libevent-devel libgio-devel libgpg-error libjansson-devel libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-test libqt5-widgets libqt5-xml libsearpc-devel libstdc++-devel libuuid-devel pkg-config python-base python-modules python3 python3-base  qt5-tools
BuildRequires: ccmake doxygen graphviz libccnet-devel libseafile-devel libsqlite3-devel libssl-devel qt5-imageformats qt5-tools-devel

BuildRequires: qt5-base-devel

BuildRequires(pre): rpm-macros-cmake

BuildRequires: libccnet-devel >= %version
BuildRequires: libseafile-devel >= %version

Conflicts: libseafile <= 2.0.4

%description
Seafile desktop gui client.
Seafile is a full-fledged document collaboration platform.

%prep
%setup

%build
PATH=%_qt5_bindir:$PATH %cmake_insource
%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%_bindir/seafile-applet
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*
%_pixmapsdir/*

%changelog
* Tue May 17 2016 Vitaly Lipatov <lav@altlinux.ru> 5.1.1-alt1
- new version 5.1.1 (with rpmrb script)
- build with Qt5, update buildreqs

* Sat Feb 13 2016 Vitaly Lipatov <lav@altlinux.ru> 5.0.4-alt1
- new version 5.0.4 (with rpmrb script)

* Fri Nov 21 2014 Vitaly Lipatov <lav@altlinux.ru> 3.1.11-alt1
- new version 3.1.11 (with rpmrb script)

* Sun Aug 31 2014 Vitaly Lipatov <lav@altlinux.ru> 3.1.5-alt2
- rebuild with rebuilt libseafile

* Thu Aug 28 2014 Vitaly Lipatov <lav@altlinux.ru> 3.1.5-alt1
- new version 3.1.5 (with rpmrb script)

* Sat Aug 23 2014 Vitaly Lipatov <lav@altlinux.ru> 3.1.4-alt1
- new version 3.1.4 (with rpmrb script)

* Mon Jan 20 2014 Denis Baranov <baraka@altlinux.ru> 2.1.1-alt1
- Update to version 2.1.1

* Sun Nov 10 2013 Denis Baranov <baraka@altlinux.ru> 2.0.6-alt1
- Initial build gui client for ALTLinux
