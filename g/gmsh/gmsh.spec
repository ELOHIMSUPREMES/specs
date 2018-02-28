%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl
%define hdf5dir %mpidir
%define petsc_dir %_libdir/petsc-real

Name: gmsh
Summary: Automatic 3D finite element grid generator
Version: 2.8.5
Release: alt2.svn20140707.1
Group: Graphics
License: GPL v2
URL: http://www.geuz.org/gmsh/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://geuz.org/svn/gmsh/trunk/
# login/password: gmsh:gmsh
Source: %name-%version.tar.gz
Source1: CMakeCache.txt

Requires: libcgns-mpi
Requires: lib%name = %EVR

BuildPreReq: libfltk-devel libjpeg-devel zlib-devel libpng-devel
BuildPreReq: libnetgen-devel libann-devel libchaco-devel chrpath
BuildPreReq: libtetgen-devel getfemxx libGL-devel libGLU-devel libX11-devel
BuildPreReq: libXft-devel libXext-devel libhdf5-mpi-devel %mpiimpl-devel
BuildPreReq: liblapack-devel texlive-base-bin libcairo-devel libavcodec53
BuildPreReq: cmake libICE-devel libSM-devel libparmetis0-devel
BuildPreReq: libXtst-devel libXau-devel libtaucs-devel libgmp-devel
BuildPreReq: libcgns-mpi-devel libXcomposite-devel libpixman-devel
BuildPreReq: libXcursor-devel libXdmcp-devel libXinerama-devel libXpm-devel
BuildPreReq: libXrandr-devel libXt-devel libXv-devel libXxf86misc-devel
BuildPreReq: libslepc-real-devel flex libamesos10 swig
BuildPreReq: libepetraext10 libifpack10 libtrilinos10 libgaleri10
BuildPreReq: libopencascade-devel libmmg3d-devel libdakota-devel
BuildPreReq: libnumpy-devel
# explicitly added texinfo for info files
BuildRequires: texinfo

%description
Gmsh is an automatic 3D finite element grid generator with a built-in CAD engine
and post-processor. Its design goal is to provide a simple meshing tool for
academic problems with parametric input and advanced visualization capabilities.

Gmsh is built around four modules: geometry, mesh, solver and post-processing.
The specification of any input to these modules is done either interactively
using the graphical user interface or in ASCII text files using Gmsh's own
scripting language.

%package demos
Summary: Tutorial and demo files for Gmsh
Group: Graphics
BuildArch: noarch

%description demos
Gmsh is an automatic 3D finite element grid generator with a built-in CAD engine
and post-processor. Its design goal is to provide a simple meshing tool for
academic problems with parametric input and advanced visualization capabilities.

Gmsh is built around four modules: geometry, mesh, solver and post-processing.
The specification of any input to these modules is done either interactively
using the graphical user interface or in ASCII text files using Gmsh's own
scripting language.

This package contains tutorial and demo files for Gmsh.

%package -n lib%name
Summary: Shared libraries of Gmsh
Group: System/Libraries

%description -n lib%name
Gmsh is an automatic 3D finite element grid generator with a built-in CAD engine
and post-processor. Its design goal is to provide a simple meshing tool for
academic problems with parametric input and advanced visualization capabilities.

Gmsh is built around four modules: geometry, mesh, solver and post-processing.
The specification of any input to these modules is done either interactively
using the graphical user interface or in ASCII text files using Gmsh's own
scripting language.

This package contains shared libraries of Gmsh.

%package -n lib%name-devel
Summary: Development files of Gmsh
Group: Development/C++
Requires: lib%name = %EVR

%description -n lib%name-devel
Gmsh is an automatic 3D finite element grid generator with a built-in CAD engine
and post-processor. Its design goal is to provide a simple meshing tool for
academic problems with parametric input and advanced visualization capabilities.

Gmsh is built around four modules: geometry, mesh, solver and post-processing.
The specification of any input to these modules is done either interactively
using the graphical user interface or in ASCII text files using Gmsh's own
scripting language.

This package contains development files of Gmsh.

%package -n python-module-%name
Summary: Python wrapper of Gmsh
Group: Development/Python
Requires: lib%name = %EVR

%description -n python-module-%name
Gmsh is an automatic 3D finite element grid generator with a built-in CAD engine
and post-processor. Its design goal is to provide a simple meshing tool for
academic problems with parametric input and advanced visualization capabilities.

Gmsh is built around four modules: geometry, mesh, solver and post-processing.
The specification of any input to these modules is done either interactively
using the graphical user interface or in ASCII text files using Gmsh's own
scripting language.

This package contains python wrapper of Gmsh.

%prep
%setup

install -p -m644 %SOURCE1 .
sed -i 's|@LIBDIR@|%_libdir|g' CMakeCache.txt
sed -i 's|@MPIDIR@|%mpidir|g' CMakeCache.txt
sed -i 's|@PETSC_DIR@|%petsc_dir|g' CMakeCache.txt
%ifarch x86_64
LIB64=64
%endif
sed -i "s|@64@|$LIB64|g" CMakeCache.txt

# avoid conflict with defs.h in other packages
ln -s defs.h contrib/Chaco/main/chaco_defs.h
CHACO_FILES="$(egrep -R 'defs\.h' contrib/Chaco/|awk -F : '{print $1}')"
sed -i 's|defs\.h|chaco_defs.h|' $CHACO_FILES

rm -fR contrib/{ANN,Metis,mmg3d}

sed -i "s|@SRCROOT@|$PWD|g" wrappers/gmshpy/setup.py.in

%build
mpi-selector --set %mpiimpl
source %_bindir/petsc-real.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib -L%_libdir/oski"
export LD_LIBRARY_PATH=%_libdir/oski

cmake \
%ifarch x86_64
	-DLIB_SUFFIX:STRING=64 \
%endif
	-DMPIDIR:PATH=%mpidir \
	.
%make_build VERBOSE=1
%make info

%install
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib -l%_libdir/oski"
export LD_LIBRARY_PATH=%_libdir/oski

%makeinstall_std

#for i in %buildroot%_bindir/*; do
for i in %buildroot%_bindir/* %buildroot%_libdir/*.so \
	%buildroot%python_sitelibdir/gmshpy/*.so
do
	chrpath -r %mpidir/lib:%petsc_dir/lib $i ||:
done

install -d %buildroot%_infodir
install -m644 doc/texinfo/*.info* %buildroot%_infodir

install -p -m644 doc/*.html %buildroot%_docdir/%name

pushd %buildroot/usr/gmshpy
%python_build_install
popd
rm -fR %buildroot/usr/gmshpy

%filter_from_requires /^debug.*(libcgns\.so.*/s/^/libcgns-mpi-debuginfo\t/

%files
%dir %_docdir/%name
%doc %_docdir/%name/*.txt
%doc %_docdir/%name/*.html
%_bindir/*
%_man1dir/*
%_infodir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%files -n python-module-%name
%python_sitelibdir/*

%files demos
%dir %_docdir/%name
%_docdir/%name/demos
%_docdir/%name/tutorial

%changelog
* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 2.8.5-alt2.svn20140707.1
- NMU: added BR: texinfo

* Thu Mar 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.5-alt2.svn20140707
- Rebuilt with OpenCASCADE 6.8.0

* Tue Jul 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.5-alt1.svn20140707
- New snapshot

* Thu Jun 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.5-alt1.svn20140618
- Version 2.8.5

* Wed Nov 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.4-alt1.svn20131112
- Version 2.8.4

* Fri Sep 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.1-alt2.svn20130710
- Rebuilt with OpenCASCADE 6.6.0

* Wed Jul 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.1-alt1.svn20130710
- Version 2.8.1

* Wed Jun 26 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.2-alt1.svn20130201
- Version 2.7.2

* Tue May 07 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.2-alt6.svn20130201
- Fixed build

* Thu Feb 07 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.2-alt5.svn20130201
- Rebuilt with OpenCASCADE 6.5.4

* Fri Feb 01 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.2-alt4.svn20130201
- New snapshot

* Wed Oct 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.2-alt4.svn20120814
- Rebuilt with gcc 4.7

* Wed Sep 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.2-alt3.svn20120814
- Rebuilt with libpng15

* Wed Sep 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.2-alt2.svn20120814
- Rebuilt with external ANN, ParMetis, Mmg3d and Netgen
- Built with OpenCASCADE

* Wed Aug 15 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.2-alt1.svn20120814
- Version 2.6.2

* Wed Jul 18 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt7.svn20100906
- Fixed build

* Sat Jul 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt6.svn20100906
- Rebuilt with PETSc 3.2_p7-alt3

* Thu Jul 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt5.svn20100906
- Rebuilt with OpenMPI 1.6

* Wed Jun 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt4.svn20100906
- Fixed build

* Wed Feb 15 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt3.svn20100906
- Built without OSMesa

* Mon Dec 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt2.svn20100906
- Rebuilt with PETSc 3.2

* Mon May 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt1.svn20100906.8
- Rebuilt with cgns 3.1.3

* Fri Apr 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt1.svn20100906.7
- Rebuilt with FLTK 1.3.0.r8575

* Thu Apr 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt1.svn20100906.6
- Rebuilt

* Tue Apr 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt1.svn20100906.5
- Built with GotoBLAS2 instead of ATLAS

* Mon Mar 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt1.svn20100906.4
- Rebuilt for debuginfo

* Fri Mar 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt1.svn20100906.3
- Added -g into compiler flags

* Mon Jan 31 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt1.svn20100906.2
- Rebuilt with libfltk13

* Wed Nov 17 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt1.svn20100906.1
- Fixed clear() function in Geo/MZoneBoundary.h

* Sun Nov 14 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt1.svn20100906
- Version 2.5.1

* Mon Aug 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.0-alt1.svn20100620.1
- Enabled MPI parallelization
- Rebuilt with PETSc 3.1

* Mon Jun 21 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.0-alt1.svn20100620
- Version 2.5.0

* Thu Dec 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.3-alt1.svn20091216
- Version 2.4.3

* Tue Nov 10 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.2-alt1.svn20091109
- Version 2.4.2
- Rebuilt with texlive instead of tetex

* Mon Sep 14 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.1-alt1
- Initial build for Sisyphus

