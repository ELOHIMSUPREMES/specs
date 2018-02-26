%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

Name: ipopt
Version: 3.10.1
Release: alt4.svn20120128
Summary: Large-Scale Nonlinear Optimization Solver (Interior Point OPTimizer)
License: CPL 1.0
Group: Sciences/Mathematics
Url: http://www.coin-or.org/projects/Ipopt.xml
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: Ipopt-%version.tar.gz

BuildPreReq: liblapack-devel libparmetis-devel libmumps-devel
BuildPreReq: gcc-fortran gcc-c++ %mpiimpl-devel libscotch-devel
BuildPreReq: libblacs-devel libscalapack-devel CoinBuildTools

%description
Ipopt (Interior Point OPTimizer, pronounced I-P-Opt) is a software
package for large-scale nonlinear optimization. It is designed to find
(local) solutions of mathematical optimization problems of the from

   min     f(x)
   x in R^n

   s.t.       g_L <= g(x) <= g_U
              x_L <=  x   <= x_U

where f(x): R^n --> R is the objective function, and g(x): R^n --> R^m
are the constraint functions. The vectors g_L and g_U denote the lower
and upper bounds on the constraints, and the vectors x_L and x_U are the
bounds on the variables x. The functions f(x) and g(x) can be nonlinear
and nonconvex, but should be twice continuously differentiable. Note
that equality constraints can be formulated in the above formulation by
setting the corresponding components of g_L and g_U to the same value.

%package -n lib%name
Summary: Shared libraries of Ipopt
Group: System/Libraries

%description -n lib%name
Ipopt (Interior Point OPTimizer, pronounced I-P-Opt) is a software
package for large-scale nonlinear optimization. It is designed to find
(local) solutions of mathematical optimization problems.

This package contains shared libraries of Ipopt.

%package -n lib%name-devel
Summary: Development files of Ipopt
Group: Development/Other
Requires: lib%name = %version-%release

%description -n lib%name-devel
Ipopt (Interior Point OPTimizer, pronounced I-P-Opt) is a software
package for large-scale nonlinear optimization. It is designed to find
(local) solutions of mathematical optimization problems.

This package contains development files of Ipopt.

%package -n lib%name-devel-doc
Summary: Documentation for Ipopt
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
Ipopt (Interior Point OPTimizer, pronounced I-P-Opt) is a software
package for large-scale nonlinear optimization. It is designed to find
(local) solutions of mathematical optimization problems.

This package contains development documentation for Ipopt.

%package examples
Summary: Examples for Ipopt
Group: Development/Documentation
BuildArch: noarch

%description examples
Ipopt (Interior Point OPTimizer, pronounced I-P-Opt) is a software
package for large-scale nonlinear optimization. It is designed to find
(local) solutions of mathematical optimization problems.

This package contains examples for Ipopt.

%prep
%setup

mkdir -p BuildTools
cp -f %_datadir/BuildTools/* %_datadir/libtool/*.m4 \
	BuildTools/

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed -Wl,-rpath,%mpidir/lib -L%mpidir/lib"

INCS="-I%_includedir/parmetis -I%mpidir/include"
%add_optflags $INCS %optflags_shared -DHAVE_SNPRINTF
sed -i 's|@MPIDIR@|%mpidir|g' Ipopt/configure.ac
sed -i "s|@TOPDIR@|$PWD|g" Ipopt/configure.ac
%autoreconf
#run_autotools

#pushd Ipopt
MUMPS="-lcmumps -ldmumps -lsmumps -lzmumps -lmumps_common -lpord"
BLASLAPACK="-llapack -lopenblas"
%configure \
	--disable-mumps-libcheck \
	--with-blas="$BLASLAPACK" \
	--with-lapack="$BLASLAPACK" \
	--with-metis="-L%mpidir/lib -lparmetis" \
	--with-metis-incdir=%mpidir/include/metis \
	--with-mumps-incdir=%_includedir \
	--with-mumps-lib="$MUMPS"
sed -i '1a\echo=echo' libtool
%make_build TOPDIR=$PWD
#popd

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed -Wl,-rpath,%mpidir/lib -L%mpidir/lib"

#pushd Ipopt
%makeinstall_std TOPDIR=$PWD

pushd Ipopt/src/LinAlg
	for i in *.hpp; do
		if [ "$i" != "IpMatrix.hpp" -a "$i" != IpSymMatrix.hpp -a "$i" != "IpVector.hpp" ];
		then
			install -p -m644 $i %buildroot%_includedir/coin
		fi
	done
popd
install -p -m644 Ipopt/src/LinAlg/TMatrices/*.hpp \
	%buildroot%_includedir/coin
pushd Ipopt/src/Algorithm
	for i in *.hpp */*.hpp; do
		cp $i %buildroot%_includedir/coin/ ||:
	done
popd

cp -fR Ipopt/tutorial Ipopt/doc/documentation.pdf Ipopt/examples \
	%buildroot%_docdir/coin/Ipopt/
#popd

rm -fR %buildroot%_datadir/coin/doc

%files
%doc ChangeLog Ipopt/AUTHORS Ipopt/LICENSE Ipopt/README

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%dir %_includedir/coin
%_includedir/coin/*
%_pkgconfigdir/*

%files -n lib%name-devel-doc
%dir %_docdir/coin
%doc %_docdir/coin/Ipopt
%exclude %_docdir/coin/Ipopt/examples

%files examples
%dir %_docdir/coin
%dir %_docdir/coin/Ipopt
%_docdir/coin/Ipopt/examples

%changelog
* Sat Aug 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.10.1-alt4.svn20120128
- Built with OpenBLAS instead of GotoBLAS2

* Tue Jun 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.10.1-alt3.svn20120128
- Rebuilt with OpenMPI 1.6

* Wed Jun 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.10.1-alt2.svn20120128
- Fixed build

* Sun Feb 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.10.1-alt1.svn20120128
- Version 3.10.1

* Sun Sep 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.10.0-alt1.svn20110903
- Version 3.10.0

* Sat Apr 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.3-alt1.svn20110414
- Version 3.9.3

* Thu Apr 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.1-alt1.svn20101209.4
- Rebuilt

* Sat Apr 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.1-alt1.svn20101209.3
- Built with GotoBLAS2 instead of ATLAS

* Mon Feb 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.1-alt1.svn20101209.2
- Added -g into compiler flags

* Fri Feb 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.1-alt1.svn20101209.1
- Rebuilt for debuginfo

* Thu Dec 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.1-alt1.svn20101209
- Version 3.9.1

* Thu Oct 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.3-alt1.svn20100820.2
- Rebuilt for soname set-versions

* Thu Oct 14 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.3-alt1.svn20100820.1
- Fixed overlinking of libraries

* Wed Sep 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.3-alt1.svn20100820
- Version 3.8.3

* Tue Jun 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.1-alt1.svn20100621
- New snapshot

* Wed Feb 24 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.1-alt1.20091222
- New snapshot

* Tue Jan 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.1-alt1
- Version 3.8.1

* Fri Sep 04 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.0-alt2
- Rebuilt with shared libraries of requirements instead static
- Fixed fprintf using

* Tue Aug 04 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.0-alt1
- Initial build for Sisyphus

