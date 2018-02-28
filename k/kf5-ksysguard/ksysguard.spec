%define rname ksysguard

Name: kf5-%rname
Version: 5.4.1
Release: alt1
%K5init altplace

Group: Graphical desktop/KDE
Summary: KDE Workspace 5 system monitor
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Requires: lm_sensors

Source: %rname-%version.tar
Patch1: alt-ksysguarddrc.patch

# Automatically added by buildreq on Mon Apr 06 2015 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils kf5-attica-devel kf5-kdoctools-devel libEGL-devel libGL-devel libcloog-isl4 libdbusmenu-qt52 libgpg-error libgst-plugins1.0 libjson-c libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-opengl libqt5-printsupport libqt5-qml libqt5-quick libqt5-sql libqt5-svg libqt5-webkit libqt5-webkitwidgets libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms python-base ruby ruby-stdlibs xml-common xml-utils
#BuildRequires: extra-cmake-modules gcc-c++ kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdelibs4support-devel kf5-kdesignerplugin-devel kf5-kdoctools kf5-kdoctools-devel-static kf5-kemoticons-devel kf5-kglobalaccel-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knewstuff-devel kf5-knotifications-devel kf5-kparts-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-libksysguard-devel kf5-solid-devel kf5-sonnet-devel libsensors3-devel python-module-google qt5-base-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++ qt5-base-devel
BuildRequires: libsensors3-devel
BuildRequires: kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel
BuildRequires: kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel
BuildRequires: kf5-kdelibs4support kf5-kdelibs4support-devel
BuildRequires: kf5-kdoctools kf5-kdoctools-devel-static
BuildRequires: kf5-kdesignerplugin-devel kf5-kemoticons-devel kf5-kglobalaccel-devel kf5-kguiaddons-devel kf5-ki18n-devel
BuildRequires: kf5-kiconthemes-devel kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel
BuildRequires: kf5-kjobwidgets-devel kf5-knewstuff-devel kf5-knotifications-devel kf5-kparts-devel kf5-kservice-devel
BuildRequires: kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel
BuildRequires: kf5-kxmlgui-devel kf5-libksysguard-devel kf5-solid-devel kf5-sonnet-devel

%description
KSysGuard is a program to monitor various elements of your system, or any
other remote system with the KSysGuard daemon (ksysgardd) installed.

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

%package -n libkf5sysguard
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5sysguard
KF5 library


%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K5build

%install
%K5install
%K5install_move data ksysguard
%find_lang %name --with-kde --all-name

%files -f %name.lang
%config(noreplace) %_sysconfdir/ksysguarddrc5
%config(noreplace) %_K5xdgconf/*
%_K5bin/*
%_K5lib/libkdeinit5_*.so
%_K5data/ksysguard/
%_K5icon/*/*/apps/*.png
%_K5notif/*
%_K5xmlgui/*
%_K5xdgapp/*.desktop

#%files common -f %name.lang
#%doc COPYING.LIB README.md

#%files devel
#%_K5inc/ksysguard_version.h
#%_K5inc/ksysguard/
#%_K5link/lib*.so
#%_K5lib/cmake/ksysguard
#%_K5archdata/mkspecs/modules/qt_ksysguard.pri

#%files -n libkf5sysguard
#%_K5lib/libksysguard.so.*

%changelog
* Thu Sep 10 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.1-alt1
- new version

* Wed Aug 26 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.0-alt1
- new version

* Sat Aug 22 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.95-alt1
- new version

* Wed Jul 01 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.2-alt1
- new version

* Fri May 29 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt1
- new version

* Thu Apr 30 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt1
- new version

* Tue Apr 28 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt0.1
- test

* Thu Apr 16 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.2-alt1
- new version

* Wed Feb 25 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.2-alt0.1
- initial build
