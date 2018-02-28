%define rname akonadi-contacts

Name: kde5-%rname
Version: 16.08.3
Release: alt1
%K5init

Group: System/Libraries
Summary: Contact Management in Akonadi
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Tue Aug 23 2016 (-bi)
# optimized out: cmake cmake-modules elfutils fontconfig gcc-c++ kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdesignerplugin-devel kf5-kdoctools kf5-kdoctools-devel kf5-kemoticons-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kparts-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libEGL-devel libGL-devel libgpg-error libical-devel libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-positioning libqt5-printsupport libqt5-qml libqt5-quick libqt5-script libqt5-sql libqt5-svg libqt5-test libqt5-webchannel libqt5-webengine libqt5-webenginecore libqt5-webenginewidgets libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms perl python-base python-modules python3 python3-base qt5-base-devel qt5-declarative-devel qt5-location-devel qt5-webchannel-devel rpm-build-python3 ruby ruby-stdlibs
#BuildRequires: boost-devel-headers extra-cmake-modules grantlee5-devel kde5-akonadi-devel kde5-akonadi-mime-devel kde5-kcalcore-devel kde5-kcontacts-devel kde5-kmime-devel kf5-kdelibs4support-devel kf5-kdoctools-devel-static kf5-kio-devel python-module-google python3-dev qt5-webengine-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5
BuildRequires: boost-devel extra-cmake-modules qt5-base-devel qt5-webengine-devel
BuildRequires: grantlee5-devel
BuildRequires: kde5-akonadi-devel kde5-akonadi-mime-devel kde5-kcalcore-devel kde5-kcontacts-devel kde5-kmime-devel
BuildRequires: kf5-kdelibs4support-devel kf5-kdoctools-devel-static kf5-kio-devel

%description
Libraries and daemons to implement Contact Management in Akonadi.

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

%package -n libkf5akonadicontact
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5akonadicontact
KF5 library


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%K5install_move data akonadicontact
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc COPYING*

%files devel
%_K5inc/akonadi-contact_version.h
%_K5inc/Akonadi/Contact/
%_K5inc/akonadi/contact/
%_K5link/lib*.so
%_K5lib/cmake/KF5AkonadiContact/
%_K5archdata/mkspecs/modules/qt_AkonadiContact.pri

%files -n libkf5akonadicontact
%_K5lib/libKF5AkonadiContact.so.*
%_K5plug/*akonadicontact*.so
%_K5srv/akonadi/contact/
%_K5srv/*akonadicontact*.desktop
#
%_datadir/akonadi5/contact/
%_K5data/akonadicontact/
%_K5srvtyp/*.desktop

%changelog
* Fri Nov 25 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.3-alt1
- new version

* Mon Sep 19 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.1-alt1
- new version

* Mon Sep 05 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.0-alt2
- update conflicts

* Mon Aug 22 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.0-alt1
- initial build
