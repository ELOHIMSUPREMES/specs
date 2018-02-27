%define oname pytest-tornado

%def_with python3

Name: python-module-%oname
Version: 0.4.2
Release: alt1.git20150219
Summary: Fixtures and markers to simplify testing of asynchronous tornado applications
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-tornado/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/eugeniy/pytest-tornado.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-tornado
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-tornado
%endif

%py_provides pytest_tornado
%py_requires pytest tornado.testing

%description
A py.test plugin providing fixtures and markers to simplify testing of
asynchronous tornado applications.

%package -n python3-module-%oname
Summary: Fixtures and markers to simplify testing of asynchronous tornado applications
Group: Development/Python3
%py3_provides pytest_tornado
%py3_requires pytest tornado.testing

%description -n python3-module-%oname
A py.test plugin providing fixtures and markers to simplify testing of
asynchronous tornado applications.

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
export PYTHONPATH=$PWD
py.test -vv
%if_with python3
pushd ../python3
python3 setup.py test
export PYTHONPATH=$PWD
py.test-%_python3_version -vv
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1.git20150219
- Initial build for Sisyphus

