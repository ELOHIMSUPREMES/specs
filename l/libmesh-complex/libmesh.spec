%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%define scalar_type complex
%define oname libmesh
%define ldir %_libdir/petsc-%scalar_type
Name: %oname-%scalar_type
Version: 0.9.2
%define blibdir %_builddir/%name-%version/lib/%_arch-alt-linux-gnu_opt
%define clibdir %_builddir/%name-%version/contrib/lib/%_arch-alt-linux-gnu_opt
Release: alt2.rc1.git20130711
Summary: Numerical simulation of partial differential equations
License: LGPL v2.1
Group: Sciences/Mathematics
Url: http://libmesh.sourceforge.net/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# git://github.com/libMesh/libmesh.git
Source: %oname-%version.tar

Requires: libslepc-%scalar_type

BuildPreReq: python-module-Pyro4 eigen3 liblaspack-devel
BuildPreReq: %mpiimpl-devel libscalapack-devel chrpath
BuildPreReq: liblapack-devel libX11-devel boost-devel
BuildPreReq: gcc-c++ gcc-fortran libpetsc-%scalar_type-devel libxdrfile-devel
BuildPreReq: libtau-devel libmpe2-devel libparpack-mpi-devel libarprec-devel
BuildPreReq: libslepc-%scalar_type-devel zlib-devel libxml2-devel
BuildPreReq: bzlib-devel libtetgen-devel libparmetis-devel libnetcdf-mpi-devel
BuildPreReq: libvtk-devel libtrilinos10-devel libnox10-devel libtaucs-devel
#BuildPreReq: doxygen graphviz texlive-latex-extra
BuildPreReq: doxygen graphviz
BuildPreReq: libfftw3-mpi-devel libexodusii-devel libparmetis0-devel
BuildPreReq: libgmp-devel libgmp_cxx-devel libblitz-devel getfemxx
BuildPreReq: libtbb-devel python-module-sphinx-devel python-module-Pygments
BuildPreReq: libglpk-devel libaztecoo10-devel libloca10-devel libbelos10-devel
BuildPreReq: librtop10-devel libthyra10-devel libtpetra10-devel libkokkos10-devel
BuildPreReq: libisorropia10-devel libadolc-devel libsparskit-devel
BuildPreReq: liboptika10-devel libctrilinos10-devel libpiro10-devel
BuildPreReq: libmesquite10-devel librythmos10-devel libSTK10-devel
BuildPreReq: libsacado10-devel libshards10-devel libglobipack10-devel
BuildPreReq: liboptipack10-devel libpliris10-devel libpamgen10-devel
BuildPreReq: libseacas10-devel libkomplex10-devel libdakota-devel
BuildPreReq: libfei10-devel libteko10-devel libtrikota10-devel
BuildPreReq: libintrepid10-devel libphalanx10-devel libmoertel10-devel
BuildPreReq: libstokhos10-devel liblaspack-devel libnetcdf_c++4-mpi-devel
BuildPreReq: libxpetra10-devel libmatio-devel

%description
The libMesh library provides a framework for the numerical simulation of
partial differential equations using arbitrary unstructured discretizations
on serial and parallel platforms. A major goal of the library is to provide
support for adaptive mesh refinement (AMR) computations in parallel while
allowing a research scientist to focus on the physics they are modeling.

libMesh currently supports 1D, 2D, and 3D steady and transient finite
element simulations. The library makes use of high-quality, existing
software whenever possible. PETSc is used for the solution of linear systems
on both serial and parallel platforms, and LASPack is included with the
library to provide linear solver support on serial machines. An optional
interface to SLEPc is also provided for solving both standard and
generalized eigenvalue problems.

%package devel
Summary: Development files of libMesh
Group: Development/C++
Requires: %name = %version-%release
Conflicts: %name-contrib-tools < %version-%release
Conflicts: %oname-complex-devel

%description devel
The libMesh library provides a framework for the numerical simulation of
partial differential equations using arbitrary unstructured discretizations
on serial and parallel platforms. A major goal of the library is to provide
support for adaptive mesh refinement (AMR) computations in parallel while
allowing a research scientist to focus on the physics they are modeling.

libMesh currently supports 1D, 2D, and 3D steady and transient finite
element simulations. The library makes use of high-quality, existing
software whenever possible. PETSc is used for the solution of linear systems
on both serial and parallel platforms, and LASPack is included with the
library to provide linear solver support on serial machines. An optional
interface to SLEPc is also provided for solving both standard and
generalized eigenvalue problems.

This package contains development files of libMesh.

%package tools
Summary: Tools for libMesh
Group: Graphics
Requires: %name = %version-%release

%description tools
The libMesh library provides a framework for the numerical simulation of
partial differential equations using arbitrary unstructured discretizations
on serial and parallel platforms. A major goal of the library is to provide
support for adaptive mesh refinement (AMR) computations in parallel while
allowing a research scientist to focus on the physics they are modeling.

libMesh currently supports 1D, 2D, and 3D steady and transient finite
element simulations. The library makes use of high-quality, existing
software whenever possible. PETSc is used for the solution of linear systems
on both serial and parallel platforms, and LASPack is included with the
library to provide linear solver support on serial machines. An optional
interface to SLEPc is also provided for solving both standard and
generalized eigenvalue problems.

This package contains tools for libMesh.

%package contrib
Summary: Contrib libraries for libMesh
Group: System/Libraries
Requires: %name = %version-%release

%description contrib
The libMesh library provides a framework for the numerical simulation of
partial differential equations using arbitrary unstructured discretizations
on serial and parallel platforms. A major goal of the library is to provide
support for adaptive mesh refinement (AMR) computations in parallel while
allowing a research scientist to focus on the physics they are modeling.

libMesh currently supports 1D, 2D, and 3D steady and transient finite
element simulations. The library makes use of high-quality, existing
software whenever possible. PETSc is used for the solution of linear systems
on both serial and parallel platforms, and LASPack is included with the
library to provide linear solver support on serial machines. An optional
interface to SLEPc is also provided for solving both standard and
generalized eigenvalue problems.

This package contains contrib libraries for libMesh.

%package contrib-devel
Summary: Development files of contrib libraries for libMesh
Group: Development/C++
Requires: %name-devel = %version-%release

%description contrib-devel
The libMesh library provides a framework for the numerical simulation of
partial differential equations using arbitrary unstructured discretizations
on serial and parallel platforms. A major goal of the library is to provide
support for adaptive mesh refinement (AMR) computations in parallel while
allowing a research scientist to focus on the physics they are modeling.

libMesh currently supports 1D, 2D, and 3D steady and transient finite
element simulations. The library makes use of high-quality, existing
software whenever possible. PETSc is used for the solution of linear systems
on both serial and parallel platforms, and LASPack is included with the
library to provide linear solver support on serial machines. An optional
interface to SLEPc is also provided for solving both standard and
generalized eigenvalue problems.

This package contains development files of contrib libraries for libMesh.

%package contrib-tools
Summary: Contrib tools for libMesh
Group: Graphics
Requires: %name-tools = %version-%release
Requires: %name-contrib = %version-%release

%description contrib-tools
The libMesh library provides a framework for the numerical simulation of
partial differential equations using arbitrary unstructured discretizations
on serial and parallel platforms. A major goal of the library is to provide
support for adaptive mesh refinement (AMR) computations in parallel while
allowing a research scientist to focus on the physics they are modeling.

libMesh currently supports 1D, 2D, and 3D steady and transient finite
element simulations. The library makes use of high-quality, existing
software whenever possible. PETSc is used for the solution of linear systems
on both serial and parallel platforms, and LASPack is included with the
library to provide linear solver support on serial machines. An optional
interface to SLEPc is also provided for solving both standard and
generalized eigenvalue problems.

This package contains contrib tools for libMesh.

%package examples
Summary: Examples for libMesh
Group: Development/Documentation
#Requires: %name = %version-%release
#BuildArch: noarch

%description examples
The libMesh library provides a framework for the numerical simulation of
partial differential equations using arbitrary unstructured discretizations
on serial and parallel platforms. A major goal of the library is to provide
support for adaptive mesh refinement (AMR) computations in parallel while
allowing a research scientist to focus on the physics they are modeling.

libMesh currently supports 1D, 2D, and 3D steady and transient finite
element simulations. The library makes use of high-quality, existing
software whenever possible. PETSc is used for the solution of linear systems
on both serial and parallel platforms, and LASPack is included with the
library to provide linear solver support on serial machines. An optional
interface to SLEPc is also provided for solving both standard and
generalized eigenvalue problems.

This package contains examples for libMesh.

%package -n %oname-doc
Summary: Documentation for libMesh
Group: Development/Documentation
BuildArch: noarch

%description -n %oname-doc
The libMesh library provides a framework for the numerical simulation of
partial differential equations using arbitrary unstructured discretizations
on serial and parallel platforms. A major goal of the library is to provide
support for adaptive mesh refinement (AMR) computations in parallel while
allowing a research scientist to focus on the physics they are modeling.

libMesh currently supports 1D, 2D, and 3D steady and transient finite
element simulations. The library makes use of high-quality, existing
software whenever possible. PETSc is used for the solution of linear systems
on both serial and parallel platforms, and LASPack is included with the
library to provide linear solver support on serial machines. An optional
interface to SLEPc is also provided for solving both standard and
generalized eigenvalue problems.

This package contains documentation for libMesh.

%prep
%setup
rm -f aclocal.m4
rm -f contrib/tetgen/tetgen.h \
	contrib/parmetis/Lib/parmetis.h \
	contrib/parmetis/Lib/proto.h

%if "%scalar_type" == "complex"
#rm -f $(find ./ -name '.depend') \
#	$(find ./ -name 'ensight_io*')
mkdir -p examples/..3 examples/..9
#cp examples/ex3/exact_solution.C examples/..3/exact_solution.C
#cp examples/ex9/exact_solution.C examples/..9/exact_solution.C
%endif

%prepare_sphinx .

#for i in $(find ./ -name Makefile) Make.common.in; do
#	sed -i 's|\-@|-|' $i
#	sed -i 's|@\$|$|' $i
#done

#rm -fR contrib/nemesis contrib/exodusii contrib/netcdf \
#	contrib/tetgen contrib/metis contrib/parmetis contrib/boost

%ifarch x86_64
LIB64=64
%endif
sed -i "s|@64@|$LIB64|g" m4/netcdf.m4 m4/metis.m4

sed -i 's|@PETSC_DIR@|%ldir|g' m4/slepc.m4

%build
mpi-selector --set %mpiimpl
source %_bindir/petsc-%scalar_type.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"
export MPIDIR=%mpidir

for i in $(find examples/ex* -name Makefile)
do
	sed -i \
		's|\$(libmesh_LIBS)\ \$(libmesh_LDFLAGS)|-Wl,-rpath,%mpidir/lib:%ldir/lib -L%blibdir -L%clibdir -lmesh|g' \
		$i
done
#sed -i 's|@BLIBDIR@|%blibdir|g' Makefile

./bootstrap
%add_optflags -DOMPI_IGNORE_CXX_SEEK -DHAVE_NOX -I%_includedir/exodusii
%add_optflags -I%mpidir/include/netcdf -fpermissive
%autoreconf
%configure \
	--prefix=%ldir \
%if "%scalar_type" == "complex"
	--enable-complex \
	--disable-trilinos \
	--disable-nox \
	--disable-aztecoo \
	--disable-netcdf \
	--disable-laspack \
%else
	--disable-complex \
	--enable-everything \
	--enable-optional \
	--enable-trilinos \
	--with-trilinos=%prefix \
	--enable-nox \
	--enable-aztecoo \
	--with-nox=%prefix \
	--with-aztecoo=%prefix \
	--enable-laspack \
	--enable-unordered-containers \
%endif
	--enable-shared \
	--enable-boost \
	--enable-petsc \
	--enable-slepc \
	--enable-exceptions \
	--enable-vtk \
	--enable-parmetis \
	--enable-metis \
	--enable-libHilbert \
	--with-vtk-include=%_includedir/vtk-5.10 \
	--enable-mpi \
	--with-mpi=%mpidir \
	--with-cxx=mpicxx \
	--with-cc=mpicc \
	--with-f77=mpif77 \
	--with-tbb=%prefix \
	--with-tbb-lib=%_libdir \
	--with-gm=%prefix \
	--with-glpk-include=%_includedir/glpk \
	--with-glpk-lib=%_libdir \
	--with-lapack=lapack \
	--with-eigen-include=%_includedir/eigen3 \
	--enable-triangle=yes \
	--with-boost=yes \
	--with-boost-libdir=%_libdir

#pushd contrib
#make_build
#popd

#pushd %clibdir
#for i in $(ls); do
#	if [ "$i" != "liblaspack.so" -a "$i" != "libtriangle.so" ]
#	then
#		mv $i $i.0
#		ln -s $i.0 $i
#	fi
#done
#popd

function makeIt() {
	%make_build LIBMESH_OPT_MODE=1 V=1 $1 \
		SLEPC_LIB=-L$SLEPC_DIR/lib \
		PACKAGES_LIBS="$(pkg-config petsc-%scalar_type --libs) -L$3 -lexoIIv2c -lglpk -lboost_system" \
		NEW_LIBDIR="$2" CONTRIB_DIR="$3" ADDLIB="$4 $5 $6 $7 $8 $9"
}

makeIt '' -L. %clibdir

%if "%scalar_type" == "real"
pushd doc
mkdir -p doc/html/doxygen
doxygen
%endif

%install
%makeinstall_std

install -d %buildroot%ldir/bin
mv %buildroot%_bindir/* %buildroot%ldir/bin/
install -d %buildroot%ldir/lib
mv %buildroot%_libdir/*.so* %buildroot%ldir/lib/

%if "%scalar_type" == "real"
install -d %buildroot%_man3dir
install -p -m644 doc/doc/man/man3/* %buildroot%_man3dir
install -d %buildroot%_docdir/%oname-%version
cp doc/doc/html/doxygen/* %buildroot%_docdir/%oname-%version/
%endif

install -d %buildroot%_docdir/%name-%version
install -p -m644 AUTHORS ChangeLog NEWS README* \
	%buildroot%_docdir/%name-%version
install -d %buildroot%_docdir/%name-%version/contrib
mkdir tmp
pushd contrib
mv gzstream/README ../tmp/README.gzstream
for i in AUTHORS COPYING ChangeLog NEWS README
do
	mv libHilbert/$i ../tmp/$i.libHilbert
done
mv sfcurves/README ../tmp/README.sfcurves
popd
install -p -m644 tmp/* %buildroot%_docdir/%name-%version/contrib
%if "%scalar_type" == "real"
install -p -m644 $(find doc -name '*.pdf') \
	%buildroot%_docdir/%oname-%version
#cp -fR doc/html %buildroot%_docdir/%oname-%version/
%endif

#rm -f $(find examples -name '*.o')
#cp -fR examples %buildroot%ldir/%oname
#cp -fR reference_elements %buildroot%ldir/%oname

pushd %buildroot%ldir
for i in bin/* lib/*.so
do
	chrpath -r %mpidir/lib:%ldir/lib $i ||:
done
popd

sed -i 's|^libdir.*|libdir=%ldir/lib|' \
	%buildroot%_sysconfdir/%oname/*.pc %buildroot%_pkgconfigdir/*.pc
sed -i 's|^includedir.*|includedir=%ldir/include|' \
	%buildroot%_sysconfdir/%oname/*.pc %buildroot%_pkgconfigdir/*.pc

%if "%scalar_type" == "real"
pushd %buildroot%_man3dir
mv statistics.h.3 mesh__statistics.h.3
rm -f CompareTypes_* ScalarTraits_* \
	boostcopy_enable_if_c_*
popd
%endif

%files
%doc %dir %_docdir/%name-%version
%doc %_docdir/%name-%version/*
%dir %ldir/lib
%ldir/lib/*.so.*

%files devel
%_sysconfdir/*
%dir %ldir/bin
%ldir/bin/%oname-config
%ldir/lib/*.so
%ldir/include/*
%ldir/Make.common
%_pkgconfigdir/*

%files tools
%dir %ldir/bin
%ldir/bin/*
%exclude %ldir/bin/%oname-config

#files contrib
#doc %dir %_docdir/%name-%version
#doc %_docdir/%name-%version/contrib
#ldir/lib/*.so.*
#exclude %ldir/lib/%oname.so.*

#files contrib-devel
#ldir/lib/*.so
#exclude %ldir/lib/%oname.so
#ldir/include/contrib

#files contrib-tools
#dir %ldir/bin
#ldir/bin/*
#exclude %ldir/bin/%oname-config
#exclude %ldir/bin/amr
#exclude %ldir/bin/compare
#exclude %ldir/bin/grid2grid
#exclude %ldir/bin/meshtool
#exclude %ldir/bin/parameterize.pl

%if "%scalar_type" == "real"
%files examples
%_datadir/reference_elements
%ldir/examples

%files -n %oname-doc
%doc %_docdir/%oname-%version
%_man3dir/*
%endif

%changelog
* Tue Sep 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt2.rc1.git20130711
- Rebuilt with Trilinos 11.4.1

* Mon Jul 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt1.rc1.git20130711
- Version 0.9.2-rc1

* Mon May 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt9.svn20120913
- Fixed build

* Thu May 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt8.svn20120913
- Rebuilt with Trilinos 11.2.3

* Sun Feb 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt7.svn20120913
- Rebuilt with Boost 1.53.0

* Mon Feb 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt6.svn20120913
- Rebuilt with glpk 4.48

* Thu Nov 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt5.svn20120913
- Rebuilt with Boost 1.52.0

* Tue Nov 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt4.svn20120913
- Fixed build

* Sun Oct 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt3.svn20120913
- Rebuilt with Trilinos 11.0.3

* Tue Sep 18 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt2.svn20120913
- Rebuilt with netcdf 4.2

* Thu Sep 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt1.svn20120913
- Version 0.8.0

* Wed Sep 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.3-alt3.svn20120228
- Rebuilt with Boost 1.51.0

* Sat Aug 18 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.3-alt2.svn20120228
- Rebuilt with Trilinos 10.12.2

* Thu Aug 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.3-alt1.svn20120228
- Version 0.7.3

* Sat Jul 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.2-alt6.svn20120228
- Changed native directory: %%_libexecdir/petsc-%scalar_type ->
  %%_libdir/petsc-%scalar_type

* Fri Jun 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.2-alt5.svn20120228
- Rebuilt with OpenMPI 1.6

* Sat Jun 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.2-alt4.svn20120228
- Rebuilt with VTK 5.10.0

* Tue Feb 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.2-alt3.svn20120228
- New snapshot

* Wed Feb 15 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.2-alt3.svn20111207
- Rebuilt with Trilinos 10.10.0

* Tue Dec 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.2-alt2.svn20111207
- Fixed RPATH

* Fri Dec 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.2-alt1.svn20111207
- Version 0.7.2

* Sun Nov 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.1-alt2.svn20110505
- Rebuilt with Trilinos 10.8.1

* Fri Sep 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.1-alt1.svn20110505.2
- Rebuilt with VTK 5.8.0

* Fri Sep 02 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.1-alt1.svn20110505.1
- Rebuilt with some system libraries instead of embedded

* Sun May 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.1-alt1.svn20110505
- Version 0.7.1

* Mon Apr 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0.3-alt1.svn20101117.5
- Rebuilt with libnetcdf7

* Tue Apr 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0.3-alt1.svn20101117.4
- Built with GotoBLAS2 instead of ATLAS

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0.3-alt1.svn20101117.3
- Rebuilt with python-module-sphinx-devel

* Mon Mar 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0.3-alt1.svn20101117.2
- Rebuilt for debuginfo

* Fri Feb 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0.3-alt1.svn20101117.1
- Rebuilt with parmetis 3.1.1-alt10

* Thu Nov 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0.3-alt1.svn20101117
- Version 0.7.0.3
- Enabled SLEPc

* Wed Oct 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.4-alt1.svn20100805.2
- Rebuilt for soname set-versions

* Sat Oct 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.4-alt1.svn20100805.1
- Fixed overlinking of libraries

* Thu Aug 05 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.4-alt1.svn20100805
- New snapshot
- Rebuilt with PETSc 3.1
- Disabled SLEPc

* Wed Jul 21 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.4-alt1.svn20100716
- New snapshot
- Rebuilt with VTK 5.6.0
- Disabled SLEPc

* Wed Jul 07 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.4-alt1.svn20100303.3
- Rebuilt with reformed ParMetis

* Mon Apr 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.4-alt1.svn20100303.2
- Rebuilt with Trilinos 10.2.0

* Sun Mar 21 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.4-alt1.svn20100303.1
- Rebuilt with new tbb

* Thu Mar 04 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.4-alt1.svn20100303
- New snapshot

* Sat Dec 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.4-alt1.svn20091216
- Version 0.6.4

* Wed Dec 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.3_rc1-alt1.svn20090917.1
- Rebuilt with Trilinos v10

* Tue Sep 22 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.3_rc1-alt1.svn20090917
- New snapshot
- Enabled NOX support
- Linked with external libraries instead of embedded

* Thu Aug 27 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.3_rc1-alt1
- Initial build for Sisyphus

