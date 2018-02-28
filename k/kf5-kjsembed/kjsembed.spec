%define rname kjsembed

Name: kf5-%rname
Version: 5.20.0
Release: alt1
%K5init altplace

Group: System/Libraries
Summary: KDE Frameworks 5 binding Javascript object to QObjects
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Tue Feb 17 2015 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils kf5-kdoctools-devel libEGL-devel libGL-devel libcloog-isl4 libgpg-error libqt5-core libqt5-gui libqt5-svg libqt5-widgets libqt5-xml libstdc++-devel python-base qt5-base-devel qt5-tools-devel ruby ruby-stdlibs xml-common xml-utils
#BuildRequires: extra-cmake-modules gcc-c++ kf5-karchive-devel kf5-kdoctools kf5-kdoctools-devel-static kf5-ki18n-devel kf5-kjs-devel python-module-google qt5-svg-devel qt5-tools-devel-static rpm-build-ruby
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++ qt5-svg-devel qt5-tools-devel-static
BuildRequires: kf5-karchive-devel kf5-kdoctools kf5-kdoctools-devel-static
BuildRequires: kf5-ki18n-devel kf5-kjs-devel

%description
KSJEmbed provides a method of binding JavaScript objects to QObjects,
so you can script your applications.

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

%package -n libkf5jsembed
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5jsembed
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
%_bindir/*5
%_K5bin/kjs*
#%_K5inc/kjsembed_version.h
%_K5inc/KJsEmbed/
%_K5link/lib*.so
%_K5lib/cmake/KF5JsEmbed
%_K5archdata/mkspecs/modules/qt_KJsEmbed.pri

%files -n libkf5jsembed
%_K5lib/libKF5JsEmbed.so.*

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
