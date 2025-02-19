# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt4.2
%define oname z3c.rmldocument

%def_with python3

Name: python-module-%oname
Version: 1.0
#Release: alt4.1
Summary: User-editable RML documents
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.rmldocument/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires z3c.rml zope.app.pagetemplate lxml

%description
z3c.rmldocument -- User-editable RML for PDF generation.

Provides a document object that has user-editable blocks of RML within a
defined RML template.

Also provides a UI widget for editing an RML subset and choose fields
that should get dynamically embedded.

%package -n python3-module-%oname
Summary: User-editable RML documents
Group: Development/Python3
%py3_requires z3c.rml zope.app.pagetemplate lxml

%description -n python3-module-%oname
z3c.rmldocument -- User-editable RML for PDF generation.

Provides a document object that has user-editable blocks of RML within a
defined RML template.

Also provides a UI widget for editing an RML subset and choose fields
that should get dynamically embedded.

%package -n python3-module-%oname-tests
Summary: Tests for User-editable RML documents
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
z3c.rmldocument -- User-editable RML for PDF generation.

Provides a document object that has user-editable blocks of RML within a
defined RML template.

Also provides a UI widget for editing an RML subset and choose fields
that should get dynamically embedded.

This package contains tests for User-editable RML documents.

%package -n python3-module-%oname-examples
Summary: Examples for User-editable RML documents
Group: Development/Documentation
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-examples
z3c.rmldocument -- User-editable RML for PDF generation.

Provides a document object that has user-editable blocks of RML within a
defined RML template.

Also provides a UI widget for editing an RML subset and choose fields
that should get dynamically embedded.

This package contains examples for User-editable RML documents.

%package tests
Summary: Tests for User-editable RML documents
Group: Development/Python
Requires: %name = %version-%release

%description tests
z3c.rmldocument -- User-editable RML for PDF generation.

Provides a document object that has user-editable blocks of RML within a
defined RML template.

Also provides a UI widget for editing an RML subset and choose fields
that should get dynamically embedded.

This package contains tests for User-editable RML documents.

%package examples
Summary: Examples for User-editable RML documents
Group: Development/Documentation
Requires: %name = %version-%release

%description examples
z3c.rmldocument -- User-editable RML for PDF generation.

Provides a document object that has user-editable blocks of RML within a
defined RML template.

Also provides a UI widget for editing an RML subset and choose fields
that should get dynamically embedded.

This package contains examples for User-editable RML documents.

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
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*
%exclude %python_sitelibdir/*/*/examples

%files tests
%python_sitelibdir/*/*/tests.*

%files examples
%python_sitelibdir/*/*/examples

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*
%exclude %python3_sitelibdir/*/*/examples

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%oname-examples
%python3_sitelibdir/*/*/examples
%endif

%changelog
* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 1.0-alt4.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0-alt4.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0-alt4.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jul 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt4
- Added moduel for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt3.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt3
- Added necessary requirements
- Excluded *.pth

* Fri Jun 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt2
- Extracted examples into separate package

* Sun Jun 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus

