%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%set_automake_version 1.11

Name: netgen
Version: 5.3
Release: alt1.svn20140625
Summary: Automatic 3d tetrahedral mesh generator
License: LGPL
Group: Graphics
Url: http://www.hpfem.jku.at/netgen/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# svn://svn.code.sf.net/p/netgen-mesher/code/netgen
Source: %name-%version.tar
Source1: demoapp.tar
Source2: dropsexport.tar

Requires: lib%name = %version-%release tcl-tix
BuildRequires(pre): rpm-build-tcl
BuildPreReq: %mpiimpl-devel libjpeg-devel libavcodec-devel tcl-devel tk-devel
BuildPreReq: tcl-togl-devel libGL-devel libGLU-devel libparmetis-devel
BuildPreReq: libavformat-devel libswscale-devel bzlib-devel zlib-devel
BuildPreReq: libopencascade-devel
BuildPreReq: libXmu-devel chrpath

%description
NETGEN is an automatic 3d tetrahedral mesh generator. It accepts input
from constructive solid geometry (CSG) or boundary representation (BRep)
from STL file format. The connection to a geometry kernel allows the
handling of IGES and STEP files. NETGEN contains modules for mesh
optimization and hierarchical mesh refinement.

%package -n lib%name
Summary: Shared library of NETGEN
Group: System/Libraries

%description -n lib%name
NETGEN is an automatic 3d tetrahedral mesh generator. It accepts input
from constructive solid geometry (CSG) or boundary representation (BRep)
from STL file format. The connection to a geometry kernel allows the
handling of IGES and STEP files. NETGEN contains modules for mesh
optimization and hierarchical mesh refinement.

This package contains shared library of NETGEN.

%package -n lib%name-devel
Summary: Development files of NETGEN
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
NETGEN is an automatic 3d tetrahedral mesh generator. It accepts input
from constructive solid geometry (CSG) or boundary representation (BRep)
from STL file format. The connection to a geometry kernel allows the
handling of IGES and STEP files. NETGEN contains modules for mesh
optimization and hierarchical mesh refinement.

This package contains development files of NETGEN.

%package doc
Summary: Documentation for NETGEN
Group: Documentation
BuildArch: noarch

%description doc
NETGEN is an automatic 3d tetrahedral mesh generator. It accepts input
from constructive solid geometry (CSG) or boundary representation (BRep)
from STL file format. The connection to a geometry kernel allows the
handling of IGES and STEP files. NETGEN contains modules for mesh
optimization and hierarchical mesh refinement.

This package contains documentation for NETGEN.

%package tutorials
Summary: Tutorials for NETGEN
Group: Documentation
BuildArch: noarch

%description tutorials
NETGEN is an automatic 3d tetrahedral mesh generator. It accepts input
from constructive solid geometry (CSG) or boundary representation (BRep)
from STL file format. The connection to a geometry kernel allows the
handling of IGES and STEP files. NETGEN contains modules for mesh
optimization and hierarchical mesh refinement.

This package contains tutorials for NETGEN.

%package demo
Summary: Demo for NETGEN
Group: Graphics
BuildArch: noarch
Requires: %name = %version-%release

%description demo
NETGEN is an automatic 3d tetrahedral mesh generator. It accepts input
from constructive solid geometry (CSG) or boundary representation (BRep)
from STL file format. The connection to a geometry kernel allows the
handling of IGES and STEP files. NETGEN contains modules for mesh
optimization and hierarchical mesh refinement.

This package contains demo for NETGEN.

%prep
%setup
%ifarch x86_64
sed -i "s|@UINT64_C@|UL|" ng/ngpkg.cpp
%else
sed -i "s|@UINT64_C@|ULL|" ng/ngpkg.cpp
%endif

tar -xf %SOURCE1
tar -xf %SOURCE2

%build
mpi-selector --set %mpiimpl
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"
source %mpidir/bin/mpivars.sh
export MPIDIR=%mpidir

sed -i 's|@MPIDIR@|%mpidir|g' configure.ac
PARS="-DPARALLEL -DOMPI_IGNORE_CXX_SEEK -DMETIS -DHAVE_IOMANIP"
PARS="$PARS -DGLX_GLXEXT_PROTOTYPES -I%mpidir/include"
%add_optflags $PARS -DJPEGLIB -DFFMPEG -DHAVE_IOSTREAM -DHAVE_LIMITS

%autoreconf
%configure \
	--enable-occ \
	--enable-nglib \
	--enable-parallel \
	--enable-jpeglib \
	--enable-ffmpeg \
	--with-tcl=%_libdir \
	--with-togl=%_tcllibdir \
	--with-tk=%_libdir
#sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build TCLLIBDIR=%_tcllibdir
# for complete linking of libraries
for i in csg stlgeom meshing interface geom2d
do
	pushd libsrc/$i
	%make clean
	popd
	if [ "$i" == "csg" ]; then
		%make_build TCLLIBDIR=%_tcllibdir \
			NGLIB=$PWD/nglib/libnglib.la LIBNETGEN=$PWD/nglib/libnetgen.la \
			TOPDIR=$PWD
	else
		%make_build TCLLIBDIR=%_tcllibdir \
			NGLIB=$PWD/nglib/libnglib.la LIBNETGEN=$PWD/nglib/libnetgen.la \
			LIBCSG=$PWD/libsrc/csg/libcsg.la \
			TOPDIR=$PWD
	fi
done

%install
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"
export MPIDIR=%mpidir

install -d %buildroot%_libdir
cp -P nglib/.libs/*.so* libsrc/csg/.libs/*.so* %buildroot%_libdir/

%makeinstall_std TCLLIBDIR=%_tcllibdir TOPDIR=$PWD

pushd dropsexport
%autoreconf
%configure \
	--enable-static=no \
	--with-netgen=%buildroot \
	--with-netgensrc=$PWD/..
%make_build
%makeinstall_std
popd

for i in %buildroot%_libdir/*.so %buildroot%_bindir/*; do
	chrpath -r %mpidir/lib:%_tcllibdir $i ||:
done

%files
%doc AUTHORS
%_bindir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*

%files doc
%_docdir/%name

%files tutorials
%_datadir/%name

%files demo
%doc demoapp

%changelog
* Mon Jul 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.3-alt1.svn20140625
- New snapshot

* Thu Jun 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.3-alt1.svn20140428
- Version 5.3

* Wed Nov 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.2-alt3.svn20130902
- Fixed build

* Wed Sep 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.2-alt2.svn20130902
- Fixed build

* Thu Sep 12 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.2-alt1.svn20130902
- Version 5.2

* Fri Jul 05 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1-alt1.svn20130527
- New snapshot

* Wed Feb 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1-alt1.svn20130203
- Version 5.1

* Tue Aug 21 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.0-alt1.svn20120820
- Version 5.0

* Tue Jun 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.14-alt4.svn20120215
- Rebuilt with OpenMPI 1.6

* Mon May 21 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.14-alt3.svn20120215
- Fixed build

* Thu Mar 01 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.14-alt2.svn20120215
- New snapshot
- Built with OpenCASCADE

* Tue Dec 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.14-alt2.svn20111201
- New snapshot
- Rebuilt with libparmetis instead of libparmetis0

* Fri Nov 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.14-alt2.svn20111103
- New snapshot

* Wed Sep 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.14-alt2.svn20110725.1
- Rebuilt with libparmetis0 instead of libparmetis

* Mon Aug 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.14-alt2.svn20110725
- Version 4.9.14

* Sun May 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.13-alt2.svn20101017.4
- Built without OpenCASCADE (awaiting fix from upstream)

* Thu Mar 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.13-alt2.svn20101017.3
- Rebuilt for debuginfo

* Sat Feb 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.13-alt2.svn20101017.2
- Rebuilt with parmetis 3.1.1-alt10

* Mon Nov 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.13-alt2.svn20101017.1
- Rebuilt for soname set-versions

* Wed Oct 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.13-alt2.svn20101017
- New snapshot

* Tue Jul 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.13-alt2
- Rebuilt with reformed ParMetis

* Mon Jun 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.13-alt1
- Version 4.9.13
- Added demo

* Mon Mar 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.9-alt4
- Fixed build with modified OpenCascade headers

* Tue Dec 22 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.9-alt3
- Rebuilt with OpenCascade

* Mon Aug 31 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.9-alt2
- Rebuilt without OpenCascade

* Thu Aug 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.9-alt1
- Initial build for Sisyphus

