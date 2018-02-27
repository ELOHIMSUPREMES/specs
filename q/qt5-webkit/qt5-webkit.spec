%add_verify_elf_skiplist %_qt5_libdir/libQt5WebKit.so.*
%add_verify_elf_skiplist %_qt5_libdir/libQt5WebKitWidgets.so.*

%define qt_module qtwebkit
%def_disable bootstrap

Name: qt5-webkit
Version: 5.4.2
Release: alt2

Group: System/Libraries
Summary: Qt5 - QtWebKit components
License: LGPLv2 / GPLv3
Url: http://qt-project.org/
Source: %qt_module-opensource-src-%version.tar

# FC
Patch1: qtwebkit-opensource-src-5.2.0-save_memory.patch
# ALT
Patch10: 5.2.1-alt-flags.patch

# Automatically added by buildreq on Mon Sep 30 2013 (-bi)
# optimized out: elfutils fontconfig glib2-devel glibc-devel-static gstreamer-devel libGL-devel libX11-devel libXfixes-devel libfreetype-devel libgst-plugins libqt5-core libqt5-gui libqt5-network libqt5-opengl libqt5-printsupport libqt5-qml libqt5-quick libqt5-sql libqt5-v8 libqt5-widgets libstdc++-devel libxml2-devel pkg-config python-base python-modules python-modules-compiler python-modules-encodings python-modules-xml python3 python3-base qt5-base-devel qt5-declarative-devel ruby ruby-stdlibs xorg-compositeproto-devel xorg-fixesproto-devel xorg-renderproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: flex fontconfig-devel gcc-c++ gperf gst-plugins-devel libXcomposite-devel libXext-devel libXrender-devel libgio-devel libicu-devel libjpeg-devel libpng-devel libsqlite3-devel libudev-devel libwebp-devel libxslt-devel perl-Term-ANSIColor python-module-distribute python-module-simplejson qt5-webkit-devel rpm-build-python3 rpm-build-ruby zlib-devel-static
BuildRequires: flex fontconfig-devel gcc-c++ libicu-devel libjpeg-devel libpng-devel
BuildRequires: libsqlite3-devel libudev-devel libwebp-devel libxslt-devel libpcre-devel gperf
BuildRequires: pkgconfig(glib-2.0) pkgconfig(gio-2.0) pkgconfig(gstreamer-1.0) pkgconfig(gstreamer-plugins-base-1.0) pkgconfig(gstreamer-app-1.0)
BuildRequires: libXcomposite-devel libXext-devel libXrender-devel libGL-devel
BuildRequires: python-module-distribute python-module-simplejson rpm-build-python
BuildRequires: rpm-build-ruby
BuildRequires: perl(Term/ANSIColor.pm) perl(Perl/Version.pm) perl(Digest/Perl/MD5.pm)
BuildRequires: zlib-devel
BuildRequires: qt5-base-devel qt5-declarative-devel
%if_disabled bootstrap
BuildRequires: qt5-tools
%endif

%description
%summary

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
Requires: qt5-declarative-devel
%description devel
%summary.

%package doc
Summary: Document for developing apps which will use Qt5 %qt_module
Group: Development/KDE and QT
BuildArch: noarch
Requires: %name-common = %EVR
%description doc
This package contains documentation for Qt5 %qt_module

%package -n libqt5-webkit
Group: System/Libraries
Summary: Qt5 library
Requires: %name-common = %EVR
%description -n libqt5-webkit
%summary

%package -n libqt5-webkitwidgets
Group: System/Libraries
Summary: Qt5 library
Requires: %name-common = %EVR
%description -n libqt5-webkitwidgets
%summary


%prep
%setup -n %qt_module-opensource-src-%version
%patch1 -p1 -b .save_memory
%patch10 -p1
syncqt.pl-qt5 \
    Source \
    -version %version \
    -private \
    -module QtWebKit \
    -module QtWebKitWidgets \
    #

# remove rpath
find ./ -type f -name \*.pr\* | \
while read f; do
    sed -i 's|\(^CONFIG[[:space:]][[:space:]]*+=[[:space:]].*\)rpath|\1|' $f
    sed -i 's|\([[:space:]]CONFIG[[:space:]][[:space:]]*+=[[:space:]].*\)rpath|\1|' $f
done

echo "nuke bundled code..."
# nuke bundled code
mkdir Source/ThirdParty/orig
mv Source/ThirdParty/{gtest/,qunit/} \
   Source/ThirdParty/orig/

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
%doc Source/WebCore/LICENSE*
%doc VERSION

%files doc
%if_disabled bootstrap
%_qt5_docdir/*
%endif

%files -n libqt5-webkit
%_qt5_libdir/libQt5WebKit.so.*
%_qt5_libexecdir/QtWebPluginProcess
%_qt5_archdatadir/qml/QtWebKit/

%files -n libqt5-webkitwidgets
%_qt5_libdir/libQt5WebKitWidgets.so.*
%_qt5_libexecdir/QtWebProcess

%files devel
%_qt5_headerdir/Qt*/
%_qt5_libdir/libQt*.so
%_qt5_libdir/libQt*.prl
%_qt5_libdir/cmake/Qt*/
%_qt5_archdatadir/mkspecs/modules/*.pri
%_pkgconfigdir/Qt*.pc

%changelog
* Tue Jun 09 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.2-alt2
- 5.4.2 release

* Fri Jun 05 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.2-alt1
- new version

* Tue Feb 24 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.1-alt1
- new version

* Fri Dec 12 2014 Sergey V Turchin <zerg@altlinux.org> 5.4.0-alt1
- new version

* Wed Oct 01 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.2-alt2
- build with gstreamer-1.0

* Wed Sep 17 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.2-alt1
- new version

* Fri Jun 27 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt0.M70P.1
- build for M70P

* Wed Jun 25 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt1
- new version

* Mon Jun 02 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt1
- new version

* Thu Feb 27 2014 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt0.M70P.1
- built for M70P

* Thu Feb 13 2014 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt1
- new version

* Tue Nov 26 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt1.M70P.2
- build docs

* Mon Nov 25 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt1.M70P.1
- built for M70P

* Fri Oct 25 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt2
- build docs

* Fri Sep 27 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt1
- initial build
