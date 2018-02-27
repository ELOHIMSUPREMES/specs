%define oname elasticsearch

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 1.3.0
Release: alt1.git20141231
Summary: Python client for Elasticsearch
License: ASL
Group: Development/Python
Url: https://pypi.python.org/pypi/elasticsearch/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/elasticsearch/elasticsearch-py.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-urllib3 python-module-requests
BuildPreReq: python-module-nose python-module-coverage
BuildPreReq: python-module-mock python-module-pyaml
BuildPreReq: python-module-nosexcover python-module-pylibmc
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-urllib3 python3-module-requests
BuildPreReq: python3-module-nose python3-module-coverage
BuildPreReq: python3-module-mock
BuildPreReq: python3-module-nosexcover
%endif

%py_provides %oname

%description
Official low-level client for Elasticsearch. Its goal is to provide
common ground for all Elasticsearch-related code in Python; because of
this it tries to be opinion-free and very extendable.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Official low-level client for Elasticsearch. Its goal is to provide
common ground for all Elasticsearch-related code in Python; because of
this it tries to be opinion-free and very extendable.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Python client for Elasticsearch
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Official low-level client for Elasticsearch. Its goal is to provide
common ground for all Elasticsearch-related code in Python; because of
this it tries to be opinion-free and very extendable.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Official low-level client for Elasticsearch. Its goal is to provide
common ground for all Elasticsearch-related code in Python; because of
this it tries to be opinion-free and very extendable.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Official low-level client for Elasticsearch. Its goal is to provide
common ground for all Elasticsearch-related code in Python; because of
this it tries to be opinion-free and very extendable.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Official low-level client for Elasticsearch. Its goal is to provide
common ground for all Elasticsearch-related code in Python; because of
this it tries to be opinion-free and very extendable.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

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
%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc AUTHORS *.rst *.md
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/*/test.*

%files tests
%python_sitelibdir/*/*/test.*

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS *.rst *.md
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/test.*
%exclude %python3_sitelibdir/*/*/*/test.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/test.*
%python3_sitelibdir/*/*/*/test.*
%endif

%changelog
* Thu Jan 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1.git20141231
- Version 1.3.0

* Thu Oct 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt2.git20141022
- Tuned requirements

* Thu Oct 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1.git20141022
- Initial build for Sisyphus

