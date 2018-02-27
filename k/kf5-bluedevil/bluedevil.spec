%define rname bluedevil

Name: kf5-%rname
Version: 5.3.0
Release: alt1
%K5init altplace

Group: Graphical desktop/KDE
Summary: KDE Workspace 5 bluetooth stack
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Requires: bluez >= 5.0 obexd

Source: %rname-%version.tar

# Automatically added by buildreq on Fri Feb 27 2015 (-bi)
# optimized out: cmake cmake-modules elfutils libEGL-devel libGL-devel libcloog-isl4 libjson-c libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms python-base ruby ruby-stdlibs shared-mime-info
#BuildRequires: extra-cmake-modules gcc-c++ kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdbusaddons-devel kf5-kglobalaccel-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-libbluedevil-devel kf5-solid-devel kf5-sonnet-devel python-module-google qt5-base-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++ qt5-base-devel qt5-declarative-devel
BuildRequires: kf5-bluez-qt-devel
BuildRequires: kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel
BuildRequires: kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdbusaddons-devel kf5-kglobalaccel-devel
BuildRequires: kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel kf5-kitemviews-devel
BuildRequires: kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kservice-devel kf5-ktextwidgets-devel
BuildRequires: kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel
BuildRequires: kf5-solid-devel kf5-sonnet-devel
BuildRequires: kf5-kded kf5-kded-devel kf5-plasma-framework-devel kf5-kpackage-devel

%description
BlueDevil is the new bluetooth stack for KDE, it's composed of:
KCM, KDED, KIO, Library and some other small applications.


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

%package -n libkf5bluedevil
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5bluedevil
KF5 library


%prep
%setup -n %rname-%version

%build
%K5build \
    -DLIBEXEC_INSTALL_DIR=%_K5exec \
    #


%install
%K5install
%K5install_move data bluedevilwizard remoteview

mv %buildroot/%_K5xdgmime/bluedevil-mime.xml %buildroot/%_K5xdgmime/kf5-bluedevil-mime.xml

%find_lang %name --all-name

%files -f %name.lang
#%doc COPYING.LIB README.md
%_K5bin/*
%_K5plug/*.so
%_K5plug/kf5/kded/*.so
%_K5exec/*
%_K5qml/org/kde/plasma/private/bluetooth/
%_K5data/plasma/plasmoids/org.kde.plasma.bluetooth/
%_K5data/bluedevilwizard/
%_K5data/remoteview/bluetooth-network.desktop
%_K5xdgapp/*.desktop
%_K5notif/*.notifyrc
%_K5srv/*.desktop
%_K5srv/*.protocol
#%_K5srv/kded/*.desktop
%_K5xdgmime/*.xml

%changelog
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
