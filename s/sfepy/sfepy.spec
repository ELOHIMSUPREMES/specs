%def_with python3

Name: sfepy
Version: 2015.1
Release: alt1.git20150311
Summary: Simple finite elements in Python (SfePy)
License: New BSD License
Group: Sciences/Mathematics
Url: http://sfepy.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/sfepy/sfepy.git
Source: %name-%version.tar.gz
Source1: README.1st

Requires: python-module-%name = %version-%release

BuildRequires(pre): rpm-build-python
BuildPreReq: python-devel python-module-scikits.umfpack libsuitesparse-devel
BuildPreReq: python-module-pyparsing ipython pytables swig
BuildPreReq: libtetgen-devel libnetgen-devel libnumpy-devel
BuildPreReq: doxygen graphviz texlive-latex-extra dvipng
BuildPreReq: python-module-sphinx-devel python-module-Pygments
BuildPreReq: python-module-tables-tests python-module-Pyrex xvfb-run
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python-tools-2to3 libnumpy-py3-devel
BuildPreReq: python3-module-scipy python3-module-matplotlib
BuildPreReq: python3-module-tables-tests python3-module-Cython
%endif

%description
A finite element analysis software based primarily on NumPy and SciPy.

%if_with python3
%package py3
Summary: Simple finite elements in Python (SfePy)
Group: Sciences/Mathematics
Requires: python3-module-%name = %version-%release

%description py3
A finite element analysis software based primarily on NumPy and SciPy.

%package -n python3-module-%name
Summary: Python module of Simple finite elements (SfePy)
Group: Development/Python3
Requires: tetgen gmsh netgen
%py3_requires pyparsing scikits.umfpack tables IPython
%add_python3_req_skip vtk

%description -n python3-module-%name
A finite element analysis software based primarily on NumPy and SciPy.

This package contains python module of SfePy.
%endif

%package -n python-module-%name
Summary: Python module of Simple finite elements (SfePy)
Group: Development/Python
%setup_python_module %name
Requires: tetgen gmsh netgen
#py_requires matplotlib.backends.backend_gtkagg
%py_requires matplotlib.backends.backend_wxagg
%py_requires pyparsing scikits.umfpack tables IPython
%if "%__python_version" != "2.5"
%py_requires multiprocessing
%endif

%description -n python-module-%name
A finite element analysis software based primarily on NumPy and SciPy.

This package contains python module of SfePy.

%package data
Summary: Data files for Simple finite elements in Python (SfePy)
Group: Sciences/Mathematics
BuildArch: noarch

%description data
A finite element analysis software based primarily on NumPy and SciPy.

This package contains data files for SfePy.

%package doc
Summary: Documentation for Simple finite elements in Python (SfePy)
Group: Documentation
BuildArch: noarch

%description doc
A finite element analysis software based primarily on NumPy and SciPy.

This package contains documentation for SfePy.

%package -n python-module-%name-pickles
Summary: Pickles for Simple finite elements in Python (SfePy)
Group: Development/Python

%description  -n python-module-%name-pickles
A finite element analysis software based primarily on NumPy and SciPy.

This package contains pickles for SfePy.

%if_with python3
%package -n python3-module-%name-tests
Summary: Tests for Simple finite elements in Python (SfePy)
Group: Development/Python3
Requires: python3-module-%name = %version-%release

%description  -n python3-module-%name-tests
A finite element analysis software based primarily on NumPy and SciPy.

This package contains tests for SfePy.
%endif

%package -n python-module-%name-tests
Summary: Tests for Simple finite elements in Python (SfePy)
Group: Development/Python
Requires: python-module-%name = %version-%release

%description  -n python-module-%name-tests
A finite element analysis software based primarily on NumPy and SciPy.

This package contains tests for SfePy.

%if_with python3
%package -n python3-module-%name-examples
Summary: Examples for Simple finite elements in Python (SfePy)
Group: Development/Python3
Requires: python3-module-%name = %version-%release

%description  -n python3-module-%name-examples
A finite element analysis software based primarily on NumPy and SciPy.

This package contains examples for SfePy.
%endif

%package -n python-module-%name-examples
Summary: Examples for Simple finite elements in Python (SfePy)
Group: Development/Python
Requires: python-module-%name = %version-%release

%description  -n python-module-%name-examples
A finite element analysis software based primarily on NumPy and SciPy.

This package contains examples for SfePy.

%prep
%setup
ln -s types.h sfepy/discrete/fem/extmods/types_s.h

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec \
	sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' '{}' +
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

install -m644 %SOURCE1 .

cp %python_sitelibdir/matplotlib/mpl-data/matplotlibrc ~/.matplotlibrc
sed -i 's|^\(backend\).*|\1 : Agg|' ~/.matplotlibrc

%prepare_sphinx .
sed -i 's|@PYVER@|%_python_version|g' doc/Makefile

%build
export PYTHONPATH=$PWD:$PWD/script
%add_optflags -fno-strict-aliasing
export CFLAGS="%optflags"
xvfb-run --server-args="-screen 0 1024x768x24" \
	python setup.py build
#python_build_debug build_ext
#pushd sfepy/terms
#sed -i "28s|\(terms.i'\)|\1, '*.c'|" extmods/setup.py
#python_build_debug build_ext
#popd

%if_with python3
export CFLAGS="%optflags $(pkg-config python3 --cflags)"
pushd ../python3
xvfb-run --server-args="-screen 0 1024x768x24" \
	python3 setup.py build
popd
%endif

%install
export PYTHONPATH=$PWD:$PWD/script

%if_with python3
pushd ../python3
xvfb-run --server-args="-screen 0 1024x768x24" \
	python3 setup.py install --root=%buildroot
popd
touch %buildroot%python3_sitelibdir/%name/script/__init__.py
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i ${i}3
done
popd
%endif

xvfb-run --server-args="-screen 0 1024x768x24" \
	python setup.py install --root=%buildroot
#python_install
#pushd sfepy/terms
#python_install
#popd
touch %buildroot%python_sitelibdir/%name/script/__init__.py

export PYTHONPATH=%buildroot%python_sitelibdir
pushd doc
doxygen doxygen.config
export LC_ALL=en_US.UTF-8
xvfb-run --server-args="-screen 0 1024x768x24" \
	make -C doc/latex
#make_build -C doc/latex
#make_build pickle
popd
install -p -m644 homogen.py %buildroot%python_sitelibdir

#generate_pickles doc doc %name

install -d %buildroot%_docdir/%name/pdf
install -m644 doc/doc/latex/*.pdf %buildroot%_docdir/%name/pdf
cp -fR doc/doc/html %buildroot%_docdir/%name/
#cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%name/

%files
%doc AUTHORS LICENSE README doc/txt/*.txt
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif

%files -n python-module-%name
%python_sitelibdir/*
#exclude %python_sitelibdir/%name/pickle
%exclude %python_sitelibdir/%name/tests
%exclude %python_sitelibdir/%name/base/testing.py*
%exclude %python_sitelibdir/%name/examples

#files data
#_datadir/%name

%files doc
%_docdir/%name

#files -n python-module-%name-pickles
#python_sitelibdir/%name/pickle

%files -n python-module-%name-tests
%python_sitelibdir/%name/tests
%python_sitelibdir/%name/base/testing.py*

%files -n python-module-%name-examples
%python_sitelibdir/%name/examples

%if_with python3
%files py3
%doc AUTHORS LICENSE README doc/txt/*.txt
%_bindir/*.py3

%files -n python3-module-%name
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%name/tests
%exclude %python3_sitelibdir/%name/base/testing.py
%exclude %python3_sitelibdir/%name/base/__pycache__/testing.*
%exclude %python3_sitelibdir/%name/examples

%files -n python3-module-%name-tests
%python3_sitelibdir/%name/tests
%python3_sitelibdir/%name/base/testing.py
%python3_sitelibdir/%name/base/__pycache__/testing.*

%files -n python3-module-%name-examples
%python3_sitelibdir/%name/examples
%endif

%changelog
* Thu Mar 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2015.1-alt1.git20150311
- Version 2015.1
- Added module for Python 3

* Mon Nov 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2014.3-alt1.git20141030
- Version 2014.3

* Sat Aug 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2014.2-alt1.git20140807
- New snapshot

* Thu Jul 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2014.2-alt1.git20140708
- Version 2014.2

* Wed May 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2014.1-alt1.git20140506
- Version 2014.1

* Thu Oct 24 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2013.3-alt1.git20131021
- Version 2013.3

* Mon Jul 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2013.2-alt1.git20130726
- Version 2013.2

* Sun Jun 16 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2012.4-alt2.git20130203
- Rebuilt with updated NumPy

* Tue Feb 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2012.4-alt1.git20130203
- Version 2012.4

* Sun Feb 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2012.2-alt3.git20120830
- Rebuilt

* Tue Oct 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2012.2-alt2.git20120830
- Rebuilt with updated NumPy

* Tue Sep 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2012.2-alt1.git20120830
- Version 2012.2

* Fri Jun 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2011.1-alt2.git20110405
- Disabled requirement on matplotlib.backends.backend_gtkagg

* Mon Apr 16 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2011.1-alt1.git20110405.2.1
- Rebuild to remove redundant libpython2.7 dependency

* Tue Nov 15 2011 Dmitry V. Levin <ldv@altlinux.org> 2011.1-alt1.git20110405.2
- Removed Mayavi from package requirements.

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2011.1-alt1.git20110405.1
- Rebuild with Python-2.7

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2011.1-alt1.git20110405
- Version 2011.1

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2010.3-alt1.git20101115.2
- Rebuilt with python-module-sphinx-devel

* Tue Mar 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2010.3-alt1.git20101115.1
- Rebuilt for debuginfo

* Tue Nov 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2010.3-alt1.git20101115
- Version 2010.3

* Mon Oct 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2010.2-alt1.git20100715.1
- Fixed underlinking

* Mon Jul 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2010.2-alt1.git20100715
- Version 2010.2

* Sat Mar 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2010.1-alt1.git20100304
- Version 2010.1
- Added pickles package

* Sat Feb 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2009.4-alt1.git20100205.1
- Added extension modules

* Sat Feb 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2009.4-alt1.git20100205
- New snapshot
- Rebuilt with reformed NumPy

* Sat Dec 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2009.4-alt1.git20091211
- Version 2009.4
- Rebuilt with texlive instead of tetex

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2009.3-alt1.git20090902.1
- Rebuilt with python 2.6

* Mon Sep 14 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2009.3-alt1.git20090902
- Initial build for Sisyphus

