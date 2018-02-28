%define rname kservice

Name: kf5-%rname
Version: 5.17.0
Release: alt1
%K5init altplace

Group: System/Libraries
Summary: KDE Frameworks 5 plugin framework for desktop services
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar
Patch1: alt-skip-antikde-mimeapps-list.patch
Patch2: alt-initial-preference.patch

# Automatically added by buildreq on Thu Feb 12 2015 (-bi)
# optimized out: cmake cmake-modules docbook-dtds elfutils kf5-kdoctools-devel libEGL-devel libGL-devel libcloog-isl4 libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms python-base ruby ruby-stdlibs xml-common xml-utils
#BuildRequires: docbook-style-xsl extra-cmake-modules gcc-c++ kf5-karchive-devel kf5-kconfig-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdoctools kf5-kdoctools-devel-static kf5-ki18n-devel kf5-kwindowsystem-devel python-module-google qt5-base-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5
BuildRequires: docbook-style-xsl extra-cmake-modules gcc-c++ qt5-base-devel
BuildRequires: kf5-karchive-devel kf5-kconfig-devel kf5-kcoreaddons-devel kf5-kcrash-devel
BuildRequires: kf5-kdbusaddons-devel kf5-kdoctools kf5-kdoctools-devel-static
BuildRequires: kf5-ki18n-devel kf5-kwindowsystem-devel

%description
KService provides a plugin framework for handling desktop services. Services can
be applications or libraries. They can be bound to MIME types or handled by
application specific code.

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

%package -n libkf5service
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
Requires: altlinux-freedesktop-menu-generic
%description -n libkf5service
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

%files devel
%_K5inc/kservice_version.h
%_K5inc/KService/
%_K5link/lib*.so
%_K5lib/cmake/KF5Service
%_K5archdata/mkspecs/modules/qt_KService.pri

%files -n libkf5service
%_bindir/kbuildsycoca5
%_K5bin/kbuildsycoca5
%_K5lib/libKF5Service.so.*
%_K5srvtyp/*.desktop

%changelog
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

* Thu Jul 16 2015 Sergey V Turchin <zerg@altlinux.org> 5.12.0-alt3
- require altlinux-freedesktop-menu

* Tue Jul 14 2015 Sergey V Turchin <zerg@altlinux.org> 5.12.0-alt2
- prefer KDE5 apps by default

* Fri Jul 10 2015 Sergey V Turchin <zerg@altlinux.org> 5.12.0-alt1
- new version

* Tue Jun 30 2015 Sergey V Turchin <zerg@altlinux.org> 5.11.0-alt1
- new version

* Mon May 11 2015 Sergey V Turchin <zerg@altlinux.org> 5.10.0-alt1
- new version

* Tue Apr 21 2015 Sergey V Turchin <zerg@altlinux.org> 5.9.0-alt2
- ignore non-kde mimeapps.list

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
