%define mname kids
%define oname %mname.txt

%def_with python3

Name: python-module-%oname
Version: 0.0.2
Release: alt1.git20150204.2
Summary: Kids text manipulation helpers
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/kids.txt/

# https://github.com/0k/kids.txt.git
Source: %name-%version.tar
Patch1: %oname-%version-alt-python3-compat.patch

BuildRequires: git-core python-module-d2to1 python-module-nose python-module-setuptools-tests time
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-d2to1 python3-module-nose python3-module-setuptools-tests
%endif

%py_provides %oname
%py_requires %mname

%description
kids.txt is a Python library providing helpers to manage text. It's part
of 'Kids' (for Keep It Dead Simple) library.

It is, for now, a very humble package.

%package -n python3-module-%oname
Summary: Kids text manipulation helpers
Group: Development/Python3
%py3_provides %oname
%py3_requires %mname

%description -n python3-module-%oname
kids.txt is a Python library providing helpers to manage text. It's part
of 'Kids' (for Keep It Dead Simple) library.

It is, for now, a very humble package.

%prep
%setup
%patch1 -p1

git config --global user.email "real at altlinux.org"
git config --global user.name "REAL"
git init-db
git add . -A
git commit -a -m "%version"
git tag %version -m "%version"

%if_with python3
cp -fR . ../python3
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
%python_sitelibdir/%mname/txt
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/%mname/txt
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Wed Aug 09 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.0.2-alt1.git20150204.2
- Fixed build.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.2-alt1.git20150204.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.0.2-alt1.git20150204.1
- NMU: Use buildreq for BR.

* Thu Feb 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.2-alt1.git20150204
- Initial build for Sisyphus

