%define oname pymeta3

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.5.0
Release: alt1.git20150114
Summary: Pattern-matching language based on OMeta for Python 2 and 3
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/PyMeta3/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/wbond/pymeta3.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-twisted-core-test
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-twisted-core-test
%endif

%py_provides %oname pymeta

%description
This is a fork of PyMeta 0.5.0 that supports Python 2 and 3.

PyMeta is an implementation of OMeta, an object-oriented
pattern-matching language developed by Alessandro Warth
(http://www.cs.ucla.edu/~awarth/ometa/). PyMeta provides a compact
syntax based on Parsing Expression Grammars (PEGs) for common lexing,
parsing and tree-transforming activities in a way that's easy to reason
about for Python programmers.

%package -n python3-module-%oname
Summary: Pattern-matching language based on OMeta for Python 2 and 3
Group: Development/Python3
%py3_provides %oname pymeta

%description -n python3-module-%oname
This is a fork of PyMeta 0.5.0 that supports Python 2 and 3.

PyMeta is an implementation of OMeta, an object-oriented
pattern-matching language developed by Alessandro Warth
(http://www.cs.ucla.edu/~awarth/ometa/). PyMeta provides a compact
syntax based on Parsing Expression Grammars (PEGs) for common lexing,
parsing and tree-transforming activities in a way that's easy to reason
about for Python programmers.

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
export PYTHONPATH=$PWD
py.test -vv
%if_with python3
pushd ../python3
export PYTHONPATH=$PWD
py.test-%_python3_version -vv
popd
%endif

%files
%doc NEWS README examples extras
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc NEWS README examples extras
%python3_sitelibdir/*
%endif

%changelog
* Mon Feb 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1.git20150114
- Initial build for Sisyphus

