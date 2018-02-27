%define rname plasma-desktop

%define kfontinst_sover 5
%define libkfontinst libkfontinst%kfontinst_sover
%define kfontinstui_sover 5
%define libkfontinstui libkfontinstui%kfontinstui_sover
%define kf5activitiesexperimentalstats_sover 1
%define libkf5activitiesexperimentalstats libkf5activitiesexperimentalstats%kf5activitiesexperimentalstats_sover


Name: kf5-%rname
Version: 5.3.0
Release: alt1
%K5init altplace

Group: Graphical desktop/KDE
Summary: KDE Workspace 5 plasma desktop view furniture
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Requires: kf5-plasma-workspace
Requires: polkit-kde-plasma-desktop

Source: %rname-%version.tar
Patch1: alt-def-font.patch

# Automatically added by buildreq on Mon Mar 23 2015 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils fontconfig fontconfig-devel glib2-devel glibc-devel-static kf5-attica-devel kf5-kdoctools-devel libEGL-devel libGL-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libcloog-isl4 libdbusmenu-qt52 libfreetype-devel libgpg-error libjson-c libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-qml libqt5-quick libqt5-quickwidgets libqt5-sql libqt5-svg libqt5-test libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libusb-compat libxcb-devel libxcbutil-image libxcbutil-keysyms libxkbfile-devel mkfontscale pkg-config python-base qt5-base-devel rpm-build-gir ruby ruby-stdlibs xml-common xml-utils xorg-fixesproto-devel xorg-inputproto-devel xorg-kbproto-devel xorg-renderproto-devel xorg-xf86miscproto-devel xorg-xproto-devel
#BuildRequires: boost-devel-headers extra-cmake-modules gcc-c++ iceauth kf5-baloo-devel kf5-kactivities-devel kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcmutils-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdelibs4support-devel kf5-kdesignerplugin-devel kf5-kdoctools kf5-kdoctools-devel-static kf5-kemoticons-devel kf5-kfilemetadata-devel kf5-kglobalaccel-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knewstuff-devel kf5-knotifications-devel kf5-knotifyconfig-devel kf5-kpackage-devel kf5-kparts-devel kf5-krunner-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwallet-devel kf5-kwidgetsaddons-devel kf5-kwin-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-libksysguard-devel kf5-plasma-framework-devel kf5-plasma-workspace-devel kf5-solid-devel kf5-sonnet-devel libGLU-devel libcanberra-devel libpulseaudio-devel libusb-compat-devel libxapian-devel libxcbutil-image-devel mkfontdir python-module-google qt5-declarative-devel qt5-phonon-devel qt5-svg-devel qt5-x11extras-devel rpm-build-ruby xset
BuildRequires(pre): rpm-build-kf5
BuildRequires: boost-devel extra-cmake-modules gcc-c++
BuildRequires: qt5-declarative-devel qt5-phonon-devel qt5-svg-devel qt5-x11extras-devel
BuildRequires: libGLU-devel libcanberra-devel libpulseaudio-devel libusb-compat-devel libxapian-devel libxcbutil-image-devel
BuildRequires: xorg-drv-synaptics-devel xorg-sdk
BuildRequires: iceauth mkfontdir xset
BuildRequires: kf5-baloo-devel kf5-kactivities-devel kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcmutils-devel
BuildRequires: kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel
BuildRequires: kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdelibs4support-devel kf5-kdesignerplugin-devel
BuildRequires: kf5-kdoctools kf5-kdoctools-devel-static
BuildRequires: kf5-kemoticons-devel kf5-kfilemetadata-devel kf5-kglobalaccel-devel kf5-kguiaddons-devel kf5-ki18n-devel
BuildRequires: kf5-kiconthemes-devel kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel
BuildRequires: kf5-knewstuff-devel kf5-knotifications-devel kf5-knotifyconfig-devel kf5-kpackage-devel kf5-kparts-devel
BuildRequires: kf5-krunner-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwallet-devel
BuildRequires: kf5-kwidgetsaddons-devel kf5-kwin-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-libksysguard-devel
BuildRequires: kf5-plasma-framework-devel kf5-plasma-workspace-devel kf5-solid-devel kf5-sonnet-devel
BuildRequires: kf5-kdeclarative-devel kf5-kpeople-devel
BuildRequires: kf5-kded kf5-kded-devel

%description
Plasma desktop view furniture.

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

%package -n polkit-kde-plasma-desktop
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: %name-common = %version-%release
Provides: polkit-kde-kfontinst
Provides: polkit-kde-kcmclock
%description -n polkit-kde-plasma-desktop
Common polkit files for %name

%package -n %libkfontinst
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkfontinst
KF5 library

%package -n %libkfontinstui
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkfontinstui
KF5 library

%package -n %libkf5activitiesexperimentalstats
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkf5activitiesexperimentalstats
KF5 library


%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K5cmake \
    -DLIBEXEC_INSTALL_DIR=%_K5exec \
    #
%K5make

%install
%K5install

%K5install_move data color-schemes doc
%K5install_move data kcm_componentchooser kcminput kcmkeyboard kcmkeys kcm_phonon kcmsolidactions
%K5install_move data kconf_update kcontrol kdisplay kdm kfontinst konqsidebartng ksmserver solid kpackage
%K5install_move data plasma/desktoptheme plasma/plasmoids/touchpad

%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc COPYING*
%_K5icon/*/*/*/*.*

%files
%config(noreplace) %_K5xdgconf/*
%config %_K5conf_dbus_sysd/*.conf
%_K5bin/*
%_K5exec/*
%_K5libexecdir/kauth/*
%_K5cf_bin/*
%_K5lib/libkdeinit5_*.so
%_K5plug/*.so
%_K5plug/kcms/*.so
%_K5plug/plasma/dataengine/*.so
%_K5qml/org/kde/plasma/private/*/
%_K5qml/org/kde/private/*/
%_K5qml/org/kde/plasma/activityswitcher/
%_K5xdgapp/*
%_K5cfg/*
%_K5srv//ServiceMenus/*.desktop
%_K5srv/kded/*.desktop
%_K5srv/*.desktop
%_K5srv/*.protocol
%_K5srvtyp/*.desktop
%_K5xmlgui/*
%_K5notif/*
%_K5data/solid/devices/solid-*.desktop
%_K5data/color-schemes/*
%_K5data/kcm*/
%_K5cf_upd/*
%_K5data/kpackage/kcms/*
%_K5data/plasma/plasmoids/*
%_K5data/plasma/packages/*
%_K5data/plasma/layout-templates/*
%_K5data/plasma/shells/*/
%_K5data/plasma/services/*
%_K5data/plasma/desktoptheme/default/icons/*
%_K5data/kcontrol/
%_K5data/kdisplay/
%_K5data/kdm/
%_K5data/kfontinst/
%_K5data/konqsidebartng/
%_K5data/ksmserver/
%_K5dbus_srv/*.service
%_K5dbus_sys_srv/*.service

%files -n polkit-kde-plasma-desktop
%_datadir/polkit-1/actions/*fontinst*.policy
%_datadir/polkit-1/actions/*kcmclock*.policy

%files devel
#%_K5inc/plasma-desktop_version.h
#%_K5inc/plasma-desktop/
%_K5link/lib*.so
#%_K5lib/cmake/plasma-desktop
#%_K5archdata/mkspecs/modules/qt_plasma-desktop.pri
%_K5dbus_iface/*.xml

%files -n %libkfontinst
%_K5lib/libkfontinst.so.*
%_K5lib/libkfontinst.so.%kfontinst_sover
%files -n %libkfontinstui
%_K5lib/libkfontinstui.so.*
%_K5lib/libkfontinstui.so.%kfontinstui_sover
%files -n %libkf5activitiesexperimentalstats
%_K5lib/libKF5ActivitiesExperimentalStats.so.*
%_K5lib/libKF5ActivitiesExperimentalStats.so.%kf5activitiesexperimentalstats_sover

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
