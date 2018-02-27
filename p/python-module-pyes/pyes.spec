%define oname pyes

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.99.6
Release: alt1.dev.git20150201
Summary: Python Elastic Search driver
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/pyes/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/aparo/pyes.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-urllib3 python-module-six
BuildPreReq: python-module-nose python-module-nose-cover3
BuildPreReq: python-module-unittest2 python-module-thrift
BuildPreReq: python-modules-json python-modules-multiprocessing
BuildPreReq: python-modules-logging
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-urllib3 python3-module-six
BuildPreReq: python3-module-nose python3-module-nose-cover3
BuildPreReq: python3-module-unittest2 python3-module-thrift
%endif

%py_provides %oname
%py_requires urllib3 six json multiprocessing logging thrift

%description
Python connector for ElasticSearch - the pythonic way to use
ElasticSearch.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Python connector for ElasticSearch - the pythonic way to use
ElasticSearch.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Python Elastic Search driver
Group: Development/Python3
%py3_provides %oname
%py3_requires urllib3 six json multiprocessing logging thrift

%description -n python3-module-%oname
Python connector for ElasticSearch - the pythonic way to use
ElasticSearch.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Python connector for ElasticSearch - the pythonic way to use
ElasticSearch.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Python connector for ElasticSearch - the pythonic way to use
ElasticSearch.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Python connector for ElasticSearch - the pythonic way to use
ElasticSearch.

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
./pyes_coverage.sh
%if_with python3
pushd ../python3
python3 setup.py test
sed -i 's|nosetests|nosetests3|' pyes_coverage.sh
./pyes_coverage.sh
popd
%endif

%files
%doc AUTHORS Changelog FAQ THANKS TODO *.md *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS Changelog FAQ THANKS TODO *.md *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*
%endif

%changelog
* Tue Feb 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.99.6-alt1.dev.git20150201
- Initial build for Sisyphus

