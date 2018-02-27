%define oname asyncio-sse

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.1
Release: alt1.git20140925
Summary: asyncio Server-Sent Events implementation
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/asyncio-sse/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/brutasse/asyncio-sse.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-asyncio python-module-aiohttp
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-asyncio python3-module-aiohttp
%endif

%py_provides sse
%py_requires asyncio aiohttp
Conflicts: python-module-sse

%description
Simple asyncio/aiohttp wrapper for Server-Sent Events.

%package -n python3-module-%oname
Summary: asyncio Server-Sent Events implementation
Group: Development/Python3
%py3_provides sse
%py3_requires asyncio aiohttp
Conflicts: python3-module-sse

%description -n python3-module-%oname
Simple asyncio/aiohttp wrapper for Server-Sent Events.

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
%doc *.md examples
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.md examples
%python3_sitelibdir/*
%endif

%changelog
* Sat Jan 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20140925
- Initial build for Sisyphus

