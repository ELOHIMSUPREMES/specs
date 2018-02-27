
%define qt_module qtdeclarative
%define gname qt5
%def_disable bootstrap

Name: qt5-declarative
Version: 5.4.2
Release: alt1

Group: System/Libraries
Summary: Qt5 - QtDeclarative component
Url: http://qt-project.org/
License: LGPLv2 / GPLv3

Source: %qt_module-opensource-src-%version.tar

BuildRequires: gcc-c++ glibc-devel qt5-base-devel qt5-xmlpatterns-devel
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

%package -n libqt5-quickwidgets
Group: System/Libraries
Summary: Qt5 - library
Requires: %name-common = %EVR
%description -n libqt5-quickwidgets
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
    -module QtQuickWidgets \
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
%_qt5_archdatadir/qml/QtQml/StateMachine/
%_qt5_archdatadir/qml/QtQuick/LocalStorage/
%_qt5_archdatadir/qml/QtQuick/XmlListModel/

%files -n libqt5-quick
%_qt5_libdir/libQt5Quick.so.*
#%_qt5_plugindir/accessible/libqtaccessiblequick.so
%_qt5_plugindir/qmltooling/
%_qt5_archdatadir/qml/QtQuick.2/
#%_qt5_archdatadir/qml/QtQuick/Dialogs/
#%_qt5_archdatadir/qml/QtQuick/PrivateWidgets/
%_qt5_archdatadir/qml/QtQuick/Window.2/

%files -n libqt5-quickparticles
%_qt5_libdir/libQt5QuickParticles.so.*
%_qt5_archdatadir/qml/QtQuick/Particles.2/

%files -n libqt5-quicktest
%_qt5_libdir/libQt5QuickTest.so.*
%_qt5_archdatadir/qml/QtTest/

%files -n libqt5-quickwidgets
%_qt5_libdir/libQt5QuickWidgets.so.*

%files devel
%_bindir/qml*
%_qt5_bindir/qml*
%_qt5_libdir/libQt*.so
%_qt5_libdir/libQt*.prl
%_qt5_headerdir/Qt*/
%_qt5_archdatadir/mkspecs/modules/*.pri
%_libdir/cmake/Qt*/
%_pkgconfigdir/Qt?Qml.pc
%_pkgconfigdir/Qt?Quick*.pc

%files devel-static
%_qt5_libdir/libQt?QmlDevTools.a
%_pkgconfigdir/Qt?QmlDevTools.pc

%changelog
* Fri Jun 05 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.2-alt1
- new version

* Tue Feb 24 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.1-alt1
- new version

* Fri Dec 12 2014 Sergey V Turchin <zerg@altlinux.org> 5.4.0-alt1
- new version

* Tue Sep 16 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.2-alt1
- new version

* Fri Jun 27 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt0.M70P.1
- build for M70P

* Wed Jun 25 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt1
- new version

* Wed Jun 04 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt2
- build docs

* Mon Jun 02 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt1
- new version

* Thu Feb 27 2014 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt0.M70P.1
- built for M70P

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
