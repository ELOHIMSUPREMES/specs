%define rname ktp-kded-module

Name: kde5-%rname
Version: 15.04.3
Release: alt1
%K5init altplace

Group: Graphical desktop/KDE
Summary: KDE integration for telepathy
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Thu Jun 18 2015 (-bi)
# optimized out: cmake cmake-modules elfutils kf5-kcmutils-devel libEGL-devel libGL-devel libdbusmenu-qt52 libgpg-error libjson-c libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-qml libqt5-quick libqt5-sql libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libtelepathy-logger-qt5 libtelepathy-qt5 libtelepathy-qt5-devel libxcbutil-keysyms python-base python3 python3-base qt5-base-devel ruby ruby-stdlibs telepathy-logger-qt5-devel
#BuildRequires: dbus-tools extra-cmake-modules gcc-c++ kde5-ktp-common-internals-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdbusaddons-devel kf5-ki18n-devel kf5-kidletime-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kservice-devel kf5-kwallet-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel libdb4-devel libtelepathy-qt5-devel-static python-module-google rpm-build-python3 rpm-build-ruby
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++ qt5-base-devel
BuildRequires: dbus-tools kde5-ktp-common-internals-devel libtelepathy-qt5-devel-static
BuildRequires: kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel
BuildRequires: kf5-kcoreaddons-devel kf5-kdbusaddons-devel kf5-ki18n-devel kf5-kidletime-devel kf5-kio-devel kf5-kitemviews-devel
BuildRequires: kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kservice-devel kf5-kwallet-devel kf5-kwidgetsaddons-devel
BuildRequires: kf5-kxmlgui-devel kf5-solid-devel

%description
This module sits in KDED and takes care of various bits of system
integration like setting user to auto-away or handling connection errors.

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

%package -n libkf5tp-kded-module
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5tp-kded-module
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
%_K5plug/*ktp*.so
%_K5srv/*ktp*.desktop
%_K5srv/kded/*ktp*.desktop
%_K5dbus_srv/org.freedesktop.Telepathy.Client.KTp.*.service

#%files devel
#%_K5inc/ktp-kded-module_version.h
#%_K5inc/ktp-kded-module/
#%_K5link/lib*.so
#%_K5lib/cmake/ktp-kded-module
#%_K5archdata/mkspecs/modules/qt_ktp-kded-module.pri

#%files -n libkf5tp-kded-module
#%_K5lib/libktp-kded-module.so.*

%changelog
* Thu Jul 09 2015 Sergey V Turchin <zerg@altlinux.org> 15.04.3-alt1
- new version

* Tue Apr 28 2015 Sergey V Turchin <zerg@altlinux.org> 15.4.2-alt0.1
- initial build
