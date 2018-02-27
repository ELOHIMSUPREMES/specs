%define oname stuf

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.9.16
Release: alt1.git20150404
Summary: Normal, default, ordered, chained, restricted, counter, and frozen dictionaries
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/stuf
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://bitbucket.org/lcrees/stuf.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-parse python-module-Fabric
BuildPreReq: python-module-nose python-module-coverage
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-parse python3-module-Fabric
BuildPreReq: python3-module-nose python3-module-coverage
%endif

%py_provides %oname
%py_requires parse

%description
A collection of Python dictionary types that support attribute-style
access. Includes defaultdict, OrderedDict, restricted, ChainMap,
Counter, and frozen implementations plus miscellaneous utilities for
writing Python software.

%if_with python3
%package -n python3-module-%oname
Summary: Normal, default, ordered, chained, restricted, counter, and frozen dictionaries
Group: Development/Python3
%py3_provides %oname
%py3_requires parse

%description -n python3-module-%oname
A collection of Python dictionary types that support attribute-style
access. Includes defaultdict, OrderedDict, restricted, ChainMap,
Counter, and frozen implementations plus miscellaneous utilities for
writing Python software.
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
nosetests -vv --with-coverage --cover-package=%oname
%if_with python3
pushd ../python3
python3 setup.py test -v
nosetests3 -vv --with-coverage --cover-package=%oname
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/tests

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/tests
%endif

%changelog
* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.16-alt1.git20150404
- Initial build for Sisyphus

