%define oname facebook-scribe

%def_with python3

Name: python-module-%oname
Version: 2.0
Release: alt1.git20130530
Summary: A Python client for Facebook Scribe
License: ASL v2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/facebook-scribe/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/tomprimozic/scribe-python.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
This is a Python client for scribe.

%package -n python3-module-%oname
Summary: A Python client for Facebook Scribe
Group: Development/Python3

%description -n python3-module-%oname
This is a Python client for scribe.

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
* Tue Sep 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.git20130530
- Initial build for Sisyphus

