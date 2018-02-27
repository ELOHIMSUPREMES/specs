%define oname aiohttp-wsgi

%def_without python2
%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.1.2
Release: alt1.git20150331
Summary: WSGI adapter for aiohttp
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/aiohttp-wsgi/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/etianen/aiohttp-wsgi.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-aiohttp python-module-nose
BuildPreReq: python-module-coverage
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-aiohttp python3-module-nose
BuildPreReq: python3-module-coverage
%endif

%py_provides aiohttp_wsgi
%py_requires aiohttp

%description
aiohttp-wsgi is a WSGI adapter for aiohttp.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
aiohttp-wsgi is a WSGI adapter for aiohttp.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: WSGI adapter for aiohttp
Group: Development/Python3
%py3_provides aiohttp_wsgi
%py3_requires aiohttp

%description -n python3-module-%oname
aiohttp-wsgi is a WSGI adapter for aiohttp.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
aiohttp-wsgi is a WSGI adapter for aiohttp.

This package contains tests for %oname.
%endif

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
python setup.py test
nosetests -v --cover-package=aiohttp_wsgi --cover-erase --with-coverage
%endif
%if_with python3
pushd ../python3
python3 setup.py test
nosetests3 -v --cover-package=aiohttp_wsgi --cover-erase --with-coverage
popd
%endif

%if_with python2
%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test*

%files tests
%python_sitelibdir/*/test*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*
%endif

%changelog
* Tue Apr 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.git20150331
- Initial build for Sisyphus

