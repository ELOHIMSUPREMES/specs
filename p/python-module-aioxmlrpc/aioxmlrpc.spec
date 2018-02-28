%define oname aioxmlrpc

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.1
Release: alt1.git20141112.1.1
Summary: XML-RPC for asyncio
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/aioxmlrpc/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mardiros/aioxmlrpc.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-asyncio python-module-aiohttp
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-asyncio python3-module-aiohttp
%endif

%py_provides %oname
%py_requires asyncio aiohttp

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python3 python3-base python3-module-asyncio python3-module-cffi python3-module-chardet python3-module-cryptography python3-module-django python3-module-dns python3-module-enum34 python3-module-greenlet python3-module-gunicorn python3-module-paste python3-module-psycopg2 python3-module-pycares python3-module-pycparser python3-module-pytest python3-module-setuptools python3-module-yaml python3-module-zope python3-module-zope.interface
BuildRequires: python3-module-aiohttp python3-module-setuptools-tests rpm-build-python3

%description
Asyncio version of the standard lib xmlrpc.

Currently only aioxmlrpc.client, which works like xmlrpc.client but with
coroutine is implemented.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Asyncio version of the standard lib xmlrpc.

Currently only aioxmlrpc.client, which works like xmlrpc.client but with
coroutine is implemented.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: XML-RPC for asyncio
Group: Development/Python3
%py3_provides %oname
%py3_requires asyncio aiohttp

%description -n python3-module-%oname
Asyncio version of the standard lib xmlrpc.

Currently only aioxmlrpc.client, which works like xmlrpc.client but with
coroutine is implemented.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Asyncio version of the standard lib xmlrpc.

Currently only aioxmlrpc.client, which works like xmlrpc.client but with
coroutine is implemented.

This package contains tests for %oname.

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
%endif
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%if_with python2
%files
%doc *.rst examples
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.rst examples
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt1.git20141112.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1-alt1.git20141112.1
- NMU: Use buildreq for BR.

* Thu Jan 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20141112
- Initial build for Sisyphus

