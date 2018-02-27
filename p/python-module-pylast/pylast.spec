%define oname pylast

%def_with python3

Name: python-module-%oname
Version: 1.0.0
Release: alt1.git20140825
Summary: A Python interface to Last.fm (and other API compatible social networks)
License: ASL v2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/pylast/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/pylast/pylast.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
A Python interface to Last.fm and other api-compatible websites such as
Libre.fm.

%package -n python3-module-%oname
Summary: A Python interface to Last.fm (and other API compatible social networks)
Group: Development/Python3

%description -n python3-module-%oname
A Python interface to Last.fm and other api-compatible websites such as
Libre.fm.

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
%doc *.yaml *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.yaml *.md
%python3_sitelibdir/*
%endif

%changelog
* Fri Oct 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.git20140825
- Initial build for Sisyphus

