%define rname powerdevil

%define powerdevilconfigcommonprivate_sover 5
%define libpowerdevilconfigcommonprivate libpowerdevilconfigcommonprivate%powerdevilconfigcommonprivate_sover
%define powerdevilui_sover 5
%define libpowerdevilui libpowerdevilui%powerdevilui_sover
%define powerdevilcore_sover 2
%define libpowerdevilcore libpowerdevilcore%powerdevilcore_sover

Name: kf5-%rname
Version: 5.4.2
Release: alt1
%K5init altplace

Group: Graphical desktop/KDE
Summary: KDE Workspace 5 advanced power management settings
Url: http://www.kde.org
License: GPLv2+

Requires: upower

Source: %rname-%version.tar
Patch1: alt-nohal.patch

# Automatically added by buildreq on Sat Mar 21 2015 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils kf5-attica-devel kf5-kdoctools-devel libEGL-devel libGL-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libcloog-isl4 libdbusmenu-qt52 libgpg-error libjson-c libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcb-devel libxcbutil-keysyms libxkbfile-devel pkg-config python-base qt5-base-devel ruby ruby-stdlibs xml-common xml-utils xorg-kbproto-devel xorg-randrproto-devel xorg-renderproto-devel xorg-xextproto-devel xorg-xf86miscproto-devel xorg-xproto-devel
#BuildRequires: extra-cmake-modules gcc-c++ kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdelibs4support-devel kf5-kdesignerplugin-devel kf5-kdoctools kf5-kdoctools-devel-static kf5-kemoticons-devel kf5-kglobalaccel-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kidletime-devel kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-knotifyconfig-devel kf5-kparts-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-plasma-workspace-devel kf5-solid-devel kf5-sonnet-devel libudev-devel python-module-google qt5-x11extras-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++ qt5-x11extras-devel
BuildRequires: libudev-devel
BuildRequires: kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel
BuildRequires: kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel
BuildRequires: kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdelibs4support-devel kf5-kdesignerplugin-devel
BuildRequires: kf5-kdoctools kf5-kdoctools-devel-static kf5-kemoticons-devel kf5-kglobalaccel-devel
BuildRequires: kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kidletime-devel kf5-kinit-devel
BuildRequires: kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel
BuildRequires: kf5-knotifications-devel kf5-knotifyconfig-devel kf5-kparts-devel kf5-kservice-devel
BuildRequires: kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel
BuildRequires: kf5-kxmlgui-devel kf5-plasma-workspace-devel kf5-solid-devel kf5-sonnet-devel
BuildRequires: kf5-libkscreen-devel kf5-kactivities-devel

%description
Advanced power management settings.

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

%package -n %libpowerdevilconfigcommonprivate
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libpowerdevilconfigcommonprivate
KF5 library

%package -n %libpowerdevilui
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libpowerdevilui
KF5 library

%package -n %libpowerdevilcore
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libpowerdevilcore
KF5 library


%prep
%setup -n %rname-%version
%patch1 -p1

find ./ -type f | \
while read f ; do
    sed -i 's|org.kde.powerdevil.backlighthelper|org.kde5.powerdevil.backlighthelper|g' $f
done

%build
%K5build

%install
%K5install
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc COPYING*

%files
%config %_K5conf_dbus_sysd/*.conf
%_K5libexecdir/kauth/*
%_K5plug/*.so
%_K5srv/kded/*.desktop
%_K5srv/*.desktop
%_K5srvtyp/*.desktop
%_K5notif/*.notifyrc
%_K5dbus_sys_srv/*.service
%_datadir/polkit-1/actions/*.policy

#%files devel
#%_K5inc/powerdevil_version.h
#%_K5inc/PowerDevil/
#%_K5link/lib*.so
#%_K5lib/cmake/PowerDevil
#%_K5archdata/mkspecs/modules/qt_PowerDevil.pri

%files -n %libpowerdevilconfigcommonprivate
%_K5lib/libpowerdevilconfigcommonprivate.so.*
%_K5lib/libpowerdevilconfigcommonprivate.so.%powerdevilconfigcommonprivate_sover
%files -n %libpowerdevilui
%_K5lib/libpowerdevilui.so.*
%_K5lib/libpowerdevilui.so.%powerdevilui_sover
%files -n %libpowerdevilcore
%_K5lib/libpowerdevilcore.so.*
%_K5lib/libpowerdevilcore.so.%powerdevilcore_sover

%changelog
* Wed Oct 07 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.2-alt1
- new version

* Thu Sep 10 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.1-alt1
- new version

* Wed Aug 26 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.0-alt1
- new version

* Sat Aug 22 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.95-alt1
- new version

* Wed Jul 01 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.2-alt1
- new version

* Fri May 29 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt1
- new version

* Thu Apr 30 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt1
- new version

* Tue Apr 28 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt0.1
- test

* Tue Apr 21 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.2-alt2
- require upower

* Thu Apr 16 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.2-alt1
- new version

* Mon Mar 30 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.2-alt0.1
- test

* Wed Feb 25 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt0.1
- initial build
