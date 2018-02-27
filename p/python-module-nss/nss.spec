%define oname nss
Name: python-module-%oname
Version: 0.17.0
Release: alt1
Summary: Python binding for NSS
License: MPL 1.1/GPL 2.0/LGPL 2.1
Group: Development/Python
Url: http://www.mozilla.org/projects/security/pki/python-nss/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone https://hg.mozilla.org/projects/python-nss
Source: %name-%version.tar

BuildPreReq: python-devel gcc-c++ libnss-devel python-module-epydoc

%description
python-nss is a Python binding for NSS (Network Security Services) and
NSPR (Netscape Portable Runtime). NSS provides cryptography services
supporting SSL, TLS, PKI, PKIX, X509, PKCS*, etc. NSS is an alternative
to OpenSSL and used extensively by major software projects. NSS is
FIPS-140 certified.

%prep
%setup

%build
%python_build_debug

python setup.py build_api_doc -a html
mv build/doc/html api

%install
%python_install

%files
%doc LICENSE* README doc/ChangeLog doc/examples api
%python_sitelibdir/*

%changelog
* Thu Feb 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.17.0-alt1
- Version 0.17.0

* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.15.0-alt1
- Version 0.15.0 (ALT #30401)

* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.1-alt1
- Version 0.14.1

* Wed Sep 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.0-alt1
- Version 0.14.0

* Tue Apr 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13-alt1
- Version 0.13

* Mon Sep 24 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12-alt1
- Initial build for Sisyphus

