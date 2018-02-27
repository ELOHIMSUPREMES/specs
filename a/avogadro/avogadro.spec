
%define sover 1
%define sover_oq 0
%define libname libavogadro%sover
%define libname_openqube libavogadro-openqube%sover_oq

Name: avogadro
Version: 1.1.1
Release: alt1

Group: Sciences/Chemistry
Summary: An advanced molecular editor for chemical purposes
Url: http://avogadro.openmolecules.net/
License: GPLv2
Packager: Sergey V Turchin <zerg@altlinux.org>

Requires: %libname = %version-%release

Source: %name-%version.tar
# FC
Patch1: avogadro-1.0.3-mkspecs-dir.patch
Patch2: avogadro-1.0.3-no-strip.patch
Patch3: avogadro-1.1.1-pkgconfig_eigen.patch
# ALT
Patch100: avogadro-1.1.0-alt-config.patch
Patch101: avogadro-1.0.3-alt-desktopfile.patch

%setup_python_module Avogadro

# Automatically added by buildreq on Tue Feb 08 2011 (-bi)
#BuildRequires: boost-devel-headers boost-python-devel cmake docbook-utils eigen2 gcc-c++ libXScrnSaver-devel libXau-devel libXcomposite-devel libXdmcp-devel libXpm-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libglew-devel libnumpy-devel libopenbabel-devel libqt3-devel libxkbfile-devel openbabel python-module-numpy-testing python-module-sip-devel python-modules-ctypes qt4-designer rpm-build-ruby zlib-devel-static
BuildRequires: boost-devel-headers boost-python-devel cmake docbook-utils docbook-utils-print eigen2 gcc-c++
BuildRequires: libglew-devel libnumpy-devel libopenbabel-devel libqt4-devel
BuildRequires: openbabel libopenbabel-devel python-module-numpy-testing python-module-sip-devel python-modules-ctypes zlib-devel
BuildRequires: kde-common-devel

%description
An advanced molecular editor designed for cross-platform use
in computational chemistry,molecular modeling, bioinformatics,
materials science,and related areas, which offers flexible
rendering and a powerful plugin architecture.


%package -n %libname
Summary: Shared library for Avogadro
Group: System/Libraries
%description -n %libname
Library for Avogadro molecular editor.

%package -n %libname_openqube
Summary: Shared library for Avogadro
Group: System/Libraries
%description -n %libname_openqube
Library for Avogadro molecular editor.

%package devel
Summary: Development files for Avogadro
Group: Development/C++
Requires: %libname = %version-%release
%description devel
Development Avogadro files.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
#
%patch100 -p1
%patch101 -p1

rm -f cmake/modules/FindPythonLibs.cmake
sed -i 's|\${PYTHON_LIB_PATH}|%python_sitelibdir|g' libavogadro/src/python/CMakeLists.txt
#find -type f -name \*.h | \
#while read header_file
#do
#    sed -i 's|^\(#include <boost/python\.hpp>\)|#ifndef Q_MOC_RUN\n\1\n#endif|g' $header_file
#done

%build
%add_optflags -DPIC -fPIC -I%_includedir/eigen2
%Kcmake \
    -DENABLE_TESTS:BOOL=OFF \
    -DENABLE_RPATH:BOOL=OFF \
    -DENABLE_GLSL:BOOL=ON \
    -DENABLE_PYTHON:BOOL=ON \
    -DENABLE_VERSIONED_PLUGIN_DIR:BOOL=OFF \
    #
%Kmake

%install
%Kinstall

%files
%doc AUTHORS ChangeLog
%_bindir/%name
%_bindir/avopkg
%dir %_libdir/%name
%_libdir/%name/colors
%_libdir/%name/extensions
%_libdir/%name/engines
%_libdir/%name/tools
%_datadir/%name
%_datadir/lib%name
%_datadir/pixmaps/%name-icon.png
%_desktopdir/%name.desktop
%_mandir/man1/%name.1*
%_mandir/man1/avopkg.1*
%python_sitelibdir/Avogadro.so

%files -n %libname
%_libdir/libavogadro.so.%{sover}
%_libdir/libavogadro.so.%{sover}.*
%files -n %libname_openqube
%_libdir/libavogadro_OpenQube.so.%{sover_oq}
%_libdir/libavogadro_OpenQube.so.%{sover_oq}.*

%files devel
%_includedir/%name
%_pkgconfigdir/avogadro.pc
%_libdir/lib*.so
%_libdir/%name/*.cmake
%_libdir/%name/cmake
%_datadir/qt4/mkspecs/features/%name.prf

%changelog
* Fri Mar 21 2014 Sergey V Turchin <zerg@altlinux.org> 1.1.1-alt1
- new version

* Mon Apr 08 2013 Sergey V Turchin <zerg@altlinux.org> 1.1.0-alt1
- new version

* Wed Nov 28 2012 Sergey V Turchin <zerg@altlinux.org> 1.0.3-alt5
- rebuilt with new boost

* Thu Sep 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt4.1
- Rebuilt with Boost 1.51.0

* Mon Aug 20 2012 Sergey V Turchin <zerg@altlinux.org> 1.0.3-alt3.M60P.1
- built for M60P

* Mon Aug 20 2012 Sergey V Turchin <zerg@altlinux.org> 1.0.3-alt4
- fix desktopfile cetegories

* Wed Apr 04 2012 Sergey V Turchin <zerg@altlinux.org> 1.0.3-alt3
- rebuild with new boost

* Fri Dec 16 2011 Sergey V Turchin <zerg@altlinux.org> 1.0.3-alt2
- rebuilt with new openbabel

* Fri Dec 02 2011 Sergey V Turchin <zerg@altlinux.org> 1.0.3-alt1
- new version

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.1-alt3.1.1
- Rebuild with Python-2.7

* Fri Jul 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt3.1
- Rebuilt with Boost 1.47.0

* Thu Mar 24 2011 Sergey V Turchin <zerg@altlinux.org> 1.0.1-alt3
- rebuilt with new boost

* Wed Mar 02 2011 Sergey V Turchin <zerg@altlinux.org> 1.0.1-alt2
- fix to build

* Tue Feb 08 2011 Sergey V Turchin <zerg@altlinux.org> 1.0.1-alt1
- initial build
