%define version 2.3
%define release alt1
%define origname txredis
%setup_python_module txredis

%def_with python3

Summary: Python/Twisted client for Redis key-value store
Name: %packagename
Version: %version
Release: %release
Source0: %origname-%version.tar
License: BSD
Group: Development/Python
BuildArch: noarch
URL: http://ooici.net/packages/txredis/
Packager: Sergey Alembekov <rt@altlinux.org>

BuildPreReq: %py_dependencies setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
%summary

%package -n python3-module-%origname
Summary: Python/Twisted client for Redis key-value store
Group: Development/Python3
%py3_requires twisted.trial

%description -n python3-module-%origname
%summary

%prep
%setup -n %origname-%version

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
mkdir -p %buildroot/%_sysconfdir/bash_completion.d

%python_install --record=INSTALLED_FILES

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files -f INSTALLED_FILES
%doc *.txt *.rst

%if_with python3
%files -n python3-module-%origname
%doc *.txt *.rst
%python3_sitelibdir/*
%endif

%changelog
* Mon Sep 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3-alt1
- Version 2.3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.2-alt1.1
- Rebuild with Python-2.7

* Mon Nov 29 2010 Sergey Alembekov <rt@altlinux.ru> 0.1.2-alt1
- initial build for ALTLinux
