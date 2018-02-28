%define rname spectacle

Name: kde5-%rname
Version: 15.12.2
Release: alt2
%K5init altplace

Group: Graphical desktop/KDE
Summary: The KDE Screenshot Utility
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar
Patch1: alt-dbus-service.patch

# Automatically added by buildreq on Tue Jan 12 2016 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils gcc-c++ gtk-update-icon-cache kf5-kdoctools-devel libEGL-devel libGL-devel libdbusmenu-qt52 libgpg-error libjson-c libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcb-devel libxcb-render-util libxcbutil-cursor libxcbutil-image libxcbutil-keysyms pkg-config python-base python-modules python3 python3-base qt5-base-devel xml-common xml-utils
#BuildRequires: extra-cmake-modules kde5-libkipi-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdoctools kf5-kdoctools-devel-static kf5-ki18n-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-libkscreen-devel kf5-solid-devel libxcbutil-cursor-devel libxcbutil-devel libxcbutil-image-devel python-module-google qt5-x11extras-devel rpm-build-python3 ruby ruby-stdlibs
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules qt5-base-devel qt5-x11extras-devel
BuildRequires: libxcbutil-cursor-devel libxcbutil-devel libxcbutil-image-devel
BuildRequires: kde5-libkipi-devel
BuildRequires: kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel
BuildRequires: kf5-kcoreaddons-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdoctools kf5-kdoctools-devel-static kf5-ki18n-devel
BuildRequires: kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kservice-devel
BuildRequires: kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-libkscreen-devel kf5-solid-devel

%description
Spectacle is screenshot taking utility for the KDE desktop. Spectacle
can also be used in non-KDE X11 desktop environments.

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

%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K5build

%install
%K5install
%K5install_move data khotkeys
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc COPYING*
%_K5bin/spectacle
%_K5xdgapp/org.kde.spectacle.desktop
%_K5icon/hicolor/*/apps/spectacle.*
%_K5notif/spectacle.notifyrc
%_K5data/khotkeys/spectacle.khotkeys
%_K5dbus_srv/org.kde.Spectacle.service

#%files devel
#%_K5dbus_iface/org.kde.Spectacle.xml

%changelog
* Wed Mar 23 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt2
- rebuild wit new libkscreen

* Fri Feb 26 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt1
- new version

* Wed Jan 20 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.1-alt1
- new version

* Wed Sep 30 2015 Sergey V Turchin <zerg@altlinux.org> 15.12.0-alt1
- initial build
