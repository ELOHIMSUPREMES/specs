%define oname minipg

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.4.3
Release: alt1.git20150208
Summary: Yet another PostgreSQL database driver
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/minipg/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/nakagami/minipg.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-Cython
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-Cython
%endif

%py_provides %oname

%description
Yet another Python PostgreSQL database driver.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Yet another Python PostgreSQL database driver.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Yet another PostgreSQL database driver
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Yet another Python PostgreSQL database driver.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Yet another Python PostgreSQL database driver.

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%add_optflags -fno-strict-aliasing
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
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif
exit 1

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test*

%files tests
%python_sitelibdir/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*
%endif

%changelog
* Mon Feb 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.3-alt1.git20150208
- Initial build for Sisyphus

