%define oname mistune

%def_with python3

Name: python-module-%oname
Version: 0.7
Release: alt1.git20150730
Summary: The fastest markdown parser in pure Python
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/mistune/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/lepture/mistune.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-Cython python-module-wheel
BuildPreReq: python-module-nose python-modules-multiprocessing
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-Cython python3-module-wheel
BuildPreReq: python3-module-nose
%endif

%py_provides %oname

%description
The fastest markdown parser in pure Python, inspired by marked.

Features:

* Pure Python. Tested in Python 2.6+, Python 3.3+ and PyPy.
* Very Fast. It is the fastest in all pure Python markdown parsers.
* More Features. Table, footnotes, autolink, fenced code etc.

%if_with python3
%package -n python3-module-%oname
Summary: The fastest markdown parser in pure Python
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
The fastest markdown parser in pure Python, inspired by marked.

Features:

* Pure Python. Tested in Python 2.6+, Python 3.3+ and PyPy.
* Very Fast. It is the fastest in all pure Python markdown parsers.
* More Features. Table, footnotes, autolink, fenced code etc.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%add_optflags -fno-strict-aliasing
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install
rm -f %buildroot%python_sitelibdir/*.py*

%if_with python3
pushd ../python3
%python3_install
rm -fR %buildroot%python3_sitelibdir/*.py \
	%buildroot%python3_sitelibdir/__pycache__
popd
%endif

%check
export PYTHONPATH=%buildroot%python_sitelibdir
nosetests -v
%if_with python3
pushd ../python3
export PYTHONPATH=%buildroot%python3_sitelibdir
nosetests3 -v
popd
%endif

%files
%doc *.rst docs/*.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/*.rst
%python3_sitelibdir/*
%endif

%changelog
* Mon Aug 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1.git20150730
- Version 0.7

* Wed Apr 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt1.git20150416
- Initial build for Sisyphus

