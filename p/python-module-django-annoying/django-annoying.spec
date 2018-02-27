%define oname django-annoying

%def_with python3

Name: python-module-%oname
Version: 0.8.0
Release: alt1.git20140525
Summary: Django application that tries to eliminate annoying things in the Django framework
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/django-annoying/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/skorokithakis/django-annoying.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
This django application eliminates certain annoyances in the Django
framework.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This django application eliminates certain annoyances in the Django
framework.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Django application that tries to eliminate annoying things in the Django framework
Group: Development/Python3

%description -n python3-module-%oname
This django application eliminates certain annoyances in the Django
framework.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This django application eliminates certain annoyances in the Django
framework.

This package contains tests for %oname.

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
%doc *.txt *.md
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.md
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Mon Sep 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt1.git20140525
- Initial build for Sisyphus

