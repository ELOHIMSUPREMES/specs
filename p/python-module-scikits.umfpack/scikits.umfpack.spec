%define mname scikits
%define oname %mname.umfpack

%def_with python3

Name: python-module-%oname
Epoch: 1
Version: 0.1
Release: alt2.git20150223
Summary: Python interface to UMFPACK sparse direct solver
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/scikit-umfpack/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/rc/scikit-umfpack.git
Source: %name-%version.tar

BuildPreReq: liblapack-devel swig libsuitesparse-devel
BuildPreReq: python-devel python-module-setuptools-tests swig
BuildPreReq: python-module-scipy libnumpy-devel
BuildPreReq: python-module-nose
BuildPreReq: python-module-sphinx-devel python-module-numpydoc
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-scipy libnumpy-py3-devel
BuildPreReq: python3-module-nose
%endif

%py_provides %oname
%py_requires %mname scipy numpy

%description
scikit-umfpack provides wrapper of UMFPACK sparse direct solver to
SciPy.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires nose

%description tests
scikit-umfpack provides wrapper of UMFPACK sparse direct solver to
SciPy.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Python interface to UMFPACK sparse direct solver
Group: Development/Python3
%py3_provides %oname
%py3_requires %mname scipy numpy

%description -n python3-module-%oname
scikit-umfpack provides wrapper of UMFPACK sparse direct solver to
SciPy.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires nose

%description -n python3-module-%oname-tests
scikit-umfpack provides wrapper of UMFPACK sparse direct solver to
SciPy.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
scikit-umfpack provides wrapper of UMFPACK sparse direct solver to
SciPy.

This package contains pickles for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

python setup.py build_ext -i
export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
pushd ~
export PYTHONPATH=%buildroot%python_sitelibdir
nosetests -v scikits.umfpack
popd
%if_with python3
pushd ../python3
pushd ~
export PYTHONPATH=%buildroot%python3_sitelibdir
nosetests3 -v scikits.umfpack
popd
popd
%endif

%files
%doc README docs/_build/html
%python_sitelibdir/%mname/umfpack
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/umfpack/tests

%files tests
%python_sitelibdir/%mname/umfpack/tests

%files pickles
%python_sitelibdir/*/pickle

%if_with python3
%files -n python3-module-%oname
%doc README docs/_build/html
%python3_sitelibdir/%mname/umfpack
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/%mname/umfpack/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/%mname/umfpack/tests
%endif

%changelog
* Tue Apr 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.1-alt2.git20150223
- Rebuilt with updated NumPy

* Sun Mar 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.1-alt1.git20150223
- Initial build for Sisyphus

