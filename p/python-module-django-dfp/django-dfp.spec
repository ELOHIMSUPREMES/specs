%define oname django-dfp

%def_with python3

Name: python-module-%oname
Version: 0.3.2
Release: alt1.git20140721
Summary: DFP implementation for Django
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/django-dfp/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/praekelt/django-dfp.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
App that provides tags to fetch Google DFP ads.

%package -n python3-module-%oname
Summary: DFP implementation for Django
Group: Development/Python3

%description -n python3-module-%oname
App that provides tags to fetch Google DFP ads.

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
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Thu Oct 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.git20140721
- Initial build for Sisyphus

