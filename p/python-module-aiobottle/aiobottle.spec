%define oname aiobottle

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.1.1
Release: alt1.git20140523
Summary: A warper bottle use aiohttp base on Asyncio (PEP-3156) 
License: Free
Group: Development/Python
Url: https://pypi.python.org/pypi/aiobottle
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Lupino/aiobottle.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-trollius python-module-aiohttp
BuildPreReq: python-module-bottle
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-asyncio python3-module-aiohttp
BuildPreReq: python3-module-bottle
%endif

%py_provides %oname
%py_requires trollius

%description
Aiobottle, a warper bottle use aiohttp base on Asyncio (PEP-3156).

%package -n python3-module-%oname
Summary: A warper bottle use aiohttp base on Asyncio (PEP-3156)
Group: Development/Python3
%py3_provides %oname
%py3_requires asyncio

%description -n python3-module-%oname
Aiobottle, a warper bottle use aiohttp base on Asyncio (PEP-3156).

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
%doc *.md example.py
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.md example.py
%python3_sitelibdir/*
%endif

%changelog
* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1.git20140523
- Initial build for Sisyphus

