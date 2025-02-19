%define _unpackaged_files_terminate_build 1
%define oname joblib

%def_with check

Name: python-module-%oname
Version: 0.13.2
Release: alt1
Summary: Lightweight pipelining: using Python functions as pipeline jobs
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/joblib

# https://github.com/joblib/joblib.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: /proc
BuildRequires: python2.7(numpy)
BuildRequires: python2.7(pytest)
BuildRequires: python3(numpy)
BuildRequires: python3(tox)
%endif

# `distributed` is not packaged yet
%filter_from_requires /python[23]\(\.[[:digit:]]\)\?(distributed\()\|\..*)\)/d
%description
Joblib is a set of tools to provide lightweight pipelining in Python. In
particular, joblib offers:

  1. transparent disk-caching of the output values and lazy
     re-evaluation (memoize pattern)
  2. easy simple parallel computing
  3. logging and tracing of the execution

Joblib is optimized to be fast and robust in particular on large data
and has specific optimizations for numpy arrays.

%package -n python3-module-%oname
Summary: Lightweight pipelining: using Python 3 functions as pipeline jobs
Group: Development/Python3

%description -n python3-module-%oname
Joblib is a set of tools to provide lightweight pipelining in Python. In
particular, joblib offers:

  1. transparent disk-caching of the output values and lazy
     re-evaluation (memoize pattern)
  2. easy simple parallel computing
  3. logging and tracing of the execution

Joblib is optimized to be fast and robust in particular on large data
and has specific optimizations for numpy arrays.

%package -n python3-module-%oname-tests
Summary: Tests for joblib (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
Joblib is a set of tools to provide lightweight pipelining in Python. In
particular, joblib offers:

  1. transparent disk-caching of the output values and lazy
     re-evaluation (memoize pattern)
  2. easy simple parallel computing
  3. logging and tracing of the execution

Joblib is optimized to be fast and robust in particular on large data
and has specific optimizations for numpy arrays.

This package contains tests for joblib.

%package tests
Summary: Tests for joblib
Group: Development/Python
Requires: %name = %version-%release

%description tests
Joblib is a set of tools to provide lightweight pipelining in Python. In
particular, joblib offers:

  1. transparent disk-caching of the output values and lazy
     re-evaluation (memoize pattern)
  2. easy simple parallel computing
  3. logging and tracing of the execution

Joblib is optimized to be fast and robust in particular on large data
and has specific optimizations for numpy arrays.

This package contains tests for joblib.

%prep
%setup

cp -a . ../python3

%build
%python_build
pushd ../python3
%python3_build
popd

%install
%python_install
pushd ../python3
%python3_build_install
popd

%check
cat > tox.ini <<EOF
[testenv]
commands =
    {envpython} -m pytest {posargs:-vra}
EOF
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python},py%{python_version_nodots python3}
tox.py3 --sitepackages -p auto -o -vr

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/test*

%files tests
%python_sitelibdir/%oname/test*

%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/test*
%exclude %python3_sitelibdir/%oname/__pycache__/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/%oname/test*
%python3_sitelibdir/%oname/__pycache__/test*

%changelog
* Wed May 08 2019 Stanislav Levin <slev@altlinux.org> 0.13.2-alt1
- Update to upstream version 0.13.2.

* Fri Aug 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.11-alt2
- Applied patch to tests.

* Fri Aug 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.11-alt1
- Update to upstream version 0.11.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.0-alt1.b3.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.9.0-alt1.b3.1
- NMU: Use buildreq for BR.

* Mon Aug 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1.b3
- Version 0.9.0b3

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.2-alt1
- Version 0.8.2

* Tue Sep 17 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.1-alt1
- Version 0.7.1

* Mon Apr 01 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0d-alt1
- Version 0.7.0d

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 0.6.4-alt1.1
- Rebuild with Python-3.3

* Mon Jun 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.4-alt1
- Version 0.6.4
- Added module for Python 3

* Fri Dec 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.6-alt1.dev
- Version 0.5.6.dev

* Fri Dec 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.5-alt1.dev
- Version 0.5.5.dev

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.1-alt1.1
- Rebuild with Python-2.7

* Thu May 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt1
- Initial build for Sisyphus

