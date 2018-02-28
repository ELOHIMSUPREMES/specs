%define rname kio-extras

%define molletnetwork_sover 5
%define libmolletnetwork libmolletnetwork5%molletnetwork_sover

%def_enable exiv2

Name: kde5-%rname
Version: 15.08.2
Release: alt1
%K5init altplace

Group: Graphical desktop/KDE
Summary: KDE Workspace 5 additional kio-slaves
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Requires: %name-common = %version-%release
Requires: kf5-kio
Provides: kf5-kio-extras = %EVR
Obsoletes: kf5-kio-extras < %EVR

Source: %rname-%version.tar

# Automatically added by buildreq on Sat Mar 21 2015 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils glibc-devel-static ilmbase-devel kf5-attica-devel kf5-kdoctools-devel libEGL-devel libGL-devel libcloog-isl4 libdbusmenu-qt52 libgpg-error libjson-c libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-svg libqt5-test libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libstdc++-devel libxcbutil-keysyms pkg-config python-base qt5-base-devel ruby ruby-stdlibs samba-libs shared-mime-info xml-common xml-utils
#BuildRequires: extra-cmake-modules gcc-c++ kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdelibs4support-devel kf5-kdesignerplugin-devel kf5-kdnssd-devel kf5-kdoctools kf5-kdoctools-devel-static kf5-kemoticons-devel kf5-kglobalaccel-devel kf5-kguiaddons-devel kf5-khtml-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kjs-devel kf5-knotifications-devel kf5-kparts-devel kf5-kpty-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwallet-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libexiv2-devel libjpeg-devel libmtp-devel libopenslp-devel libsmbclient-devel libssh-devel openexr-devel python-module-google qt5-phonon-devel qt5-svg-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++ qt5-phonon-devel qt5-svg-devel
%if_enabled exiv2
BuildRequires: libexiv2-devel
%endif
BuildRequires: libjpeg-devel libmtp-devel libopenslp-devel libsmbclient-devel libssh-devel openexr-devel
BuildRequires: kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel
BuildRequires: kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel
BuildRequires: kf5-kdelibs4support kf5-kdelibs4support-devel
BuildRequires: kf5-kdesignerplugin-devel kf5-kdnssd-devel
BuildRequires: kf5-kdoctools kf5-kdoctools-devel-static
BuildRequires: kf5-kemoticons-devel kf5-kglobalaccel-devel kf5-kguiaddons-devel kf5-khtml-devel kf5-ki18n-devel
BuildRequires: kf5-kiconthemes-devel kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel
BuildRequires: kf5-kjobwidgets-devel kf5-kjs-devel kf5-knotifications-devel kf5-kparts-devel kf5-kpty-devel kf5-kservice-devel
BuildRequires: kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwallet-devel kf5-kwidgetsaddons-devel
BuildRequires: kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel

%description
Additional kio-slaves.

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

%package -n %libmolletnetwork
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libmolletnetwork
KF5 library


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install

%K5install_move data kio_bookmarks kio_desktop kio_docfilter kio_info konqsidebartng konqueror remoteview
%K5install_move data doc solid

# workaround against man compressor
rm -rf %buildroot/%_K5doc/*/kioslave5/man

%find_lang %name --with-kde --all-name

%files common -f %name.lang
#%doc COPYING.LIB README.md
%_K5xdgmime/*.xml

%files
%_K5plug/kf5/kio/*.so
%_K5plug/*.so
%_K5data/kio_*/
%_K5data/konqsidebartng
%_K5data/konqueror
%_K5data/remoteview
%_K5srv/*.desktop
%_K5srv/kded/*.desktop
%_K5srv/*.protocol
%_K5srvtyp/*.desktop
%_K5data/solid/actions/*.desktop
%_K5cfg/*.kcfg

%files devel
#%_K5inc/kio_version.h
#%_K5inc/KIO*/
#%_K5inc/kio/
#%_K5link/lib*.so
#%_K5lib/cmake/KF5KIO/
#%_K5archdata/mkspecs/modules/qt_KIO*.pri
%_K5dbus_iface/*.xml

%files -n %libmolletnetwork
%_K5lib/libmolletnetwork5.so.*
%_K5lib/libmolletnetwork5.so.%molletnetwork_sover

%changelog
* Wed Oct 14 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.2-alt1
- new version

* Wed Sep 16 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.1-alt1
- new version

* Thu Aug 20 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.0-alt1
- new version

* Wed Jul 01 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.2-alt1
- new version

* Fri May 29 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt1
- new version

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
