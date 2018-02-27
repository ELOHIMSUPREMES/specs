%define oname django-facebook-applications

%def_with python3

Name: python-module-%oname
Version: 0.1.1
Release: alt1.git20130323
Summary: Django implementation for Facebook Graph API Applications
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/django-facebook-applications/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ramusus/django-facebook-applications.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
Application for interacting with Facebook Graph API Applications objects
using Django model interface.

%package -n python3-module-%oname
Summary: Django implementation for Facebook Graph API Applications
Group: Development/Python3

%description -n python3-module-%oname
Application for interacting with Facebook Graph API Applications objects
using Django model interface.

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
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Mon Sep 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1.git20130323
- Initial build for Sisyphus

