# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt2.a1.2
%define oname z3c.configurator

%def_with python3

Name: python-module-%oname
Version: 2.0.0
#Release: alt2.a1.1
Summary: Dynamic configuration for Zope3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.configurator/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope.component zope.i18nmessageid zope.interface
%py_requires zope.schema

%description
This package provides a configurator which is designed to extend a
component after its creation for Zope3.

%package -n python3-module-%oname
Summary: Dynamic configuration for Zope3
Group: Development/Python3
%py3_requires zope.component zope.i18nmessageid zope.interface
%py3_requires zope.schema

%description -n python3-module-%oname
This package provides a configurator which is designed to extend a
component after its creation for Zope3.

%package -n python3-module-%oname-tests
Summary: Tests for Dynamic configuration for Zope3
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.annotation zope.dublincore zope.formlib
%py3_requires zope.securitypolicy zope.testbrowser zope.testing
%py3_requires zope.app.pagetemplate zope.app.testing zope.app.zcmlfiles

%description -n python3-module-%oname-tests
This package provides a configurator which is designed to extend a
component after its creation for Zope3.

This package contains tests for Dynamic configuration for Zope3.

%package tests
Summary: Tests for Dynamic configuration for Zope3
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.annotation zope.dublincore zope.formlib
%py_requires zope.securitypolicy zope.testbrowser zope.testing
%py_requires zope.app.pagetemplate zope.app.testing zope.app.zcmlfiles

%description tests
This package provides a configurator which is designed to extend a
component after its creation for Zope3.

This package contains tests for Dynamic configuration for Zope3.

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
%exclude %python_sitelibdir/*/*/*/test*

%files tests
%python_sitelibdir/*/*/test*
%python_sitelibdir/*/*/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*
%exclude %python3_sitelibdir/*/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*
%python3_sitelibdir/*/*/*/*/test*
%endif

%changelog
* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 2.0.0-alt2.a1.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.0-alt2.a1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.0-alt2.a1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt2.a1
- Added module for Python 3

* Thu Apr 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.a1
- Version 2.0.0a1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3.0-alt2.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt2
- Added necessary requirements
- Excluded *.pth

* Wed Jun 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1
- Initial build for Sisyphus

