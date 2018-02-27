%define oname phonenumbers

%def_with python3

Name: python-module-%oname
Version: 7.0.0
Release: alt1.git20141102
Summary: Python port of Google's libphonenumber
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/phonenumbers/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/daviddrysdale/python-phonenumbers.git
# branch: dev
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname

%description
Python version of Google's common library for parsing, formatting,
storing and validating international phone numbers.

%package -n python3-module-%oname
Summary: Python port of Google's libphonenumber
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Python version of Google's common library for parsing, formatting,
storing and validating international phone numbers.

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
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.md python/HISTORY
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md python/HISTORY
%python3_sitelibdir/*
%endif

%changelog
* Tue Nov 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.0.0-alt1.git20141102
- Version 7.0.0

* Sat Nov 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.3.0-alt1.git20141026
- Initial build for Sisyphus

