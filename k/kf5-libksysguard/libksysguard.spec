%define rname libksysguard
%define sover 7
%define libksgrd libksgrd%sover
%define libksignalplotter libksignalplotter%sover
%define liblsofui liblsofui%sover
%define libprocesscore libprocesscore%sover
%define libprocessui libprocessui%sover

Name: kf5-%rname
Version: 5.3.0
Release: alt1
%K5init altplace

Group: System/Libraries
Summary: KDE Workspace 5 performance monitor library
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Wed Feb 25 2015 (-bi)
# optimized out: cmake cmake-modules elfutils libEGL-devel libGL-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libcloog-isl4 libgst-plugins1.0 libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-opengl libqt5-positioning libqt5-printsupport libqt5-qml libqt5-quick libqt5-script libqt5-sensors libqt5-sql libqt5-webkit libqt5-webkitwidgets libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcb-devel libxcbutil-keysyms libxkbfile-devel python-base qt5-base-devel ruby ruby-stdlibs xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: extra-cmake-modules gcc-c++ kf5-kauth-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdbusaddons-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kitemviews-devel kf5-kpackage-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-plasma-framework-devel python-module-google qt5-script-devel qt5-webkit-devel qt5-x11extras-devel rpm-build-gir rpm-build-ruby zlib-devel-static
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++ zlib-devel
BuildRequires: qt5-script-devel qt5-webkit-devel qt5-x11extras-devel
BuildRequires: kf5-kauth-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel
BuildRequires: kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdbusaddons-devel kf5-kguiaddons-devel
BuildRequires: kf5-ki18n-devel kf5-kiconthemes-devel kf5-kitemviews-devel kf5-kpackage-devel kf5-kservice-devel
BuildRequires: kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-plasma-framework-devel

%description
Performance monitor library

%package common
Summary: %name common package
Group: System/Configuration/Other
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

%package -n polkit-kde-ksysguard
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: %name-common = %version-%release
%description -n polkit-kde-ksysguard
Common polkit files for %name

%package -n %libksgrd
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libksgrd
KF5 library

%package -n %libksignalplotter
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libksignalplotter
KF5 library

%package -n %libprocesscore
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
Requires: polkit-kde-ksysguard
%description -n %libprocesscore
KF5 library

%package -n %liblsofui
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %liblsofui
KF5 library

%package -n %libprocessui
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libprocessui
KF5 library


%prep
%setup -n %rname-%version

%build
%K5build \
    -DKDE_INSTALL_INCLUDEDIR=%_K5inc \
    #

%install
%K5install
%K5install_move data ksysguard
%find_lang %name --all-name

%files common -f %name.lang
%doc COPYING.LIB
%dir %_K5data/ksysguard/

%files devel
#%_K5inc/libksysguard_version.h
%_K5inc/ksysguard/
%_K5link/lib*.so
%_K5lib/cmake/KF5SysGuard
#%_K5archdata/mkspecs/modules/qt_libKSysGuard.pri


%files -n %libprocesscore
%_K5lib/libprocesscore.so.%sover
%_K5lib/libprocesscore.so.*
%_K5libexecdir/kauth/ksysguardprocesslist_helper
%_K5conf_dbus_sysd/org.kde.ksysguard.processlisthelper.conf
%_K5dbus_sys_srv/org.kde.ksysguard.processlisthelper.service

%files -n polkit-kde-ksysguard
%_datadir/polkit-1/actions/org.kde.ksysguard.processlisthelper.policy

%files -n %libprocessui
%_K5lib/libprocessui.so.%sover
%_K5lib/libprocessui.so.*
%_K5data/ksysguard/scripts/

%files -n %libksgrd
%_K5lib/libksgrd.so.%sover
%_K5lib/libksgrd.so.*
%files -n %libksignalplotter
%_K5lib/libksignalplotter.so.%sover
%_K5lib/libksignalplotter.so.*
%files -n %liblsofui
%_K5lib/liblsofui.so.%sover
%_K5lib/liblsofui.so.*

%changelog
* Thu Apr 30 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt1
- new version

* Tue Apr 28 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt0.1
- test

* Thu Apr 16 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.2-alt1
- new version

* Mon Mar 30 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.2-alt0.1
- test

* Wed Feb 25 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt0.1
- initial build
