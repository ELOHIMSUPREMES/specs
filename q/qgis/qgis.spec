# WARNING: Rebuild QGIS whenever a new version of GRASS is shipped! Even though the soname might stay the same, it won't work anymore.
# http://hub.qgis.org/issues/5274

Name:    qgis
Version: 2.4.0
Release: alt2.git4dce5ec

Summary: A user friendly Open Source Geographic Information System
License: GPLv3+ with exceptions
Group:   Sciences/Geosciences
Url:     http://qgis.org/

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
# %%name-mapserver-httpd.conf
# %%name-mapserver-README.fedora

# Fix detection problem for GRASS libraries
Patch0: %name-2.4.0-grass.patch
Patch1: %name-ignore-bundled-modules.patch
Patch2: %name-2.4.0-qreal.patch
Patch3: %name-2.4.0-sip.patch

# Fix unresolved symbols in grass based libs
%set_verify_elf_method unresolved=relaxed

# Set proper libexec directory
%define _libexecdir %prefix/libexec

# TODO: Pyspatialite is included if you use the bundled libspatialite.
# Some plug-ins need it.
# The license is not totally clear, see:
# http://code.google.com/p/pyspatialite/issues/detail?id=3
# It also is sort of a fork of pysqlite, which is not elegant.

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: libexpat-devel
BuildRequires: libfcgi-devel
BuildRequires: flex bison
BuildRequires: libgdal-devel
BuildRequires: libgeos-devel
BuildRequires: grass-devel = 6.4.3
BuildRequires: libgsl-devel
BuildRequires: libspatialite-devel
BuildRequires: postgresql-devel
BuildRequires: libproj-devel
BuildRequires: python-module-PyQt4-devel
BuildRequires: txt2tags
BuildRequires: python-devel
BuildRequires: libqt4-devel
# Fail to build with Qt-Mobility. See http://hub.qgis.org/issues/7753
#BuildRequires: qt4-mobility-devel
BuildRequires: libqt4-webkit
BuildRequires: python-module-PyQwt-devel
BuildRequires: qextserialport-devel
BuildRequires: libqwtpolar-devel
BuildRequires: python-module-sip-devel >= 4.15
BuildRequires: spatialindex-devel
BuildRequires: libsqlite3-devel
BuildRequires: python-module-qscintilla2-qt4-devel
BuildRequires: libqscintilla2-qt4-devel
BuildRequires: python-module-OWSLib

Requires: gpsbabel

# We don't want to provide private Python extension libs
%add_findprov_skiplist %%python_sitelibdir/%%name/*.so 

%description
Geographic Information System (GIS) manages, analyzes, and displays
databases of geographic information. Quantum GIS (QGIS) supports shape
file viewing and editing, spatial data storage with PostgreSQL/PostGIS,
projection on-the-fly, map composition, and a number of other features
via a plugin interface. QGIS also supports display of various
geo-referenced raster and Digital Elevation Model (DEM) formats
including GeoTIFF, Arc/Info ASCII Grid, and USGS ASCII DEM.

%package devel
Summary: Development Libraries for the Quantum GIS
Group: Development/C
Requires: %name = %version-%release

%description devel
Development packages for Quantum GIS including the C header files.

%package grass 
Summary: GRASS Support Libraries for Quantum GIS
Group: Sciences/Geosciences
Requires: %name = %version-%release
Requires: grass
  
%description grass
GRASS plugin for Quantum GIS required to interface with the GRASS
system.

%package python 
Summary: Python integration and plug-ins for Quantum GIS
Group: Sciences/Geosciences
Requires: %name = %version-%release
Requires: python-module-gdal
Requires: python-module-qscintilla2-qt4
# SPI API >= 9.1
Requires: python-module-sip

%description python
Python integration and plug-ins for Quantum GIS.

%package mapserver 
Summary: FCGI based OGC web map server
Group: Sciences/Geosciences
Requires: %name = %version-%release
Requires: libfcgi

%description mapserver
This FastCGI OGC web map server implements OGC WMS 1.3.0 and 1.1.1.
The services are prepared as regular projects in QGIS. They're rendered
using the QGIS libraries. The server also supports SLD (Styled Layer
Descriptor) for styling. Sample configurations for Httpd and Lighttpd
are included.

Please refer to %name-mapserver-README for details!

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

# Delete bundled libs
rm -rf src/core/spatialite
rm -rf src/core/gps/qwtpolar
rm -rf src/core/gps/qextserialport

# TODO Don't build unsupported Python bindings
subst 's/^\(ADD_SUBDIRECTORY(otb)\)/#\1/' python/plugins/processing/algs/CMakeLists.txt
subst 's/^\(ADD_SUBDIRECTORY(saga)\)/#\1/' python/plugins/processing/algs/CMakeLists.txt
rm -rf python/plugins/processing/algs/{otb,saga}
subst 's/^\(.*OTBAlgorithmProvider\)/#\1/g' python/plugins/processing/core/Processing.py
subst 's/^\(.*SagaAlgorithmProvider\)/#\1/g' python/plugins/processing/core/Processing.py

%build
CFLAGS="${CFLAGS:-%optflags}"; export CFLAGS;
CXXFLAGS="${CXXFLAGS:-%optflags}"; export CXXFLAGS;
cmake \
	-DCMAKE_C_FLAGS_RELEASE:STRING="-DNDEBUG" \
	-DCMAKE_CXX_FLAGS_RELEASE:STRING="-DNDEBUG" \
	-DCMAKE_Fortran_FLAGS_RELEASE:STRING="-DNDEBUG" \
	-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
	-DCMAKE_INSTALL_PREFIX:PATH=%_prefix \
	-DINCLUDE_INSTALL_DIR:PATH=%_includedir \
	-DLIB_INSTALL_DIR:PATH=%_libdir \
	-DSYSCONF_INSTALL_DIR:PATH=%_sysconfdir \
	-DSHARE_INSTALL_PREFIX:PATH=%_datadir \
%if "%_lib" == "lib64"
	-DLIB_SUFFIX="64" \
%endif
	-DBUILD_SHARED_LIBS:BOOL=ON \
	-DCMAKE_SKIP_RPATH:BOOL=ON \
	-DQGIS_LIB_SUBDIR:PATH=%_lib \
	-DQGIS_MANUAL_SUBDIR:PATH=/share/man \
	-DQGIS_PLUGIN_SUBDIR:PATH=%_lib/%name \
	-DQGIS_CGIBIN_SUBDIR:PATH=%_libexecdir/%name \
	-DWITH_BINDINGS:BOOL=TRUE \
	-DGRASS_PREFIX:PATH=%_libdir/grass \
	-DWITH_MAPSERVER:BOOL=TRUE \
	-DBINDINGS_GLOBAL_INSTALL:BOOL=TRUE \
	-DGDAL_INCLUDE_DIR:PATH=%_includedir/gdal \
	-DGDAL_LIBRARY:PATH=%_libdir/libgdal.so \
	-DGEOS_LIBRARY:PATH=%_libdir/libgeos_c.so \
	-DENABLE_TESTS:BOOL=FALSE \
	-DWITH_INTERNAL_QWTPOLAR:BOOL=FALSE \
	-DWITH_INTERNAL_QEXTSERIALPORT:BOOL=FALSE \
	-DWITH_PYSPATIALITE:BOOL=FALSE \
	-DWITH_SPATIALITE:BOOL=TRUE \
	-DWITH_INTERNAL_SPATIALITE:BOOL=FALSE \
	-DQEXTSERIALPORT_LIBRARY:PATH=%_libdir/libqextserialport.so \
	-DQEXTSERIALPORT_INCLUDE_DIR:PATH=%_includedir/qt4/QtExtSerialPort \
	-DQWTPOLAR_INCLUDE_DIR:PATH=%_includedir/qwt \
	-DWITH_QTMOBILITY:BOOL=FALSE \
	-DWITH_TOUCH:BOOL=TRUE \
	.
%make_build

%install
%makeinstall_std

# Install desktop files
desktop-file-install --dir=%buildroot%_datadir/applications ./altlinux/%name.desktop
desktop-file-install --dir=%buildroot%_datadir/applications ./altlinux/qbrowser.desktop

# Install MIME type definitions
install -pd %buildroot%_datadir/mime/packages
install -pm0644 ./altlinux/%name.xml %buildroot%_datadir/mime/packages/%name.xml
install -pd %buildroot%_datadir/mimelnk/application
install -pt %buildroot%_datadir/mimelnk/application ./altlinux/mimelnk/*

# Install application and MIME icons
install -pd %buildroot%_datadir/pixmaps
install -pd %buildroot%_datadir/icons/hicolor/16x16/apps
install -pd %buildroot%_datadir/icons/hicolor/scalable/apps
install -pd %buildroot%_datadir/icons/hicolor/128x128/mimetypes
install -pm0644 \
	%buildroot%_datadir/%name/images/icons/%name-icon.png \
	%buildroot%_datadir/pixmaps/%name.png
install -pm0644 \
	images/icons/%name-icon-16x16.png \
	%buildroot%_datadir/icons/hicolor/16x16/apps/%name.png
install -pm0644 \
	images/icons/%{name}_icon.svg \
	%buildroot%_datadir/icons/hicolor/scalable/apps/%name.svg
install -pm0644 \
	%buildroot%_datadir/%name/images/icons/%name-mime-icon.png \
	%buildroot%_datadir/icons/hicolor/128x128/mimetypes/application-x-qgis-layer-settings.png
install -pm0644 \
	%buildroot%_datadir/%name/images/icons/%name-mime-icon.png \
	%buildroot%_datadir/icons/hicolor/128x128/mimetypes/application-x-qgis-project.png

# Packed by %%doc in mapserver, see qgis-mapserver-README
rm -f %buildroot%_libexecdir/%name/wms_metadata.xml
rm -f %buildroot%_libexecdir/%name/admin.sld

# Remove files packaged by doc
pushd %buildroot%_datadir/%name/doc
rm -f BUGS \
	CHANGELOG \
	CODING \
	COPYING \
	INSTALL \
	PROVENANCE \
	README
popd

# Fix Serbian locale names
mv %buildroot%_datadir/qgis/i18n/qgis_sr{_Cyrl,}.qm
mv %buildroot%_datadir/qgis/i18n/qgis_sr{_Latn,@latin}.qm
%find_lang %name --with-qt

%files -f %{name}.lang
#TODO: Encoding problem on the help page
# CONTRIBUTORS and AUTHORS are intended be viewed in the About-Box
# ChangeLog is 4 MB, therefore don't ship it
%doc BUGS NEWS CODING COPYING Exception_to_GPL_for_Qt.txt PROVENANCE README
# QGIS shows these files in the GUI
%_datadir/%name/doc

%dir %_datadir/%name/i18n/
%_libdir/lib%{name}_analysis.so.*
%_libdir/lib%{name}_core.so.*
%_libdir/lib%{name}_gui.so.*
%_libdir/lib%{name}sqlanyconnection.so.*
%_libdir/lib%{name}_networkanalysis.so.*
%_libdir/%name
%_bindir/%name
%_bindir/qbrowser
%doc %_man1dir/*
%dir %_datadir/%name/
%_datadir/mime/packages/%name.xml
%_datadir/pixmaps/%name.png
%_datadir/icons/hicolor/16x16/apps/%name.png
%_datadir/icons/hicolor/128x128/mimetypes/application-x-%name-project.png
%_datadir/icons/hicolor/128x128/mimetypes/application-x-%name-layer-settings.png
%_datadir/icons/hicolor/scalable/apps/%name.svg
%_datadir/applications/*.desktop
%_datadir/%name/images
%_datadir/%name/resources
%_datadir/%name/svg
%exclude %_libdir/libqgisgrass.so.*
%exclude %_libdir/%name/libgrassprovider.so
%exclude %_libdir/%name/libgrassrasterprovider.so
%exclude %_libdir/%name/libgrassplugin.so
%exclude %_libdir/%name/grass
%_datadir/mimelnk/application/*

%files devel
%_datadir/%name/FindQGIS.cmake
%_includedir/%name
%_libdir/lib%{name}*.so

%files grass
%_libdir/lib%{name}grass.so.*
%_libdir/%name/libgrassprovider.so
%_libdir/%name/libgrassrasterprovider.so
%_libdir/%name/libgrassplugin.so
%_libdir/%name/grass
%_datadir/%name/grass

%files python
%_libdir/libqgispython.so.*
%_datadir/%name/python
%python_sitelibdir/%name

%files mapserver
%doc ./src/mapserver/admin.sld ./src/mapserver/wms_metadata.xml ./altlinux/%{name}-mapserver-README ./altlinux/%name-mapserver-httpd.conf
%_libexecdir/%name

%changelog
* Thu Apr 16 2015 Yuri N. Sedunov <aris@altlinux.org> 2.4.0-alt2.git4dce5ec
- rebuilt with qwt-6.1.2/qwtpolar-1.1.1

* Tue Aug 26 2014 Andrey Cherepanov <cas@altlinux.org> 2.4.0-alt1.git4dce5ec
- New version 2.4.0 with update source to Git commit 4dce5ec
- Merge patchset with Fedora

* Mon Feb 24 2014 Andrey Cherepanov <cas@altlinux.org> 2.2.0-alt1
- New version

* Mon Jan 27 2014 Andrey Cherepanov <cas@altlinux.org> 2.0.1-alt1
- New version (ALT #27790)
- Fix Grass version to make breakage more visible

* Fri Dec 06 2013 Andrey Kolotov <qwest@altlinux.org> 1.8.0-alt1.1
- build fixed

* Fri Jun 07 2013 Ivan Ovcherenko <asdus@altlinux.org> 1.8.0-alt1
- New upstream release

* Fri Oct 19 2012 Ilya Mashkin <oddity@altlinux.ru> 1.7.4-alt2
- fix build 

* Thu Feb 23 2012 Ilya Mashkin <oddity@altlinux.ru> 1.7.4-alt1
- 1.7.4

* Tue Feb 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.3-alt1.1
- Rebuilt with libqwt6 instead of libqwt

* Sun Dec 18 2011 Ilya Mashkin <oddity@altlinux.ru> 1.7.3-alt1
- 1.7.3

* Tue Dec 06 2011 Ilya Mashkin <oddity@altlinux.ru> 1.7.2-alt1
- 1.7.2

* Fri Oct 28 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.7.1-alt1.1
- Rebuild with Python-2.7

* Thu Oct 06 2011 Ilya Mashkin <oddity@altlinux.ru> 1.7.1-alt1
- 1.7.1

* Wed Jun 22 2011 Ilya Mashkin <oddity@altlinux.ru> 1.7.0-alt1
- 1.7.0

* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.6.0-alt2.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for qgis

* Thu May 12 2011 Ilya Mashkin <oddity@altlinux.ru> 1.6.0-alt2
- fix build (Patch3)

* Wed Dec 22 2010 Ilya Mashkin <oddity@altlinux.ru> 1.6.0-alt1
- 1.6.0
- without grass

* Sun Dec 28 2008 Vitaly Lipatov <lav@altlinux.ru> 0.11.0-alt2
- fix build on x86_64
- cleanup spec, move libqgisgrass to qgis-grass package

* Sat Nov 29 2008 Vitaly Lipatov <lav@altlinux.ru> 0.11.0-alt1
- new version 0.11.0 (with rpmrb script)

* Sun Feb 03 2008 Vitaly Lipatov <lav@altlinux.ru> 0.9.1-alt1
- initial build for ALT Linux Sisyphus

* Mon Jan 28 2008 Douglas E. Warner <silfreed@silfreed.net> 0.9.1-2
- defining lib path in build
- installing python bindings globally
- adding patch to determine python site packages dir correctly

* Mon Dec 17 2007 Douglas E. Warner <silfreed@silfreed.net> 0.9.1-1
- update to 0.9.1
- removing lib64 and man instal path patches (included upstream)
- enabling python integration

* Fri Oct 05 2007 Douglas E. Warner <silfreed@silfreed.net> 0.9.0-2
- enabling build for PPC64 (bug#247152)

* Wed Sep 26 2007 Douglas E. Warner <silfreed@silfreed.net> 0.9.0-1
- update to 0.9.0
- remove settings-include-workdir.patch
- updated man-install-share.patch to man-install-share-0.9.0.patch
- updated lib64-suffix.patch to lib64-suffix-0.9.0.patch
- enabled python to support msexport tool
- added Requires: grass to grass subpackage

* Tue Aug 28 2007 Douglas E. Warner <silfreed@silfreed.net> 0.8.1-13
- bump for expat 2.0 rebuild bug#195888

* Thu Aug 02 2007 Douglas E. Warner <silfreed@silfreed.net> 0.8.1-12
- updated License from GPL to GPLv2+

* Tue Jul 10 2007 Douglas E. Warner <silfreed@silfreed.net> 0.8.1-11
- allowing docs to be installed by qgis so they can be referenced by internal
  help system (bug#241403)
- updated lib64 patch (bug#247549) to try to get plugins found on x86_64

* Thu Jul 05 2007 Douglas E. Warner <silfreed@silfreed.net> 0.8.1-10
- updated lib64 patch for core and grass libraries

* Thu Jul 05 2007 Douglas E. Warner <silfreed@silfreed.net> 0.8.1-9
- updated lib64 patch

* Thu Jul 05 2007 Douglas E. Warner <silfreed@silfreed.net> 0.8.1-8
- adding ExcludeArch: ppc64 for bug#247152 (lrelease segfault)

* Thu Jul 05 2007 Douglas E. Warner <silfreed@silfreed.net> 0.8.1-7
- adding patch for lib64 support through lib_suffix

* Thu Jun 28 2007 Douglas E. Warner <silfreed@silfreed.net> 0.8.1-6
- fixed date of changelog entry for 0.8.1-5 from Wed Jun 27 2007 to
  Thu Jun 28 2007
- linking icon to included png instead of packaging it again

* Thu Jun 28 2007 Douglas E. Warner <silfreed@silfreed.net> 0.8.1-5
- adding comment on why grass is required in addition to grass-devel for BR
- fixing typo

* Wed Jun 27 2007 Douglas E. Warner <silfreed@silfreed.net> 0.8.1-4
- adding contributors to doc
- adding desktop file and icon

* Mon Jun 25 2007 Douglas E. Warner <silfreed@silfreed.net> 0.8.1-3
- updating detection of grass libraries to not use RPM call
- disabling building of -devel package due to shared libraries not being
  versioned and having no other packages that compile against qgis
  (see bug #241403)
- removing chmod of test_export.py due to lack of python requirement
- removing msexport and share/python directory due to removal of python

* Fri Jun 22 2007 Douglas E. Warner <silfreed@silfreed.net> 0.8.1-2
- added BuildRequires: cmake
- updated build to use cmake macro and make verbose

* Mon Jun 19 2007 Douglas E. Warner <silfreed@silfreed.net> 0.8.1-1
- updating version
- removed BuildRequires: python-devel due to lack of PyQt4 bindings
- updated build for use of cmake instead of autotools
- added patch for setting WORKDIR in settings.pro file
- added patch for fixing install path of man pages
- updated library names

* Tue May 29 2007 Douglas E. Warner <silfreed@silfreed.net> 0.8.0-6
- adding BuildRequires bison, flex

* Tue May 29 2007 Douglas E. Warner <silfreed@silfreed.net> 0.8.0-5
- fixing more directory owernship (themes, themes-default)
- fixing qt4 hardcoded lib path
- removing Requires ldconfig
- adding BuildRequires sqlite-devel
- adding patch for supporting python 2.5 in configure script

* Sat May 26 2007 Douglas E. Warner <silfreed@silfreed.net> 0.8.0-4
- moving all BuildRequires to main section
- dropping use of makeinstall macro
- making sure directories are owned by this package
- removing *.a and *.la files
- disabled stripping of libraries and binaries to allow debuginfo package
  to be built
- fixing macros in changelog
- removing executable bits on source files

* Wed May 16 2007 Douglas E. Warner <silfreed@silfreed.net> 0.8.0-3
- fixing Requires statements for sub-packages

* Tue May 15 2007 Douglas E. Warner <silfreed@silfreed.net> 0.8.0-2
- added devel dependancy on qgis
- moved qgis-config to devel package
- moving doc directory
- removed zero-length NEWS doc
- added postin/postun ldconfig calls
- split packages up to reduce package size and split out dependancies
  grass, theme-nkids

* Mon May 14 2007 Douglas E. Warner <silfreed@silfreed.net> 0.8.0-1
- Initial RPM release.

