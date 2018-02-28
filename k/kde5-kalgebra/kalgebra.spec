%define rname kalgebra

Name: kde5-%rname
Version: 15.12.2
Release: alt1
%K5init

Group: Education
Summary: Graph Calculator
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Wed Mar 30 2016 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils gcc-c++ gtk-update-icon-cache kf5-kdoctools kf5-kdoctools-devel libEGL-devel libGL-devel libgpg-error libgst-plugins1.0 libncurses-devel libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-opengl libqt5-positioning libqt5-printsupport libqt5-qml libqt5-quick libqt5-sensors libqt5-sql libqt5-svg libqt5-test libqt5-webchannel libqt5-webkit libqt5-webkitwidgets libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libtinfo-devel libxcbutil-keysyms python-base python-modules python3 qt5-base-devel qt5-declarative-devel rpm-build-python3 xml-common xml-utils
#BuildRequires: extra-cmake-modules kde5-analitza-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdelibs4support kf5-kdoctools-devel-static kf5-ki18n-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel libGLU-devel libreadline-devel python-module-google python3-base qt5-svg-devel qt5-webkit-devel ruby ruby-stdlibs
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules qt5-svg-devel qt5-webkit-devel
BuildRequires: libGLU-devel libreadline-devel
BuildRequires: kde5-analitza-devel
BuildRequires: kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel
BuildRequires: kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdelibs4support kf5-kdoctools-devel-static
BuildRequires: kf5-ki18n-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel
BuildRequires: kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel

%description
KAlgebra is an application that can replace your graphing calculator.
It has numerical, logical, symbolic, and analysis features that let you calculate
mathematical expressions on the console and graphically plot the results in 2D or 3D.
KAlgebra is rooted in the Mathematical Markup Language (MathML);
however, one does not need to know MathML to use KAlgebra.

%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%K5install_move data plasma kalgebramobile
%find_lang %name --with-kde --all-name

%files -f %name.lang
%_K5bin/*algebra*
%_K5data/kalgebramobile/
%_K5xdgapp/*algebra*.desktop
%_K5data/plasma/plasmoids/org.kde.graphsplasmoid/
%_K5srv/graphsplasmoid.desktop
%_datadir/katepart5/syntax/kalgebra.xml
%_K5icon/*/*/apps/*algebra.*

%changelog
* Thu Mar 17 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt1
- initial build
