%define oname nose-parameterized

%def_with python3

Name: python-module-%oname
Version: 0.3.5
Release: alt1.git20141105
Summary: Decorator for parameterized testing with Nose
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/nose-parameterized/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/wolever/nose-parameterized.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-nose
%endif

%py_provides nose_parameterized

%description
nose-parameterized is a decorator for parameterized testing with nose.

%package -n python3-module-%oname
Summary: Decorator for parameterized testing with Nose
Group: Development/Python3
%py3_provides nose_parameterized

%description -n python3-module-%oname
nose-parameterized is a decorator for parameterized testing with nose.

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
nosetests
%if_with python3
pushd ../python3
python3 setup.py test
nosetests3
popd
%endif

%files
%doc *.txt *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.5-alt1.git20141105
- Initial build for Sisyphus

