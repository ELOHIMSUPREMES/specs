%define oname pytest-django

%def_with python3

Name: python-module-%oname
Version: 2.7.0
Release: alt1.git20141012
Summary: A Django plugin for py.test
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-django/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/pytest-dev/pytest-django.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pytest python-module-django-tests
BuildPreReq: python-module-django-configurations python-module-wheel
BuildPreReq: python-module-pytest-xdist python-module-twine
BuildPreReq: python-module-south python-module-isort python-module-tox
BuildPreReq: python-module-sphinx-devel
BuildPreReq: python-module-django-dbbackend-sqlite3
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pytest python3-module-django-tests
BuildPreReq: python3-module-django-configurations python3-module-wheel
BuildPreReq: python3-module-pytest-xdist python3-module-twine
BuildPreReq: python3-module-south python3-module-isort python3-module-tox
BuildPreReq: python3-module-django-dbbackend-sqlite3
%endif

%description
pytest-django allows you to test your Django project/applications with
the pytest testing tool.

%package -n python3-module-%oname
Summary: A Django plugin for py.test
Group: Development/Python3

%description -n python3-module-%oname
pytest-django allows you to test your Django project/applications with
the pytest testing tool.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
pytest-django allows you to test your Django project/applications with
the pytest testing tool.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
pytest-django allows you to test your Django project/applications with
the pytest testing tool.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

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

%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
export PYTHONPATH=$PWD
python setup.py test
py.test
%if_with python3
pushd ../python3
export PYTHONPATH=$PWD
python3 setup.py test
py.test-%_python3_version
popd
%endif

%files
%doc AUTHORS *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.0-alt1.git20141012
- Initial build for Sisyphus

