%define rname karchive

Name: kf5-%rname
Version: 5.17.0
Release: alt1
%K5init altplace

Group: System/Libraries
Summary: KDE Frameworks 5 compression and decompression of data
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Tue Jan 20 2015 (-bi)
# optimized out: cmake cmake-modules elfutils libcloog-isl4 libqt5-core libqt5-test libstdc++-devel python-base ruby ruby-stdlibs zlib-devel
#BuildRequires: bzlib-devel extra-cmake-modules gcc-c++ liblzma-devel python-module-google qt5-base-devel rpm-build-ruby zlib-devel-static
BuildRequires(pre): rpm-build-kf5
BuildRequires: bzlib-devel extra-cmake-modules gcc-c++ liblzma-devel qt5-base-devel zlib-devel

%description
KArchive provides classes for easy reading, creation and manipulation of
"archive" formats like ZIP and TAR. It also provides transparent
compression and decompression of data, like the GZip format,
via a subclass of QIODevice.

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

%package -n libkf5archive
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5archive
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
%_K5inc/karchive_version.h
%_K5inc/KArchive/
%_K5link/lib*.so
%_K5lib/cmake/KF5Archive
%_K5archdata/mkspecs/modules/qt_KArchive.pri

%files -n libkf5archive
%_K5lib/libKF5Archive.so.*

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
