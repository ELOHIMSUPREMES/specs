%define oname zope.minmax

%def_with python3

Name: python-module-%oname
Version: 2.0.0
Release: alt2
Summary: Homogeneous values favoring maximum or minimum for ZODB conflict resolution
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.minmax/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope ZODB3 zope.interface

%description
This package provides support for homogeneous values favoring maximum or
minimum for ZODB conflict resolution.

%package -n python3-module-%oname
Summary: Homogeneous values favoring maximum or minimum for ZODB conflict resolution
Group: Development/Python3
%py3_requires zope ZODB3 zope.interface

%description -n python3-module-%oname
This package provides support for homogeneous values favoring maximum or
minimum for ZODB conflict resolution.

%package -n python3-module-%oname-tests
Summary: Tests for zope.minmax
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
This package provides support for homogeneous values favoring maximum or
minimum for ZODB conflict resolution.

This package contains tests for zope.minmax.

%package tests
Summary: Tests for zope.minmax
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package provides support for homogeneous values favoring maximum or
minimum for ZODB conflict resolution.

This package contains tests for zope.minmax.

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
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%endif

%changelog
* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt2
- Added module for Python 3

* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1
- Version 2.0.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.2-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt2
- Added necessary requirements
- Excluded *.pth

* Sun May 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt1
- Initial build for Sisyphus

