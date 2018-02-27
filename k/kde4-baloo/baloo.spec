%define _kde_alternate_placement 1

%define rname baloo
Name: kde4-baloo
Version: 4.13.1
Release: alt2

Group: Graphical desktop/KDE
Summary: A framework for searching and managing metadata
Url: https://projects.kde.org/projects/kde/kdelibs/baloo
License: GPLv2 / LGPLv2

Conflicts: kde4base-runtime-core < 4.12.90

Source: %rname-%version.tar
Patch1: alt-disable-indexing.patch
Patch2: alt-indexing-checkbox-up.patch

# Automatically added by buildreq on Tue Apr 29 2014 (-bi)
# optimized out: automoc boost-devel-headers cmake cmake-modules docbook-dtds docbook-style-xsl elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs kde4libs-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86vm-devel libakonadi4-calendar libakonadi4-contact libakonadi4-kabc libakonadi4-kcal libakonadi4-kde libakonadi4-kmime libakonadi4-notes libakonadi4-socialutils libakonadi4-xml libcloog-isl4 libdbus-devel libdbusmenu-qt2 libfreetype-devel libgpg-error libgpgmexx4-pthread libgst-plugins libpng-devel libqt4-core libqt4-dbus libqt4-declarative libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-script libqt4-sql libqt4-svg libqt4-test libqt4-uitools libqt4-webkit libqt4-xml libqt4-xmlpatterns libsoprano-devel libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base ruby ruby-stdlibs xml-common xml-utils xorg-kbproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: akonadi-devel gcc-c++ glib2-devel kde4-baloo kde4-kfilemetadata-devel kde4base-runtime-core kde4pimlibs-devel libxapian-devel python-module-protobuf qjson-devel qt4-designer rpm-build-ruby zlib-devel-static
BuildRequires: akonadi-devel gcc-c++ kde4-kfilemetadata-devel kde4pimlibs-devel libxapian-devel qjson-devel
BuildRequires: kde-common-devel

%description
%summary.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
%description common
%name common package


%package devel
Group: Development/KDE and QT
Summary: Developer files for %name
Requires: kde4libs-devel kde4-kfilemetadata-devel
%description devel
%summary.

%package -n libbaloocore4
Group: System/Libraries
Summary: %name library
Requires: %name-common = %EVR
%description -n libbaloocore4
%name library

%package -n libbaloofiles4
Group: System/Libraries
Summary: %name library
Requires: %name-common = %EVR
%description -n libbaloofiles4
%name library

%package -n libbaloopim4
Group: System/Libraries
Summary: %name library
Requires: %name-common = %EVR
%description -n libbaloopim4
%name library

%package -n libbalooxapian4
Group: System/Libraries
Summary: %name library
Requires: %name-common = %EVR
%description -n libbalooxapian4
%name library


%prep
%setup -qn %rname-%version
%patch1 -p1
%patch2 -p1


%build
%K4build


%install
%K4install


%files common
%files
%_sysconfdir/dbus-1/system.d/org.kde.baloo.filewatch.conf
%_kde4_bindir/akonadi_baloo_indexer
%_kde4_bindir/baloo_file
%_kde4_bindir/baloo_file_cleaner
%_kde4_bindir/baloo_file_extractor
%_kde4_bindir/balooctl
%_kde4_bindir/baloosearch
%_kde4_bindir/balooshow
%_K4exec/kde_baloo_filewatch_raiselimit
%_datadir/akonadi/agents/akonadibalooindexingagent.desktop
%_K4start/baloo_file.desktop
%_datadir/dbus-1/interfaces/org.kde.baloo.file.indexer.xml
%_datadir/dbus-1/system-services/org.kde.baloo.filewatch.service
%_kde4_iconsdir/hicolor/*/*/*.*
%_K4srv/baloo_contactsearchstore.desktop
%_K4srv/baloo_emailsearchstore.desktop
%_K4srv/baloo_filesearchstore.desktop
%_K4srv/baloo_notesearchstore.desktop
%_K4srv/baloosearch.protocol
%_K4srv/kcm_baloofile.desktop
%_K4srv/plasma-runner-baloosearch.desktop
%_K4srv/tags.protocol
%_K4srv/timeline.protocol
%_K4srvtyp/baloosearchstore.desktop
%_datadir/polkit-1/actions/org.kde.baloo.filewatch.policy
%_K4lib/akonadi/akonadi_baloo_searchplugin.so
%_K4lib/akonadi/akonadibaloosearchplugin.desktop
%_K4lib/baloo_contactsearchstore.so
%_K4lib/baloo_emailsearchstore.so
%_K4lib/baloo_filesearchstore.so
%_K4lib/baloo_notesearchstore.so
%_K4lib/kcm_baloofile.so
%_K4lib/kio_baloosearch.so
%_K4lib/kio_tags.so
%_K4lib/kio_timeline.so
%_K4lib/krunner_baloosearchrunner.so

%files devel
%_K4includedir/baloo/
%_K4link/lib*.so
%_K4libdir/cmake/Baloo/

%files -n libbaloocore4
%_K4libdir/libbaloocore.so.*
%files -n libbaloofiles4
%_K4libdir/libbaloofiles.so.*
%files -n libbaloopim4
%_K4libdir/libbaloopim.so.*
%files -n libbalooxapian4
%_K4libdir/libbalooxapian.so.*

%changelog
* Fri May 16 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.1-alt2
- disable indexing by default
- drop advanced configuration module

* Tue May 13 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.1-alt1
- new version

* Mon Apr 28 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.0-alt3
- add advanced configuration module

* Tue Apr 22 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.0-alt2
- fix requires

* Fri Apr 18 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.0-alt1
- initial build
