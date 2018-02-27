%define mname kids
%define oname %mname.cmd

%def_with python3

Name: python-module-%oname
Version: 0.0.1
Release: alt1.git20150205
Summary: Kids python command line library
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/kids.cmd/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/0k/kids.cmd.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests git
BuildPreReq: python-module-d2to1 python-module-coverage
BuildPreReq: python-module-nose python-module-docopt
BuildPreReq: python-module-kids.cache python-module-kids.file
BuildPreReq: python-module-kids.data python-module-kids.txt
BuildPreReq: python-module-kids.cfg python-module-kids.ansi
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests git
BuildPreReq: python3-module-d2to1 python3-module-coverage
BuildPreReq: python3-module-nose python3-module-docopt
BuildPreReq: python3-module-kids.cache python3-module-kids.file
BuildPreReq: python3-module-kids.data python3-module-kids.txt
BuildPreReq: python3-module-kids.cfg python3-module-kids.ansi
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires %mname docopt kids.cache kids.file kids.data kids.txt
%py_requires kids.cfg kids.ansi

%description
kids.cmd is a Python library providing helpers when writing command line
utilities in python.

It's part of 'Kids' (for Keep It Dead Simple) library.

%package -n python3-module-%oname
Summary: Kids python command line library
Group: Development/Python3
%py3_provides %oname
%py3_requires %mname docopt kids.cache kids.file kids.data kids.txt
%py3_requires kids.cfg kids.ansi

%description -n python3-module-%oname
kids.cmd is a Python library providing helpers when writing command line
utilities in python.

It's part of 'Kids' (for Keep It Dead Simple) library.

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
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst TODO
%python_sitelibdir/%mname/cmd
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc *.rst TODO
%python3_sitelibdir/%mname/cmd
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Thu Feb 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.git20150205
- Initial build for Sisyphus

