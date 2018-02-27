%define oname pluggy

%def_with python3

Name: python-module-%oname
Version: 0.3.0
Release: alt1.git20150528
Summary: Plugin and hook calling mechanisms for python
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pluggy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/hpk42/pluggy.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname

%description
This is the plugin manager as used by pytest but stripped of pytest
specific details.

%if_with python3
%package -n python3-module-%oname
Summary: Plugin and hook calling mechanisms for python
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
This is the plugin manager as used by pytest but stripped of pytest
specific details.
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
py.test -vv
%if_with python3
pushd ../python3
python3 setup.py test -v
py.test-%_python3_version -vv
popd
%endif

%files
%doc CHANGELOG *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc CHANGELOG *.rst
%python3_sitelibdir/*
%endif

%changelog
* Tue Jul 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1.git20150528
- Initial build for Sisyphus

