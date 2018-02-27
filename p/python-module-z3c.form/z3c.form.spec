%define oname z3c.form

%def_with python3

Name: python-module-%oname
Version: 3.2.1
Release: alt1
Summary: An advanced form and widget framework for Zope 3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.form
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope.browser zope.component zope.configuration
%py_requires zope.contentprovider zope.event zope.i18n
%py_requires zope.i18nmessageid zope.interface zope.lifecycleevent
%py_requires zope.location zope.pagetemplate zope.publisher zope.schema
%py_requires zope.security zope.traversing

%description
This package provides an implementation for HTML forms and widgets. The
goal is to provide a simple API but with the ability to easily customize
any data or steps.

%package -n python3-module-%oname
Summary: An advanced form and widget framework for Zope 3
Group: Development/Python3
%py3_requires zope.browser zope.component zope.configuration
%py3_requires zope.contentprovider zope.event zope.i18n
%py3_requires zope.i18nmessageid zope.interface zope.lifecycleevent
%py3_requires zope.location zope.pagetemplate zope.publisher zope.schema
%py3_requires zope.security zope.traversing

%description -n python3-module-%oname
This package provides an implementation for HTML forms and widgets. The
goal is to provide a simple API but with the ability to easily customize
any data or steps.

%package -n python3-module-%oname-tests
Summary: Tests for z3c.form
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires lxml z3c.coverage z3c.template zc.sourcefactory
%py3_requires zope.app.component zope.app.container zope.app.pagetemplate
%py3_requires zope.app.security zope.app.testing zope.testing

%description -n python3-module-%oname-tests
This package provides an implementation for HTML forms and widgets. The
goal is to provide a simple API but with the ability to easily customize
any data or steps.

This package contains tests for z3c.form.

%package tests
Summary: Tests for z3c.form
Group: Development/Python
Requires: %name = %version-%release
%py_requires lxml z3c.coverage z3c.template zc.sourcefactory
%py_requires zope.app.component zope.app.container zope.app.pagetemplate
%py_requires zope.app.security zope.app.testing zope.testing

%description tests
This package provides an implementation for HTML forms and widgets. The
goal is to provide a simple API but with the ability to easily customize
any data or steps.

This package contains tests for z3c.form.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
export LC_ALL=en_US.UTF-8

%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
export LC_ALL=en_US.UTF-8

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
* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1
- Version 3.2.1

* Mon Dec 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.5-alt1
- Version 3.0.5

* Tue Sep 24 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.3-alt1
- Version 3.0.3

* Thu Apr 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0-alt1.a2
- Version 3.0.0a2

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt1
- Version 2.5.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4.3-alt2.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.3-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.3-alt1
- Initial build for Sisyphus

