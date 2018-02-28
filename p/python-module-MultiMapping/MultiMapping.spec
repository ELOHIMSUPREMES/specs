%define oname MultiMapping
Name: python-module-%oname
Version: 3.0
Release: alt1.dev0.git20150411
Summary: Special MultiMapping objects used in Zope2
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/MultiMapping/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopefoundation/MultiMapping.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-Zope2-tests

%py_requires ExtensionClass

%description
MultiMapping provides special objects used in some Zope2 internals like
ZRDB.

%package tests
Summary: Tests for MultiMapping
Group: Development/Python
Requires: %name = %version-%release

%description tests
MultiMapping provides special objects used in some Zope2 internals like
ZRDB.

This package contains tests for MultiMapping.

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
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%changelog
* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0-alt1.dev0.git20150411
- Version 3.0.dev0

* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.1-alt1.dev.git20130313
- Version 2.13.1dev
- Enabled testing

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.13.0-alt2.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.13.0-alt2.1
- Rebuild with Python-2.7

* Tue Jun 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.0-alt2
- Added necessary requirements

* Sat Jun 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.0-alt1
- Initial build for Sisyphus

