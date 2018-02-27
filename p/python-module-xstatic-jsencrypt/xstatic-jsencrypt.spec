%define mname xstatic
%define oname %mname-jsencrypt

%def_with python3

Name: python-module-%oname
Version: 2.0.0.2
Release: alt1
Summary: JSEncrypt 2.0.0 (XStatic packaging standard)
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/XStatic-JSEncrypt/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-%mname
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-%mname
%endif

%py_provides %mname.pkg.jsencrypt
%py_requires %mname.pkg

%description
JSEncrypt JavaScript library packaged for setuptools (easy_install) /
pip.

This package is intended to be used by **any** project that needs these
files.

%package -n python3-module-%oname
Summary: JSEncrypt 2.0.0 (XStatic packaging standard)
Group: Development/Python3
%py3_provides %mname.pkg.jsencrypt
%py3_requires %mname.pkg

%description -n python3-module-%oname
JSEncrypt JavaScript library packaged for setuptools (easy_install) /
pip.

This package is intended to be used by **any** project that needs these
files.

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
%doc *.txt
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/%mname/*
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Mon Nov 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0.2-alt1
- Initial build for Sisyphus

