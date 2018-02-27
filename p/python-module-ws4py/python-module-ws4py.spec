%define oname ws4py
%def_with python3

Summary: WebSocket for Python (ws4py)
Name: python-module-ws4py
Version: 0.3.4
Release: alt1
Url: https://github.com/Lawouach/WebSocket-for-Python
Source: %name-%version.tar
Packager: Valentin Rosavitskiy <valintinr@altlinux.org>
License: ASL 2.0
Group: Development/Python

BuildArch: noarch
BuildRequires: python-dev python-module-setupdocs python-module-setuptools

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setupdocs python3-module-setuptools
%endif

%description
ws4py is a Python package implementing the WebSocket protocol as
defined in RFC 6455.

%package -n python3-module-%oname
Summary: WebSocket for Python (ws4py)
Group: Development/Python3

%description -n python3-module-%oname
ws4py is a Python package implementing the WebSocket protocol as
defined in RFC 6455.


%prep
%setup

%if_with python3
cp -fR . ../python3
%endif



%build
%add_optflags -fno-strict-aliasing
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif


%install
%python_build_install --prefix=/usr

%if_with python3
pushd ../python3
%python3_install
popd
%endif


%files
%doc CHANGELOG.txt LICENSE README.md
%python_sitelibdir/*


%if_with python3
%files -n python3-module-%oname
%doc CHANGELOG.txt LICENSE README.md
%python3_sitelibdir/*
%endif



%changelog
* Thu Oct 30 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 0.3.4-alt1
- Initla build for ALT

