
%define qt_module qttools
%define gname qt5
%def_disable bootstrap
%def_disable qtconfig

Name: qt5-tools
Version: 5.5.0
Release: alt1

Group: System/Libraries
Summary: Qt5 - QtTool components
Url: http://qt-project.org/
License: LGPLv2 / GPLv3

Requires: %name-common = %EVR

Source: %qt_module-opensource-src-%version.tar

Source20: assistant.desktop
Source21: designer.desktop
Source22: linguist.desktop
Source23: qdbusviewer.desktop
Source24: qtconfig.desktop

Patch1: alt-build-qtconfig.patch

# Automatically added by buildreq on Tue Oct 01 2013 (-bi)
# optimized out: elfutils libGL-devel libgst-plugins libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-opengl libqt5-printsupport libqt5-qml libqt5-quick libqt5-sql libqt5-v8 libqt5-webkit libqt5-webkitwidgets libqt5-widgets libqt5-xml libstdc++-devel pkg-config python-base python3 python3-base qt5-base-devel qt5-declarative-devel ruby ruby-stdlibs
#BuildRequires: desktop-file-utils gcc-c++ glibc-devel-static python-module-distribute qt5-webkit-devel rpm-build-python3 rpm-build-ruby
BuildRequires: desktop-file-utils gcc-c++ glibc-devel libicu-devel /usr/bin/convert
BuildRequires: qt5-base-devel qt5-declarative-devel-static qt5-webkit-devel
BuildRequires: libXext-devel libX11-devel
#BuildRequires: gstreamer-devel gst-plugins-devel
BuildRequires: libxslt-devel libudev-devel libgio-devel libsqlite3-devel
%if_disabled bootstrap
BuildRequires: qt5-tools
%endif

%description
%summary.

%package common
Summary: Common package for %name
Group: System/Configuration/Other
BuildArch: noarch
Requires: qt5-base-common
%description common
Common package for %name

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common = %EVR
Requires: qt5-base-devel
Requires: %name
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
Summary: Document for developing apps which will use Qt5 %qt_module
Group: Development/KDE and QT
BuildArch: noarch
Requires: %name-common = %EVR
%description doc
This package contains documentation for Qt5 %qt_module

%package -n qt5-assistant
Group: Text tools
Summary: Documentation browser for Qt5
Requires: %name-common = %EVR
Requires: %name = %EVR
%description -n qt5-assistant
%summary.

%package -n qt5-designer
Group: Development/KDE and QT
Summary: Designer for the Qt5
Requires: %name-common = %EVR
Requires: %name = %EVR
Provides: qt5-linguist = %EVR
%description -n qt5-designer
%summary.

%package -n qt5-dbus
Group: System/Configuration/Other
Summary: This package contains D-Bus utilities for Qt5
Requires: %name-common = %EVR
%description -n qt5-dbus
This package contains D-Bus utilities for Qt5.

%package -n qt5-qtconfig
Group: System/Configuration/Other
Summary: A configuration tool for Qt5
Requires: %name-common = %EVR
%description -n qt5-qtconfig
This package contains a configuration tool for Qt5.

%package -n libqt5-uitools
Group: System/Libraries
Summary: Qt5 library
Requires: %name-common = %EVR
%description -n libqt5-uitools
%summary

%package -n libqt5-clucene
Group: System/Libraries
Summary: Qt5 library
Requires: %name-common = %EVR
%description -n libqt5-clucene
%summary

%package -n libqt5-designer
Group: System/Libraries
Summary: Qt5 library
Requires: %name-common = %EVR
%description -n libqt5-designer
%summary

%package -n libqt5-designercomponents
Group: System/Libraries
Summary: Qt5 library
Requires: %name-common = %EVR
%description -n libqt5-designercomponents
%summary

%package -n libqt5-help
Group: System/Libraries
Summary: Qt5 library
Requires: %name-common = %EVR
%description -n libqt5-help
%summary


%prep
%setup -n %qt_module-opensource-src-%version
%if_enabled qtconfig
%patch1 -p1
%endif
syncqt.pl-qt5 \
    -version %version \
    -private \
    -module QtCLucene \
    -module QtDesigner \
    -module QtDesignerComponents \
    -module QtHelp \
    -module QtUiPlugin \
    -module QtUiTools \
    #
%qmake_qt5


%build
%make_build
%if_disabled bootstrap
%make docs
%endif

%install
%install_qt5
%make INSTALL_ROOT=%buildroot install_docs

# fix pc-files
sed -i -e '/^Requires:/s/Qt5UiPlugin//' %buildroot/%_pkgconfigdir/*.pc

# Add desktop files
desktop-file-install \
  --dir=%buildroot/%_desktopdir \
  --vendor="qt5" \
  %SOURCE20 %SOURCE21 %SOURCE22 %SOURCE23 \
%if_enabled qtconfig
  %SOURCE24 \
%endif
  #

# icons
install -m644 -p -D src/assistant/assistant/images/assistant.png %buildroot/%_iconsdir/hicolor/32x32/apps/assistant-qt5.png
install -m644 -p -D src/assistant/assistant/images/assistant-128.png %buildroot/%_iconsdir/hicolor/128x128/apps/assistant-qt5.png
install -m644 -p -D src/designer/src/designer/images/designer.png %buildroot/%_iconsdir/hicolor/32x32/apps/designer-qt5.png
install -m644 -p -D src/qdbus/qdbusviewer/images/qdbusviewer.png %buildroot/%_iconsdir/hicolor/32x32/apps/qdbusviewer-qt5.png
install -m644 -p -D src/qdbus/qdbusviewer/images/qdbusviewer-128.png %buildroot/%_iconsdir/hicolor/128x128/apps/qdbusviewer-qt5.png
%if_enabled qtconfig
convert -resize 32x32 src/qtconfig/images/appicon.png %buildroot/%_iconsdir/hicolor/32x32/apps/qtconfig-qt5.png
%endif
# linguist icons
for icon in src/linguist/linguist/images/icons/linguist-*-32.png ; do
  size=$(echo $(basename ${icon}) | cut -d- -f2)
  install -p -m644 -D ${icon} %buildroot/%_iconsdir/hicolor/${size}x${size}/apps/linguist.png
done


%files common
%_qt5_datadir/phrasebooks/

%files
%_bindir/lconvert*
%_bindir/lrelease*
%_bindir/lupdate*
%_bindir/pixeltool*
%_bindir/qcollectiongenerator*
%_bindir/qhelpconverter*
%_bindir/qhelpgenerator*
%_bindir/qtpaths*
%_bindir/qtdiag*
%_bindir/qtplugininfo*
%_qt5_bindir/lconvert*
%_qt5_bindir/lrelease*
%_qt5_bindir/lupdate*
%_qt5_bindir/pixeltool*
%_qt5_bindir/qcollectiongenerator*
%_qt5_bindir/qhelpconverter*
%_qt5_bindir/qhelpgenerator*
%_qt5_bindir/qtpaths*
%_qt5_bindir/qtdiag*
%_qt5_bindir/qtplugininfo*

%if_enabled qtconfig
%files -n qt5-qtconfig
%_bindir/qtconfig-qt5
%_qt5_bindir/qtconfig
%_desktopdir/*qtconfig.desktop
%_iconsdir/hicolor/*/apps/qtconfig*.*
%endif

%files -n qt5-assistant
%_bindir/assistant-qt5
%_qt5_bindir/assistant
%_desktopdir/*assistant.desktop
%_iconsdir/hicolor/*/apps/assistant*.*
%if_disabled bootstrap
%_qt5_docdir/qtassistant/
%_qt5_docdir/qtassistant.qch
%endif

%files -n qt5-dbus
%_bindir/qdbus-qt5
%_qt5_bindir/qdbus
%_bindir/qdbusviewer*
%_qt5_bindir/qdbusviewer*
%_desktopdir/*qdbusviewer.desktop
%_iconsdir/hicolor/*/apps/qdbusviewer*.*

%files -n qt5-designer
%_bindir/designer*
%_bindir/linguist*
%_qt5_bindir/linguist*
%_qt5_bindir/designer*
%_qt5_plugindir/designer/lib*.so
%_desktopdir/*designer.desktop
%_desktopdir/*linguist.desktop
%_iconsdir/hicolor/*/apps/designer*.*
%_iconsdir/hicolor/*/apps/linguist*.*

%files devel
%_qt5_headerdir/QtCLucene/
%_qt5_headerdir/QtDesigner/
%_qt5_headerdir/QtDesignerComponents/
%_qt5_headerdir/QtHelp/
%_qt5_headerdir/QtUiTools/
%_qt5_headerdir/QtUiPlugin/
%_qt5_libdir/libQt*.prl
%_qt5_libdir/libQt*.so
%_qt5_libdir/pkgconfig/Qt*CLucene.pc
%_qt5_libdir/pkgconfig/Qt*DesignerComponents.pc
%_qt5_libdir/pkgconfig/Qt*Designer.pc
%_qt5_libdir/pkgconfig/Qt*Help.pc
%_qt5_archdatadir/mkspecs/modules/*.pri
%_libdir/cmake/Qt*/

%files devel-static
%_qt5_libdir/libQt?*.a
%_pkgconfigdir/Qt?UiTools.pc

%files doc
%if_disabled bootstrap
%_qt5_docdir/*
%exclude %_qt5_docdir/qtassistant/
%exclude %_qt5_docdir/qtassistant.qch
%endif

#%files -n libqt5-uitools
#%_qt5_libdir/libQt5UiTools.so.*
%files -n libqt5-clucene
%_qt5_libdir/libQt5CLucene.so.*
%files -n libqt5-designer
%_qt5_libdir/libQt5Designer.so.*
%files -n libqt5-designercomponents
%_qt5_libdir/libQt5DesignerComponents.so.*
%files -n libqt5-help
%_qt5_libdir/libQt5Help.so.*


%changelog
* Mon Jul 06 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt1
- new version

* Tue Jun 09 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.2-alt1
- new version

* Wed Feb 25 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.1-alt1
- new version

* Tue Dec 16 2014 Sergey V Turchin <zerg@altlinux.org> 5.4.0-alt1
- new version

* Wed Sep 17 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.2-alt1
- new version

* Fri Jun 27 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt0.M70P.1
- build for M70P

* Wed Jun 25 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt1
- new version

* Tue Jun 03 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt1
- new version

* Thu Feb 27 2014 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt0.M70P.1
- built for M70P

* Thu Feb 13 2014 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt1
- new version

* Wed Jan 29 2014 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt5.M70P.1
- built for M70P

* Wed Jan 29 2014 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt6
- fix cmake config file (ALT#29761)

* Tue Jan 28 2014 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt4.M70P.1
- built for M70P

* Tue Jan 28 2014 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt5
- fix paths in cmake config (ALT#29761)

* Tue Nov 26 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt3.M70P.2
- build docs

* Mon Nov 25 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt3.M70P.1
- built for M70P

* Thu Oct 31 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt4
- built qtconfig

* Fri Oct 25 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt3
- built docs

* Wed Oct 23 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt2
- move static libs to separate package

* Mon Sep 30 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt1
- initial build

