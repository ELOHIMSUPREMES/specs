%def_disable zeitgeist

Name: qt5-phonon
Version: 4.8.1
Release: alt1

Group: Graphical desktop/KDE
Summary: KDE5 Multimedia Framework
Url: http://phonon.kde.org/
License: LGPLv2+

#Source: ftp://ftp.kde.org/pub/kde/stable/%name/%version/%name-%version.tar.bz2
Source: phonon-%version.tar
# ALT
Patch100: alt-no-rpath.patch
Patch101: alt-fix-install.patch

BuildRequires(pre): qt5-base-devel
BuildRequires: qt5-tools-devel qt5-quick1-devel
BuildRequires: libEGL-devel libGL-devel
BuildRequires: ImageMagick-tools automoc cmake gcc-c++
BuildRequires: libalsa-devel libpulseaudio-devel gst-plugins-devel
BuildRequires: kde-common-devel
%if_enabled zeitgeist
BuildRequires: libqzeitgeist-devel
%endif

%description
Phonon is the KDE5 Multimedia Framework

%package -n libphonon4qt5experimental
Group: System/Libraries
Summary: Phonon library
%description -n libphonon4qt5experimental
Phonon library.

%package -n libphonon4qt5
Group: System/Libraries
Summary: Phonon library
%description -n libphonon4qt5
Phonon library.

%package devel
Group: Development/KDE and QT
Summary: Header files and documentation for compiling Phonon applications
%description devel
This package includes the header files you will need to compile applications
with Phonon.


%prep
%setup -qn phonon-%version
%patch100 -p1
%patch101 -p1


%build
%Kcmake \
    -DPHONON_BUILD_PHONON4QT5:BOOL=ON \
    -DSHARE_INSTALL_PREFIX:PATH=%_datadir \
    -DPLUGIN_INSTALL_DIR:PATH=%_qt5_archdatadir \
    -DINCLUDE_INSTALL_DIR:PATH=%_includedir/phonon4qt5 \
    -DPHONON_INSTALL_QT_EXTENSIONS_INTO_SYSTEM_QT:BOOL=ON \
    #
%Kmake

%install
%Kinstall

mkdir -p %buildroot/%_qt5_plugindir/phonon_backend


%files -n libphonon4qt5experimental
%_libdir/libphonon4qt5experimental.so.*

%files -n libphonon4qt5
%dir %_qt5_plugindir/phonon_backend/
%_libdir/libphonon4qt5.so.*

%files devel
%_includedir/phonon4qt5
#%_includedir/KDE
%_libdir/libphonon4qt5.so
%_libdir/libphonon4qt5experimental.so
%dir %_datadir/phonon4qt5/
%_datadir/phonon4qt5/buildsystem/
%_libdir/cmake/phonon4qt5/
%_qt5_plugindir/designer/libphononwidgets.so
%_qt5_archdatadir/mkspecs/modules/qt_phonon4qt5.pri
%_pkgconfigdir/phonon4qt5.pc
%_datadir/dbus-1/interfaces/org.kde.Phonon4Qt5.AudioOutput.xml

%changelog
* Tue Oct 21 2014 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt1
- new version

* Mon Sep 15 2014 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt3
- fix cmake configs

* Fri Sep 12 2014 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt2
- fix install paths

* Fri Sep 12 2014 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt1
- new version

* Thu Aug 28 2014 Sergey V Turchin <zerg@altlinux.org> 4.7.80-alt0.M70P.1
- build for M70P

* Mon Aug 25 2014 Sergey V Turchin <zerg@altlinux.org> 4.7.80-alt1
- new version

* Fri Jun 27 2014 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt1
- initial build
