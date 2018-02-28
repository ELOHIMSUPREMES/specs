%define rname kwallet

Name: kf5-%rname
Version: 5.17.0
Release: alt1
%K5init altplace

Group: System/Libraries
Summary: KDE Frameworks 5 safe desktop-wide storage for passwords
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar
Patch1: alt-kwalletd4.patch
Patch2: alt-def-blowfish.patch

# Automatically added by buildreq on Fri Feb 13 2015 (-bi)
# optimized out: cmake cmake-modules elfutils libEGL-devel libGL-devel libcloog-isl4 libgpg-error libgpg-error-devel libqt5-core libqt5-dbus libqt5-gui libqt5-svg libqt5-test libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms python-base ruby ruby-stdlibs
#BuildRequires: extra-cmake-modules gcc-c++ glibc-devel-static kf5-kauth-devel kf5-kcodecs-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdbusaddons-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kitemviews-devel kf5-knotifications-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel libgcrypt-devel libgpgme-devel python-module-google qt5-base-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++ glibc-devel qt5-base-devel
BuildRequires: kf5-kauth-devel kf5-kcodecs-devel kf5-kconfig-devel kf5-kconfigwidgets-devel
BuildRequires: kf5-kcoreaddons-devel kf5-kdbusaddons-devel kf5-kguiaddons-devel kf5-ki18n-devel
BuildRequires: kf5-kiconthemes-devel kf5-kitemviews-devel kf5-knotifications-devel
BuildRequires: kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel
BuildRequires: libgcrypt-devel libgpgme-devel
BuildRequires: kf5-kdoctools-devel-static kf5-kdoctools
BuildRequires: kde5-gpgmepp-devel boost-devel-headers

%description
This framework contains two main components:
* Interface to KWallet, the safe desktop-wide storage for passwords on KDE work spaces.
* The kwalletd used to safely store the passwords on KDE work spaces.

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

%package -n libkf5wallet
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5wallet
KF5 library

%package -n libkwalletbackend5
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkwalletbackend5
KF5 library


%prep
%setup -n %rname-%version
%patch1 -p1
%patch2 -p1

%build
%K5build

%install
%K5install
%find_lang %name --all-name
%K5find_qtlang %name --all-name

%files common -f %name.lang
%doc COPYING.LIB README.md

%files
%_bindir/kwalletd5
%_K5bin/kwalletd5
%_K5bin/kwallet-query
%_K5notif/*.notifyrc
%_K5srv/*.desktop
%_K5dbus_srv/*.service
%_datadir/dbus-1/services/*.service

%files devel
%_K5inc/kwallet_version.h
%_K5inc/KWallet/
%_K5link/lib*.so
%_K5lib/cmake/KF5Wallet
%_K5archdata/mkspecs/modules/qt_KWallet.pri
%_K5dbus_iface/*.xml

%files -n libkf5wallet
%_K5lib/libKF5Wallet.so.*
%files -n libkwalletbackend5
%_K5lib/libkwalletbackend5.so.*

%changelog
* Fri Dec 18 2015 Sergey V Turchin <zerg@altlinux.org> 5.17.0-alt1
- new version

* Wed Nov 18 2015 Sergey V Turchin <zerg@altlinux.org> 5.16.0-alt1
- new version

* Mon Oct 12 2015 Sergey V Turchin <zerg@altlinux.org> 5.15.0-alt1
- new version

* Tue Oct 06 2015 Sergey V Turchin <zerg@altlinux.org> 5.14.0-alt2
- don't use gpg by default

* Mon Sep 14 2015 Sergey V Turchin <zerg@altlinux.org> 5.14.0-alt1
- new version

* Wed Aug 19 2015 Sergey V Turchin <zerg@altlinux.org> 5.13.0-alt1
- new version

* Mon Aug 03 2015 Sergey V Turchin <zerg@altlinux.org> 5.12.0-alt3
- build with gpgmepp

* Fri Jul 31 2015 Sergey V Turchin <zerg@altlinux.org> 5.12.0-alt2
- move dbus service to standard place

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
- test

* Tue Feb 10 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt0.1
- initial build
