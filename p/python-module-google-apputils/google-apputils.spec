%define gname google
%define oname %gname-apputils

%def_with python3

Name: python-module-%oname
Version: 0.4.0
Release: alt1
Summary: Google Application Utilities for Python
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/google-apputils/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python-tools-2to3
%endif

Requires: python-module-%gname = %EVR

%description
This project is a small collection of utilities for building Python
applications. It includes some of the same set of utilities used to
build and run internal Python apps at Google.

%package -n python-module-%gname
Summary: Core files of %gname
Group: Development/Python

%description -n python-module-%gname
Core files of %gname.

%package -n python3-module-%oname
Summary: Google Application Utilities for Python
Group: Development/Python3
Requires: python3-module-%gname = %EVR
%py3_provides %gname.apputils

%description -n python3-module-%oname
This project is a small collection of utilities for building Python
applications. It includes some of the same set of utilities used to
build and run internal Python apps at Google.

%package -n python3-module-%gname
Summary: Core files of %gname
Group: Development/Python3
%py3_provides %gname

%description -n python3-module-%gname
Core files of %gname.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
install -p -m644 google/__init__.py \
	%buildroot%python_sitelibdir/%gname/

%if_with python3
pushd ../python3
%python3_install
install -p -m644 google/__init__.py \
	%buildroot%python3_sitelibdir/%gname/
popd
%endif

%files
%doc LICENSE README
%python_sitelibdir/*
%exclude %python_sitelibdir/%gname/__init__.py*

%files -n python-module-%gname
%python_sitelibdir/%gname/__init__.py*

%if_with python3
%files -n python3-module-%oname
%doc LICENSE README
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%gname/__init__.py
%exclude %python3_sitelibdir/%gname/__pycache__/__init__.*

%files -n python3-module-%gname
%python3_sitelibdir/%gname/__init__.py
%python3_sitelibdir/%gname/__pycache__/__init__.*
%endif

%changelog
* Thu Aug 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1
- Initial build for Sisyphus

