%define oname pyramid_restler

%def_with python3

Name: python-module-%oname
Version: 0.1a4
Release: alt3
Summary: RESTful views for Pyramid
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/pyramid_restler/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires pyramid

%description
pyramid_restler is a somewhat-opinionated toolkit for building RESTful
Web services and applications on top of the Pyramid framework.
Essentially, it routes HTTP requests to Pyramid views. These views
interact with model entities via a uniform context interface, and then
respond with appropriate status codes and entity representations.

%package -n python3-module-%oname
Summary: RESTful views for Pyramid
Group: Development/Python3
%py3_requires pyramid

%description -n python3-module-%oname
pyramid_restler is a somewhat-opinionated toolkit for building RESTful
Web services and applications on top of the Pyramid framework.
Essentially, it routes HTTP requests to Pyramid views. These views
interact with model entities via a uniform context interface, and then
respond with appropriate status codes and entity representations.

%package -n python3-module-%oname-tests
Summary: Tests for pyramid_restler
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
pyramid_restler is a somewhat-opinionated toolkit for building RESTful
Web services and applications on top of the Pyramid framework.
Essentially, it routes HTTP requests to Pyramid views. These views
interact with model entities via a uniform context interface, and then
respond with appropriate status codes and entity representations.

This package contains tests for pyramid_restler.

%package tests
Summary: Tests for pyramid_restler
Group: Development/Python
Requires: %name = %version-%release

%description tests
pyramid_restler is a somewhat-opinionated toolkit for building RESTful
Web services and applications on top of the Pyramid framework.
Essentially, it routes HTTP requests to Pyramid views. These views
interact with model entities via a uniform context interface, and then
respond with appropriate status codes and entity representations.

This package contains tests for pyramid_restler.

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

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc *.txt examples
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*
%exclude %python_sitelibdir/examples

%files tests
%python_sitelibdir/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt examples
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/examples

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*
%endif

%changelog
* Thu Jul 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1a4-alt3
- Added module for Python 3

* Fri Sep 20 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1a4-alt2
- Removed %python_sitelibdir/examples from main package

* Thu Sep 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1a4-alt1
- Version 0.1a4

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1a3-alt1
- Version 0.1a3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1a1-alt1.1
- Rebuild with Python-2.7

* Thu Jul 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1a1-alt1
- Initial build for Sisyphus

