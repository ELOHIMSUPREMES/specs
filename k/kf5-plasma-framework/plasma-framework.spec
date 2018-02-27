%define rname plasma-framework

%add_findreq_skiplist %_K5data/plasma/plasma_scriptengine_ruby/*.rb

Name: kf5-%rname
Version: 5.9.0
Release: alt1
%K5init altplace

Group: System/Libraries
Summary: KDE Frameworks 5 plasma framework
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar
Patch1: alt-plasma-install-dir.patch

# Automatically added by buildreq on Thu Feb 19 2015 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils kf5-kdoctools-devel libEGL-devel libGL-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libcloog-isl4 libgpg-error libjson-c libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-qml libqt5-quick libqt5-script libqt5-sql libqt5-svg libqt5-test libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libwayland-client libwayland-server libxcb-devel libxcbutil-keysyms libxkbfile-devel pkg-config python-base qt5-base-devel ruby ruby-stdlibs xml-common xml-utils xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel
#BuildRequires: extra-cmake-modules gcc-c++ kf5-kactivities-devel kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdbusaddons-devel kf5-kdeclarative-devel kf5-kdoctools kf5-kdoctools-devel-static kf5-kglobalaccel-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kpackage-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libGLU-devel python-module-google qt5-declarative-devel qt5-script-devel qt5-svg-devel qt5-x11extras-devel rpm-build-gir rpm-build-ruby
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++
BuildRequires: libGLU-devel
BuildRequires: rpm-build-ruby
BuildRequires: qt5-declarative-devel qt5-script-devel qt5-svg-devel qt5-x11extras-devel
BuildRequires: kf5-kactivities-devel kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel
BuildRequires: kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel
BuildRequires: kf5-kdbusaddons-devel kf5-kdeclarative-devel kf5-kdoctools kf5-kdoctools-devel-static
BuildRequires: kf5-kglobalaccel-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel
BuildRequires: kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kpackage-devel
BuildRequires: kf5-kservice-devel kf5-ktextwidgets-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel
BuildRequires: kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel

%description
The plasma framework provides the foundations that can be used to build a primary user interface, from graphical to logical components.

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

%package -n libkf5plasma
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5plasma
KF5 library

%package -n libkf5plasmaquick
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5plasmaquick
KF5 library


%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K5build

%install
%K5install
%K5install_move data locale
%find_lang %name --all-name
%K5find_qtlang %name --all-name

%files common -f %name.lang
%doc COPYING.LIB README.md
%_K5i18n/*/LC_SCRIPTS/libplasma5/
%dir %_K5data/plasma/
%_K5data/plasma/desktoptheme/
#%_K5notif/*.notifyrc

#%files
#%_K5qml/*
#%exclude %_K5qml/org/kde/plasma/components/private/
#%exclude %_K5qml/org/kde/plasma/core/private/

%files devel
%_K5inc/plasma_version.h
%_K5inc/?lasma/
%_K5link/lib*.so
%_K5lib/cmake/KF5Plasma*
#%_K5archdata/mkspecs/modules/qt_Plasma-Framework.pri
%_K5dbus_iface/*.xml

%files -n libkf5plasma
%_K5lib/libKF5Plasma.so.*
%_K5plug/kf5/kded/platformstatus.so
%_K5plug/plasma_engine_testengine.so

%files -n libkf5plasmaquick
%_K5lib/libKF5PlasmaQuick.so.*
%_K5bin/*
%_K5plug/plasma_appletscript_declarative.so
%_K5data/plasma/*
%exclude %_K5data/plasma/desktoptheme
%_K5qml/QtQuick/
%_K5qml/org/kde/plasma/accessdenied/
%_K5qml/org/kde/plasma/calendar/
%_K5qml/org/kde/plasma/core/
%_K5qml/org/kde/plasma/components/
%_K5qml/org/kde/plasma/extras/
%_K5qml/org/kde/plasma/platformcomponents/
%_K5srv/kded/*.desktop
%_K5srv/*.desktop
%_K5srvtyp/*.desktop

%changelog
* Fri Apr 10 2015 Sergey V Turchin <zerg@altlinux.org> 5.9.0-alt1
- new version

* Mon Apr 06 2015 Sergey V Turchin <zerg@altlinux.org> 5.8.0-alt1
- new version

* Wed Mar 18 2015 Sergey V Turchin <zerg@altlinux.org> 5.8.0-alt0.1
- test

* Mon Feb 16 2015 Sergey V Turchin <zerg@altlinux.org> 5.7.0-alt0.1
- initial build
