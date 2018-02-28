%define rname networkmanager-qt

Name: kf5-%rname
Version: 5.14.0
Release: alt1
%K5init altplace

Group: System/Libraries
Summary: KDE Frameworks 5 Qt wrapper for NetworkManager DBus API
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Thu Feb 19 2015 (-bi)
# optimized out: cmake cmake-modules elfutils glib2-devel libcloog-isl4 libgio-devel libqt5-core libqt5-dbus libqt5-network libstdc++-devel pkg-config python-base ruby ruby-stdlibs
#BuildRequires: extra-cmake-modules gcc-c++ libnm-devel python-module-google qt5-base-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++ qt5-base-devel
BuildRequires: libnm-devel libnm-util-devel NetworkManager-devel

%description
NetworkManagerQt provides access to all NetworkManager features
exposed on DBus. It allows you to manage your connections and control
your network devices and also provides a library for parsing connection
settings which are used in DBus communication.

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

%package -n libkf5networkmanagerqt
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5networkmanagerqt
KF5 library


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%find_lang %name --all-name
%K5find_qtlang %name --all-name

%files common -f %name.lang
%doc COPYING.LIB README.md

%files devel
%_K5inc/networkmanagerqt_version.h
%_K5inc/NetworkManagerQt/
%_K5link/lib*.so
%_K5lib/cmake/KF5NetworkManagerQt
%_K5archdata/mkspecs/modules/qt_NetworkManagerQt.pri

%files -n libkf5networkmanagerqt
%_K5lib/libKF5NetworkManagerQt.so.*

%changelog
* Mon Sep 14 2015 Sergey V Turchin <zerg@altlinux.org> 5.14.0-alt1
- new version

* Wed Aug 19 2015 Sergey V Turchin <zerg@altlinux.org> 5.13.0-alt1
- new version

* Fri Jul 10 2015 Sergey V Turchin <zerg@altlinux.org> 5.12.0-alt1
- new version

* Tue Jun 30 2015 Sergey V Turchin <zerg@altlinux.org> 5.11.0-alt1
- new version

* Mon May 11 2015 Sergey V Turchin <zerg@altlinux.org> 5.10.0-alt1
- new version

* Fri Apr 10 2015 Sergey V Turchin <zerg@altlinux.org> 5.9.0-alt1
- new version

* Mon Apr 06 2015 Sergey V Turchin <zerg@altlinux.org> 5.8.0-alt1
- new version

* Wed Mar 18 2015 Sergey V Turchin <zerg@altlinux.org> 5.8.0-alt0.1
- test

* Mon Feb 16 2015 Sergey V Turchin <zerg@altlinux.org> 5.7.0-alt0.1
- initial build
