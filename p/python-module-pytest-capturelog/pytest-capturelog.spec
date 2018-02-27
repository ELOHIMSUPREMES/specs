%define oname pytest-capturelog

%def_with python3

Name: python-module-%oname
Version: 0.7
Release: alt1
Summary: py.test plugin to capture log messages
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-capturelog/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides pytest_capturelog
%py_requires pytest

%description
py.test plugin to capture log messages.

%package -n python3-module-%oname
Summary: py.test plugin to capture log messages
Group: Development/Python3
%py3_provides pytest_capturelog
%py3_requires pytest

%description -n python3-module-%oname
py.test plugin to capture log messages.

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
%doc README
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc README
%python3_sitelibdir/*
%endif

%changelog
* Wed Feb 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1
- Initial build for Sisyphus

