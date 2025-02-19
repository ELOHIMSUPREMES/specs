%define _unpackaged_files_terminate_build 1

%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

Name: parmetis
Version: 4.0.3
Release: alt2
Summary: Parallel Graph Partitioning and Fill-reducing Matrix Ordering
License: Free for non-commertial
Group: Sciences/Mathematics
Url: http://glaros.dtc.umn.edu/gkhome/metis/parmetis/overview

Source: ParMetis-%version.tar
Source1: %name.pc

Patch1: ParMetis-%version-alt.patch

BuildRequires(pre): %mpiimpl-devel
BuildRequires: cmake libpcre-devel

%description
ParMETIS is an MPI-based parallel library that implements a variety of
algorithms for partitioning unstructured graphs, meshes, and for computing
fill-reducing orderings of sparse matrices. ParMETIS extends the functionality
provided by METIS and includes routines that are especially suited for parallel
AMR computations and large scale numerical simulations. The algorithms
implemented in ParMETIS are based on the parallel multilevel k-way
graph-partitioning, adaptive repartitioning, and parallel multi-constrained
partitioning schemes developed in our lab.

%package -n lib%name
Summary: Shared libraries of ParMETIS
Group: System/Libraries

%description -n lib%name
ParMETIS is an MPI-based parallel library that implements a variety of
algorithms for partitioning unstructured graphs, meshes, and for computing
fill-reducing orderings of sparse matrices. ParMETIS extends the functionality
provided by METIS and includes routines that are especially suited for parallel
AMR computations and large scale numerical simulations. The algorithms
implemented in ParMETIS are based on the parallel multilevel k-way
graph-partitioning, adaptive repartitioning, and parallel multi-constrained
partitioning schemes developed in our lab.

This package contains shared libraries of ParMETIS.

%package -n lib%name-devel
Summary: Development files of ParMETIS
Group: Development/C
Requires: lib%name = %EVR
Conflicts: lib%name-devel < %EVR
Obsoletes: lib%name-devel < %EVR
Requires: %mpiimpl-devel

%description -n lib%name-devel
ParMETIS is an MPI-based parallel library that implements a variety of
algorithms for partitioning unstructured graphs, meshes, and for computing
fill-reducing orderings of sparse matrices. ParMETIS extends the functionality
provided by METIS and includes routines that are especially suited for parallel
AMR computations and large scale numerical simulations. The algorithms
implemented in ParMETIS are based on the parallel multilevel k-way
graph-partitioning, adaptive repartitioning, and parallel multi-constrained
partitioning schemes developed in our lab.

This package contains development files of ParMETIS.

%package -n lib%name-devel-doc
Summary: Development documentation of ParMETIS
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
ParMETIS is an MPI-based parallel library that implements a variety of
algorithms for partitioning unstructured graphs, meshes, and for computing
fill-reducing orderings of sparse matrices. ParMETIS extends the functionality
provided by METIS and includes routines that are especially suited for parallel
AMR computations and large scale numerical simulations. The algorithms
implemented in ParMETIS are based on the parallel multilevel k-way
graph-partitioning, adaptive repartitioning, and parallel multi-constrained
partitioning schemes developed in our lab.

This package contains development documentation of ParMETIS.

%package examples
Summary: Example graphs for ParMETIS
Group: Development/Documentation
BuildArch: noarch

%description examples
ParMETIS is an MPI-based parallel library that implements a variety of
algorithms for partitioning unstructured graphs, meshes, and for computing
fill-reducing orderings of sparse matrices. ParMETIS extends the functionality
provided by METIS and includes routines that are especially suited for parallel
AMR computations and large scale numerical simulations. The algorithms
implemented in ParMETIS are based on the parallel multilevel k-way
graph-partitioning, adaptive repartitioning, and parallel multi-constrained
partitioning schemes developed in our lab.

This package contains example graphs for ParMETIS.

%prep
%setup
%patch1 -p1
install -m644 %SOURCE1 %name.pc
sed -i -e "s|@libdir@|%_lib|" -e "s|@VERSION@|%version|" %name.pc

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath=%mpidir/lib -L%mpidir/lib"

%add_optflags -I%_includedir/pcre
%cmake_insource \
	-DCMAKE_STRIP:FILEPATH="/bin/echo" \
	-DMPIEXEC_MAX_NUMPROCS:STRING=16 \
	-DCMAKE_C_COMPILER:FILEPATH=mpicc \
	-DCMAKE_CXX_COMPILER:FILEPATH=mpicxx \
	-DCMAKE_EXE_LINKER_FLAGS:STRING="-Wl,-R%mpidir/lib" \
	-DCMAKE_EXPORT_COMPILE_COMMANDS:BOOL=ON \
	-DPCRE:BOOL=ON \
	-DGDB:BOOL=ON \
	-DGKRAND:BOOL=ON \
	%nil

%make_build VERBOSE=1

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath=%mpidir/lib -L%mpidir/lib"

%makeinstall_std

install -d %buildroot%mpidir/bin
install -d %buildroot%mpidir/include/metis
install -d %buildroot%_docdir/%name
install -d %buildroot%_datadir/%name
install -d %buildroot%_pkgconfigdir

pushd Graphs
install -p -m644 * %buildroot%_datadir/%name
popd

install -m644 manual/* %buildroot%_docdir/%name
install -m644 metis/include/*.h %buildroot%mpidir/include/metis
install -m644 %name.pc %buildroot%_pkgconfigdir

# shared libraries

TOPDIR=$PWD
pushd %buildroot%_libdir
for i in %name; do
	mpicc -shared -Wl,--whole-archive lib$i.a $TOPDIR/libmetis/libmetis.a \
		-Wl,--no-whole-archive -lpcreposix -lm -Wl,-soname,lib$i.so.0 \
		-o lib$i.so.0 -Wl,-z,defs -Wl,-R%mpidir/lib
	ln -s lib$i.so.0 lib$i.so
	rm -f *.o
done
popd

rm -rf %buildroot%_libdir/*.a

%files
%doc Changelog LICENSE.txt
%_bindir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%mpidir/include/*
%_includedir/*
%_pkgconfigdir/*

%files -n lib%name-devel-doc
%_docdir/%name

%files examples
%_datadir/%name

%changelog
* Wed Dec 26 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.0.3-alt2
- Spec cleanup and rebuild with new toolchain.

* Fri Jul 05 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.3-alt1
- Version 4.0.3

* Sun Jun 24 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt3
- Rebuilt with OpenMPI 1.6

* Wed Jun 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt2
- Fixed build

* Wed Dec 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1
- Version 4.0.2

* Fri Sep 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt1
- Version 4.0

* Thu Apr 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.0-alt1
- Version 3.2.0
- Disabled devel-static package

* Fri Feb 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.1-alt10
- Removed libmetis.so*

* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.1-alt9
- Rebuilt for debuginfo

* Mon Nov 29 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.1-alt8
- Packed all necessary symbols into libparmetis.so

* Tue Oct 12 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.1-alt7
- Fixed overlinking of libraries

* Fri Jul 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.1-alt6
- Avoided conflict with metis

* Sat Aug 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.1-alt5
- Added link parmetis.pc -> metis.pc

* Thu Aug 27 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.1-alt4
- Added shared libraries

* Sun Aug 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.1-alt3
- Added pkg-config file
- Fixed "format not a string literal and no format arguments"

* Fri Jun 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.1-alt2
- Rebuild with PIC

* Tue May 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.1-alt1
- Initial build for Sisyphus

