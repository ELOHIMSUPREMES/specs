%define oname pytest-variables

%def_with python3

Name: python-module-%oname
Version: 1.1
Release: alt1.git20150716
Summary: pytest plugin for providing variables to tests/fixtures
License: MPLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-variables/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/davehunt/pytest-variables.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides pytest_variables
%py_requires pytest

%description
pytest-variables is a plugin for py.test that provides variables to
tests/fixtures as a dict via a JSON file specified on the command line.

%if_with python3
%package -n python3-module-%oname
Summary: pytest plugin for providing variables to tests/fixtures
Group: Development/Python3
%py3_provides pytest_variables
%py3_requires pytest

%description -n python3-module-%oname
pytest-variables is a plugin for py.test that provides variables to
tests/fixtures as a dict via a JSON file specified on the command line.
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
python setup.py test -v
%if_with python3
pushd ../python3
python3 setup.py test -v
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
* Wed Jul 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.git20150716
- Initial build for Sisyphus

