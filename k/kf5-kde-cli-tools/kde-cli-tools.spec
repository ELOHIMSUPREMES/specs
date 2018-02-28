%define rname kde-cli-tools

Name: kf5-%rname
Version: 5.4.0
Release: alt1
%K5init altplace

Group: Graphical desktop/KDE
Summary: KDE Workspace 5 common cli tools
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Requires: eject
#Requires: kf5-kdialog
#Requires: %_K5bin/kdialog
Requires: kf5-kdelibs4support

Source: %rname-%version.tar

# Automatically added by buildreq on Tue Mar 03 2015 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils kf5-kdoctools-devel libEGL-devel libGL-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libcloog-isl4 libgpg-error libjson-c libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-svg libqt5-test libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcb-devel libxcbutil-keysyms libxkbfile-devel python-base qt5-base-devel ruby ruby-stdlibs xml-common xml-utils xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++ qt5-svg-devel qt5-x11extras-devel
BuildRequires: kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcmutils-devel kf5-kcodecs-devel
BuildRequires: kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel
BuildRequires: kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdelibs4support-devel kf5-kdesignerplugin-devel
BuildRequires: kf5-kdesu-devel kf5-kdoctools kf5-kdoctools-devel-static kf5-kemoticons-devel kf5-kglobalaccel-devel
BuildRequires: kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel
BuildRequires: kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kparts-devel kf5-kpty-devel
BuildRequires: kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwidgetsaddons-devel
BuildRequires: kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel

%description
KDE common command line tools.

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

%package -n libkf5de-cli-tools
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5de-cli-tools
KF5 library


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc COPYING*
%_bindir/*5
%_K5bin/*
%_K5exec/*
%_K5lib/libkdeinit5_*.so
%_K5plug/*.so
%_K5srv/*.desktop

%changelog
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
- rebuild to test add_findpackage_path macro

* Thu Apr 16 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.2-alt1
- new version

* Mon Mar 30 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.2-alt0.1
- test

* Wed Feb 25 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt0.1
- initial build
