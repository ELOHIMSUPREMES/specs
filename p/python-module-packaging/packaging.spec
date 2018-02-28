%define oname packaging

%def_with python3

Name: python-module-%oname
Version: 15.4
Release: alt1.dev0.git20150801
Summary: Core utilities for Python packages
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/packaging
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/pypa/packaging.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-tox python-module-invoke
BuildPreReq: python-module-progress python-module-coverage
BuildPreReq: python-module-pretend
BuildPreReq: python-module-sphinx-devel python-module-sphinx_rtd_theme
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-tox python3-module-invoke
BuildPreReq: python3-module-progress python3-module-coverage
BuildPreReq: python3-module-pretend
%endif

%py_provides %oname

%description
Core utilities for Python packages.

%if_with python3
%package -n python3-module-%oname
Summary: Core utilities for Python packages
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Core utilities for Python packages.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Core utilities for Python packages.

This package contains pickles for %oname.

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

export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test -v
python -m coverage run --source packaging/ -m pytest --strict -vv
%if_with python3
pushd ../python3
python3 setup.py test -v
python3 -m coverage run --source packaging/ -m pytest --strict -vv
popd
%endif

%files
%doc *.rst docs/_build/html tasks
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/_build/html tasks
%python3_sitelibdir/*
%endif

%changelog
* Sun Aug 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 15.4-alt1.dev0.git20150801
- Initial build for Sisyphus

