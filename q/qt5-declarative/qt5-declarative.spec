
%define qt_module qtdeclarative
%define gname qt5
%def_disable bootstrap

Name: qt5-declarative
Version: 5.2.1
Release: alt1

Group: System/Libraries
Summary: Qt5 - QtDeclarative component
Url: http://qt-project.org/
License: LGPLv2 / GPLv3

Source: %qt_module-opensource-src-%version.tar

BuildRequires: gcc-c++ glibc-devel qt5-base-devel
%if_disabled bootstrap
BuildRequires: qt5-tools
%endif

%description
%summary

%package common
Summary: Common package for %name
Group: System/Configuration/Other
Requires: qt5-base-common
%description common
Common package for %name

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common = %EVR
Requires: qt5-base-devel
%description devel
%summary.

%package devel-static
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common = %EVR
Requires: %name-devel
%description devel-static
%summary.

%package doc
BuildArch: noarch
Summary: Document for developing apps which will use Qt5 %qt_module
Group: Development/KDE and QT
Requires: %name-common = %EVR
%description doc
This package contains documentation for Qt5 %qt_module

%package -n libqt5-qml
Group: System/Libraries
Summary: Qt5 - library
Requires: %name-common = %EVR
Obsoletes: libqt5-v8 < %version-%release
%description -n libqt5-qml
%summary

%package -n libqt5-quick
Group: System/Libraries
Summary: Qt5 - library
Requires: %name-common = %EVR
%description -n libqt5-quick
%summary

%package -n libqt5-quickparticles
Group: System/Libraries
Summary: Qt5 - library
Requires: %name-common = %EVR
%description -n libqt5-quickparticles
%summary

%package -n libqt5-quicktest
Group: System/Libraries
Summary: Qt5 - library
Requires: %name-common = %EVR
%description -n libqt5-quicktest
%summary

%prep
%setup -n %qt_module-opensource-src-%version
syncqt.pl-qt5 \
    -version %version \
    -private \
    -module QtQml \
    -module QtQuick \
    -module QtQuickTest \
    -module QtQuickParticles \
    #

%build
%qmake_qt5
%make_build
%if_disabled bootstrap
%make docs
%endif


%install
%install_qt5
%if_disabled bootstrap
%make INSTALL_ROOT=%buildroot install_docs ||:
%endif


%files common
%doc LGPL_EXCEPTION.txt
%doc dist/changes*
%dir %_qt5_archdatadir/qml/
%dir %_qt5_archdatadir/qml/Qt/
%dir %_qt5_archdatadir/qml/Qt/labs/
%dir %_qt5_archdatadir/qml/QtQml/
%dir %_qt5_archdatadir/qml/QtQuick/

%files doc
%if_disabled bootstrap
%_qt5_docdir/*
%endif

%files -n libqt5-qml
%_qt5_libdir/libQt5Qml.so.*
%_qt5_archdatadir/qml/Qt/labs/folderlistmodel/
%_qt5_archdatadir/qml/Qt/labs/settings/
%_qt5_archdatadir/qml/QtQml/Models.2/
%_qt5_archdatadir/qml/QtQuick/LocalStorage/

%files -n libqt5-quick
%_qt5_libdir/libQt5Quick.so.*
%_qt5_plugindir/accessible/libqtaccessiblequick.so
%_qt5_plugindir/qmltooling/
%_qt5_archdatadir/qml/QtQuick.2/
%_qt5_archdatadir/qml/QtQuick/Dialogs/
%_qt5_archdatadir/qml/QtQuick/PrivateWidgets/
%_qt5_archdatadir/qml/QtQuick/Window.2/

%files -n libqt5-quickparticles
%_qt5_libdir/libQt5QuickParticles.so.*
%_qt5_archdatadir/qml/QtQuick/Particles.2/

%files -n libqt5-quicktest
%_qt5_libdir/libQt5QuickTest.so.*
%_qt5_archdatadir/qml/QtTest/

%files devel
%_bindir/qml*
%_qt5_bindir/qml*
%_qt5_libdir/libQt*.so
%_qt5_libdir/libQt*.prl
%_qt5_headerdir/Qt*/
%_qt5_archdatadir/mkspecs/modules/*.pri
%_libdir/cmake/Qt*/
%_pkgconfigdir/Qt?Qml.pc
%_pkgconfigdir/Qt?QuickParticles.pc
%_pkgconfigdir/Qt?Quick.pc
%_pkgconfigdir/Qt?QuickTest.pc

%files devel-static
%_qt5_libdir/libQt?*.a
%_pkgconfigdir/Qt?QmlDevTools.pc

%changelog
* Wed Feb 12 2014 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt1
- new version

* Tue Nov 26 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt1.M70P.2
- build docs

* Mon Nov 25 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt1.M70P.1
- built for M70P

* Thu Oct 24 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt2
- build docs

* Thu Sep 26 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt1
- initial build
