%define rname kemoticons

Name: kf5-%rname
Version: 5.8.0
Release: alt1
%K5init altplace

Group: System/Libraries
Summary: KDE Frameworks 5 converting text emoticons to graphical emoticons
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Fri Feb 13 2015 (-bi)
# optimized out: cmake cmake-modules elfutils libEGL-devel libGL-devel libcloog-isl4 libqt5-core libqt5-dbus libqt5-gui libqt5-test libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel python-base ruby ruby-stdlibs
#BuildRequires: extra-cmake-modules gcc-c++ kf5-karchive-devel kf5-kconfig-devel kf5-kcoreaddons-devel kf5-kdbusaddons-devel kf5-ki18n-devel kf5-kservice-devel python-module-google qt5-base-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++ qt5-base-devel
BuildRequires: kf5-karchive-devel kf5-kconfig-devel kf5-kcoreaddons-devel kf5-kdbusaddons-devel
BuildRequires: kf5-ki18n-devel kf5-kservice-devel

%description
KEmoticons converts emoticons from text to a graphical representation with
images in HTML. It supports setting different themes for emoticons coming
from different providers.

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

%package -n libkf5emoticons
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5emoticons
KF5 library


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%K5install_move data emoticons
%find_lang %name --with-qt --all-name
%K5find_qtlang %name --all-name

%files common -f %name.lang
%doc COPYING.LIB README.md
%_K5emo/*

%files devel
%_K5inc/kemoticons_version.h
%_K5inc/KEmoticons/
%_K5link/lib*.so
%_K5lib/cmake/KF5Emoticons
%_K5archdata/mkspecs/modules/qt_KEmoticons.pri

%files -n libkf5emoticons
%_K5lib/libKF5Emoticons.so.*
%_K5plug/kf5/*.so
%_K5plug/kf5/emoticonsthemes/
%_K5srv/*.desktop
%_K5srvtyp/*.desktop

%changelog
* Mon Apr 06 2015 Sergey V Turchin <zerg@altlinux.org> 5.8.0-alt1
- new version

* Wed Mar 18 2015 Sergey V Turchin <zerg@altlinux.org> 5.8.0-alt0.1
- test

* Mon Feb 16 2015 Sergey V Turchin <zerg@altlinux.org> 5.7.0-alt0.1
- test

* Tue Feb 10 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt0.1
- initial build
