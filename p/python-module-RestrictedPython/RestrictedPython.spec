%define oname RestrictedPython
Name: python-module-%oname
Version: 3.6.1
Release: alt2.dev.git20130312
Summary: Provides a restricted execution environment for Python, e.g. for running untrusted code
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/RestrictedPython/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopefoundation/RestrictedPython.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests

%description
RestrictedPython provides a restricted execution environment for Python,
e.g. for running untrusted code.

%package tests
Summary: Tests for RestrictedPython
Group: Development/Python
Requires: %name = %version-%release

%description tests
RestrictedPython provides a restricted execution environment for Python,
e.g. for running untrusted code.

This package contains tests for RestrictedPython.

%prep
%setup

%build
%python_build

%install
%python_install

%check
python setup.py test -v
export PYTHONPATH=$PWD/src
for i in src/%oname/tests/*.py; do
	py.test -vv $i
done

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/tests

%files tests
%python_sitelibdir/%oname/tests

%changelog
* Sun Aug 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt2.dev.git20130312
- Added tests

* Mon Oct 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt1.dev.git20130312
- Version 3.6.1dev

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.0-alt1.1
- Rebuild with Python-2.7

* Tue May 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.0-alt1
- Initial build for Sisyphus

