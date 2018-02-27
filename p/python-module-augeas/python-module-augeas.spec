%define oname augeas

%def_with python3

Name: python-module-%oname
Version: 0.5.0
Release: alt1.git20140831
Summary: Python bindings to augeas
Group: Development/Python
License: LGPLv2+
Url: http://augeas.net/
Source0: %name-%version.tar

BuildArch: noarch

BuildRequires: python-module-setuptools python-devel libaugeas-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setuptools python3-devel
%endif

%description
python-augeas is a set of Python bindings around augeas.

%package -n python3-module-%oname
Summary: Python bindings to augeas
Group: Development/Python3

%description -n python3-module-%oname
python-augeas is a set of Python bindings around augeas.

%prep
%setup

%if_with python3
cp -fR . ../python3
sed -i 's|python|python3|' ../python3/test/Makefile
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
%make check
%if_with python3
pushd ../python3
%make check
popd
%endif

%files
%doc COPYING AUTHORS README.txt
%python_sitelibdir/augeas.py*
%python_sitelibdir/*augeas*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc COPYING AUTHORS README.txt
%python3_sitelibdir/augeas.py*
%python3_sitelibdir/*augeas*.egg-info
%python3_sitelibdir/__pycache__/*
%endif

%changelog
* Mon Sep 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1.git20140831
- Version 0.5.0
- Added module for Python 3

* Tue Aug 13 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0.4.1-alt2
- rebuild for autoimports (https://bugzilla.altlinux.org/show_bug.cgi?id=27419)

* Mon Aug 12 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0.4.1-alt1
- build for ALT
