%define rname baloo

Name: kf5-%rname
Version: 5.3.1
Release: alt1
%K5init altplace

Group: Graphical desktop/KDE
Summary: KDE Workspace 5 framework for searching and managing metadata
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Requires: polkit-kde-baloo

Source: %rname-%version.tar
Patch1: alt-disable-indexing.patch

# Automatically added by buildreq on Fri Feb 27 2015 (-bi)
# optimized out: cmake cmake-modules elfutils kf5-kdoctools-devel libEGL-devel libGL-devel libcloog-isl4 libjson-c libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-qml libqt5-quick libqt5-sql libqt5-svg libqt5-test libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms python-base qt5-base-devel ruby ruby-stdlibs
#BuildRequires: extra-cmake-modules gcc-c++ kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdelibs4support-devel kf5-kdesignerplugin-devel kf5-kdoctools kf5-kdoctools-devel-static kf5-kemoticons-devel kf5-kfilemetadata-devel kf5-kglobalaccel-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kidletime-devel kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kparts-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libxapian-devel python-module-google qt5-declarative-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++ qt5-declarative-devel
BuildRequires: libxapian-devel
BuildRequires: kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel
BuildRequires: kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel
BuildRequires: kf5-kdelibs4support kf5-kdelibs4support-devel
BuildRequires: kf5-kdoctools kf5-kdoctools-devel-static
BuildRequires: kf5-kdesignerplugin-devel kf5-kemoticons-devel kf5-kfilemetadata-devel kf5-kglobalaccel-devel
BuildRequires: kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kidletime-devel kf5-kinit-devel
BuildRequires: kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel
BuildRequires: kf5-kparts-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel
BuildRequires: kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel

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

%package -n polkit-kde-baloo
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: %name-common = %version-%release
%description -n polkit-kde-baloo
Common polkit files for %name

%package -n libkf5baloo
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5baloo
KF5 library

%package -n libkf5balooxapian
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5balooxapian
KF5 library


%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K5build

%install
%K5install
%find_lang %name --all-name

%files common -f %name.lang
%doc COPYING.LIB Readme.md

%files
%_K5bin/baloo*
%_K5libexecdir/kauth/*baloo*
%_K5plug/kded_baloosearch_kio.so
%_K5plug/kf5/kio/*.so
%_K5qml/org/kde/baloo/
%_K5start/baloo*.desktop
%_K5srv/kded/*.desktop
%_K5srv/*.protocol
%_K5conf_dbus_sysd/*.conf
%_K5dbus_sys_srv/*.service
%_K5icon/hicolor/*/apps/baloo.*

%files -n polkit-kde-baloo
%_datadir/polkit-1/actions/*baloo*filewatch*.policy

%files devel
%_K5inc/baloo_version.h
%_K5inc/Baloo/
%_K5link/lib*.so
%_K5lib/cmake/KF5Baloo
#%_K5archdata/mkspecs/modules/qt_Baloo.pri
%_K5dbus_iface/*.baloo.*.xml

%files -n libkf5baloo
%_K5lib/libKF5Baloo.so.*
%files -n libkf5balooxapian
%_K5lib/libKF5BalooXapian.so.*

%changelog
* Mon Jun 08 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt1
- new version

* Sun Jun 07 2015 Michael Shigorin <mike@altlinux.org> 5.3.0-alt2.1
- NMU: rebuilt against current libxapian

* Mon May 18 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt2
- fix desktop-file

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
