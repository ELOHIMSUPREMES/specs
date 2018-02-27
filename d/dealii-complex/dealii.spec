%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%define oname dealii
%define scalar_type complex
%define ldir %_libdir/petsc-%scalar_type

Name: %oname-%scalar_type
Version: 8.2
Release: alt1.pre.svn20140707.1
Summary: A Finite Element Differential Equations Analysis Library (%scalar_type scalars)
License: QPL v1.0
Group: Sciences/Mathematics
Url: http://www.dealii.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://svn.dealii.org/trunk/
Source: %name-%version.tar
Patch: %oname-8.2pre-alt-i586.patch

BuildPreReq: python-module-petsc-config zlib-devel
BuildPreReq: gcc-c++ doxygen graphviz %mpiimpl-devel libqt4-devel
BuildPreReq: libpetsc-%scalar_type-devel libslepc-%scalar_type-devel
BuildPreReq: libarprec-devel libnetcdf-mpi-devel libgsl-devel
BuildPreReq: libtbb-devel libopendx-devel libp4est-devel
BuildPreReq: libstratimikos10-devel libbelos10-devel librtop10-devel
BuildPreReq: libsacado10-devel libthyra10-devel libtrilinos10-devel
BuildPreReq: libmumps-devel libhypre-devel libsuitesparse-devel
BuildPreReq: chrpath rpm-macros-make boost-signals-devel
BuildPreReq: libnetcdf_c++-mpi-devel libdakota-devel cmake
BuildPreReq: libdakota-devel bzlib-devel libmuparser-devel
BuildPreReq: libsc-devel

Requires: lib%name = %version-%release

%description
deal.II is a C++ program library targeted at the computational solution
of partial differential equations using adaptive finite elements. It
uses state-of-the-art programming techniques to offer you a modern
interface to the complex data structures and algorithms required.

The main aim of deal.II is to enable rapid development of modern finite
element codes, using among other aspects adaptive meshes and a wide
array of tools classes often used in finite element program. Writing
such programs is a non-trivial task, and successful programs tend to
become very large and complex. We believe that this is best done using a
program library that takes care of the details of grid handling and
refinement, handling of degrees of freedom, input of meshes and output
of results in graphics formats, and the like. Likewise, support for
several space dimensions at once is included in a way such that programs
can be written independent of the space dimension without unreasonable
penalties on run-time and memory consumption.

%package devel-common
Summary: Development common files for deal.II (%scalar_type scalars)
Group: Development/C++
Conflicts: lib%name < %version-%release

%description devel-common
deal.II is a C++ program library targeted at the computational solution
of partial differential equations using adaptive finite elements. It
uses state-of-the-art programming techniques to offer you a modern
interface to the complex data structures and algorithms required.

This package contains development common files for deal.II.

%package data
Summary: Data files for deal.II (%scalar_type scalars)
Group: Sciences/Mathematics
Conflicts: lib%name < %version-%release

%description data
deal.II is a C++ program library targeted at the computational solution
of partial differential equations using adaptive finite elements. It
uses state-of-the-art programming techniques to offer you a modern
interface to the complex data structures and algorithms required.

This package contains data files for deal.II.

%package -n lib%name
Summary: Shared libraries of deal.II (%scalar_type scalars)
Group: System/Libraries
#Requires: %name-data = %version-%release

%description -n lib%name
deal.II is a C++ program library targeted at the computational solution
of partial differential equations using adaptive finite elements. It
uses state-of-the-art programming techniques to offer you a modern
interface to the complex data structures and algorithms required.

This package contains shared libraries of deal.II.

%package -n lib%name-devel
Summary: Development files of deal.II (%scalar_type scalars)
Group: Development/C++
Requires: lib%name = %version-%release
#Requires: %name-devel-common = %version-%release
Requires: libpetsc-%scalar_type-devel
Requires: libslepc-%scalar_type-devel
Requires: libtrilinos10-devel
Requires: libtbb-devel

%description -n lib%name-devel
deal.II is a C++ program library targeted at the computational solution
of partial differential equations using adaptive finite elements. It
uses state-of-the-art programming techniques to offer you a modern
interface to the complex data structures and algorithms required.

This package contains development files of deal.II.

%package -n lib%oname-devel-doc
Summary: Documentation and examples for deal.II
Group: Development/Documentation
BuildArch: noarch

%description -n lib%oname-devel-doc
deal.II is a C++ program library targeted at the computational solution
of partial differential equations using adaptive finite elements. It
uses state-of-the-art programming techniques to offer you a modern
interface to the complex data structures and algorithms required.

This package contains development documentation and examples for
deal.II.

%prep
%setup

%ifnarch x86_64
%patch -p2
%endif

rm -fR bundled/tbb* bundled/boost* bundled/umfpack
#sed -i 's|@PETSC_DIR@|%ldir|g' configure.in

TRILINOS_VERSION_MAJOR=$(rpm -q --queryformat="%{VERSION}" libtrilinos10 |sed 's|\([0-9]*\)\..*|\1|')
sed -i "s|@TRILINOS_VERSION_MAJOR@|$TRILINOS_VERSION_MAJOR|" \
	include/deal.II/base/config.h.in
TRILINOS_VERSION_MINOR=$(rpm -q --queryformat="%{VERSION}" libtrilinos10 |sed 's|[0-9]*\.\([0-9]*\).*|\1|')
sed -i "s|@TRILINOS_VERSION_MINOR@|$TRILINOS_VERSION_MINOR|" \
	include/deal.II/base/config.h.in
TRILINOS_VERSION_SUBMINOR=$(rpm -q --queryformat="%{VERSION}" libtrilinos10 |sed 's|[0-9]*\.[0-9]*\.\(.*\)|\1|')
sed -i "s|@TRILINOS_VERSION_SUBMINOR@|$TRILINOS_VERSION_SUBMINOR|" \
	include/deal.II/base/config.h.in
sed -i 's|@P4EST_VERSION_SUBMINOR@|0|' include/deal.II/base/config.h.in
sed -i 's|@P4EST_VERSION_PATCH@|0|' include/deal.II/base/config.h.in

%build
source %_bindir/petsc-%scalar_type.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"
export PATH=$PATH:%_qt4dir/bin
export MPIDIR=%mpidir

INCS="-I%_includedir/hypre -I%_includedir/gsl -I%_includedir/tbb"
DEFS="-DHAS_C99_TR1_CMATH -DDEAL_II_USE_EXTERNAL_BOOST"
%add_optflags $INCS $DEFS -fno-strict-aliasing -std=gnu99 -fpermissive %optflags_shared

cmake \
	-DCMAKE_BUILD_TYPE:STRING=Release \
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DBLAS_blas_LIBRARY:FILEPATH=%_libdir/libopenblas.so \
	-DCMAKE_STRIP:FILEPATH="/bin/echo" \
	-DDEAL_II_COMPONENT_DOCUMENTATION:BOOL=ON \
	-DDEAL_II_COMPONENT_PARAMETER_GUI:BOOL=ON \
	-DDEAL_II_CXX_FLAGS_RELEASE:STRING="%optflags" \
	-DDEAL_II_FORCE_BUNDLED_FUNCTIONPARSER:BOOL=ON \
	-DDEAL_II_WITH_LAPACK:BOOL=ON \
	-DDEAL_II_WITH_MPI:BOOL=ON \
	-DDEAL_II_WITH_MUMPS:BOOL=ON \
	-DDEAL_II_WITH_NETCDF:BOOL=ON \
	-DDEAL_II_WITH_P4EST:BOOL=ON \
	-DDEAL_II_WITH_PETSC:BOOL=ON \
	-DDEAL_II_WITH_SLEPC:BOOL=ON \
	-DDEAL_II_WITH_UMFPACK:BOOL=ON \
	-DHDF5_DIR:PATH=%mpidir \
	-DHDF5_INCLUDE_DIR:PATH=%mpidir/include \
	-DMPI_LIBRARY:FILEPATH=%mpidir/lib/libmpi.so \
	-DNETCDF_INCLUDE_DIR:PATH=%mpidir/include/netcdf \
	-DPETSC_DIR:PATH=%ldir \
	-DTrilinos_INCLUDE_DIRS:PATH=%_includedir \
	-DTrilinos_TPL_LIBRARIES:STRING="epetra;sacado;amesos;ifpack;aztecoo;teuchos" \
	-DTrilinos_PACKAGE_LIST:STRING="Amesos Epetra Ifpack AztecOO Sacado Teuchos" \
	.
%make_build VERBOSE=1

%install
source %_bindir/petsc-%scalar_type.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%makeinstall_std

install -d %buildroot%ldir/lib
install -d %buildroot%_docdir/%name
pushd %buildroot%prefix
mv bin include common cmake %buildroot%ldir/
mv lib/cmake lib/*.so* %buildroot%ldir/lib/
mv doc examples %buildroot%_docdir/%name/
popd

%files
%doc doc/license.html
%ldir/bin/*

#files devel-common
#ldir/include/*
#ldir/common

%files -n lib%name
%ldir/lib/*.so.*

%files -n lib%name-devel
%ldir/lib/*.so
%ldir/cmake
%ldir/lib/cmake
%ldir/include/*
%ldir/common

%if "%scalar_type" == "real"
%files -n lib%oname-devel-doc
%_docdir/%name
%endif

%changelog
* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 8.2-alt1.pre.svn20140707.1
- rebuild with boost 1.57.0

* Wed Jul 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 8.2-alt1.pre.svn20140707
- New snapshot

* Fri Jun 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 8.2-alt1.pre.svn20140626
- New snapshot

* Wed May 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 8.2-alt1.pre.svn20140527
- Version 8.2.pre

* Mon Nov 11 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 8.1-alt1.pre.svn20131111
- Version 8.1.pre

* Thu Jul 11 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 8.0-alt3.pre.svn20130617
- Rebuilt with new PETSc

* Thu Jun 27 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 8.0-alt2.pre.svn20130617
- Rebuilt with new libhdf5

* Tue Jun 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 8.0-alt1.pre.svn20130617
- Version 8.0.pre

* Thu May 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.3-alt4.pre.svn20130201
- Rebuilt with Trilinos 11.2.3

* Sun Feb 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.3-alt3.pre.svn20130201
- New snapshot

* Sun Oct 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.3-alt3.pre.svn20121027
- New snapshot

* Wed Oct 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.3-alt3.pre.svn20120904
- Rebuilt with gcc 4.7

* Tue Sep 25 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.3-alt2.pre.svn20120904
- Rebuilt with netcdf 4.2

* Wed Sep 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.3-alt1.pre.svn20120904
- Version 7.3

* Mon Aug 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.2-alt5.pre.svn20120813
- New snapshot

* Sat Jul 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.2-alt5.pre.svn20120224
- Changed native directory: %%_libexecdir/petsc-%scalar_type ->
  %%_libdir/petsc-%scalar_type

* Sat Jun 30 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.2-alt4.pre.svn20120224
- Rebuilt with OpenMPI 1.6

* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.2-alt3.pre.svn20120224
- Rebuilt with Boost 1.49.0

* Sat Feb 25 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.2-alt2.pre.svn20120224
- New snapshot

* Wed Feb 15 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.2-alt2.pre.svn20111204
- Rebuilt with Trilinos 10.10.0

* Wed Dec 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.2-alt1.pre.svn20111204
- Version 7.2.pre

* Thu Nov 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.1-alt1.pre.svn20110826.2
- Rebuilt with Trilinos 10.8.1

* Wed Aug 31 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.1-alt1.pre.svn20110826.1
- Fixed linking of library

* Sun Aug 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.1-alt1.pre.svn20110826
- New snapshot

* Tue Jul 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.1-alt1.pre.svn20110504.1
- Rebuilt with Boost 1.47.0

* Sun May 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.1-alt1.pre.svn20110504
- New snapshot

* Mon Apr 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.1-alt1.pre.svn20110331.3
- Rebuilt with libnetcdf7

* Thu Apr 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.1-alt1.pre.svn20110331.2
- Fixed permissions for libraries

* Tue Apr 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.1-alt1.pre.svn20110331.1
- Built with GotoBLAS2 instead of ATLAS

* Sat Apr 02 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.1-alt1.pre.svn20110331
- New snapshot
- Disabled debug libraries (we have debuginfo packages now)

* Wed Mar 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.1-alt1.pre.svn20110121.2
- Rebuilt with Boost 1.46.1

* Wed Mar 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.1-alt1.pre.svn20110121.1
- Fixed build by using internal Boost instead of system
- Rebuilt with debuginfo

* Thu Jan 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.1-alt1.pre.svn20110121
- Version 7.1.pre
- Added debug subpackages

* Sat Jan 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.4-alt1.pre.svn20101223
- Initial build for Sisyphus
