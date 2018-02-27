%define oname z3c.widgets.flashupload
Name: python-module-%oname
Version: 1.0c1
Release: alt3
Summary: Zope Flash Upload Widget
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.widgets.flashupload/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.component zope.event zope.filerepresentation
%py_requires zope.i18nmessageid zope.interface zope.publisher
%py_requires zope.security zope.traversing zope.app.cache
%py_requires zope.app.component zope.app.container zope.app.pagetemplate

Requires: python-module-z3c.widgets = %EVR

%description
A Zope specific flash upload widget.

%package tests
Summary: Tests for Zope Flash Upload Widget
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing zope.app.testing

%description tests
A Zope specific flash upload widget.

This package contains tests for Zope Flash Upload Widget.

%package -n python-module-z3c.widgets
Summary: Core package of z3c.widgets
Group: Development/Python

%description -n python-module-z3c.widgets
This package contains core package of z3c.widgets.

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

touch %buildroot%python_sitelibdir/z3c/widgets/__init__.py

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/*/tests.*
%exclude %python_sitelibdir/z3c/widgets/__init__.py*

%files tests
%python_sitelibdir/*/*/*/tests.*

%files -n python-module-z3c.widgets
%python_sitelibdir/z3c/widgets/__init__.py*

%changelog
* Mon Apr 08 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0c1-alt3
- Added python-module-z3c.widgets

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0c1-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0c1-alt2
- Added necesssary requirements
- Excluded *.pth

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0c1-alt1
- Initial build for Sisyphus

