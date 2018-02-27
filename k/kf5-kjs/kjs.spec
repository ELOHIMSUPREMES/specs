%define rname kjs

Name: kf5-%rname
Version: 5.8.0
Release: alt1
%K5init altplace

Group: System/Libraries
Summary: KDE Frameworks 5 Javascript engine
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Thu Mar 19 2015 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils kf5-kdoctools-devel libcloog-isl4 libgpg-error libqt5-core libqt5-test libstdc++-devel pkg-config python-base ruby ruby-stdlibs xml-common xml-utils
#BuildRequires: extra-cmake-modules gcc-c++ kf5-karchive-devel kf5-kdelibs4support kf5-kdoctools kf5-kdoctools-devel-static libpcre-devel python-module-google qt5-base-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++ qt5-base-devel
BuildRequires: kf5-karchive-devel kf5-kdoctools kf5-kdoctools-devel-static
#BuildRequires: kf5-kdelibs4support
BuildRequires: libpcre-devel

%description
This library provides an ECMAScript compatible interpreter. The ECMA standard
is based on well known scripting languages such as Netscape's JavaScript and
Microsoft's JScript.

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
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkf5js
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5js
KF5 library

%package -n libkf5jsapi
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5jsapi
KF5 library


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%find_lang %name --with-qt --all-name
%K5find_qtlang %name --all-name

%files common -f %name.lang
%doc COPYING.LIB README.md

%files devel
%_K5bin/kjs5
%_K5inc/kjs_version.h
%_K5inc/wtf/
%_K5inc/kjs/
%_K5link/lib*.so
%_K5lib/cmake/KF5JS
%_K5archdata/mkspecs/modules/qt_KJS.pri
%_K5archdata/mkspecs/modules/qt_KJSApi.pri
%_K5data/kjs/

%files -n libkf5js
%_K5lib/libKF5JS.so.*
%files -n libkf5jsapi
%_K5lib/libKF5JSApi.so.*

%changelog
* Mon Apr 06 2015 Sergey V Turchin <zerg@altlinux.org> 5.8.0-alt1
- new version

* Wed Mar 18 2015 Sergey V Turchin <zerg@altlinux.org> 5.8.0-alt0.1
- test

* Mon Feb 16 2015 Sergey V Turchin <zerg@altlinux.org> 5.7.0-alt0.1
- test

* Tue Feb 03 2015 Sergey V Turchin <zerg@altlinux.org> 5.6.0-alt0.1
- test

* Mon Dec 22 2014 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt1
- initial build
