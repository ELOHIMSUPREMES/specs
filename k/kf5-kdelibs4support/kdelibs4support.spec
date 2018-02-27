%define rname kdelibs4support

Name: kf5-%rname
Version: 5.11.0
Release: alt1
%K5init altplace

Group: System/Libraries
Summary: KDE Frameworks 5 KDELibs 4 support
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar
Patch1: alt-find-docbookxml.patch

# Automatically added by buildreq on Wed Feb 18 2015 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils kf5-kdoctools-devel libEGL-devel libGL-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libcloog-isl4 libcom_err-devel libgpg-error libjson-c libkrb5-devel libqt5-core libqt5-dbus libqt5-designer libqt5-gui libqt5-network libqt5-printsupport libqt5-svg libqt5-test libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcb-devel libxcbutil-keysyms libxkbfile-devel pkg-config python-base qt5-base-devel ruby ruby-stdlibs xml-common xml-utils xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel
#BuildRequires: extra-cmake-modules gcc-c++ kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdesignerplugin-devel kf5-kdoctools kf5-kdoctools-devel-static kf5-kglobalaccel-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kparts-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libssl-devel nss-ldapd python-module-google qt5-quick1-devel qt5-svg-devel qt5-tools-devel qt5-x11extras-devel rpm-build-gir rpm-build-ruby
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++ perl-URI
BuildRequires: libssl-devel
BuildRequires: qt5-quick1-devel qt5-svg-devel qt5-tools-devel qt5-x11extras-devel
BuildRequires: kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel
BuildRequires: kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel
BuildRequires: kf5-kdbusaddons-devel kf5-kdesignerplugin-devel
BuildRequires: kf5-kdoctools kf5-kdoctools-devel-static
BuildRequires: kf5-kglobalaccel-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel
BuildRequires: kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kparts-devel kf5-kservice-devel
BuildRequires: kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel
BuildRequires: kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel

%description
This framework provides code and utilities to ease the transition from
kdelibs 4 to KDE Frameworks 5.  This includes CMake macros and C++
classes whose functionality has been replaced by code in CMake, Qt and
other frameworks.

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

%package -n libkf5kdelibs4support
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5kdelibs4support
KF5 library


%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K5build

%install
%K5install
mv %buildroot/%_datadir/locale/* %buildroot/%_K5i18n/

%find_lang %name --with-kde --all-name
%K5find_qtlang %name --all-name

%files common -f %name.lang
%doc COPYING.LIB README.md
%dir %_K5xdgconf/colors/
%_K5i18n/countries/
%_K5i18n/currency/
%_K5i18n/kf5_all_languages

%files
%config %_K5xdgconf/colors/*
%config %_K5xdgconf/k*
%_bindir/*5
%_K5bin/*
%_K5exec/*
%_K5plug/designer/kf5deprecatedwidgets.so
%_K5plug/kcm_ssl.so
%_K5plug/kf5/kded/networkstatus.so
%_K5plug/kf5/kio/metainfo.so
%_K5srv/qimageioplugins/
%_K5data/kdoctools/
%_K5data/kssl/
%_K5data/widgets/pics/*.png
%_K5srv/*.desktop
%_K5srv/kded/networkstatus.desktop
%_K5srv/metainfo.protocol
%_K5srvtyp/*.desktop



%files devel
%_K5inc/kdelibs4support_version.h
%_K5inc/KDELibs4Support/
%_K5link/lib*.so
%_K5lib/cmake/KF5KDELibs4Support/
%_K5lib/cmake/KDELibs4/
%_K5lib/cmake/KF5KDE4Support/
#%_K5archdata/mkspecs/modules/qt_KDELibs4Support.pri
%_K5dbus_iface/*.xml

%files -n libkf5kdelibs4support
%_K5lib/libKF5KDELibs4Support.so.*

%changelog
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
