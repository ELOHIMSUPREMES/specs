%define rname kimageformats

Name: kf5-%rname
Version: 5.16.0
Release: alt1
%K5init altplace

Group: System/Libraries
Summary: KDE Frameworks 5 plugins to allow QImage to support extra file formats
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Requires: kf5-filesystem

Source: %rname-%version.tar

# Automatically added by buildreq on Thu Feb 05 2015 (-bi)
# optimized out: cmake cmake-modules elfutils ilmbase-devel libEGL-devel libGL-devel libcloog-isl4 libqt5-core libqt5-gui libqt5-printsupport libqt5-widgets libstdc++-devel pkg-config python-base ruby ruby-stdlibs
#BuildRequires: extra-cmake-modules gcc-c++ openexr-devel python-module-google qt5-base-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++ openexr-devel qt5-base-devel

%description
This framework provides additional image format plugins for QtGui.  As
such it is not required for the compilation of any other software, but
may be a runtime requirement for Qt-based software to support certain
image formats.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
%description common
%name common package


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%find_lang %name --all-name
%K5find_qtlang %name --all-name

%files
%doc COPYING.LIB README.md
%_K5plug/imageformats/kimg_*.so
%_K5srv/qimageioplugins/


%changelog
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

* Mon Jun 15 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 5.10.0-alt1.1
- Rebuilt for gcc5 C++11 ABI.

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

* Tue Feb 03 2015 Sergey V Turchin <zerg@altlinux.org> 5.6.0-alt0.1
- test

* Mon Dec 22 2014 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt1
- initial build
