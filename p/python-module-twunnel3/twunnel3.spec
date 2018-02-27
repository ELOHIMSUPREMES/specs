%define oname twunnel3

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.3.0
Release: alt1.git20140701
Summary: A HTTPS/SOCKS4/SOCKS5 tunnel for AsyncIO
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/twunnel3/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/jvansteirteghem/twunnel3.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-asyncio
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-asyncio
%endif

%py_provides %oname
%py_requires asyncio

%description
A HTTPS/SOCKS4/SOCKS5 tunnel for AsyncIO.

Supports:

* TCP
* TCP over SSL

%package -n python3-module-%oname
Summary: A HTTPS/SOCKS4/SOCKS5 tunnel for AsyncIO
Group: Development/Python3
%py3_provides %oname
%py3_requires asyncio

%description -n python3-module-%oname
A HTTPS/SOCKS4/SOCKS5 tunnel for AsyncIO.

Supports:

* TCP
* TCP over SSL

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%if_with python2
%python_build_debug
%endif

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python2
%python_install
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
%if_with python2
python setup.py test
%endif
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%if_with python2
%files
%doc *.rst examples
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.rst examples
%python3_sitelibdir/*
%endif

%changelog
* Mon Jan 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1.git20140701
- Initial build for Sisyphus

