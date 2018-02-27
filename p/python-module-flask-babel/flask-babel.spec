%define oname flask-babel

%def_with python3

Name: python-module-%oname
Version: 0.9
Release: alt1.git20130729
Summary: Adds i18n/l10n support to Flask applications
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/Flask-Babel/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mitsuhiko/flask-babel.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-flask python-module-babel
BuildPreReq: python-module-speaklater python-module-jinja2
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-flask python3-module-babel
BuildPreReq: python3-module-speaklater python3-module-jinja2
%endif

%py_provides flask_babel

%description
Adds i18n/l10n support to Flask applications with the help of the Babel
library.

%package -n python3-module-%oname
Summary: Adds i18n/l10n support to Flask applications
Group: Development/Python3
%py3_provides flask_babel

%description -n python3-module-%oname
Adds i18n/l10n support to Flask applications with the help of the Babel
library.

%prep
%setup

%if_with python3
cp -fR . ../python3
sed -i 's|python|python3|g' ../python3/Makefile
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
make test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc README docs/*.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc README docs/*.rst
%python3_sitelibdir/*
%endif

%changelog
* Tue Oct 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt1.git20130729
- Initial build for Sisyphus

