%define packagename python-module-mox
%define origname mox

%def_without python3

Summary: mock object framework for Python
Name: %packagename
Version: 0.5.3
Release: alt1.svn20121116
Source0: %origname-%version.tar
License: Apache License 2.0
Group: Development/Python
URL: http://code.google.com/p/pymox/
Packager: Mikhail Pokidko <pma@altlinux.org>
BuildArch: noarch

# Automatically added by buildreq on Sat Apr 05 2008
BuildRequires: python-devel

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python-tools-2to3
%endif

%description
Mox is a mock object framework for Python. Mox is based on EasyMock, a
Java mock object framework.
Mox will make mock objects for you, so you don't have to create your
own!
It mocks the public/protected interfaces of Python objects.
You set up your mock objects expected behavior using a domain specific
language (DSL), which makes it easy to use, understand, and refactor!

%package -n python3-module-%origname
Summary: mock object framework for Python
Group: Development/Python3

%description -n python3-module-%origname
Mox is a mock object framework for Python. Mox is based on EasyMock, a
Java mock object framework.
Mox will make mock objects for you, so you don't have to create your
own!
It mocks the public/protected interfaces of Python objects.
You set up your mock objects expected behavior using a domain specific
language (DSL), which makes it easy to use, understand, and refactor!

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
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc COPYING README
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%origname
%doc COPYING README
%python3_sitelibdir/*
%endif

%changelog
* Fri Aug 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.3-alt1.svn20121116
- New snapshot

* Fri Dec 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.3-alt1
- Version 0.5.3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.0-alt2.1.1
- Rebuild with Python-2.7

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt2.1
- Rebuilt with python 2.6

* Mon Sep 28 2009 Mikhail Pokidko <pma@altlinux.org> 0.5.0-alt2
- Fixed packaging errors

* Tue Nov 18 2008 Mikhail Pokidko <pma@altlinux.org> 0.5.0-alt1
- Initial ALT build


