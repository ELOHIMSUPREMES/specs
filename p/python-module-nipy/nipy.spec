%define oname nipy

%def_enable docs
%def_with python3

Name: python-module-%oname
Version: 0.4.0
Release: alt3.git20140617
Summary: The neuroimaging in python (NIPY) project
License: MIT
Group: Development/Python
Url: http://neuroimaging.scipy.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# git://github.com/nipy/nipy.git
Source: %oname-%version.tar.gz

Requires: %oname-data

BuildPreReq: python-devel python-module-nifti python-module-scipy
BuildPreReq: python-module-sympy liblapack-devel python-module-matplotlib
BuildPreReq: /proc gcc-fortran %oname-data libnumpy-devel sympy
BuildPreReq: dvipng libniftilib-devel
BuildPreReq: python-module-nibabel python-module-Cython
BuildPreReq: python-module-sphinx-devel python-module-Pygments
BuildPreReq: graphviz ghostscript-utils
BuildPreReq: %py_dependencies pl
BuildPreReq: xvfb-run python-module-pygobject3 python-module-pycairo
%setup_python_module %oname
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-nibabel libnumpy-py3-devel
BuildPreReq: python3-module-scipy python3-module-sympy
%endif

%description
The neuroimaging in python (NIPY) project is an environment for the
analysis of structural and functional neuroimaging data. It currently
has a full system for general linear modeling of functional magnetic
resonance imaging (fMRI).

%package -n python3-module-%oname
Summary: The neuroimaging in python (NIPY) project
Group: Development/Python3
Requires: %oname-data

%description -n python3-module-%oname
The neuroimaging in python (NIPY) project is an environment for the
analysis of structural and functional neuroimaging data. It currently
has a full system for general linear modeling of functional magnetic
resonance imaging (fMRI).

%package -n python3-module-%oname-tests
Summary: Tests for neuroimaging in python (NIPY) project
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
The neuroimaging in python (NIPY) project is an environment for the
analysis of structural and functional neuroimaging data. It currently
has a full system for general linear modeling of functional magnetic
resonance imaging (fMRI).

This package contains tests for NIPY.

%package examples
Summary: Examples for neuroimaging in python (NIPY) project
Group: Development/Documentation
Requires: %name = %version-%release

%description examples
The neuroimaging in python (NIPY) project is an environment for the
analysis of structural and functional neuroimaging data. It currently
has a full system for general linear modeling of functional magnetic
resonance imaging (fMRI).

This package contains examples for NIPY.

%package tests
Summary: Tests for neuroimaging in python (NIPY) project
Group: Development/Python
Requires: %name = %version-%release

%description tests
The neuroimaging in python (NIPY) project is an environment for the
analysis of structural and functional neuroimaging data. It currently
has a full system for general linear modeling of functional magnetic
resonance imaging (fMRI).

This package contains tests for NIPY.

%if_enabled docs

%package docs
Summary: Documentation for neuroimaging in python (NIPY) project
Group: Development/Documentation
#BuildArch: noarch

%description docs
The neuroimaging in python (NIPY) project is an environment for the
analysis of structural and functional neuroimaging data. It currently
has a full system for general linear modeling of functional magnetic
resonance imaging (fMRI).

This package contains documentation for NIPY.

%package pickles
Summary: Pickles for neuroimaging in python (NIPY) project
Group: Development/Python

%description pickles
The neuroimaging in python (NIPY) project is an environment for the
analysis of structural and functional neuroimaging data. It currently
has a full system for general linear modeling of functional magnetic
resonance imaging (fMRI).

This package contains pickles for NIPY.

%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%if_enabled docs
sed -i 's|@PYVER@|%_python_version|g' doc/Makefile
%prepare_sphinx .
%endif

rm -f doc/labs/image_registration.rst

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

export PYTHONPATH=%buildroot%python_sitelibdir

mkdir -p ~/.matplotlib
cp %python_sitelibdir/matplotlib/mpl-data/matplotlibrc ~/.matplotlib/
sed -i 's|^\(backend\).*|\1 : PDF|' ~/.matplotlib/matplotlibrc

%if_enabled docs
xvfb-run make -C doc pickle
xvfb-run make -C doc html
#make -C doc pdf
%endif

install fff2.py %buildroot%python_sitelibdir
cp -fR examples %buildroot%python_sitelibdir/%oname/

%if_enabled docs
#mkdir -p doc/pdf
#for i in $(find doc -name '*.pdf'); do
#	cp -f $i doc/pdf/
#done

cp -fR doc/build/pickle %buildroot%python_sitelibdir/%oname/
%endif

# bad syntax
rm -f %buildroot%python_sitelibdir/nipy/examples/ds105/parallel_run.py

%files
%doc AUTHOR Changelog LICENSE README* THANKS
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%if_enabled docs
%exclude %python_sitelibdir/%oname/pickle
%endif
%exclude %python_sitelibdir/*/examples
%exclude %python_sitelibdir/*/test*
%exclude %python_sitelibdir/*/*/tests
%exclude %python_sitelibdir/*/*/*/tests
%exclude %python_sitelibdir/*/*/*/testing
%exclude %python_sitelibdir/*/*/*/*/tests
#exclude %python_sitelibdir/*/*/*/*/*/tests
%exclude %python_sitelibdir/*/*/*/test

%if_enabled docs
%files docs
%doc doc/build/html/*
#doc doc/pdf

%files pickles
%dir %python_sitelibdir/%oname
%python_sitelibdir/%oname/pickle
%endif

%files examples
%python_sitelibdir/*/examples

%files tests
%python_sitelibdir/*/*/*/test
%python_sitelibdir/*/test*
%python_sitelibdir/*/*/tests
%python_sitelibdir/*/*/*/tests
%python_sitelibdir/*/*/*/testing
%python_sitelibdir/*/*/*/*/tests
#python_sitelibdir/*/*/*/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc AUTHOR Changelog LICENSE README* THANKS
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*
%exclude %python3_sitelibdir/*/*/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*
%python3_sitelibdir/*/*/*/*/tests
%endif

%changelog
* Sat Aug 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt3.git20140617
- Enabled docs
- Added module for Python 3

* Mon Jul 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt2.git20140617
- New snapshot

* Wed Nov 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt2.git20131031
- New snapshot

* Thu Sep 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt2.git20130903
- Moved all tests into tests subpackage

* Wed Sep 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1.git20130903
- New snapshot

* Tue Apr 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1.git20130205
- Version 0.4.0

* Sun Aug 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt2.git20120705
- Built with OpenBLAS instead of GotoBLAS2

* Tue Jul 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20120705
- Version 0.2.0
- Disabled docs (what's wrong in girar-builder?)

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.2-alt2.git20110404.1
- Rebuild to remove redundant libpython2.7 dependency

* Mon Nov 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt2.git20110404
- Enabled docs (except pdf)

* Tue Nov 15 2011 Dmitry V. Levin <ldv@altlinux.org> 0.1.2-alt1.git20110404.2
- Removed Mayavi from package requirements.

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.2-alt1.git20110404.1
- Rebuild with Python-2.7

* Sat Apr 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.git20110404
- New snapshot
- Build with GotoBLAS2 instead of ATLAS

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.git20101104.2
- Rebuilt with python-module-sphinx-devel

* Sat Mar 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.git20101104.1
- Rebuilt for debuginfo

* Wed Nov 24 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.git20101104
- New snapshot

* Mon Oct 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.git20100828.2
- Fixed underlinking

* Tue Sep 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.git20100828.1
- Moved all tests into tests package

* Mon Sep 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.git20100828
- New snapshot
- Fixed build of docs

* Tue Jun 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.git20100601
- New snapshot

* Sun Mar 07 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.bzr20100301
- New snapshot
- Extracted examples and tests into separate packages
- Added docs and pickles packages

* Mon Jan 11 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.bzr20090924.3
- Rebuilt with new NumPy

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.bzr20090924.2
- Rebuilt with python 2.6

* Fri Oct 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.bzr20090924.1
- Added necessary requitements: nipy-data, python2.x(enthought)

* Fri Sep 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.bzr20090924
- Initial build for Sisyphus

