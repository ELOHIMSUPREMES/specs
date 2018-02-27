%define oname jsonm

%def_with python3

Name: python-module-%oname
Version: 1.0.11
Release: alt1.git20150126
Summary: Python object to (json + redis)
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/jsonm/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/dantezhu/jsonm.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-redis-py
BuildPreReq: python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-redis-py
%endif

%py_provides %oname
%py_requires json

%description
Python object to (json + redis).

%package -n python3-module-%oname
Summary: Python object to (json + redis)
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Python object to (json + redis).

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
%doc *.md examples
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md examples
%python3_sitelibdir/*
%endif

%changelog
* Tue Jan 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.11-alt1.git20150126
- Version 1.0.11

* Fri Jan 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.git20150122
- Initial build for Sisyphus

