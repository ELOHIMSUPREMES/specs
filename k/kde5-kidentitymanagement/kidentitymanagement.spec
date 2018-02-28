%define rname kidentitymanagement

Name: kde5-%rname
Version: 15.08.0
Release: alt1
%K5init altplace

Group: Graphical desktop/KDE
Summary: Manage PIM identity
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Tue Aug 11 2015 (-bi)
# optimized out: cmake cmake-modules elfutils kf5-kdoctools-devel libEGL-devel libGL-devel libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms python-base python3 python3-base ruby ruby-stdlibs
#BuildRequires: extra-cmake-modules gcc-c++ kde5-kpimtextedit-devel kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdelibs4support-devel kf5-kdesignerplugin-devel kf5-kdoctools kf5-kdoctools-devel-static kf5-kemoticons-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kparts-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libdb4-devel python-module-google qt5-base-devel rpm-build-python3 rpm-build-ruby
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++ qt5-base-devel
BuildRequires: kde5-kpimtextedit-devel
BuildRequires: kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel
BuildRequires: kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel
BuildRequires: kf5-kdelibs4support kf5-kdelibs4support-devel kf5-kdesignerplugin-devel kf5-kdoctools kf5-kdoctools-devel-static
BuildRequires: kf5-kemoticons-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kio-devel
BuildRequires: kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kparts-devel
BuildRequires: kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwidgetsaddons-devel
BuildRequires: kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel

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

%package -n libkf5identitymanagement
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5identitymanagement
KF5 library


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
#%find_lang %name --with-kde --all-name

#files common -f %name.lang
%files common
#%doc COPYING*

%files devel
%_K5inc/kidentitymanagement_version.h
%_K5inc/KIdentityManagement/
%_K5link/lib*.so
%_K5lib/cmake/KF5IdentityManagement/
%_K5archdata/mkspecs/modules/qt_KIdentityManagement.pri
%_K5dbus_iface/*.IdentityManager.xml

%files -n libkf5identitymanagement
%_K5lib/libKF5IdentityManagement.so.*

%changelog
* Thu Aug 20 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.0-alt1
- new version

* Mon Aug 10 2015 Sergey V Turchin <zerg@altlinux.org> 15.7.90-alt1
- initial build
