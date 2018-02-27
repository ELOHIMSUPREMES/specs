%define oname aiomanhole

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.2.1
Release: alt1.git20140914
Summary: Python module to provide a manhole in asyncio applications
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/aiomanhole/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/nathan-hoad/aiomanhole.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-asyncio
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-asyncio
%endif

%py_provides %oname
%py_requires asyncio

%description
Manhole for accessing asyncio applications. This is useful for debugging
application state in situations where you have access to the process,
but need to access internal application state.

%package -n python3-module-%oname
Summary: Python module to provide a manhole in asyncio applications
Group: Development/Python3
%py3_provides %oname
%py3_requires asyncio

%description -n python3-module-%oname
Manhole for accessing asyncio applications. This is useful for debugging
application state in situations where you have access to the process,
but need to access internal application state.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%if_with python2
%python_build_debug
%endif

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python2
%python_install
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
%if_with python2
py.test -vv
%endif
%if_with python3
pushd ../python3
py.test-%_python3_version -vv
popd
%endif

%if_with python2
%files
%doc *.rst
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Jan 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.git20140914
- Initial build for Sisyphus

