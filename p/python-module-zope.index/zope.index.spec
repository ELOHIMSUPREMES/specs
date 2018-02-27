%define oname zope.index
Name: python-module-%oname
Version: 4.0.1
Release: alt1
Summary: Indices for using with catalog like text, field, etc.
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.index/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope ZODB3 zope.interface

%description
The zope.index package provides several indices for the Zope catalog.
These include:

  * a field index (for indexing orderable values),
  * a keyword index,
  * a topic index,
  * a text index (with support for lexicon, splitter, normalizer, etc.)

%package tests
Summary: Tests for zope.index
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
The zope.index package provides several indices for the Zope catalog.
These include:

  * a field index (for indexing orderable values),
  * a keyword index,
  * a topic index,
  * a text index (with support for lexicon, splitter, normalizer, etc.)

This package contains tests for zope.index.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests*
%exclude %python_sitelibdir/*/*/*/tests*

%files tests
%python_sitelibdir/*/*/tests*
%python_sitelibdir/*/*/*/tests*

%changelog
* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1
- Version 4.0.1

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.3-alt1.1
- Rebuild to remove redundant libpython2.7 dependency

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.3-alt1
- Version 3.6.3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.1-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt1
- Initial build for Sisyphus

