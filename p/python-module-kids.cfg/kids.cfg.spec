%define mname kids
%define oname %mname.cfg

%def_with python3

Name: python-module-%oname
Version: 0.0.1
Release: alt1.git20140514
Summary: Kids config loading helpers
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/kids.cfg/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/0k/kids.cfg.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests git
BuildPreReq: python-module-d2to1 python-module-coverage
BuildPreReq: python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests git
BuildPreReq: python3-module-d2to1 python3-module-coverage
BuildPreReq: python3-module-nose
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires %mname

%description
kids.cfg is a Python library providing helpers for loading your cfg
file.

It's part of 'Kids' (for Keep It Dead Simple) library.

%package -n python3-module-%oname
Summary: Kids config loading helpers
Group: Development/Python3
%py3_provides %oname
%py3_requires %mname

%description -n python3-module-%oname
kids.cfg is a Python library providing helpers for loading your cfg
file.

%prep
%setup

git config --global user.email "real at altlinux.org"
git config --global user.name "REAL"
git init-db
git add . -A
git commit -a -m "%version"
git tag %version -m "%version"

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
./autogen.sh
%python_build_debug

%if_with python3
pushd ../python3
./autogen.sh
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

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test
nosetests
%if_with python3
pushd ../python3
python3 setup.py test
nosetests3
popd
%endif

%files
%doc *.rst
%python_sitelibdir/%mname/cfg
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/%mname/cfg
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Thu Feb 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.git20140514
- Initial build for Sisyphus

