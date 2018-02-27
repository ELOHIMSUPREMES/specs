%define mname xstatic
%define oname %mname-jasmine

%def_with python3

Name: python-module-%oname
Version: 2.1.2.0
Release: alt1
Summary: Jasmine 2.1.2 (XStatic packaging standard)
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/XStatic-Jasmine/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-%mname
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-%mname
%endif

%py_provides %mname.pkg.jasmine
%py_requires %mname.pkg

%description
Jasmine JavaScript library packaged for setuptools (easy_install) / pip.

This package is intended to be used by **any** project that needs these
files.

%package -n python3-module-%oname
Summary: Jasmine 2.1.2 (XStatic packaging standard)
Group: Development/Python3
%py3_provides %mname.pkg.jasmine
%py3_requires %mname.pkg

%description -n python3-module-%oname
Jasmine JavaScript library packaged for setuptools (easy_install) / pip.

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
* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.2.0-alt1
- Version 2.1.2.0

* Mon Nov 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1.1-alt1
- Initial build for Sisyphus

