%define oname paginate_sqlalchemy

%def_with python3

Name: python-module-%oname
Version: 0.2.0
Release: alt1.git20140911
Summary: Extension to paginate.Page that supports SQLAlchemy queries
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/paginate_sqlalchemy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Pylons/paginate_sqlalchemy.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-SQLAlchemy python-module-paginate
BuildPreReq: python-module-nose python-modules-sqlite3
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-SQLAlchemy python3-module-paginate
BuildPreReq: python3-module-nose python3-modules-sqlite3
%endif

%py_provides %oname
%py_requires sqlite3

%description
This module helps divide up large result sets into pages or chunks. The
user gets displayed one page at a time and can navigate to other pages.
It is especially useful when developing web interfaces and showing the
users only a selection of information at a time.

This module uses and extends the functionality of the paginate module to
support SQLAlchemy queries.

%package -n python3-module-%oname
Summary: Extension to paginate.Page that supports SQLAlchemy queries
Group: Development/Python3
%py3_provides %oname
%py3_requires sqlite3

%description -n python3-module-%oname
This module helps divide up large result sets into pages or chunks. The
user gets displayed one page at a time and can navigate to other pages.
It is especially useful when developing web interfaces and showing the
users only a selection of information at a time.

This module uses and extends the functionality of the paginate module to
support SQLAlchemy queries.

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
export PYTHONPATH=$PWD
py.test
%if_with python3
pushd ../python3
python3 setup.py test
export PYTHONPATH=$PWD
py.test-%_python3_version
popd
%endif

%files
%doc CHANGELOG README TODO
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc CHANGELOG README TODO
%python3_sitelibdir/*
%endif

%changelog
* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20140911
- Initial build for Sisyphus

