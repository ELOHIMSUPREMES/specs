%define oname ipwhois

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.10.3
Release: alt1.git20150814
Summary: Retrieve and parse whois data for IPv4 and IPv6 addresses
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/ipwhois
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/secynic/ipwhois.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-dns python-module-ipaddr
BuildPreReq: python-module-nose
BuildPreReq: python-module-sphinx-devel python-module-sphinx_rtd_theme
BuildPreReq: python-module-sphinxcontrib-napoleon
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-dns
BuildPreReq: python3-module-nose
%endif

%py_provides %oname
%py_requires dns ipaddr

%description
ipwhois is a Python package focused on retrieving and parsing whois data
for IPv4 and IPv6 addresses.

Features:
* Parses a majority of whois fields in to a standard dictionary
* IPv4 and IPv6 support
* Referral whois support
* Supports REST queries (useful if whois is blocked from your network)
* Proxy support for REST queries
* Recursive network parsing for IPs with parent/children networks listed
* Python 2.6+ and 3.3+ supported
* Useful set of utilities
* BSD license

%if_with python3
%package -n python3-module-%oname
Summary: Retrieve and parse whois data for IPv4 and IPv6 addresses
Group: Development/Python3
%py3_provides %oname
%py3_requires dns

%description -n python3-module-%oname
ipwhois is a Python package focused on retrieving and parsing whois data
for IPv4 and IPv6 addresses.

Features:
* Parses a majority of whois fields in to a standard dictionary
* IPv4 and IPv6 support
* Referral whois support
* Supports REST queries (useful if whois is blocked from your network)
* Proxy support for REST queries
* Recursive network parsing for IPs with parent/children networks listed
* Python 2.6+ and 3.3+ supported
* Useful set of utilities
* BSD license
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
ipwhois is a Python package focused on retrieving and parsing whois data
for IPv4 and IPv6 addresses.

Features:
* Parses a majority of whois fields in to a standard dictionary
* IPv4 and IPv6 support
* Referral whois support
* Supports REST queries (useful if whois is blocked from your network)
* Proxy support for REST queries
* Recursive network parsing for IPs with parent/children networks listed
* Python 2.6+ and 3.3+ supported
* Useful set of utilities
* BSD license

This package contains pickles for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx %oname/docs
ln -s ../objects.inv %oname/docs/source/

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

export PYTHONPATH=$PWD
%make -C %oname/docs pickle
%make -C %oname/docs html
cp -fR ipwhois-docs/pickle %buildroot%python_sitelibdir/%oname/

%check
nosetests -v -w %oname
%if_with python3
pushd ../python3
nosetests3 -v -w %oname
popd
%endif

%files
%doc *.rst ipwhois-docs/html
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%if_with python3
%files -n python3-module-%oname
%doc *.rst ipwhois-docs/html
%python3_sitelibdir/*
%endif

%changelog
* Sun Aug 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.3-alt1.git20150814
- Initial build for Sisyphus

