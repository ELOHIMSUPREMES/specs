%define rname kded

Name: kf5-%rname
Version: 5.20.0
Release: alt1
%K5init altplace

Group: System/Libraries
Summary: KDE Frameworks 5 central daemon of KDE work spaces
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Requires: %name-common = %version-%release

Source: %rname-%version.tar

# Automatically added by buildreq on Tue Feb 17 2015 (-bi)
# optimized out: cmake cmake-modules docbook-dtds elfutils kf5-kdoctools-devel libEGL-devel libGL-devel libcloog-isl4 libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms python-base ruby ruby-stdlibs xml-common xml-utils
#BuildRequires: docbook-style-xsl extra-cmake-modules gcc-c++ kf5-karchive-devel kf5-kconfig-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdoctools kf5-kdoctools-devel-static kf5-ki18n-devel kf5-kinit-devel kf5-kservice-devel kf5-kwindowsystem-devel python-module-google qt5-base-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5
BuildRequires: docbook-style-xsl extra-cmake-modules gcc-c++ qt5-base-devel
BuildRequires: kf5-karchive-devel kf5-kconfig-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel
BuildRequires: kf5-kdoctools kf5-kdoctools-devel-static
BuildRequires: kf5-ki18n-devel kf5-kinit-devel kf5-kservice-devel kf5-kwindowsystem-devel

%description
KDED stands for KDE Daemon which isn't very descriptive.
KDED runs in the background and performs a number of small tasks.
Some of these tasks are built in, others are started on demand.

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
Requires: %name-common = %version-%release
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkf5ded
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5ded
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

%files
%_bindir/kded5
%_K5bin/kded5
%_K5lib/libkdeinit5_*.so
%_K5srvtyp/*.desktop
#%_K5dbus_srv/*.service
%_datadir/dbus-1/services/*.service

%files devel
#%_K5inc/kded_version.h
#%_K5inc/KDED/
#%_K5link/lib*.so
%_K5lib/cmake/KDED
#%_K5archdata/mkspecs/modules/qt_KDED.pri
%_K5dbus_iface/*.xml

#%files -n libkf5ded
#%_K5lib/libKF5DED.so.*

%changelog
* Tue Mar 15 2016 Sergey V Turchin <zerg@altlinux.org> 5.20.0-alt1
- new version

* Tue Feb 16 2016 Sergey V Turchin <zerg@altlinux.org> 5.19.0-alt1
- new version

* Mon Jan 11 2016 Sergey V Turchin <zerg@altlinux.org> 5.18.0-alt1
- new version

* Fri Dec 18 2015 Sergey V Turchin <zerg@altlinux.org> 5.17.0-alt1
- new version

* Wed Nov 18 2015 Sergey V Turchin <zerg@altlinux.org> 5.16.0-alt1
- new version

* Mon Oct 12 2015 Sergey V Turchin <zerg@altlinux.org> 5.15.0-alt1
- new version

* Mon Sep 14 2015 Sergey V Turchin <zerg@altlinux.org> 5.14.0-alt1
- new version

* Wed Aug 19 2015 Sergey V Turchin <zerg@altlinux.org> 5.13.0-alt1
- new version

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
- initial build
