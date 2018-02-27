%define oname pytest-translations

%def_with python3
# because we have old polib
%def_disable check

Name: python-module-%oname
Version: 0.2.0
Release: alt1.git20150101
Summary: Test your translation files
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-translations/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Thermondo/pytest-translations.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-polib
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-polib
%endif

%py_provides pytest_translations
%py_requires polib

%description
py.test plugin to test your translation files.

%package -n python3-module-%oname
Summary: Test your translation files
Group: Development/Python3
%py3_provides pytest_translations
%py3_requires polib

%description -n python3-module-%oname
py.test plugin to test your translation files.

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
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Jan 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20150101
- Initial build for Sisyphus

