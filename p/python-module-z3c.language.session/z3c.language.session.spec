%define oname z3c.language.session
Name: python-module-%oname
Version: 1.0.2
Release: alt3
Summary: Zope3 i18n language session
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.language.session/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.app.generations zope.component zope.interface
%py_requires zope.publisher zope.session

Requires: python-module-z3c.language = %EVR

%description
This package provides a session which can be used to store a language.
See z3c.language.negotiator for a sample usage.

%package tests
Summary: Tests for Zope3 i18n language session
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing z3c.coverage

%description tests
This package provides a session which can be used to store a language.
See z3c.language.negotiator for a sample usage.

This package contains tests for Zope3 i18n language session.

%package -n python-module-z3c.language
Summary: Core package of z3c.language
Group: Development/Python

%description -n python-module-z3c.language
This package contains core package of z3c.language.

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

touch %buildroot%python_sitelibdir/z3c/language/__init__.py

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/*/tests.*
%exclude %python_sitelibdir/z3c/language/__init__.py*

%files tests
%python_sitelibdir/*/*/*/tests.*

%files -n python-module-z3c.language
%python_sitelibdir/z3c/language/__init__.py*

%changelog
* Fri Apr 05 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt3
- Added python-module-z3c.language

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.2-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus

