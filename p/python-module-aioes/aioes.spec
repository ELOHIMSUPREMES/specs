%define oname aioes

%def_without python2
%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.1.0
Release: alt1.git20141228
Summary: Elasticsearch integration with asyncio
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/aioes/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/aio-libs/aioes.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-asyncio python-module-aiohttp
BuildPreReq: python-module-nose pyflakes python-tools-pep8
BuildPreReq: python-module-elasticsearch
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-asyncio python3-module-aiohttp
BuildPreReq: python3-module-nose python3-pyflakes python3-tools-pep8
BuildPreReq: python3-module-elasticsearch
%endif

%py_provides %oname
%py_requires asyncio aiohttp

%description
aioes is a asyncio compatible library for working with ElasticSearch.

%package -n python3-module-%oname
Summary: Elasticsearch integration with asyncio
Group: Development/Python3
%py3_provides %oname
%py3_requires asyncio aiohttp

%description -n python3-module-%oname
aioes is a asyncio compatible library for working with ElasticSearch.

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
pep8 .
pyflakes .
nosetests -s -v tests
python cmp.py
%endif
%if_with python3
pushd ../python3
python3 setup.py test
python3-pep8 .
python3-pyflakes .
nosetests3 -s -v tests
python3 cmp.py
popd
%endif

%if_with python2
%files
%doc *.txt *.rst cmp.py docs/*.rst
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst cmp.py docs/*.rst
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.git20141228
- Initial build for Sisyphus

