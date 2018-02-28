%define oname lmdb

%def_with python3

Name: python-module-%oname
Version: 0.89
Release: alt1
Summary: Universal Python binding for the LMDB 'Lightning' Database
License: OpenLDAP BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/lmdb/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/dw/py-lmdb.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildPreReq: liblmdb-devel
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-memsink
%if_with python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname
%py_requires memsink

%description
Universal Python binding for the LMDB 'Lightning' Database.

%package -n python3-module-%oname
Summary: Universal Python binding for the LMDB 'Lightning' Database
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Universal Python binding for the LMDB 'Lightning' Database.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
export LMDB_FORCE_SYSTEM=1
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
export LMDB_FORCE_SYSTEM=1
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
export LMDB_FORCE_SYSTEM=1
python setup.py test
export PYTHONPATH=%buildroot%python_sitelibdir
py.test
%if_with python3
pushd ../python3
python3 setup.py test
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test-%_python3_version
popd
%endif

%files
%doc ChangeLog *.md docs/*.rst examples LICENSE
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc ChangeLog *.md docs/*.rst examples LICENSE
%python3_sitelibdir/*
%endif

%changelog
* Wed Jun 29 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.89-alt1
- Updated to 0.89.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.84-alt1.git20141109.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Sat Nov 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.84-alt1.git20141109
- Initial build for Sisyphus
