%define oname zope.structuredtext
Name: python-module-%oname
Version: 4.0.0
Release: alt1
Summary: StructuredText parser
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.structuredtext/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope

%description
This package provides a parser and renderers for the classic Zope
"structured text" markup dialect (STX). STX is a plain text markup in
which document structure is signalled primarily by identation

%package tests
Summary: Tests for StructuredText parser
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package provides a parser and renderers for the classic Zope
"structured text" markup dialect (STX). STX is a plain text markup in
which document structure is signalled primarily by identation

This package contains tests for StructuredText parser.

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

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%changelog
* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1
- Version 4.0.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.1-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.1-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.1-alt1
- Initial build for Sisyphus

