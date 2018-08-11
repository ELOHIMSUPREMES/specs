%define rname ring-kde

%define sover 7
%define libringclientkde libringclientkde%sover

Name: ring-client-kde5
Version: 2.3.0
Release: alt0.6%ubt
%K5init no_altplace

Group: Communications
Summary: Ring KDE Client
# https://projects.kde.org/projects/playground/pim/ring-kde/
Url: http://www.kde.org
License: GPLv2+

PreReq(post,preun): alternatives >= 0.2
Requires: ring-daemon

Source: %rname-%version.tar
Source1: add-po
Patch1: alt-add-translations.patch
Patch2: alt-dont-fetch.patch
Patch3: alt-fix-compile.patch

# Automatically added by buildreq on Mon Sep 05 2016 (-bi)
# optimized out: alternatives cmake cmake-modules elfutils gcc-c++ gtk-update-icon-cache kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdesignerplugin-devel kf5-kdoctools kf5-kdoctools-devel kf5-kemoticons-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kparts-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libEGL-devel libGL-devel libdbusmenu-qt52 libgpg-error libical-devel libjson-c libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-opengl libqt5-printsupport libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms perl python-base python-modules python3 python3-base qt5-base-devel rpm-build-python3
#BuildRequires: boost-devel-headers extra-cmake-modules kde5-akonadi-contacts-devel kde5-akonadi-devel kde5-kcalcore-devel kde5-kcontacts-devel kf5-kdelibs4support-devel kf5-kdoctools-devel-static kf5-kglobalaccel-devel kf5-kio-devel kf5-knotifyconfig-devel libGLU-devel libringclient-devel python-module-google python3-dev qt5-svg-devel ruby ruby-stdlibs
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: boost-devel-headers extra-cmake-modules qt5-svg-devel
BuildRequires: libGLU-devel
BuildRequires: libringclient-devel
BuildRequires: kde5-akonadi-contacts-devel kde5-akonadi-devel kde5-kcalcore-devel kde5-kcontacts-devel
BuildRequires: kf5-kdelibs4support-devel kf5-kdoctools-devel-static kf5-kglobalaccel-devel kf5-kio-devel kf5-knotifyconfig-devel

%description
Ring-KDE is a Qt based client for the Ring(www.ring.cx) daemon.

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.


%prep
%setup -n %rname-%version
%patch1 -p1
%patch2 -p1
%patch3 -p1

# add translations
mv .gear/po ./
cat %SOURCE1 >> CMakeLists.txt

%build
%K5build

%install
%K5install
%find_lang %name --with-kde --all-name

# install alternative
install -d %buildroot/%_sysconfdir/alternatives/packages.d
cat > %buildroot/%_sysconfdir/alternatives/packages.d/%name <<__EOF__
%_bindir/ring       %_K5bin/ring-kde      50
__EOF__


%files -f %name.lang
%doc COPYING* AUTHORS
%config /%_sysconfdir/alternatives/packages.d/%name
%_K5bin/ring-kde
%_datadir/ring-kde/
%_K5xdgapp/cx.ring.ring-kde.desktop
%_K5cfg/ring-kde.kcfg
%_K5xmlgui/ring-kde/
%_K5notif/ring-kde.notifyrc
%_K5icon/hicolor/*/apps/ring-kde.*

%files devel
%_K5dbus_iface/cx.ring.ring-kde.xml

%changelog
* Thu Jul 12 2018 Sergey V Turchin <zerg@altlinux.org> 2.3.0-alt0.6%ubt
- update russian translation

* Tue Jul 25 2017 Sergey V Turchin <zerg@altlinux.org> 2.3.0-alt0.5%ubt
- rebuild

* Mon Feb 27 2017 Sergey V Turchin <zerg@altlinux.org> 2.3.0-alt0.4%ubt
- update from master branch

* Mon Sep 05 2016 Sergey V Turchin <zerg@altlinux.org> 2.3.0-alt0.3
- update build requires

* Thu May 19 2016 Sergey V Turchin <zerg@altlinux.org> 2.3.0-alt0.2
- add translations

* Wed May 11 2016 Sergey V Turchin <zerg@altlinux.org> 2.3.0-alt0.1
- new version

* Wed Mar 16 2016 Sergey V Turchin <zerg@altlinux.org> 2.2.0-alt0.1
- initial build
