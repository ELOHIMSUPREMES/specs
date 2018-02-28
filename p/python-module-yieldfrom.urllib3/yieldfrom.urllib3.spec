%define mname yieldfrom
%define oname %mname.urllib3

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.1.2
Release: alt2.git20141229.1
Summary: Asyncio HTTP library with thread-safe connection pooling, file post, and more
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/yieldfrom.urllib3/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/rdbhost/yieldfromUrllib3.git
Source: %name-%version.tar

%if_with python2
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-asyncio python-module-nose
#BuildPreReq: python-module-yieldfrom.http.client
#BuildPreReq: python-module-tornado
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-asyncio python3-module-nose
#BuildPreReq: python3-module-yieldfrom.http.client
#BuildPreReq: python3-module-tornado
%endif

%py_provides %oname
Requires: python-module-%mname = %EVR
%py_requires asyncio
%py_requires yieldfrom.http.client

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python3 python3-base python3-module-pytest python3-module-setuptools python3-module-zope.interface
BuildRequires: python3-module-nose python3-module-pycares python3-module-setuptools-tests python3-module-yieldfrom.http.client python3-module-zope rpm-build-python3

%description
Yieldfrom is a project to port various useful Python 3 libraries, both
standard library and otherwise, to work under Asyncio. The intention is
to have the port be as alike as possible to the original, so that the
learning curve is minimal, and to make porting dependent modules as easy
as possible.

This package is a port of the Urllib3 package.

%package -n python3-module-%oname
Summary: Asyncio HTTP library with thread-safe connection pooling, file post, and more
Group: Development/Python3
%py3_provides %oname
Requires: python3-module-%mname = %EVR
%py3_requires asyncio
%py3_requires yieldfrom.http.client

%description -n python3-module-%oname
Yieldfrom is a project to port various useful Python 3 libraries, both
standard library and otherwise, to work under Asyncio. The intention is
to have the port be as alike as possible to the original, so that the
learning curve is minimal, and to make porting dependent modules as easy
as possible.

This package is a port of the Urllib3 package.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_provides %mname

%description -n python-module-%mname
Core files of %mname.

%package -n python3-module-%mname
Summary: Core files of %mname
Group: Development/Python3
%py3_provides %mname

%description -n python3-module-%mname
Core files of %mname.

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

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -d %buildroot%python_sitelibdir/%mname
install -p -m644 %mname/__init__.py \
	%buildroot%python_sitelibdir/%mname/
%if_with python3
pushd ../python3
install -p -m644 %mname/__init__.py \
	%buildroot%python3_sitelibdir/%mname/
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
%doc *.txt *.rst
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/__init__.py*
%endif

%files -n python-module-%mname
%dir %python_sitelibdir/%mname
%python_sitelibdir/%mname/__init__.py*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/%mname/*
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/%mname/__init__.*
%exclude %python3_sitelibdir/%mname/__pycache__/__init__.*

%files -n python3-module-%mname
%dir %python3_sitelibdir/%mname
%dir %python3_sitelibdir/%mname/__pycache__
%python3_sitelibdir/%mname/__init__.*
%python3_sitelibdir/%mname/__pycache__/__init__.*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.2-alt2.git20141229.1
- NMU: Use buildreq for BR.

* Sun Jan 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt2.git20141229
- Added necessary requirements
- Enabled testing

* Sun Jan 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.git20141229
- Initial build for Sisyphus

