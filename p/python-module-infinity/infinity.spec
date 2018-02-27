%define oname infinity

%def_with python3

Name: python-module-%oname
Version: 1.3
Release: alt1.git20141021
Summary: All-in-one infinity value for Python. Can be compared to any object
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/infinity/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/kvesteri/infinity.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-Pygments python-module-six
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-Pygments python3-module-six
%endif

%py_provides %oname

%description
All-in-one infinity value for Python. Can be compared to any object.

%package -n python3-module-%oname
Summary: All-in-one infinity value for Python. Can be compared to any object
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
All-in-one infinity value for Python. Can be compared to any object.

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
python setup.py test
py.test
%if_with python3
pushd ../python3
python3 setup.py test
py.test-%_python3_version
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Sat Nov 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1.git20141021
- Initial build for Sisyphus

