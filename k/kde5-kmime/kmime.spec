%define rname kmime

Name: kde5-%rname
Version: 15.08.1
Release: alt1
%K5init altplace

Group: Graphical desktop/KDE
Summary: KMime Library
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Mon Aug 10 2015 (-bi)
# optimized out: cmake cmake-modules elfutils libqt5-core libstdc++-devel python-base python3 python3-base ruby ruby-stdlibs
#BuildRequires: boost-devel-headers extra-cmake-modules gcc-c++ kf5-kcodecs-devel kf5-ki18n-devel libdb4-devel python-module-google qt5-base-devel rpm-build-python3 rpm-build-ruby
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++ qt5-base-devel
BuildRequires: boost-devel-headers
BuildRequires: kf5-kcodecs-devel kf5-ki18n-devel

%description
%summary.

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

%package -n libkf5mime
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5mime
KF5 library


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc COPYING*

%files devel
%_K5inc/kmime_version.h
%_K5inc/KMime/
%_K5link/lib*.so
%_K5lib/cmake/KF5Mime/
%_K5archdata/mkspecs/modules/qt_KMime.pri

%files -n libkf5mime
%_K5lib/libKF5Mime.so.*

%changelog
* Wed Sep 16 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.1-alt1
- new version

* Thu Aug 20 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.0-alt1
- new version

* Mon Aug 10 2015 Sergey V Turchin <zerg@altlinux.org> 15.7.90-alt1
- initial build
