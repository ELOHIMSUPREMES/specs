%define oname aiocutter

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.0.3
Release: alt1.git20150120
Summary: Scraping tool for asyncio
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/aiocutter/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/icoxfog417/aiocutter.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-aiohttp python-module-BeautifulSoup4
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-aiohttp python3-module-BeautifulSoup4
%endif

%py_provides %oname
%py_requires asyncio aiohttp bs4

%description
aiocutter is scraping tool for asyncio.

%package -n python3-module-%oname
Summary: Scraping tool for asyncio
Group: Development/Python3
%py3_provides %oname
%py3_requires asyncio aiohttp bs4

%description -n python3-module-%oname
aiocutter is scraping tool for asyncio.

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

%if_with python2
%files
%doc *.md
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Tue Feb 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.3-alt1.git20150120
- Version 0.0.3

* Tue Jan 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.2-alt1.git20150120
- Initial build for Sisyphus

