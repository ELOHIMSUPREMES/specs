
%global qt_module qtgraphicaleffects

Name: qt5-graphicaleffects
Version: 5.3.1
Release: alt1

Group: System/Libraries
Summary: Qt5 - QtGraphicalEffects component
Url: http://qt-project.org/
License: LGPLv2 / GPLv3

Requires: %name-common = %EVR
#Requires: libqt5-quick

Source: %qt_module-opensource-src-%version.tar

# Automatically added by buildreq on Wed Jun 04 2014 (-bi)
# optimized out: libqt5-clucene libqt5-core libqt5-gui libqt5-help libqt5-network libqt5-sql libqt5-widgets libqt5-xml python-base qt5-base-devel qt5-declarative-devel qt5-tools
#BuildRequires: qt5-script-devel qt5-tools-devel qt5-webkit-devel qt5-xmlpatterns-devel ruby ruby-stdlibs
BuildRequires: gcc-c++ glibc-devel qt5-base-devel qt5-tools

%description
The Qt Graphical Effects module provides a set of QML types for adding
visually impressive and configurable effects to user interfaces. Effects
are visual items that can be added to Qt Quick user interface as UI
components.

%package common
Summary: Common package for %name
Group: System/Configuration/Other
BuildArch: noarch
Requires: qt5-base-common
%description common
Common package for %name

%package doc
BuildArch: noarch
Summary: Document for developing apps which will use Qt5 %qt_module
Group: Development/KDE and QT
Requires: %name-common = %EVR
%description doc
This package contains documentation for Qt5 %qt_module

%prep
%setup -qn %qt_module-opensource-src-%version

%build
%qmake_qt5
%make_build
%make docs

%install
%install_qt5
%make INSTALL_ROOT=%buildroot install_docs ||:

%files common
%files
%doc LGPL_EXCEPTION.txt
%_qt5_archdatadir/qml/QtGraphicalEffects/

%files doc
%_qt5_docdir/*

%changelog
* Thu Jun 26 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt1
- new version

* Wed Jun 04 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt1
- initial build
