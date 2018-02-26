%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%define somver 0
%define sover %somver.0.0

%define svn svn6034

Name: elmerfem
Version: 7.0
Release: alt2.%svn

Summary: Open Source Finite Element Software for Multiphysical Problems
License: GPLv2+
Group: Sciences/Physics

Url: http://www.csc.fi/english/pages/elmer
Source: %name-%version.tar
# https://elmerfem.svn.sourceforge.net/svnroot/elmerfem/trunk
Patch7: elmer-5.5.0-debian-node-partition.patch
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildRequires: gcc-c++ libncurses-devel

BuildRequires: gcc-fortran liblapack-devel libxblas-devel %mpiimpl-devel
BuildRequires: libncurses-devel libreadline-devel libmetis0-devel
BuildRequires: libopencascade-devel libftgl-devel R-devel
BuildpreReq: libtetgen-devel libsuitesparse-devel libarpack-devel
BuildPreReq: python-module-PyQt4 libqwt-devel libvtk-devel
BuildPreReq: libparpack-mpi-devel qt4-devel tcl-devel tk-devel
BuildPreReq: libhypre-devel rpm-macros-make

Requires: lib%name = %version-%release

%define elmer_modules matc meshgen2d eio hutiter elmerparam post

%description
Elmer is an open source multiphysical simulation software
developed by CSC. Elmer development was started 1995 in
collaboration with Finnish Universities, research institutes
and industry.

Elmer includes physical models of fluid dynamics, structural
mechanics, electromagnetics, heat transfer and acoustics, for
example. These are described by partial differential equations
which Elmer solves by the Finite Element Method (FEM).

%package -n lib%name
Summary: Shared libraries of Elmer Finite Element Software
Group: System/Libraries

%description -n lib%name
Elmer is an open source multiphysical simulation software
developed by CSC. Elmer development was started 1995 in
collaboration with Finnish Universities, research institutes
and industry.

Elmer includes physical models of fluid dynamics, structural
mechanics, electromagnetics, heat transfer and acoustics, for
example. These are described by partial differential equations
which Elmer solves by the Finite Element Method (FEM).

This package contains shared libraries of Elmer Finite Element
Software.

%package -n lib%name-devel
Summary: Development files of Elmer Finite Element Software
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
Elmer is an open source multiphysical simulation software
developed by CSC. Elmer development was started 1995 in
collaboration with Finnish Universities, research institutes
and industry.

Elmer includes physical models of fluid dynamics, structural
mechanics, electromagnetics, heat transfer and acoustics, for
example. These are described by partial differential equations
which Elmer solves by the Finite Element Method (FEM).

This package contains development files of Elmer Finite Element
Software.

%package -n ElmerGUI
Summary: GUI for Elmer Finite Element Software
Group: Sciences/Physics
Requires: %name = %version-%release

%description -n ElmerGUI
Elmer is an open source multiphysical simulation software
developed by CSC. Elmer development was started 1995 in
collaboration with Finnish Universities, research institutes
and industry.

Elmer includes physical models of fluid dynamics, structural
mechanics, electromagnetics, heat transfer and acoustics, for
example. These are described by partial differential equations
which Elmer solves by the Finite Element Method (FEM).

This package contains GUI for Elmer Finite Element
Software.

%package -n ElmerGUIlogger
Summary: Data logger for ElmerGUI
Group: Sciences/Physics
Requires: ElmerGUI = %version-%release

%description -n ElmerGUIlogger
Elmer is an open source multiphysical simulation software
developed by CSC. Elmer development was started 1995 in
collaboration with Finnish Universities, research institutes
and industry.

Elmer includes physical models of fluid dynamics, structural
mechanics, electromagnetics, heat transfer and acoustics, for
example. These are described by partial differential equations
which Elmer solves by the Finite Element Method (FEM).

This package contains data logger for ElmerGUI.

%prep
%setup
%patch7 -p1

rm -fR hutiter/examples/ex1/hutiex \
	elmerparam/src/matlab/elmer_param.mexsol \
	meshgen2d/src/Mesh2d \
	fem/autom4te.cache

%ifarch x86_64
sed -i 's|^\(BITS\).*|\1 = 64|' ElmerGUI/ElmerGUI.pri
LIB_SUFFIX=64
%endif
sed -i "s|@LIB_SUFFIX@|$LIB_SUFFIX|g" \
	fem/src/ModelDescription.src \
	fem/src/Load.c \
	fem/src/elmerf90.in \
	fem/src/elmerf90-nosh.in \
	fem/src/ElementDescription.src \
	buildtools/installer/elmer.nsi \
	front/src/ecif_userinterface_TCL.cpp \
	ElmerGUItester/src/tester.cpp \
	ElmerGUI/Application/src/main.cpp \
	post/src/ElmerPost.c \
	ElmerGUIlogger/src/mainwindow.cpp
sed -i 's|@PYVER@|%_python_version|g' \
	ElmerGUI/ElmerGUI.pri \
	ElmerGUI/Application/Application.pro

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"
export MPIDIR=%mpidir
%ifarch x86_64
export LIB_SUFFIX=64
%endif

function shareIt() {
	if [ "$1" == "libelmerparam" ]; then
		ADDLIB="-L$PWD/../matc/src -lmatc"
	else
		ADDLIB=
	fi
	mkdir src/tmp
	pushd src/tmp
		for i in $@; do
			if [ "$i" == "libelmerparamf" ]; then
				ADDLIB="-L$PWD/.. -lelmerparam $ADDLIB"
			fi
			ar x ../$i.a
			g++ -shared * -Wl,-soname,$i.so.%somver \
				-o ../$i.so.%sover $ADDLIB -lopenblas -lgfortran
			ln -s $i.so.%sover ../$i.so.%somver
			ln -s $i.so.%somver ../$i.so
			rm -f * ../$i.a
		done
	popd
	rmdir src/tmp
}

export TOPDIR=$PWD
for i in %elmer_modules; do
	pushd $i
	%autoreconf
	if [ "$i" == "post" ]; then
		sed -i "s|\(\-lmatc\)|-L`pwd`/../matc/src \1|" configure
	fi
	%add_optflags %optflags_shared -I%_includedir/freetype2
	%configure
	%make
	if [ "$i" == "matc" ]; then
		shareIt libmatc
	fi
	if [ "$i" == "eio" ]; then
		shareIt libeiof libeioc
	fi
	if [ "$i" == "hutiter" ]; then
		shareIt libhuti
	fi
	if [ "$i" == "elmerparam" ]; then
		shareIt libelmerparam libelmerparamf
	fi
	popd
done

export LD_LIBRARY_PATH=$PWD/matc/src:$PWD/eio/src:$PWD/hutiter/src

%add_optflags %optflags_shared
export FCPPFLAGS="$CFLAGS"
export FCFLAGS="$CFLAGS"
pushd elmergrid
%autoreconf
%configure \
	--with-metis=%prefix \
	--with-metis-include=%_includedir/metis \
	--with-metis-libs=%_libdir \
	--with-matc=$PWD/../matc/src/libmatc.so
%make_build_ext
popd

pushd fem
%autoreconf
%add_optflags %optflags_shared
%configure \
	--with-mpi=yes \
	--with-mpi-dir=%mpidir \
	--with-mpi-lib-dir=%mpidir/lib \
	--with-mpi-inc-dir=%mpidir/include \
	--with-blas=-lopenblas \
	--with-lapack=-llapack \
	--with-huti=$PWD/../hutiter/src/libhuti.so \
	--with-eiof=$PWD/../eio/src/libeiof.so \
	--with-arpack=-larpack_LINUX \
	--with-parpack=-lparpack_MPI-LINUX \
	--with-hypre=-lHYPRE \
	--with-umfpack=-lumfpack \
	--with-matc=$PWD/../matc/src/libmatc.so
%make_build_ext MPI_F90=mpif90
popd

pushd front
%autoreconf
%add_optflags %optflags_shared
%configure \
	--with-x \
	--with-eioc=$PWD/../eio/src/libeioc.so \
	--with-matc=$PWD/../matc/src/libmatc.so
%make_build_ext
popd

pushd ElmerGUI
qmake-qt4 QMAKE_CFLAGS_RELEASE="%optflags" \
	QMAKE_CXXFLAGS_RELEASE="%optflags" ElmerGUI.pro
%make
popd

pushd misc/tetgen_plugin
export ELMER_HOME=%prefix
qmake-qt4 QMAKE_CFLAGS_RELEASE="%optflags" \
	QMAKE_CXXFLAGS_RELEASE="%optflags" tetgen_plugin.pro
%make_build
popd

pushd ElmerGUIlogger
qmake-qt4 -project -d QMAKE_CFLAGS_RELEASE="%optflags" \
	QMAKE_CXXFLAGS_RELEASE="%optflags"
qmake-qt4 QMAKE_CFLAGS_RELEASE="%optflags" \
	QMAKE_CXXFLAGS_RELEASE="%optflags"
%make_build
popd

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"
export MPIDIR=%mpidir
%ifarch x86_64
export LIB_SUFFIX=64
%endif

install -d %buildroot%_includedir
install -d %buildroot%_libdir
install -d %buildroot%_libexecdir
cp -P */src/lib*.so* misc/tetgen_plugin/plugin/*.so* \
	%buildroot%_libdir/
export LD_LIBRARY_PATH=%buildroot%_libdir

for i in %elmer_modules elmergrid fem front \
	ElmerGUI ElmerGUIlogger
do
	pushd $i
	%makeinstall_std INSTALL_ROOT=%buildroot MPI_F90=mpif90
	popd
done

install -m755 ElmerGUIlogger/ElmerGUIlogger %buildroot%_bindir
install -d %buildroot%_niconsdir
install -p -m644 ElmerGUIlogger/icons/*.png \
	%buildroot%_niconsdir

%ifarch x86_64
mv %buildroot%_libexecdir/*.so %buildroot%_libdir/
%endif

install -m644 eio/config.h %buildroot%_includedir/eio_config.h
sed -i 's|\.\.\/config\.h|eio_config.h|' \
	%buildroot%_includedir/eio_api.h

pushd %buildroot%_libdir/elmerpost/fonts/TrueType
for i in Free*.ttf; do
	rm -f $i
	ln -s %_datadir/fonts/ttf/freefont/$i .
done
popd

%pre
rm -f %_datadir/fonts/ttf/freefont/Free*.ttf

%files
%doc LICENSES
%_bindir/*
%exclude %_bindir/ElmerGUI*
%_libdir/elmersolver
%exclude %_libdir/elmersolver/include
%_libdir/elmerfront
%_libdir/elmerpost

%files -n lib%name
%_libdir/*.so.*
%_libdir/libelmersolver-7.0.so

%files -n lib%name-devel
%_libdir/*.so
%exclude %_libdir/libelmersolver-7.0.so
%_libdir/elmersolver/include
%_includedir/*

%files -n ElmerGUI
%doc ElmerGUI/GPL* ElmerGUI/LICENSES ElmerGUI/README
%_bindir/ElmerGUI
%_datadir/edf
%_datadir/edf-extra

%files -n ElmerGUIlogger
%doc ElmerGUIlogger/README
%_bindir/ElmerGUIlogger
%_niconsdir/ElmerGUI.png
%_niconsdir/application-exit.png
%_niconsdir/document-print.png
%_niconsdir/document-save-as.png

%changelog
* Mon Feb 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.0-alt2.svn6034
- New snapshot

* Wed Sep 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.0-alt2.svn5812
- Fixed build

* Sat Aug 18 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.0-alt1.svn5812
- Version 7.0

* Mon Aug 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.2-alt5.svn5602
- Built with OpenBLAS instead of GotoBLAS2

* Wed Jul 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.2-alt4.svn5602
- Rebuilt with OpenMPI 1.6

* Sat Jun 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.2-alt3.svn5602
- Rebuilt with VTK 5.10.0

* Mon May 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.2-alt2.svn5602
- Fixed build

* Thu Mar 01 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.2-alt1.svn5602
- New snapshot

* Wed Jan 25 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.2-alt1.svn5526
- New snapshot

* Fri Dec 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.2-alt1.svn5475
- Version 6.2

* Tue Dec 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.5.0-alt2.svn5184
- Fixed RPATH

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 5.5.0-alt1.svn5184.2.1
- Rebuild with Python-2.7

* Fri Sep 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.5.0-alt1.svn5184.2
- Rebuilt with VTK 5.8.0

* Sat Sep 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.5.0-alt1.svn5184.1
- Rebuilt with metis 5.0.1

* Sun May 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.5.0-alt1.svn5184
- New snapshot

* Fri Apr 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.5.0-alt1.svn4804.7
- Enabled build with R

* Tue Apr 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.5.0-alt1.svn4804.6
- Built with GotoBLAS2 instead of ATLAS

* Sat Apr 02 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.5.0-alt1.svn4804.5
- Replaced fonts by links to fonts from fonts-ttf-freefont (ALT #25333)

* Tue Mar 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.5.0-alt1.svn4804.4
- Rebuilt with libftgl2

* Tue Mar 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.5.0-alt1.svn4804.3
- Rebuilt for debuginfo

* Fri Feb 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.5.0-alt1.svn4804.2
- Rebuilt with metis 4.0.1-alt9

* Thu Nov 25 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.5.0-alt1.svn4804.1
- Rebuilt for soname set-versions

* Wed Nov 10 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.5.0-alt1.svn4804
- New snapshot

* Wed Oct 13 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.5.0-alt1.svn4645.2
- Fixed linking of libraries

* Tue Sep 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.5.0-alt1.svn4645.1
- Built with VTK and OpenCASCADE

* Wed Sep 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.5.0-alt1.svn4645
- Initial build for Sisyphus

* Thu Sep 02 2010 Michael Shigorin <mike@altlinux.org> 5.5.0-alt1svn4613
- built for ALT Linux
  + heavily based on Debian package
