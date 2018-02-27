%define oname simplecosine

%def_with python3

Name: python-module-%oname
Version: 1.0
Release: alt1
Summary: Simple cosine distance
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/simplecosine/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-numpy
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-numpy
%endif

%py_provides %oname
%py_requires numpy

%description
Simple cosine distance.

%if_with python3
%package -n python3-module-%oname
Summary: Simple cosine distance
Group: Development/Python3
%py3_provides %oname
%py3_requires numpy

%description -n python3-module-%oname
Simple cosine distance.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

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

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%endif

%changelog
* Mon Mar 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus

