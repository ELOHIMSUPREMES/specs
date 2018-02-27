%define rname kdbusaddons

Name: kf5-%rname
Version: 5.12.0
Release: alt1
%K5init altplace

Group: System/Libraries
Summary: KDE Frameworks 5 convenience classes for DBus
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Tue Jan 20 2015 (-bi)
# optimized out: cmake cmake-modules elfutils libEGL-devel libGL-devel libcloog-isl4 libqt5-core libqt5-dbus libqt5-gui libqt5-test libqt5-x11extras libqt5-xml libstdc++-devel python-base qt5-base-devel qt5-tools ruby ruby-stdlibs
#BuildRequires: extra-cmake-modules gcc-c++ python-module-google qt5-tools-devel qt5-x11extras-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++ qt5-tools-devel qt5-x11extras-devel

%description
KDBusAddons provides convenience classes on top of QtDBus, as well as an API to
create KDED modules.

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

%package -n libkf5dbusaddons
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5dbusaddons
KF5 library


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%find_lang %name --all-name
%K5find_qtlang %name --all-name

%files
%_bindir/kquitapp5
%_K5bin/kquitapp5

%files common -f %name.lang
%doc COPYING.LIB README.md

%files devel
%_K5inc/kdbusaddons_version.h
%_K5inc/KDBusAddons/
%_K5link/lib*.so
%_K5lib/cmake/KF5DBusAddons
%_K5archdata/mkspecs/modules/qt_KDBusAddons.pri

%files -n libkf5dbusaddons
%_K5lib/libKF5DBusAddons.so.*

%changelog
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

* Mon Jan 19 2015 Sergey V Turchin <zerg@altlinux.org> 5.6.0-alt0.1
- test

* Mon Dec 22 2014 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt1
- initial build
