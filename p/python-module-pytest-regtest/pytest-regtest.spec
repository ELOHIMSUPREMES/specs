%define oname pytest-regtest

%def_with python3

Name: python-module-%oname
Version: 0.4.1
Release: alt1.git20141120
Summary: py.test plugin for regression tests
License: GPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-regtest/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://sissource.ethz.ch/uweschmitt/pytest-regtest.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BUildPreReq: python-tools-2to3
%endif

%py_provides pytest_regtest

%description
This pytest-plugin allows capturing of output of test functions which
can be compared to the captured output from former runs. This is a
common technique to start TDD if you have to refactor legacy code which
ships without tests.

%package -n python3-module-%oname
Summary: py.test plugin for regression tests
Group: Development/Python3
%py3_provides pytest_regtest

%description -n python3-module-%oname
This pytest-plugin allows capturing of output of test functions which
can be compared to the captured output from former runs. This is a
common technique to start TDD if you have to refactor legacy code which
ships without tests.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.git20141120
- Version 0.4.1

* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1.git20141114
- Initial build for Sisyphus

