%define rname ktp-contact-list

Name: kde5-%rname
Version: 15.08.0
Release: alt1
%K5init altplace

Group: Graphical desktop/KDE
Summary: Telepathy contact list application
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Requires: kde5-ktp-common-internals-core

Source: %rname-%version.tar

# Automatically added by buildreq on Wed Jun 17 2015 (-bi)
# optimized out: cmake cmake-modules elfutils kf5-kcmutils-devel libEGL-devel libGL-devel libdbusmenu-qt52 libgpg-error libjson-c libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-qml libqt5-quick libqt5-sql libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libtelepathy-logger-qt5 libtelepathy-qt5 libtelepathy-qt5-devel libxcbutil-keysyms python-base python3 python3-base qt5-base-devel telepathy-logger-qt5-devel
#BuildRequires: extra-cmake-modules gcc-c++ kde5-ktp-common-internals-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdbusaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-knotifyconfig-devel kf5-kpeople-devel kf5-kservice-devel kf5-kwallet-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel libdb4-devel libtelepathy-qt5-devel-static python-module-google rpm-build-python3 ruby ruby-stdlibs
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++ qt5-base-devel
BuildRequires: kde5-ktp-common-internals-devel libtelepathy-qt5-devel-static
BuildRequires: kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel
BuildRequires: kf5-kcoreaddons-devel kf5-kdbusaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel kf5-kitemviews-devel
BuildRequires: kf5-kjobwidgets-devel kf5-knotifications-devel kf5-knotifyconfig-devel kf5-kpeople-devel kf5-kservice-devel
BuildRequires: kf5-kwallet-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel

%description
%summary

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

%package -n libkf5tp-contact-list
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5tp-contact-list
KF5 library


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc COPYING*
%_K5bin/ktp-contactlist
%_K5xdgapp/org.kde.ktpcontactlist.desktop
%_K5dbus_srv/org.kde.ktpcontactlist.service

#%files devel
#%_K5inc/ktp-contact-list_version.h
#%_K5inc/ktp-contact-list/
#%_K5link/lib*.so
#%_K5lib/cmake/ktp-contact-list
#%_K5archdata/mkspecs/modules/qt_ktp-contact-list.pri

#%files -n libkf5tp-contact-list
#%_K5lib/libktp-contact-list.so.*

%changelog
* Tue Sep 08 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.0-alt1
- new version

* Tue Jul 14 2015 Sergey V Turchin <zerg@altlinux.org> 15.04.3-alt2
- fix requires

* Thu Jul 09 2015 Sergey V Turchin <zerg@altlinux.org> 15.04.3-alt1
- new version

* Tue Apr 28 2015 Sergey V Turchin <zerg@altlinux.org> 15.4.2-alt0.1
- initial build
