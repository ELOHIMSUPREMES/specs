%define oname SQLAlchemy-FullText-Search

%def_with python3

Name: python-module-%oname
Version: 0.2.1
Release: alt1.git20141028
Summary: Offering FullText Search of MySQL in SQLAlchemy
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/SQLAlchemy-FullText-Search/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mengzhuo/sqlalchemy-fulltext-search.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-SQLAlchemy python-module-pymysql
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-SQLAlchemy python3-module-pymysql
%endif

%py_provides sqlalchemy_fulltext

%description
Provide FullText for MYSQL & SQLAlchemy model.

%package -n python3-module-%oname
Summary: Offering FullText Search of MySQL in SQLAlchemy
Group: Development/Python3
%py3_provides sqlalchemy_fulltext

%description -n python3-module-%oname
Provide FullText for MYSQL & SQLAlchemy model.

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
* Tue Oct 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.git20141028
- Initial build for Sisyphus

