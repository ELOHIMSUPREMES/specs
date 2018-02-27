%define oname nine

%def_with python3

Name: python-module-%oname
Version: 0.3.3
Release: alt2
Summary: Python 2 / 3 compatibility, like six, but favouring Python 3
License: Public Domain
Group: Development/Python
Url: https://pypi.python.org/pypi/nine
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
Python 2 and 3 compatibility library, such that your code looks more
like Python 3.

%package -n python3-module-%oname
Summary: Python 2 / 3 compatibility, like six, but favouring Python 3
Group: Development/Python3

%description -n python3-module-%oname
Python 2 and 3 compatibility library, such that your code looks more
like Python 3.

%package -n python3-module-%oname-test
Summary: Test for nine
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-test
Python 2 and 3 compatibility library, such that your code looks more
like Python 3.

This package contains test for nine.

%package test
Summary: Test for nine
Group: Development/Python
Requires: %name = %EVR

%description test
Python 2 and 3 compatibility library, such that your code looks more
like Python 3.

This package contains test for nine.

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
%exclude %python_sitelibdir/*/test*

%files test
%python_sitelibdir/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*

%files -n python3-module-%oname-test
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*
%endif

%changelog
* Sat Aug 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.3-alt2
- Added module for Python 3

* Tue Sep 17 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.3-alt1
- Initial build for Sisyphus

