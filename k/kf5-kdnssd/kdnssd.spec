%define rname kdnssd

Name: kf5-%rname
Version: 5.11.0
Release: alt1
%K5init altplace

Group: System/Libraries
Summary: KDE Frameworks 5 network service discovery using Zeroconf
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Wed Feb 11 2015 (-bi)
# optimized out: cmake cmake-modules elfutils libcloog-isl4 libqt5-core libqt5-dbus libqt5-network libqt5-xml libstdc++-devel python-base qt5-base-devel qt5-tools ruby ruby-stdlibs
#BuildRequires: extra-cmake-modules gcc-c++ libavahi-devel python-module-google qt5-tools-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++ libavahi-devel qt5-tools-devel

%description
KDNSSD is a library for handling the DNS-based Service Discovery Protocol
(DNS-SD), the layer of (Zeroconf](http://www.zeroconf.org) that allows network
services, such as printers, to be discovered without any user intervention or
centralized infrastructure.

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

%package -n libkf5dnssd
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5dnssd
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
#%_K5inc/kdnssd_version.h
%_K5inc/KDNSSD/
%_K5link/lib*.so
%_K5lib/cmake/KF5DNSSD
%_K5archdata/mkspecs/modules/qt_KDNSSD.pri

%files -n libkf5dnssd
%_K5lib/libKF5DNSSD.so.*

%changelog
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
