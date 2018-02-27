%define mname collective
%define oname %mname.funkload

%def_disable check

Name: python-module-%oname
Version: 0.5
Release: alt1.dev0.git20140620
Summary: Zope and Plone focussed extensions to funkload
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.funkload/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.funkload.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests funkload
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-zope.testrunner
BuildPreReq: python-module-zope.pagetemplate
BuildPreReq: python-module-docutils
BuildPreReq: python-module-transaction

%py_provides %oname
%py_requires %mname zope.testing zope.testrunner zope.pagetemplate

%description
Complex functional load testing and benchmarking.

collective.funkload provides some extensions of Funkload, a web
performance testing and reporting tool. These extensions provide
flexible yet simple ways to:

* run benchmarks of multiple test scenarios
* run these benchmarks against multiple setups
* generate comparisons between those setups

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Complex functional load testing and benchmarking.

collective.funkload provides some extensions of Funkload, a web
performance testing and reporting tool. These extensions provide
flexible yet simple ways to:

* run benchmarks of multiple test scenarios
* run these benchmarks against multiple setups
* generate comparisons between those setups

This package contains tests for %oname.

%prep
%setup

ln -s $PWD/README.rst src/collective/funkload/README.txt

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

mv %buildroot%_bindir/fl-run-bench %buildroot%_bindir/fl-run-bench.py

%check
python setup.py test

%files
%doc *.rst docs/*
%_bindir/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/test*

%files tests
%python_sitelibdir/%mname/*/test*

%changelog
* Mon Oct 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.dev0.git20140620
- Initial build for Sisyphus

