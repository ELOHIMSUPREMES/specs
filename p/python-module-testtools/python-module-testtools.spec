%define oname testtools

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 1.4.0
Release: alt1
Summary: extensions to the Python standard library's unit testing framework

Group: Development/Python
License: MIT
Url: http://pypi.python.org/pypi/testtools

Source: %name-%version.tar
Packager: Vladimir Lettiev <crux@altlinux.ru>

BuildArch: noarch
BuildRequires: python-module-setuptools-tests
BuildRequires: python-module-unittest2 python-module-mimeparse
BuildRequires: python-module-six python-module-argparse
BuildRequires: python-module-sphinx-devel python-module-extras
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools-tests
BuildRequires: python3-module-unittest2 python3-module-mimeparse
BuildRequires: python3-module-six python3-module-argparse
BuildPreReq: python3-module-extras
%endif

%description
testtools is a set of extensions to the Python standard library's unit
testing framework. These extensions have been derived from years of
experience with unit testing in Python and come from many different
sources.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
testtools is a set of extensions to the Python standard library's unit
testing framework. These extensions have been derived from years of
experience with unit testing in Python and come from many different
sources.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation

%description docs
testtools is a set of extensions to the Python standard library's unit
testing framework. These extensions have been derived from years of
experience with unit testing in Python and come from many different
sources.

This package contains documentation for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: extensions to the Python 3 standard library's unit testing framework
Group: Development/Python3
%add_python3_req_skip twisted

%description -n python3-module-%oname
testtools is a set of extensions to the Python standard library's unit
testing framework. These extensions have been derived from years of
experience with unit testing in Python and come from many different
sources.
%endif

%prep
%setup

sed -i 's|python-mimeparse|mimeparse|' setup.py
sed -i "s|.*unittest2.*||" setup.py

%prepare_sphinx .
ln -s ../objects.inv doc/

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
%python3_build
popd
%endif

export PYTHONPATH=$PWD
%make -C doc pickle
%make -C doc html

%install
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%python_sitelibdir/testtools*
%doc LICENSE NEWS README*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc doc/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc LICENSE NEWS README*
%python3_sitelibdir/*
%endif

%changelog
* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1
- Version 1.4.0

* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt2
- Fixed requirements

* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1
- Version 1.1.0
- Added docs

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 0.9.8-alt1.2.1
- Rebuild with Python-3.3

* Thu Apr 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8-alt1.2
- Added module for Python 3 (bootstrap)

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.8-alt1.1
- Rebuild with Python-2.7

* Mon Jan 10 2011 Vladimir Lettiev <crux@altlinux.ru> 0.9.8-alt1
- New version 0.9.8

* Mon Oct 18 2010 Vladimir Lettiev <crux@altlinux.ru> 0.9.7-alt1
- New version 0.9.7

* Mon Sep 20 2010 Vladimir Lettiev <crux@altlinux.ru> 0.9.6-alt1
- initial build

