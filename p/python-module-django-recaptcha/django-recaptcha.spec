%define oname django-recaptcha

%def_with python3

Name: python-module-%oname
Version: 1.0.2
Release: alt1.git20140916
Summary: Django recaptcha form field/widget app
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/django-recaptcha/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/praekelt/django-recaptcha.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
django-recaptcha uses a modified version of the Python reCAPTCHA client
which is included in the package as client.py.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
django-recaptcha uses a modified version of the Python reCAPTCHA client
which is included in the package as client.py.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Django recaptcha form field/widget app
Group: Development/Python3

%description -n python3-module-%oname
django-recaptcha uses a modified version of the Python reCAPTCHA client
which is included in the package as client.py.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
django-recaptcha uses a modified version of the Python reCAPTCHA client
which is included in the package as client.py.

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
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*
%endif

%changelog
* Wed Oct 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.git20140916
- Initial build for Sisyphus

