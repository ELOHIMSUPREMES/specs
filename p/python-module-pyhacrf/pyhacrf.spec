%define oname pyhacrf

%def_with python3

Name: python-module-%oname
Version: 0.0.12
Release: alt1.git20150818.1
Summary: Hidden alignment conditional random field, discriminative string edit distance
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/pyhacrf
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/dirko/pyhacrf.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-Cython libnumpy-devel
BuildPreReq: python-module-pylbfgs
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-Cython libnumpy-py3-devel
BuildPreReq: python3-module-pylbfgs
%endif

%py_provides %oname
%py_requires numpy pylbfgs

%description
Hidden alignment conditional random field for classifying string pairs -
a learnable edit distance.

This package aims to implement the HACRF machine learning model with a
sklearn-like interface. It includes ways to fit a model to training
examples and score new example.

%if_with python3
%package -n python3-module-%oname
Summary: Hidden alignment conditional random field, discriminative string edit distance
Group: Development/Python3
%py3_provides %oname
%py3_requires numpy pylbfgs

%description -n python3-module-%oname
Hidden alignment conditional random field for classifying string pairs -
a learnable edit distance.

This package aims to implement the HACRF machine learning model with a
sklearn-like interface. It includes ways to fit a model to training
examples and score new example.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%add_optflags -fno-strict-aliasing

cython %oname/algorithms.pyx
%python_build_debug

%if_with python3
pushd ../python3
cython3 %oname/algorithms.pyx
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

%check
%ifnarch %ix86
python setup.py test -v
python setup.py build_ext -i
py.test -vv
%if_with python3
pushd ../python3
python3 setup.py test -v
python3 setup.py build_ext -i
py.test-%_python3_version -vv
popd
%endif
%endif

%files
%doc *.rst *.md examples
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst *.md examples
%python3_sitelibdir/*
%endif

%changelog
* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.12-alt1.git20150818.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Sun Aug 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.12-alt1.git20150818
- Initial build for Sisyphus

