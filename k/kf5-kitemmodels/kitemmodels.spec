%define rname kitemmodels

Name: kf5-%rname
Version: 5.8.0
Release: alt1
%K5init altplace

Group: System/Libraries
Summary: Set of item models extending the Qt model-view framework
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Wed Dec 24 2014 (-bi)
# optimized out: cmake cmake-modules elfutils libcloog-isl4 libqt5-core libstdc++-devel python-base ruby ruby-stdlibs
#BuildRequires: extra-cmake-modules gcc-c++ python-module-google qt5-base-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++ qt5-base-devel qt5-tools-devel

%description
KItemModels provides a set of item models extending the Qt model-view framework.

%package common
Summary: %name common package
Group: Graphical desktop/KDE
BuildArch: noarch
Requires: kf5-filesystem
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: kf5-filesystem
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkf5itemmodels
Group: System/Libraries
Summary: KF5 library
#Requires: %name-common = %version-%release
%description -n libkf5itemmodels
KF5 library


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install

#%files common -f %name.lang

%files devel
%_K5link/lib*.so
%_K5inc/kitemmodels_version.h
%_K5inc/KItemModels/
%_K5lib/cmake/KF5ItemModels
%_K5archdata/mkspecs/modules/qt_KItemModels.pri

%files -n libkf5itemmodels
%doc COPYING.LIB README.md
%_K5lib/libKF5ItemModels.so.*

%changelog
* Mon Apr 06 2015 Sergey V Turchin <zerg@altlinux.org> 5.8.0-alt1
- new version

* Wed Mar 18 2015 Sergey V Turchin <zerg@altlinux.org> 5.8.0-alt0.1
- test

* Mon Feb 16 2015 Sergey V Turchin <zerg@altlinux.org> 5.7.0-alt0.1
- test

* Fri Jan 16 2015 Sergey V Turchin <zerg@altlinux.org> 5.6.0-alt0.1
- test

* Mon Dec 22 2014 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt1
- initial build
