%define oname radar

%def_with python3

Name: python-module-%oname
Version: 0.3
Release: alt1.git20131211
Summary: Random date generation
License: GPLv2.0/LGPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/radar/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/barseghyanartur/radar.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-simple_timer
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-simple_timer
%endif

%py_provides %oname

%description
Generate random date(time).

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires simple_timer

%description tests
Generate random date(time).

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Random date generation
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Generate random date(time).

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires simple_timer

%description -n python3-module-%oname-tests
Generate random date(time).

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

%check
export PYTHONPATH=$PWD/src
python setup.py test
./test.sh
%if_with python3
pushd ../python3
export PYTHONPATH=$PWD/src
python3 setup.py test
sed -i 's|python|python3|' test.sh
./test.sh
popd
%endif

%files
%doc *.rst docs/*.rst example
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test.*

%files tests
%python_sitelibdir/*/test.*

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/*.rst example
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test.*
%exclude %python3_sitelibdir/*/*/test.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test.*
%python3_sitelibdir/*/*/test.*
%doc *.rst docs/*.rst example
%endif

%changelog
* Tue Feb 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.git20131211
- Initial build for Sisyphus

