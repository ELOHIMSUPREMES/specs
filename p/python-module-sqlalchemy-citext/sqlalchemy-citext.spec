%define oname sqlalchemy-citext

%def_with python3

Name: python-module-%oname
Version: 1.3.0
Release: alt1.git20150108
Summary: A sqlalchemy plugin that allows postgres use of CITEXT
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/sqlalchemy-citext/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mahmoudimus/sqlalchemy-citext.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-SQLAlchemy python-module-psycopg2
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-SQLAlchemy python3-module-psycopg2
%endif

%py_provides citext
%py_requires sqlalchemy psycopg2

%description
Creates a SQLAlchemy user defined type to understand PostgreSQL's CIText
extension.

%package -n python3-module-%oname
Summary: A sqlalchemy plugin that allows postgres use of CITEXT
Group: Development/Python3
%py3_provides citext
%py3_requires sqlalchemy psycopg2

%description -n python3-module-%oname
Creates a SQLAlchemy user defined type to understand PostgreSQL's CIText
extension.

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
%doc *.md
%python_sitelibdir/*
%exclude %python_sitelibdir/tests

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%exclude %python3_sitelibdir/tests
%endif

%changelog
* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1.git20150108
- Initial build for Sisyphus

