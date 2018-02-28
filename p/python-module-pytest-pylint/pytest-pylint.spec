%define oname pytest-pylint

%def_with python3

Name: python-module-%oname
Version: 0.1.0
Release: alt1.git20150423.1
Summary: pytest plugin to check source code with pylint
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-pylint/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/carsongee/pytest-pylint.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests pylint
BuildPreReq: python-module-pytest-pep8
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests pylint-py3
BuildPreReq: python3-module-pytest-pep8
%endif

%py_provides pytest_pylint
%py_requires pytest pylint pytest_pep8

%description
Run pylint with pytest and have configurable rule types (i.e.
Convention, Warn, and Error) fail the build. You can also specify a
pylintrc file.

%if_with python3
%package -n python3-module-%oname
Summary: pytest plugin to check source code with pylint
Group: Development/Python3
%py3_provides pytest_pylint
%py3_requires pytest pylint pytest_pep8

%description -n python3-module-%oname
Run pylint with pytest and have configurable rule types (i.e.
Convention, Warn, and Error) fail the build. You can also specify a
pylintrc file.
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
%doc *.rst pylintrc
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst pylintrc
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.0-alt1.git20150423.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Apr 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.git20150423
- Initial build for Sisyphus

