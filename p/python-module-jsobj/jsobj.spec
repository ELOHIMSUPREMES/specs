%define oname jsobj

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 1.0.4
Release: alt1.git20150120
Summary: Jsobj provides JavaScript-Style Objects in Python
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/jsobj/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/gkovacs/jsobj.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname

%description
jsobj provides JavaScript-Style Objects in Python. It is based on
jsobject, but returns None if you try accessing non-existent keys
instead of throwing an exception.

%package -n python3-module-%oname
Summary: Jsobj provides JavaScript-Style Objects in Python
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
jsobj provides JavaScript-Style Objects in Python. It is based on
jsobject, but returns None if you try accessing non-existent keys
instead of throwing an exception.

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
%doc *.txt *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%endif

%changelog
* Tue Jan 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.4-alt1.git20150120
- Initial build for Sisyphus

