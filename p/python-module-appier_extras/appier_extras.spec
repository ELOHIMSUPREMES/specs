%define oname appier_extras

%def_with python3

Name: python-module-%oname
Version: 0.2.19
Release: alt1
Summary: Appier Framework Extra Elements
License: GPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/appier_extras/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
Set of extra elements for Appier Framework infra-structure.

%package -n python3-module-%oname
Summary: Appier Framework Extra Elements
Group: Development/Python3

%description -n python3-module-%oname
Set of extra elements for Appier Framework infra-structure.

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
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%endif

%changelog
* Mon Sep 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.19-alt1
- Initial build for Sisyphus

