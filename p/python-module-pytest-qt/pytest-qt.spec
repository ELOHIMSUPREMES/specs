%define oname pytest-qt

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 1.2.2
Release: alt1.git20141105
Summary: pytest plugin for Qt (PyQt and PySide) application testing
License: LGPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-qt/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/nicoddemus/pytest-qt.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-PyQt4 python-module-PySide
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-PyQt4 python3-module-PySide
%endif

%py_provides pytestqt
%py_requires PyQt4 PySide

%description
pytest-qt is a pytest plugin that allows programmers to write tests for
PySide and PyQt applications.

%package -n python3-module-%oname
Summary: pytest plugin for Qt (PyQt and PySide) application testing
Group: Development/Python3
%py3_provides pytestqt
%py3_requires PyQt4 PySide

%description -n python3-module-%oname
pytest-qt is a pytest plugin that allows programmers to write tests for
PySide and PyQt applications.

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
%doc *.rst docs/*.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/*.rst
%python3_sitelibdir/*
%endif

%changelog
* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt1.git20141105
- Initial build for Sisyphus

