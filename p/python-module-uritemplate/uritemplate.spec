%define oname uritemplate

%def_with python3

Name: python-module-%oname
Version: 0.6
Release: alt2

Summary: Python implementation of RFC6570, URI Template
License: Apache Software License
Group: Development/Python

Url: https://pypi.python.org/pypi/uritemplate

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel
%endif

%setup_python_module %oname

%description
This is a Python implementation of RFC6570, URI Template, and can expand
templates up to and including Level 4 in that specification.

%package -n python3-module-%oname
Summary: Python implementation of RFC6570, URI Template
Group: Development/Python3

%description -n python3-module-%oname
This is a Python implementation of RFC6570, URI Template, and can expand
templates up to and including Level 4 in that specification.

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

%files
%doc README.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc README.rst
%python3_sitelibdir/*
%endif

%changelog
* Tue Aug 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt2
- Added module for Python 3

* Thu Sep 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt1
- Version 0.6

* Wed Apr 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.2-alt1
- Initial build for Sisyphus

