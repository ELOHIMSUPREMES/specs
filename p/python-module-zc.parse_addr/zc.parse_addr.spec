%define oname zc.parse_addr

%def_with python3

Name: python-module-%oname
Version: 1.0.0
Release: alt1
Summary: Parse network addresses of the form: HOST:PORT
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/zc.parse_addr/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname
%py_requires zc

%description
Parse network addresses of the form: HOST:PORT.

%package -n python3-module-%oname
Summary: Parse network addresses of the form: HOST:PORT
Group: Development/Python3
%py3_provides %oname
%py3_requires zc

%description -n python3-module-%oname
Parse network addresses of the form: HOST:PORT.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
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

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc PKG-INFO
%python_sitelibdir/zc/*
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc PKG-INFO
%python3_sitelibdir/zc/*
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Sun Nov 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus

