%define oname passlib

%def_with python3
# very slow:
%def_disable check

Name:		python-module-%oname
Version:	1.7
Release:	alt1.dev0.hg20131228
Summary:	Comprehensive password hashing framework supporting over 20 schemes
Group:		Development/Python
License:	BSD and Beerware and Copyright only
URL:		http://passlib.googlecode.com
Source0:	%{name}-%{version}.tar.gz

BuildArch:	noarch
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-nose
BuildPreReq: python-module-sphinx-devel
#BuildPreReq: python-module-cloud_sptheme
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-nose
%endif

%py_provides %oname

%description
Passlib is a password hashing library for Python 2 & 3, which provides
cross-platform implementations of over 20 password hashing algorithms,
as well as a framework for managing existing password hashes. It's
designed to be useful for a wide range of tasks, from verifying a hash
found in /etc/shadow, to providing full-strength password hashing for
multi-user application.

%package -n python3-module-%oname
Summary: Comprehensive password hashing framework supporting over 20 schemes
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Passlib is a password hashing library for Python 2 & 3, which provides
cross-platform implementations of over 20 password hashing algorithms,
as well as a framework for managing existing password hashes. It's
designed to be useful for a wide range of tasks, from verifying a hash
found in /etc/shadow, to providing full-strength password hashing for
multi-user application.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Passlib is a password hashing library for Python 2 & 3, which provides
cross-platform implementations of over 20 password hashing algorithms,
as well as a framework for managing existing password hashes. It's
designed to be useful for a wide range of tasks, from verifying a hash
found in /etc/shadow, to providing full-strength password hashing for
multi-user application.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation

%description docs
Passlib is a password hashing library for Python 2 & 3, which provides
cross-platform implementations of over 20 password hashing algorithms,
as well as a framework for managing existing password hashes. It's
designed to be useful for a wide range of tasks, from verifying a hash
found in /etc/shadow, to providing full-strength password hashing for
multi-user application.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/
sed -i 's|@VERSION@|%version|' docs/conf.py

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

%if 0
export PYTHONPATH=$PWD
pushd docs
sphinx-build -b pickle -d build/doctrees . build/pickle
sphinx-build -b html -d build/doctrees . build/html
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
%doc LICENSE README CHANGES
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc LICENSE README CHANGES
%python3_sitelibdir/*
%endif

%changelog
* Fri Oct 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7-alt1.dev0.hg20131228
- Version 1.7.dev0
- Added module for Python 3

* Mon Sep 17 2012 Pavel Shilovsky <piastry@altlinux.org> 1.5.3-alt1
- Initial release for Sisyphus (based on Fedora)
