%define oname oslosphinx

%def_with python3

Name: python-module-%oname
Version: 3.2.0
Release: alt1
Summary: OpenStack Sphinx Extensions and Theme
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/oslosphinx/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/openstack/oslosphinx.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: git
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pbr >= 1.6 python-module-sphinx-devel
BuildPreReq: python-module-hacking python-module-mccabe
BuildPreReq: python-module-flake8 pyflakes
BuildPreReq: python-module-requests >= 2.5.2

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pbr python3-module-sphinx
BuildPreReq: python3-module-hacking python3-module-mccabe
BuildPreReq: python3-module-flake8 python3-pyflakes
BuildPreReq: python3-module-requests
%endif

%py_provides %oname
%py_requires hacking

%description
Theme and extension support for Sphinx documentation from the OpenStack
project.

%package -n python3-module-%oname
Summary: OpenStack Sphinx Extensions and Theme
Group: Development/Python3
%py3_provides %oname
%py3_requires hacking

%description -n python3-module-%oname
Theme and extension support for Sphinx documentation from the OpenStack
project.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Theme and extension support for Sphinx documentation from the OpenStack
project.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Theme and extension support for Sphinx documentation from the OpenStack
project.

This package contains documentation for %oname.

%prep
%setup

git init-db
git config user.email "real at altlinux.org"
git config user.name "REAL"
git add . -A
git commit -a -m "commit"
git tag %version


%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx doc
ln -s ../objects.inv doc/source/

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install
mv %buildroot%python_sitelibdir/%oname-*-py%_python_version.egg-info \
	%buildroot%python_sitelibdir/%oname-py%_python_version.egg-info

%if_with python3
pushd ../python3
%python3_install
popd
mv %buildroot%python3_sitelibdir/%oname-*-py%_python3_version.egg-info \
	%buildroot%python3_sitelibdir/%oname-py%_python3_version.egg-info
%endif

pushd doc
sphinx-build -b pickle -d build/doctrees source build/pickle
sphinx-build -b html -d build/doctrees source build/html
popd

cp -fR doc/build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
py.test
%if_with python3
pushd ../python3
python3 setup.py test
py.test-%_python3_version
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc doc/build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Wed Oct 28 2015 Alexey Shabalin <shaba@altlinux.ru> 3.2.0-alt1
- 3.2.0

* Sat Jul 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0-alt1
- Version 3.0.0

* Fri May 15 2015 Alexey Shabalin <shaba@altlinux.ru> 2.5.0-alt1
- 2.5.0

* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.0-alt2.git20141011
- Added necessary requirements
- Enabled testing

* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.0-alt1.git20141011
- Initial build for Sisyphus

