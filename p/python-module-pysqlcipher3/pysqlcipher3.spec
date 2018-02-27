%define oname pysqlcipher3

%def_with python3

Name: python-module-%oname
Version: 1.0.2
Release: alt1.git20150226
Summary: DB-API 2.0 interface for SQLCIPHER 3.x
License: zlib/libpng
Group: Development/Python
Url: https://pypi.python.org/pypi/pysqlcipher3/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/rigglemania/pysqlcipher3.git
Source: %name-%version.tar

BuildPreReq: libssl-devel libsqlite3-devel libsqlcipher-devel
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-nose python-test
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-nose python3-test
%endif

%description
This library is a fork of pysqlcipher targeted for use with Python 3,
although support for Python 2 is still maintained. It is still in the
beta state, although this library contains minimal new code and instead
heavily pulls from the core Python sqlite source code while linking
against libsqlcipher.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
Requires: python-test

%description tests
This library is a fork of pysqlcipher targeted for use with Python 3,
although support for Python 2 is still maintained. It is still in the
beta state, although this library contains minimal new code and instead
heavily pulls from the core Python sqlite source code while linking
against libsqlcipher.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: DB-API 2.0 interface for SQLCIPHER 3.x
Group: Development/Python3

%description -n python3-module-%oname
This library is a fork of pysqlcipher targeted for use with Python 3,
although support for Python 2 is still maintained. It is still in the
beta state, although this library contains minimal new code and instead
heavily pulls from the core Python sqlite source code while linking
against libsqlcipher.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
Requires: python3-test

%description -n python3-module-%oname-tests
This library is a fork of pysqlcipher targeted for use with Python 3,
although support for Python 2 is still maintained. It is still in the
beta state, although this library contains minimal new code and instead
heavily pulls from the core Python sqlite source code while linking
against libsqlcipher.

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
export OPENSSL_CONF=%_bindir/openssl-config
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
export OPENSSL_CONF=%_bindir/openssl-config
python setup.py test
export PYTHONPATH=%buildroot%python_sitelibdir
pushd ~
nosetests -v %oname
popd
%if_with python3
pushd ../python3
python3 setup.py test
export PYTHONPATH=%buildroot%python3_sitelibdir
pushd ~
nosetests3 -v %oname
popd
popd
%endif

%files
%doc LICENSE *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test

%files tests
%python_sitelibdir/*/test

%if_with python3
%files -n python3-module-%oname
%doc LICENSE *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test
%endif

%changelog
* Fri Feb 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.git20150226
- Initial build for Sisyphus

