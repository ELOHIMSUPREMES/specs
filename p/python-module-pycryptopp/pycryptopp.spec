%define oname pycryptopp
Name: python-module-%oname
Version: 0.6.0
Release: alt1.git20130916
Summary: Python wrappers for a few algorithms from the Crypto++ library
License: GPLv2+ or other (see copyright)
Group: Development/Python
Url: https://pypi.python.org/pypi/pycryptopp/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/tahoe-lafs/pycryptopp.git
Source: %name-%version.tar

BuildPreReq: gcc-c++ libcryptopp-devel git
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-ecdsa python-module-ed25519

%py_provides %oname
%py_requires ecdsa ed25519

%description
pycryptopp is a python wrapper around a few algorithms from the Crypto++
and python-Ed25519 libraries.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
pycryptopp is a python wrapper around a few algorithms from the Crypto++
and python-Ed25519 libraries.

This package contains tests for %oname.

%prep
%setup

sed -i 's|@VERSION@|%version|' \
	src/pycryptopp/publickey/ed25519/_version.py
git config --global user.email "real at altlinux.org"
git config --global user.name "REAL"
git init-db
git add . -A
git commit -a -m "%oname-%version"
git tag %oname-%version -m "%oname-%version"

%build
%python_build_debug --disable-embedded-cryptopp

%install
%python_install

%check
python setup.py test

%files
%doc COPYING* copyright *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test*
%exclude %python_sitelibdir/*/bench

%files tests
%python_sitelibdir/*/test*
%python_sitelibdir/*/bench

%changelog
* Thu Feb 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1.git20130916
- Initial build for Sisyphus

