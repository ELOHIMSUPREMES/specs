%define oname zope.browsermenu

%def_with python3

Name: python-module-%oname
Version: 4.1.1
Release: alt1
Summary: Browser menu implementation for Zope
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.browsermenu/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-zope.browser python-module-zope.configuration
BuildPreReq: python-module-zope.i18nmessageid python-module-zope.pagetemplate
BuildPreReq: python-module-zope.publisher python-module-zope.schema
BuildPreReq: python-module-zope.security python-module-zope.traversing
BuildPreReq: python-module-zope.testrunner python-module-zope.component-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-zope.browser python3-module-zope.configuration
BuildPreReq: python3-module-zope.i18nmessageid python3-module-zope.pagetemplate
BuildPreReq: python3-module-zope.publisher python3-module-zope.schema
BuildPreReq: python3-module-zope.security python3-module-zope.traversing
BuildPreReq: python3-module-zope.testrunner python3-module-zope.component-tests
%endif

%py_requires zope zope.browser zope.component zope.configuration
%py_requires zope.i18nmessageid zope.interface zope.pagetemplate
%py_requires zope.publisher zope.schema zope.security zope.traversing

%description
This package provides an implementation of browser menus and ZCML
directives for configuring them.

%package -n python3-module-%oname
Summary: Browser menu implementation for Zope
Group: Development/Python3
%py3_requires zope zope.browser zope.component zope.configuration
%py3_requires zope.i18nmessageid zope.interface zope.pagetemplate
%py3_requires zope.publisher zope.schema zope.security zope.traversing

%description -n python3-module-%oname
This package provides an implementation of browser menus and ZCML
directives for configuring them.

%package -n python3-module-%oname-tests
Summary: Tests for zope.browsermenu
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing zope.testrunner

%description -n python3-module-%oname-tests
This package provides an implementation of browser menus and ZCML
directives for configuring them.

This package contains tests for zope.browsermenu.

%package tests
Summary: Tests for zope.browsermenu
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing zope.testrunner

%description tests
This package provides an implementation of browser menus and ZCML
directives for configuring them.

This package contains tests for zope.browsermenu.

%prep
%setup

%if_with python3
cp -fR . ../python3
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
%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

%check
python setup.py test -v
#if_with python3
%if 0
pushd ../python3
python3 setup.py test -v
popd
%endif

%files
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests
%endif

%changelog
* Fri Aug 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1
- Version 4.1.1
- Enabled check

* Thu Dec 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt3
- Version 4.1.0

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt2.a1
- Added module for Python 3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1.a1
- Version 4.1.0a1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.9.1-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.1-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.1-alt1
- Initial build for Sisyphus

