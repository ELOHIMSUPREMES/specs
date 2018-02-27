%define oname json_patch

%def_with python3

Name: python-module-%oname
Version: 0.1
Release: alt1
Summary: Implementation of the json-patch spec
License: Free
Group: Development/Python
Url: https://pypi.python.org/pypi/json_patch/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-modules-json
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-json_pointer
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-json_pointer
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname

%description
Implementation of json-patch draft 04:

  http://tools.ietf.org/html/draft-pbryan-json-patch-04

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Implementation of json-patch draft 04:

  http://tools.ietf.org/html/draft-pbryan-json-patch-04

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Implementation of the json-patch spec
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Implementation of json-patch draft 04:

  http://tools.ietf.org/html/draft-pbryan-json-patch-04

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Implementation of json-patch draft 04:

  http://tools.ietf.org/html/draft-pbryan-json-patch-04

This package contains tests for %oname.

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

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test.*

%files tests
%python_sitelibdir/*/test.*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test.*
%exclude %python3_sitelibdir/*/*/test.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test.*
%python3_sitelibdir/*/*/test.*
%endif

%changelog
* Tue Nov 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

