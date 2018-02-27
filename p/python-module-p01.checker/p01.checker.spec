%define mname p01
%define oname %mname.checker
Name: python-module-%oname
Version: 0.5.6
Release: alt1
Summary: Python, ZCML, PT, HTML, JS, CSS source checking/linting
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/p01.checker/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-cssutils python-module-polib pyflakes
BuildPreReq: python-module-lxml python-module-zope.testing

%py_provides %oname
%py_requires %mname cssutils polib pyflakes lxml zope.testing

%description
This package provides a source checking/linting tool.

%prep
%setup

sed -i 's|\r||' $(find src -name '*.txt')

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test
export PYTHONPATH=$PWD/src
py.test -vv src/p01/checker/tests.py

%files
%doc *.txt
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info

%changelog
* Sat Feb 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.6-alt1
- Initial build for Sisyphus

