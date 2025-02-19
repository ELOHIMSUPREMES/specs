# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt2.2
%define oname z3c.tabular

%def_with python3

Name: python-module-%oname
Version: 0.6.2
#Release: alt2.1
Summary: Table with form support based on z3c.form and z3c.table for Zope3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.tabular/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires z3c.form z3c.formui z3c.table z3c.template
%py_requires zope.i18nmessageid zope.interface

%description
This package provides a table implementation including form support for
Zope3 based on z3c.form and z3c.table.

%package -n python3-module-%oname
Summary: Table with form support based on z3c.form and z3c.table for Zope3
Group: Development/Python3
%py3_requires z3c.form z3c.formui z3c.table z3c.template
%py3_requires zope.i18nmessageid zope.interface

%description -n python3-module-%oname
This package provides a table implementation including form support for
Zope3 based on z3c.form and z3c.table.

%package -n python3-module-%oname-tests
Summary: Tests for z3c.tabular
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires z3c.form z3c.macro z3c.testing zope.app.publisher
%py3_requires zope.app.testing zope.browserpage zope.publisher
%py3_requires zope.testing

%description -n python3-module-%oname-tests
This package provides a table implementation including form support for
Zope3 based on z3c.form and z3c.table.

This package contains tests for z3c.tabular.

%package tests
Summary: Tests for z3c.tabular
Group: Development/Python
Requires: %name = %version-%release
%py_requires z3c.form z3c.macro z3c.testing zope.app.publisher
%py_requires zope.app.testing zope.browserpage zope.publisher
%py_requires zope.testing

%description tests
This package provides a table implementation including form support for
Zope3 based on z3c.form and z3c.table.

This package contains tests for z3c.tabular.

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
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*
%endif

%changelog
* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 0.6.2-alt2.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.2-alt2.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.2-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jul 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt2
- Added module for Python 3

* Mon Apr 08 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt1
- Version 0.6.2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.0-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt2
- Added necessary requirements
- Excluded *.pth

* Sun May 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1
- Initial build for Sisyphus

