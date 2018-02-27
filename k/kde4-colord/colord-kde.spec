%define _kde_alternate_placement 1

%define rname colord-kde
Name: kde4-colord
Version: 0.3.0
Release: alt1

Group: Graphical desktop/KDE
Summary: Colord support for KDE
Url: http://www.kde.org/
License: GPLv2+

Requires: colord

Source: %rname-%version.tar

# Automatically added by buildreq on Wed Nov 28 2012 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-svg libqt4-xml libsoprano-devel libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base ruby xorg-kbproto-devel xorg-randrproto-devel xorg-renderproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel iceauth kde4libs-devel libXxf86misc-devel libicu liblcms2-devel libqt3-devel python-module-distribute rpm-build-ruby zlib-devel-static
BuildRequires: gcc-c++ kde4libs-devel liblcms2-devel kde-common-devel


%description
KDE support for colord including KDE Daemon module and System Settings module.

%prep
%setup -qn %rname-%version

%build
%K4build

%install
%K4install

%files
%doc MAINTAINERS TODO
%_kde4_bindir/colord-kde-icc-importer
%_kde4_xdg_apps/colordkdeiccimporter.desktop
%_K4lib/*_colord.so
%_K4srv/*_colord.desktop
%_K4srv/kded/*colord.desktop

%changelog
* Thu Aug 01 2013 Sergey V Turchin <zerg@altlinux.org> 0.3.0-alt1
- new version

* Wed Nov 28 2012 Sergey V Turchin <zerg@altlinux.org> 0.2.0-alt1
- initial build
