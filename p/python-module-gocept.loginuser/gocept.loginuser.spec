%define mname gocept
%define oname %mname.loginuser
Name: python-module-%oname
Version: 1.0.1
Release: alt1
Summary: Sqlalchemy user object and password management
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/gocept.loginuser/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-SQLAlchemy python-module-bcrypt
BuildPreReq: python-module-gocept.testing

%py_provides %oname
%py_requires %mname sqlalchemy bcrypt

%description
Sqlalchemy user object and password management.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires gocept.testing

%description tests
Sqlalchemy user object and password management.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test

%files
%doc *.txt doc/*.txt
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests

%files tests
%python_sitelibdir/%mname/*/tests

%changelog
* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus

