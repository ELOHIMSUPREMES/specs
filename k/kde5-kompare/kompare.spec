%define rname kompare

%define sover 5
%define libkomparedialogpages libkomparedialogpages%sover
%define libkompareinterface libkompareinterface%sover

Name: kde5-%rname
Version: 15.12.1
Release: alt1
%K5init altplace

Group: Graphical desktop/KDE
Summary: Files differences viewer.
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Mon Jan 11 2016 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils gcc-c++ gtk-update-icon-cache kf5-kdoctools-devel libEGL-devel libGL-devel libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-script libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms python-base python-modules python3 python3-base ruby ruby-stdlibs xml-common xml-utils
#BuildRequires: extra-cmake-modules kde5-libkomparediff2-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdelibs4support kf5-kdoctools kf5-kdoctools-devel-static kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kparts-devel kf5-kservice-devel kf5-ktexteditor-devel kf5-ktextwidgets-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel python-module-google qt5-base-devel rpm-build-python3 rpm-build-ruby
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules qt5-base-devel
BuildRequires: kde5-libkomparediff2-devel
BuildRequires: kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel
BuildRequires: kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdelibs4support kf5-kdoctools kf5-kdoctools-devel-static
BuildRequires: kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kparts-devel
BuildRequires: kf5-kservice-devel kf5-ktexteditor-devel kf5-ktextwidgets-devel kf5-kwidgetsaddons-devel
BuildRequires: kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel

%description
Kompare is a program to view the differences between files.

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

%package -n %libkomparedialogpages
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkomparedialogpages
KF5 library

%package -n %libkompareinterface
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkompareinterface
KF5 library


%prep
%setup -n %rname-%version

%build
%K5build \
    -DINCLUDE_INSTALL_DIR=%_K5inc \
    #

%install
%K5install
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc COPYING*

%files
%_K5bin/kompare
%_K5plug/kompare*.so
%_K5xdgapp/org.kde.kompare.desktop
%_K5icon/hicolor/*/apps/kompare.*
%_K5xmlgui/kompare/
%_K5srv/kompare*.desktop
%_K5srvtyp/kompare*.desktop

%files devel
#%_K5inc/kompare_version.h
%_K5inc/kompare/
%_K5link/lib*.so
#%_K5lib/cmake/kompare
#%_K5archdata/mkspecs/modules/qt_kompare.pri

%files -n %libkompareinterface
%_K5lib/libkompareinterface.so.%sover
%_K5lib/libkompareinterface.so.*
%files -n %libkomparedialogpages
%_K5lib/libkomparedialogpages.so.%sover
%_K5lib/libkomparedialogpages.so.*

%changelog
* Wed Jan 20 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.1-alt1
- new version

* Mon Jan 11 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.0-alt1
- initial build
