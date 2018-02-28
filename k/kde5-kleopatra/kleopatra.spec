%define rname kleopatra

%define kleopatraclientcore_sover 1
%define libkleopatraclientcore libkleopatraclientcore%kleopatraclientcore_sover
%define kleopatraclientgui_sover 1
%define libkleopatraclientgui libkleopatraclientgui%kleopatraclientgui_sover

Name: kde5-%rname
Version: 16.04.3
Release: alt1
%K5init

Group: Graphical desktop/KDE
Summary: Certificate Manager for KDE
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Provides: kde5-pim-kleopatra = %EVR
Obsoletes: kde5-pim-kleopatra < %EVR
Requires: gnupg2 dirmngr pinentry-x11

Source: %rname-%version.tar

# Automatically added by buildreq on Fri Apr 29 2016 (-bi)
# optimized out: boost-devel-headers cmake cmake-modules docbook-dtds docbook-style-xsl elfutils gcc-c++ glibc-devel-static gtk-update-icon-cache kf5-kdoctools kf5-kdoctools-devel libEGL-devel libGL-devel libdbusmenu-qt52 libgpg-error libgpg-error-devel libjson-c libkf5gpgmepp-pthread libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-qml libqt5-quick libqt5-svg libqt5-test libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms perl python-base python-modules python3 python3-base qt5-base-devel rpm-build-python3 ruby ruby-stdlibs xml-common xml-utils
#BuildRequires: extra-cmake-modules kde5-gpgmepp-devel kde5-kmime-devel kde5-libkleo-devel kf5-kauth-devel kf5-kcmutils-devel kf5-kcodecs-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdoctools-devel-static kf5-ki18n-devel kf5-kiconthemes-devel kf5-knotifications-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-sonnet-devel libassuan-devel libgpgme-devel python-module-google python3-dev rpm-build-ruby
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules
BuildRequires: libassuan-devel libgpgme-devel
BuildRequires: kde5-gpgmepp-devel kde5-kmime-devel kde5-libkleo-devel kf5-kauth-devel kf5-kcmutils-devel kf5-kcodecs-devel kf5-kconfig-devel
BuildRequires: kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdoctools-devel-static
BuildRequires: kf5-ki18n-devel kf5-kiconthemes-devel kf5-knotifications-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kwidgetsaddons-devel
BuildRequires: kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-sonnet-devel

%description
%summary


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

%package -n %libkleopatraclientcore
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkleopatraclientcore
KF5 library

%package -n %libkleopatraclientgui
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkleopatraclientgui
KF5 library

%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%K5install_move data kleopatra kwatchgnupg kconf_update
%find_lang %name --with-kde --all-name

%files common -f %name.lang
#%doc COPYING*

%files
%config(noreplace) %_K5xdgconf/kleopatra.categories
%_K5bin/kleopatra
%_K5xdgapp/org.kde.kleopatra.desktop
%_K5xdgapp/kleopatra_import.desktop
%_K5data/kleopatra/
%_K5cf_upd/*kleopatra*
%_K5plug/kcm_kleopatra.so
%_K5srv/kleopatra_*.desktop
%_K5icon/*/*/apps/kleopatra.*
#
%_K5bin/kwatchgnupg
%_K5data/kwatchgnupg/

%files -n %libkleopatraclientcore
%_K5lib/libkleopatraclientcore.so.%kleopatraclientcore_sover
%_K5lib/libkleopatraclientcore.so.*
%files -n %libkleopatraclientgui
%_K5lib/libkleopatraclientgui.so.%kleopatraclientgui_sover
%_K5lib/libkleopatraclientgui.so.*

%changelog
* Wed Jul 13 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.3-alt1
- new version

* Thu Jun 30 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.2-alt1
- new version

* Tue May 10 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.1-alt1
- new version

* Wed Apr 27 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.0-alt1
- initial build
