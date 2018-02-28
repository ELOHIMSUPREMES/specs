%define oname whois

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.4
Release: alt1
Summary: Whois querying and parsing of domain registration information
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/python-whois
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-simplejson
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-simplejson
%endif

%py_provides %oname

%description
Whois querying and parsing of domain registration information.

Goal:
* Create a simple importable Python module which will produce parsed
  WHOIS data for a given domain.
* Able to extract data for all the popular TLDs (com, org, net, ...)
* Query a WHOIS server directly instead of going through an intermediate
  web service like many others do.
* Works with Python 2.4+ and no external dependencies

%if_with python3
%package -n python3-module-%oname
Summary: Whois querying and parsing of domain registration information
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Whois querying and parsing of domain registration information.

Goal:
* Create a simple importable Python module which will produce parsed
  WHOIS data for a given domain.
* Able to extract data for all the popular TLDs (com, org, net, ...)
* Query a WHOIS server directly instead of going through an intermediate
  web service like many others do.
* Works with Python 2.4+ and no external dependencies
%endif

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
python setup.py test -v
%if_with python3
pushd ../python3
python3 setup.py test -v
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Sun Aug 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1
- Initial build for Sisyphus

