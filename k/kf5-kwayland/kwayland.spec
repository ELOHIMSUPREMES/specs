%define rname kwayland

Name: kf5-%rname
Version: 5.3.2
Release: alt1
%K5init altplace

Group: System/Libraries
Summary: KDE Workspace 5 client and server wrapper for Wayland libraries
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Thu Mar 05 2015 (-bi)
# optimized out: cmake cmake-modules elfutils libEGL-devel libGL-devel libcloog-isl4 libqt5-concurrent libqt5-core libqt5-gui libqt5-test libqt5-widgets libstdc++-devel libwayland-client libwayland-server pkg-config python-base ruby ruby-stdlibs wayland-devel
#BuildRequires: extra-cmake-modules gcc-c++ libwayland-client-devel libwayland-server-devel python-module-google qt5-base-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++ qt5-base-devel
BuildRequires: libwayland-client-devel libwayland-server-devel

%description
KWayland provides a Qt-style Client and Server library wrapper for the Wayland libraries.

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

%package -n libkf5waylandclient
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5waylandclient
KF5 library

%package -n libkf5waylandserver
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5waylandserver
KF5 library


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%find_lang %name --all-name

%files common -f %name.lang
%doc COPYING.LIB

%files devel
%_K5inc/kwayland_version.h
%_K5inc/KWayland/
%_K5link/lib*.so
%_K5lib/cmake/KF5Wayland
#%_K5archdata/mkspecs/modules/qt_KWayland.pri

%files -n libkf5waylandclient
%_K5lib/libKF5WaylandClient.so.*
%files -n libkf5waylandserver
%_K5lib/libKF5WaylandServer.so.*

%changelog
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

* Mon Mar 30 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.2-alt0.1
- test

* Wed Feb 25 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt0.1
- initial build
