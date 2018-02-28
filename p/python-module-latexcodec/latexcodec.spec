%define oname latexcodec

%def_with python3

Name: python-module-%oname
Version: 1.0.2
Release: alt1.a1.git20150826
Summary: A lexer and codec to work with LaTeX code in Python
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/latexcodec
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mcmtroffaes/latexcodec.git
# branch: develop
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-six
BuildPreReq: python-module-nose python-module-coverage
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-six
BuildPreReq: python3-module-nose python3-module-coverage
%endif

%py_provides %oname
%py_requires six

%description
A lexer and codec to work with LaTeX code in Python.

%if_with python3
%package -n python3-module-%oname
Summary: A lexer and codec to work with LaTeX code in Python
Group: Development/Python3
%py3_provides %oname
%py3_requires six

%description -n python3-module-%oname
A lexer and codec to work with LaTeX code in Python.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
A lexer and codec to work with LaTeX code in Python.

This package contains pickles for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv doc/

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
%make -C doc pickle
%make -C doc html
cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test -v
export PYTHONPATH=$PWD
coverage run --source=latexcodec $(type -p nosetests) -vv
%if_with python3
pushd ../python3
python3 setup.py test -v
export PYTHONPATH=$PWD
coverage3 run --source=latexcodec $(type -p nosetests3) -vv
popd
%endif

%files
%doc *.rst doc/_build/html
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%if_with python3
%files -n python3-module-%oname
%doc *.rst doc/_build/html
%python3_sitelibdir/*
%endif

%changelog
* Mon Aug 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.a1.git20150826
- Initial build for Sisyphus

