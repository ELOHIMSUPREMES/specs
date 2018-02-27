%define _kde_alternate_placement 1

%define rname nepomuk-core
Name: kde4-nepomuk-core
%define major  4
%define minor  11
%define bugfix 3
Version: %major.%minor.%bugfix
Release: alt2
%define sover %major

Group: Graphical desktop/KDE
Summary: Nepomuk Server and core services
Url: http://kde.org/
License: LGPLv2+

Requires: %name-common = %EVR
Requires: libnepomukcore4 = %EVR
Requires: soprano soprano-backend-redland soprano-backend-virtuoso

Source: %rname-%version.tar
# ALT
Patch1: kdebase-runtime-4.8.0-alt-def-nepomuk.patch
Patch2: nepomuk-core-4.10.0-alt-nepomuk-backup-on.patch
Patch3: nepomuk-core-4.9.1-alt-ontology-dir.patch

# Automatically added by buildreq on Wed Sep 26 2012 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-svg libqt4-test libqt4-xml libsoprano-devel libssl-devel libstdc++-devel libstrigi-devel libxkbfile-devel phonon-devel pkg-config python-base rpm-build-gir ruby shared-desktop-ontologies shared-desktop-ontologies-devel soprano-backend-redland soprano-backend-virtuoso xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: doxygen gcc-c++ glib2-devel graphviz kde4libs-devel libicu libqt3-devel python-module-distribute rpm-build-ruby soprano zlib-devel-static
BuildRequires: gcc-c++ glib2-devel kde4libs-devel
#BuildRequires: doxygen graphviz
BuildRequires: soprano-backend-redland soprano-backend-virtuoso soprano shared-desktop-ontologies-devel
BuildRequires: libtag-devel libpoppler-qt4-devel libexiv2-devel ebook-tools-devel
BuildRequires: libavcodec-devel libavformat-devel libavdevice-devel libavutil-devel
BuildRequires: libswscale-devel libpostproc-devel
BuildRequires: kde-common-devel

%description
This package contains Nepomuk Server providing Storage services, strigi controlling,
file indexer service, monitoring file changes.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common >= %major.%minor
Conflicts: kde4base-runtime-common < 4.9
%description common
%name common package

%package -n libnepomukextractor4
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %version-%release
%description -n libnepomukextractor4
%name library

%package -n libnepomukcleaner4
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %version-%release
%description -n libnepomukcleaner4
%name library

%package -n libnepomukcore4
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %version-%release
%description -n libnepomukcore4
%name library

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: kde4libs-devel
Requires: %name-common >= %version-%release
Requires: libnepomukextractor4 = %EVR
%description devel
Development files for %name


%prep
%setup -qn %rname-%version
%patch1 -p2
%patch2 -p1
%patch3 -p1

sed -i 's|^\(include.*KDE4Defaults.*\)|\1\ninclude(SopranoAddOntology)|' CMakeLists.txt


%build
%K4build


%install
%K4install

# fix paths in ontology descriptions
find %buildroot/%_datadir/ontology -type f -name \*.ontology | \
while read f
do
    sed -i 's|Path=.*/share/ontology/\(.*\.trig\)|Path=%_datadir/ontology/\1|' "$f"
done


%files
%_kde4_bindir/nepomuk*
%_K4exec/kde_nepomuk_filewatch_raiselimit
%_K4libdir/libkdeinit4_nepomukserver.so
%_K4libdir/libnepomukcommon.so
%_K4lib/nepomuk*.so
%_kde4_xdg_apps/nepomuk*.desktop
%_K4apps/fileindexerservice/
%_K4apps/nepomukfilewatch/
%_K4apps/nepomukstorage/
%_K4start/nepomukserver.desktop
%_K4srv/nepomuk*.desktop
%_K4srvtyp/nepomuk*.desktop
%_K4dbus_system/org.kde.nepomuk.filewatch.conf
%_K4dbus_sys_services/org.kde.nepomuk.filewatch.service
%_datadir/polkit-1/actions/org.kde.nepomuk.filewatch.policy

%files common
%dir %_datadir/ontology/kde/
%_datadir/ontology/kde/*

%files -n libnepomukextractor4
%_K4libdir/libnepomukextractor.so

%files -n libnepomukcleaner4
%_K4libdir/libnepomukcleaner.so.*

%files -n libnepomukcore4
%_K4libdir/libnepomukcore.so.*

%files devel
%_K4dbus_interfaces/org.kde.*
%_libdir/cmake/NepomukCore/
#%_libdir/pkgconfig/*
%_K4includedir/*
%_K4link/*.so

%changelog
* Fri Dec 06 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.3-alt2
- rebuild with new exiv2

* Thu Nov 07 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.3-alt0.M70P.1
- built for M70P

* Tue Nov 05 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.3-alt1
- new version

* Fri Oct 04 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.2-alt0.M70P.1
- built for M70P

* Tue Oct 01 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.2-alt1
- new version

* Tue Sep 03 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.1-alt1
- new version

* Mon Jul 01 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.5-alt1
- new version

* Fri Jun 28 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.4-alt2
- require soprano

* Mon Jun 03 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.4-alt1
- new version

* Thu May 16 2013 Sergey V Turchin <zerg at altlinux dot org> 4.10.3-alt2
- fix paths in ontology descriptions

* Tue May 07 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.3-alt1
- new version

* Wed Apr 03 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.2-alt2
- new version

* Thu Mar 21 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.1-alt2
- update from 4.10 branch

* Wed Mar 13 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.1-alt1
- update from 4.10 branch

* Mon Feb 25 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt3
- update from 4.10 branch

* Mon Feb 04 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt2
- update from 4.10 branch

* Thu Jan 31 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt1
- update from 4.10 branch

* Tue Jan 29 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.9
- update from 4.10 branch

* Mon Jan 28 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.8
- update from 4.10 branch

* Fri Jan 25 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.7
- fix requires

* Thu Jan 24 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.6
- rebuilt whith new exiv2

* Wed Jan 16 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.5
- update from 4.10 branch

* Thu Jan 10 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.4
- update from 4.10 branch

* Wed Jan 09 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.3
- update from 4.10 branch

* Thu Dec 20 2012 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.2
- update from 4.10 branch

* Mon Dec 10 2012 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.1
- new beta version

* Wed Dec 05 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.4-alt1
- new version

* Wed Nov 07 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.3-alt1
- new version

* Fri Oct 12 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.2-alt1
- new version

* Wed Sep 26 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.1-alt1
- initial build
