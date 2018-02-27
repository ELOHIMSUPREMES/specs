%define rname kdesu

Name: kf5-%rname
Version: 5.8.0
Release: alt1
%K5init altplace

Group: System/Libraries
Summary: KDE Frameworks 5 user interface for running shell commands with root privileges
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar
Patch1: alt-dont-close-pty.patch
Patch2: alt-export-vars.patch
Patch3: alt-defaults.patch

# Automatically added by buildreq on Fri Feb 13 2015 (-bi)
# optimized out: cmake cmake-modules elfutils libICE-devel libSM-devel libX11-devel libXau-devel libXext-devel libXfixes-devel libXi-devel libXrender-devel libXt-devel libcloog-isl4 libqt5-core libqt5-dbus libqt5-gui libqt5-x11extras libqt5-xml libstdc++-devel python-base ruby ruby-stdlibs xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel
#BuildRequires: extra-cmake-modules gcc-c++ kf5-kconfig-devel kf5-kcoreaddons-devel kf5-kdbusaddons-devel kf5-ki18n-devel kf5-kpty-devel kf5-kservice-devel libXScrnSaver-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXft-devel libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libxkbfile-devel nss-ldapd python-module-google qt5-base-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++ qt5-base-devel
BuildRequires: kf5-kconfig-devel kf5-kcoreaddons-devel kf5-kdbusaddons-devel kf5-ki18n-devel
BuildRequires: kf5-kpty-devel kf5-kservice-devel
BuildRequires: libXScrnSaver-devel libXcomposite-devel libXcursor-devel libXdamage-devel
BuildRequires: libXdmcp-devel libXft-devel libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel
BuildRequires: libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libxkbfile-devel

%description
KDESU provides functionality for building GUI front ends for
(password asking) console mode programs. For example, kdesu and
kdessh use it to interface with su and ssh respectively.

%package common
Summary: %name common package
Group: Graphical desktop/KDE
BuildArch: noarch
Requires: kf5-filesystem
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkf5desu
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5desu
KF5 library


%prep
%setup -n %rname-%version
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%K5build

%install
%K5install
%find_lang %name --with-qt --all-name
%K5find_qtlang %name --all-name

%files common -f %name.lang
%doc COPYING.LIB README.md

%files devel
%_K5inc/kdesu_version.h
%_K5inc/KDESu/
%_K5link/lib*.so
%_K5lib/cmake/KF5Su
%_K5archdata/mkspecs/modules/qt_KDESu.pri

%files -n libkf5desu
%_K5exec/kdesu_stub
%attr(2711,root,nobody) %_K5exec/kdesud
%_K5lib/libKF5Su.so.*

%changelog
* Mon Apr 06 2015 Sergey V Turchin <zerg@altlinux.org> 5.8.0-alt1
- new version

* Wed Mar 18 2015 Sergey V Turchin <zerg@altlinux.org> 5.8.0-alt0.1
- test

* Mon Feb 16 2015 Sergey V Turchin <zerg@altlinux.org> 5.7.0-alt0.1
- test

* Tue Feb 10 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt0.1
- initial build
