# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt3.2
%define oname zope.app.dtmlpage

%def_with python3

Name: python-module-%oname
Version: 3.5.0
#Release: alt3.1
Summary: DTML Page -- A Zope 3 Content Component
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.dtmlpage/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires ZODB3 zope.annotation zope.app.publication zope.app.preview
%py_requires zope.app.testing zope.container zope.documenttemplate
%py_requires zope.filerepresentation zope.interface zope.schema
%py_requires zope.security zope.traversing

%description
This package provides a Zope 3 content component that contains DTML
code, which is executed when the component is accessed via its URL.

%package -n python3-module-%oname
Summary: DTML Page -- A Zope 3 Content Component
Group: Development/Python3
%py3_requires ZODB3 zope.annotation zope.app.publication zope.app.preview
%py3_requires zope.app.testing zope.container zope.documenttemplate
%py3_requires zope.filerepresentation zope.interface zope.schema
%py3_requires zope.security zope.traversing

%description -n python3-module-%oname
This package provides a Zope 3 content component that contains DTML
code, which is executed when the component is accessed via its URL.

%package -n python3-module-%oname-tests
Summary: Tests for zope.app.dtmlpage
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.app.testing zope.app.preference
%py3_requires zope.app.securitypolicy zope.app.zcmlfiles

%description -n python3-module-%oname-tests
This package provides a Zope 3 content component that contains DTML
code, which is executed when the component is accessed via its URL.

This package contains tests for zope.app.dtmlpage.

%package tests
Summary: Tests for zope.app.dtmlpage
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.app.preference
%py_requires zope.app.securitypolicy zope.app.zcmlfiles

%description tests
This package provides a Zope 3 content component that contains DTML
code, which is executed when the component is accessed via its URL.

This package contains tests for zope.app.dtmlpage.

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
%exclude %python_sitelibdir/*/*/*/test*

%files tests
%python_sitelibdir/*/*/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*/test*
%exclude %python3_sitelibdir/*/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/test*
%python3_sitelibdir/*/*/*/*/test*
%endif

%changelog
* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 3.5.0-alt3.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.5.0-alt3.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.5.0-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Jul 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.0-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt1
- Initial build for Sisyphus

