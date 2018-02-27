%define oname nose-testconfig

%def_with python3

Name: python-module-%oname
Version: 0.9
Release: alt1.git20130419
Summary: Test Configuration plugin for nosetests
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/nose-testconfig/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/singingwolfboy/nose-testconfig.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-nose python-module-yaml
BuildPreReq: python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-nose python3-module-yaml
%endif

%py_provides testconfig

%description
nose-testconfig is a plugin to the nose test framework which provides a
faculty for passing test-specific (or test-run specific) configuration
data to the tests being executed.

%package -n python3-module-%oname
Summary: Test Configuration plugin for nosetests
Group: Development/Python3
%py3_provides testconfig

%description -n python3-module-%oname
nose-testconfig is a plugin to the nose test framework which provides a
faculty for passing test-specific (or test-run specific) configuration
data to the tests being executed.

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
%doc ACKS TODO docs/* examples
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc ACKS TODO docs/* examples
%python3_sitelibdir/*
%endif

%changelog
* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt1.git20130419
- Initial build for Sisyphus

