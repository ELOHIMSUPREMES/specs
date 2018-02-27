%define rname ktp-auth-handler

Name: kde5-%rname
Version: 15.04.3
Release: alt1
%K5init altplace

Group: Graphical desktop/KDE
Summary: Provide UI/KWallet Telepathy Integration
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Requires: qca-qt5-ossl
Requires: signon-plugin-oauth2

Source: %rname-%version.tar

# Automatically added by buildreq on Wed Jun 17 2015 (-bi)
# optimized out: cmake cmake-modules elfutils libEGL-devel libGL-devel libaccounts-glib libaccounts-qt51 libdbusmenu-qt52 libgpg-error libjson-c libqca-qt5 libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-svg libqt5-webkit libqt5-webkitwidgets libqt5-widgets libqt5-x11extras libqt5-xml libsignon-qt51 libstdc++-devel libtelepathy-logger-qt5 libtelepathy-qt5 libtelepathy-qt5-devel libxcbutil-keysyms python-base python-module-google python3 python3-base qt5-base-devel qt5-webkit-devel telepathy-logger-qt5-devel
#BuildRequires: accounts-qt5-devel extra-cmake-modules gcc-c++ kde5-kaccounts-integration-devel kde5-ktp-common-internals-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdewebkit-devel kf5-ki18n-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwallet-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel libdb4-devel libqca-qt5-devel libtelepathy-qt5-devel-static rpm-build-python3 ruby ruby-stdlibs signon-devel
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++ qt5-base-devel
BuildRequires: accounts-qt5-devel libqca-qt5-devel libtelepathy-qt5-devel-static signon-devel
BuildRequires: kde5-kaccounts-integration-devel kde5-ktp-common-internals-devel
BuildRequires: kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel
BuildRequires: kf5-kdewebkit-devel kf5-ki18n-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwallet-devel
BuildRequires: kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel

%description
Provide UI/KWallet Integration For Passwords and SSL Errors on Account Connect

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

%package -n libkf5tp-auth-handler
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5tp-auth-handler
KF5 library


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%K5install_move exec all
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc COPYING*
%_K5exec/ktp-auth-handler
%_K5dbus_srv/org.freedesktop.Telepathy.Client.*.service
%_datadir/telepathy/clients/KTp.*.client

#%files devel
#%_K5inc/ktp-auth-handler_version.h
#%_K5inc/ktp-auth-handler/
#%_K5link/lib*.so
#%_K5lib/cmake/ktp-auth-handler
#%_K5archdata/mkspecs/modules/qt_ktp-auth-handler.pri

#%files -n libkf5tp-auth-handler
#%_K5lib/libktp-auth-handler.so.*

%changelog
* Thu Jul 09 2015 Sergey V Turchin <zerg@altlinux.org> 15.04.3-alt1
- new version

* Tue Apr 28 2015 Sergey V Turchin <zerg@altlinux.org> 15.4.2-alt0.1
- initial build
