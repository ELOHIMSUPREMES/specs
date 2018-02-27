# TODO: enable system libtiff when it will support BigTiff (from 4.0?)
%def_without libtiff
%def_without geotiff
%def_with mysql
%def_with pg
%def_with sqlite
%def_with python3

Summary: The Geospatial Data Abstraction Library (GDAL)
Name: gdal
Version: 1.11.2
Release: alt1
Group: Sciences/Geosciences

License: MIT
URL: http://www.gdal.org/

Source: %name-%version.tar

Patch0: %name-1.7.1-alt-swig_python.patch
# Patch1: %name-1.7.1-alt-pydir.patch
Patch2: %name-1.7.1-alt-apps_install.patch
Patch3: %name-1.7.1-alt-inst_docs.patch
# Patch4: %name-1.8.0-alt-libpng15.patch
Patch5: %name-1.8.0-alt-libproj.so_name.patch
Patch6: %name-1.11.2-alt-python3.patch

%define libname lib%name

# Automatically added by buildreq on Thu Aug 12 2010
BuildRequires: doxygen gcc-c++ libMySQL-devel libcfitsio-devel libcurl-devel libexpat-devel libgeos-devel libgif-devel libhdf5-devel libjasper-devel libjpeg-devel libnumpy-devel libpng-devel libsqlite3-devel libunixODBC-devel libxerces-c28-devel perl-devel postgresql-devel python-module-BeautifulSoup python-module-genshi python-module-xlwt python-modules-ctypes swig

BuildPreReq: chrpath
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel libnumpy-py3-devel python3-module-genshi
BuildPreReq: python3-module-BeautifulSoup python3-module-xlwt-future
%endif

Requires: libproj

%description
The Geospatial Data Abstraction Library (GDAL) is a unifying
C/C++ API for accessing raster geospatial data, and currently
includes formats like GeoTIFF, Erdas Imagine, Arc/Info
Binary, CEOS, DTED, GXF, and SDTS. It is intended to provide
efficient access, suitable for use in viewer applications,
and also attempts to preserve coordinate systems and metadata.
Python, C, and C++ interfaces are available.

%package doc
Summary: Documentation for GDAL/OGR
Group: Documentation
BuildArch: noarch

%description doc
This package contains documentation for the GDAL/OGR library
and utilities.

%package scripts
Summary: Scripts for GDAL
Group: Sciences/Geosciences

%description scripts
This package contains various scripts for GDAL (written in python)

%package -n %libname
Summary: Libraries required for the GDAL library
Group: Sciences/Geosciences

%description -n %libname
Libraries required for the GDAL library

%package -n %libname-devel
Summary: Development files for using the GDAL library
Group: Development/C
Requires: %libname = %version-%release

%description -n lib%name-devel
Development files for using the GDAL library

%package -n python-module-%name
Summary: The Python bindings for the GDAL library
Group: Development/Python
Requires: %libname = %version
Requires: %name
Provides: python-module-osgeo = %version

%description -n python-module-%name
Python module for %name.

%if_with python3
%package -n python3-module-%name
Summary: The Python bindings for the GDAL library
Group: Development/Python3
Requires: %libname = %version
Requires: %name
Provides: python3-module-osgeo = %version

%description -n python3-module-%name
Python module for %name.
%endif

%package -n perl-Geo-GDAL
Summary: Perl bindings for the GDAL library
Group: Development/Perl
Requires: %libname = %version
Requires: %name

%description -n perl-Geo-GDAL
Perl modules for GDAL/OGR.

%prep
%setup
%patch0 -p1
# %patch1 -p2
%patch2 -p2
%patch3 -p2
# %patch4 -p2
%patch5 -p2
%patch6 -p2

%if_with python3
cp -fR swig/python swig/python3
find swig/python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%add_optflags -fno-strict-aliasing
%configure \
        --enable-static=no \
        --disable-rpath \
	--datadir=%_datadir/%name \
	--includedir=%_includedir/%name \
	--with-libz \
	--with-png \
%if_with libtiff
	--with-libtiff=yes \
%else
	--with-libtiff=internal \
%endif
%if_with geotiff
	--with-geotiff=yes \
%else
	--with-geotiff=internal \
%endif
	--with-gif \
	--with-jpeg \
	--with-ogr \
	--with-hdf5=%_libdir/hdf5-seq \
	--with-geos \
	--with-jasper\
	--with-odbc \
	--with-curl \
	%{subst_with mysql} \
	%{subst_with pg} \
	%{subst_with sqlite} \
	--with-python \
	--with-pythonlib=%python_libdir \
	--with-perl \
	--without-php \
	--without-ruby \
	--with-xerces \
	--with-xerces-inc=%_includedir/xercesc \
	--with-xerces-lib=%_libdir\
	--without-pcraster        \
	--with-threads
#	--with-grass=%_libdir/grass62 \

# Hack around the issue: https://trac.osgeo.org/gdal/ticket/3084
pushd swig/perl
%make_build veryclean
%make_build generate
popd

%make_build LD_RUN_PATH= lib-target
%make_build LD_RUN_PATH=
make docs
make -B man

%if_with python3
pushd swig/python3
%python3_build_debug
popd
%endif

%install
mkdir -p %buildroot%python_sitelibdir
%makeinstall_std PYTHONPATH=$PYTHONPATH:%buildroot%python_sitelibdir INSTALLDIRS=vendor
cp -a %buildroot%python_sitelibdir/GDAL*/osgeo %buildroot%python_sitelibdir/
make DESTDIR=%buildroot install-docs
make DESTDIR=%buildroot install-man
mv %buildroot/usr/man %buildroot/usr/share
install -p -m644 NEWS %buildroot%_docdir/%name
mkdir -p  %buildroot/%_libdir/perl5/
mv %buildroot/usr/lib/perl5/*-linux-thread-multi/* %buildroot/%_libdir/perl5/

for i in %buildroot%_bindir/*
do
	chrpath -d $i ||:
done

%if_with python3
pushd swig/python3
%python3_install
popd
%endif

%files
%_datadir/%name
%_bindir/ogr*
%_bindir/gdal*
%_bindir/testepsg
%_bindir/nearblack
%exclude %_bindir/gdal-config
%exclude %_bindir/*.dox
%exclude %_bindir/*.py
%_man1dir/*

%files doc
%_docdir/%name

%files scripts
%_bindir/*.py

%files -n %libname-devel
%_bindir/gdal-config
%_libdir/*.so
%_includedir/%name
%_pkgconfigdir/*

%files -n %libname
%_libdir/*.so.*

%files -n python-module-%name
%python_sitelibdir/*
#exclude %python_sitelibdir/[^o]*

%if_with python3
%files -n python3-module-%name
%python3_sitelibdir/*
%endif

%files -n perl-Geo-GDAL
%perl_vendor_archlib/Geo
%perl_vendor_autolib/Geo
# %exclude %perl_vendor_archlib/Geo/*.dox
# %exclude %perl_vendor_archlib/Geo/GDAL/*.dox

%changelog
* Sat Mar 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.11.2-alt1
- Version 1.11.2
- Added module for Python 3

* Wed Jan 21 2015 Dmitry Derjavin <dd@altlinux.org> 1.11.1-alt1
- 1.11.1;
- Perl module build Error 255 workaround.

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.10.1-alt3.1.1
- rebuild with new perl 5.20.1

* Wed Mar 26 2014 Sergey V Turchin <zerg@altlinux.org> 1.10.1-alt3.1
- NMU: rebuilt with new cfitsio

* Fri Jan 31 2014 Dmitry Derjavin <dd@altlinux.org> 1.10.1-alt3
- libproj: fixed hardcoded library path and dependency added

* Mon Jan 20 2014 Dmitry Derjavin <dd@altlinux.org> 1.10.1-alt2
- Static build disabled;
- accidentally disabled apps-install patch got back.

* Thu Jan 16 2014 Dmitry Derjavin <dd@altlinux.org> 1.10.1-alt1
- 1.10.1

* Fri Aug 30 2013 Vladimir Lettiev <crux@altlinux.ru> 1.8.0-alt4
- built for perl 5.18

* Tue Jul 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt3.1
- Rebuilt with new libhdf5

* Sun Jan 27 2013 Fr. Br. George <george@altlinux.ru> 1.8.0-alt3
- Move python module out of .egg directory (Closes: #26462)

* Fri Sep 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt2.1
- Rebuilt with libpng15

* Tue Sep 04 2012 Vladimir Lettiev <crux@altlinux.ru> 1.8.0-alt2
- rebuilt for perl-5.16

* Tue Jul 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt1.4
- Rebuilt with libhdf5-7-seq 1.8.8-alt2

* Mon Apr 16 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.8.0-alt1.3.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Feb 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt1.3
- Removed bad RPATH

* Mon Nov 07 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.8.0-alt1.2.1
- Rebuild with Python-2.7

* Sun Oct 16 2011 Alexey Tourbin <at@altlinux.ru> 1.8.0-alt1.2
- rebuilt for perl-5.14

* Thu Sep 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt1.1
- Rebuilt with libhdf5-7

* Fri Apr 15 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.8.0-alt1
- 1.8.0
- build fixed

* Fri Nov 05 2010 Vladimir Lettiev <crux@altlinux.ru> 1.7.1-alt3.1
- rebuilt with perl 5.12

* Thu Aug 12 2010 Egor Vyscrebentsov <evyscr@altlinux.org> 1.7.1-alt3
- packaged python scripts into subpackage (break circular dependencies)

* Mon Jun 07 2010 Egor Vyscrebentsov <evyscr@altlinux.org> 1.7.1-alt2
- packaged utils binaries, not wrappers (#23397)
- packaged docs and mans

* Wed Apr 22 2010 Egor Vyscrebentsov <evyscr@altlinux.org> 1.7.1-alt1
- new version: 1.7.1
- enabled perl bindings
- fixed python bindings

* Tue Nov 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.1-alt2.1
- Rebuilt with python 2.6

* Tue Jul 28 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1.6.1-alt2
- use %%python_sitelibdir instead of hardcoded path

* Tue Jul 14 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.6.1-alt1
- new version

* Mon Oct 27 2008 Andriy Stepanov <stanv@altlinux.ru> 1.5.3-alt0.M41.1
- M41

* Mon Oct 27 2008 Andriy Stepanov <stanv@altlinux.ru> 1.5.3-alt1
- New version

* Tue Aug 28 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1.1
- changes from Sir Raorn <raorn@altlinux.ru> 1.4.0-alt1.1:
-- Major spec cleanup
-- Packaged headers
-- Disabled perl/python/ruby in configure (not packaged by default)
-- Fixed Group

* Thu Jan 18 2007 Dmitri Kuzishchin <dim@altlinux.ru> 1.4.0-alt1
- Initial package.
