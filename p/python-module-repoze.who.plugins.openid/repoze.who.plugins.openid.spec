# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt2.2
%define oname repoze.who.plugins.openid

%def_with python3

Name: python-module-%oname
Version: 0.5.3
#Release: alt2.1
Summary: An OpenID plugin for repoze.who
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.who.plugins.openid/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires repoze.who.plugins openid webob zope.interface repoze.who

%description
repoze.who.plugins.openid is a plugin for the repoze.who framework
enabling OpenID logins.

%package -n python3-module-%oname
Summary: An OpenID plugin for repoze.who
Group: Development/Python3
%py3_requires repoze.who.plugins openid webob zope.interface repoze.who

%description -n python3-module-%oname
repoze.who.plugins.openid is a plugin for the repoze.who framework
enabling OpenID logins.

%package -n python3-module-%oname-tests
Summary: Tests for repoze.who.plugins.openid
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
repoze.who.plugins.openid is a plugin for the repoze.who framework
enabling OpenID logins.

This package contains tests for repoze.who.plugins.openid.

%package tests
Summary: Tests for repoze.who.plugins.openid
Group: Development/Python
Requires: %name = %version-%release

%description tests
repoze.who.plugins.openid is a plugin for the repoze.who framework
enabling OpenID logins.

This package contains tests for repoze.who.plugins.openid.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install
%if "%python_sitelibdir_noarch" != "%python_sitelibdir"
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

%files
%doc *.txt docs/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/*/*/tests

%files tests
%python_sitelibdir/*/*/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt docs/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/*/tests
%endif

%changelog
* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 0.5.3-alt2.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.3-alt2.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.3-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jul 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.3-alt2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.3-alt1.1
- Rebuild with Python-2.7

* Fri Jul 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.3-alt1
- Initial build for Sisyphus

