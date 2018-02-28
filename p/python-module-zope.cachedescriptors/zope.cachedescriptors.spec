%define oname zope.cachedescriptors

%def_with python3

Name: python-module-%oname
Version: 4.1.1
Release: alt1.dev0.git20150204
Summary: Method and property caching decorators
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.cachedescriptors/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-zope.testrunner
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-zope.testrunner
%endif

%py_requires zope

%description
Cached descriptors cache their output. They take into account instance
attributes that they depend on, so when the instance attributes change,
the descriptors will change the values they return.

Cached descriptors cache their data in _v_ attributes, so they are also
useful for managing the computation of volatile attributes for
persistent objects.

%package -n python3-module-%oname
Summary: Method and property caching decorators
Group: Development/Python3
%py3_requires zope

%description -n python3-module-%oname
Cached descriptors cache their output. They take into account instance
attributes that they depend on, so when the instance attributes change,
the descriptors will change the values they return.

Cached descriptors cache their data in _v_ attributes, so they are also
useful for managing the computation of volatile attributes for
persistent objects.

%package -n python3-module-%oname-tests
Summary: Tests for zope.cachedescriptors
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
Cached descriptors cache their output. They take into account instance
attributes that they depend on, so when the instance attributes change,
the descriptors will change the values they return.

Cached descriptors cache their data in _v_ attributes, so they are also
useful for managing the computation of volatile attributes for
persistent objects.

This package contains tests for zope.cachedescriptors.

%package tests
Summary: Tests for zope.cachedescriptors
Group: Development/Python
Requires: %name = %version-%release

%description tests
Cached descriptors cache their output. They take into account instance
attributes that they depend on, so when the instance attributes change,
the descriptors will change the values they return.

Cached descriptors cache their data in _v_ attributes, so they are also
useful for managing the computation of volatile attributes for
persistent objects.

This package contains tests for zope.cachedescriptors.

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

%check
python setup.py test -v
%if_with python3
pushd ../python3
python3 setup.py test -v
popd
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
* Sat Aug 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1.dev0.git20150204
- Version 4.1.1.dev0
- Enabled check

* Mon Dec 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1
- Version 4.1.0

* Fri Jul 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt2
- Added module for Python 3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1
- Version 4.0.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.1-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.1-alt2
- Added necesssary requirements
- Excluded *.pth

* Sat May 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.1-alt1
- Initial build for Sisyphus

