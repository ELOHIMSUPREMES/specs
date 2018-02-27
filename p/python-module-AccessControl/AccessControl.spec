%define oname AccessControl

Name: python-module-%oname
Version: 3.0.11
Release: alt1.git20141102
Summary: Security framework for Zope2
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/AccessControl/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopefoundation/AccessControl.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-Zope2-tests
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-zope.deferredimport
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.security
BuildPreReq: python-module-zope.testing

%py_requires Acquisition DateTime ExtensionClass Persistence Record
%py_requires RestrictedPython transaction zExceptions ZODB3
%py_requires zope.component zope.configuration zope.deferredimport
%py_requires zope.interface zope.publisher zope.schema zope.security
%py_requires zope.testing

%description
AccessControl provides a general security framework for use in Zope2.

%package tests
Summary: Tests for Security framework for Zope2
Group: Development/Python
Requires: %name = %version-%release

%description tests
AccessControl provides a general security framework for use in Zope2.

This package contains tests for Security framework for Zope2.

%prep
%setup

%build
%python_build

%install
%python_install

%check
python setup.py test

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%changelog
* Tue Nov 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.11-alt1.git20141102
- Version 3.0.11

* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.10-alt1.dev.git20140808
- Version 3.0.10dev
- Enabled testing

* Fri Jul 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.8-alt3
- Return requirement on ZODB3

* Wed Jul 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.8-alt2
- Avoid requirement on ZODB3

* Mon Sep 16 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.8-alt1
- Version 3.0.8

* Tue Feb 12 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.6-alt1
- Version 3.0.6

* Fri Sep 21 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.4-alt1
- Version 3.0.4

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.13.4-alt2.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.13.4-alt2.1
- Rebuild with Python-2.7

* Tue Jun 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.4-alt2
- Added necessary requirements

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.4-alt1
- Initial build for Sisyphus

