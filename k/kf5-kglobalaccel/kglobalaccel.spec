%define rname kglobalaccel

Name: kf5-%rname
Version: 5.19.0
Release: alt1
%K5init altplace

Group: System/Libraries
Summary: KDE Frameworks 5 global desktop keyboard shortcuts
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Mon Feb 16 2015 (-bi)
# optimized out: cmake cmake-modules elfutils libEGL-devel libGL-devel libICE-devel libSM-devel libX11-devel libXau-devel libXext-devel libXfixes-devel libXi-devel libXrender-devel libXt-devel libcloog-isl4 libqt5-core libqt5-dbus libqt5-gui libqt5-test libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcb-devel libxcbutil-keysyms pkg-config python-base qt5-base-devel qt5-tools ruby ruby-stdlibs xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel
#BuildRequires: extra-cmake-modules gcc-c++ kf5-kconfig-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-ki18n-devel kf5-kwindowsystem-devel libXScrnSaver-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXft-devel libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libxcbutil-keysyms-devel libxkbfile-devel python-module-google qt5-tools-devel qt5-x11extras-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++ qt5-tools-devel
BuildRequires: libXScrnSaver-devel libXcomposite-devel libXcursor-devel libXdamage-devel
BuildRequires: libXdmcp-devel libXft-devel libXinerama-devel libXmu-devel libXpm-devel
BuildRequires: libXrandr-devel libXtst-devel libXv-devel libXxf86misc-devel
BuildRequires: libXxf86vm-devel libxcbutil-keysyms-devel libxkbfile-devel
BuildRequires: qt5-x11extras-devel
BuildRequires: kf5-kconfig-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel
BuildRequires: kf5-ki18n-devel kf5-kwindowsystem-devel

%description
KGlobalAccel allows you to have global accelerators that are independent of
the focused window.  Unlike regular shortcuts, the application's window does not
need focus for them to be activated.

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
Requires: libkf5globalaccelprivate
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkf5globalaccel
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5globalaccel
KF5 library

%package -n libkf5globalaccelprivate
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5globalaccelprivate
KF5 library


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%K5install_move data locale
%find_lang %name --all-name
%K5find_qtlang %name --all-name

%files common -f %name.lang
%doc COPYING.LIB README.md

%files
%_bindir/*5
%_K5bin/kglobalaccel5
%_K5srv/kglobalaccel5.desktop
%_K5dbus_srv/org.kde.kglobalaccel.service
%_K5plug/org.kde.kglobalaccel5*/

%files devel
%_K5inc/kglobalaccel_version.h
%_K5inc/KGlobalAccel/
%_K5link/lib*.so
%_K5lib/cmake/KF5GlobalAccel
%_K5archdata/mkspecs/modules/qt_KGlobalAccel.pri
%_K5dbus_iface/kf5_org.kde.??lobal?ccel*

%files -n libkf5globalaccel
%_K5lib/libKF5GlobalAccel.so.*
%files -n libkf5globalaccelprivate
%_K5lib/libKF5GlobalAccelPrivate.so.*

%changelog
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
- initial build
