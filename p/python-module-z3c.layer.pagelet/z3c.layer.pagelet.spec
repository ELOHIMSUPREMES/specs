%define oname z3c.layer.pagelet
Name: python-module-%oname
Version: 2.0.0
Release: alt1.a1
Summary: Pagelet layer setup for Zope 3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.layer.pagelet/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires z3c.pagelet z3c.template zope.authentication zope.browser
%py_requires zope.browserresource zope.component zope.interface
%py_requires zope.login zope.publisher

Requires: python-module-z3c.layer

%description
This package provides a pagelet based layer setup for Zope3.

%package tests
Summary: Tests for Pagelet layer setup for Zope 3
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testbrowser zope.app.wsgi zope.exceptions
%py_requires zope.principalregistry zope.publisher zope.security
%py_requires zope.securitypolicy zope.testing

%description tests
This package provides a pagelet based layer setup for Zope3.

This package contains tests for Pagelet layer setup for Zope 3.

%package -n python-module-z3c.layer
Summary: Core package of z3c.layer
Group: Development/Python

%description -n python-module-z3c.layer
This package contains core package of z3c.layer.

%prep
%setup

%build
%python_build

%install
%python_install

%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

touch %buildroot%python_sitelibdir/z3c/layer/__init__.py

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/*/test*
%exclude %python_sitelibdir/z3c/layer/__init__.py*

%files tests
%python_sitelibdir/*/*/*/test*

%files -n python-module-z3c.layer
%dir %python_sitelibdir/z3c/layer
%python_sitelibdir/z3c/layer/__init__.py*

%changelog
* Fri Apr 05 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.a1
- Version 2.0.0a1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.9.0-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.0-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.0-alt1
- Initial build for Sisyphus

