%define oname glob2

%def_with python3

Name: python-module-%oname
Version: 0.4.1
Release: alt1.git20140122
Summary: Extended version of Python's builtin glob module
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/glob2/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/miracle2k/python-glob2.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-nose
%endif

%py_provides %oname

%description
Version of the glob module that can capture patterns and supports
recursive wildcards.

%package -n python3-module-%oname
Summary: Extended version of Python's builtin glob module
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Version of the glob module that can capture patterns and supports
recursive wildcards.

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
%doc CHANGES TODO *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc CHANGES TODO *.rst
%python3_sitelibdir/*
%endif

%changelog
* Mon Nov 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.git20140122
- Initial build for Sisyphus

