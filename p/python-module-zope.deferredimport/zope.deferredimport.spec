%define oname zope.deferredimport

%def_with python3

Name: python-module-%oname
Version: 4.1.0
Release: alt1
Summary: Allows you to perform imports names that will be resolved when used in the code
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.deferredimport/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope zope.proxy

%description
Often, especially for package modules, you want to import names for
convenience, but not actually perform the imports until necessary. The
zope.deferredimport package provided facilities for defining names in
modules that will be imported from somewhere else when used. You can
also cause deprecation warnings to be issued when a variable is used.

%package -n python3-module-%oname
Summary: Allows you to perform imports names that will be resolved when used in the code
Group: Development/Python3
%py3_requires zope zope.proxy

%description -n python3-module-%oname
Often, especially for package modules, you want to import names for
convenience, but not actually perform the imports until necessary. The
zope.deferredimport package provided facilities for defining names in
modules that will be imported from somewhere else when used. You can
also cause deprecation warnings to be issued when a variable is used.

%package -n python3-module-%oname-tests
Summary: Tests for zope.deferredimport
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing

%description -n python3-module-%oname-tests
Often, especially for package modules, you want to import names for
convenience, but not actually perform the imports until necessary. The
zope.deferredimport package provided facilities for defining names in
modules that will be imported from somewhere else when used. You can
also cause deprecation warnings to be issued when a variable is used.

This package contains tests for zope.deferredimport.

%package tests
Summary: Tests for zope.deferredimport
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
Often, especially for package modules, you want to import names for
convenience, but not actually perform the imports until necessary. The
zope.deferredimport package provided facilities for defining names in
modules that will be imported from somewhere else when used. You can
also cause deprecation warnings to be issued when a variable is used.

This package contains tests for zope.deferredimport.

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

%files
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%endif

%changelog
* Mon Dec 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1
- Version 4.1.0

* Mon Jul 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt2
- Added module for Python 3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1
- Version 4.0.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.3-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.3-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.3-alt1
- Initial build for Sisyphus

