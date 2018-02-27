%define oname flask-cors

%def_with python3

Name: python-module-%oname
Version: 1.9.0
Release: alt1.git20141028
Summary: Cross Origin Resource Sharing ( CORS ) support for Flask
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/Flask-Cors/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/wcdolphin/flask-cors.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-flask python-module-six
BuildPreReq: python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-flask python3-module-six
BuildPreReq: python3-module-nose
%endif

%py_provides flask_cors

%description
A Flask extension for handling Cross Origin Resource Sharing (CORS),
making cross-origin AJAX possible.

%package -n python3-module-%oname
Summary: Cross Origin Resource Sharing ( CORS ) support for Flask
Group: Development/Python3
%py3_provides flask_cors

%description -n python3-module-%oname
A Flask extension for handling Cross Origin Resource Sharing (CORS),
making cross-origin AJAX possible.

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
%doc *.rst docs/*.rst examples
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/*.rst examples
%python3_sitelibdir/*
%endif

%changelog
* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.0-alt1.git20141028
- Initial build for Sisyphus

