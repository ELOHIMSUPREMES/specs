%define oname pyrrd

%def_with python3

Name: python-module-%oname
Version: 0.1.0
Release: alt1.git20120117
Summary: An Object-Oriented Python Interface for RRDTool
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/PyRRD/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/oubiwann/pyrrd.git
Source: %name-%version.tar
# fix from https://github.com/kommmy/pyrrd.git
Patch: pyrrd-0.1.1-fix.patch
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests rrd-utils
BuildPreReq: python-module-docutils python-module-RRDtool
BuildPreReq: python-modules-xml
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-docutils python3-module-RRDtool
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
Requires: rrd-utils
%py_requires xml rrdtool

%description
PyRRD lets you use RRDTool from Python code that takes advantage of
standard object-oriented patterns. The makes the programmatic usage of
RRDTool much easier and reusable.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
PyRRD lets you use RRDTool from Python code that takes advantage of
standard object-oriented patterns. The makes the programmatic usage of
RRDTool much easier and reusable.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: An Object-Oriented Python Interface for RRDTool
Group: Development/Python3
%py3_provides %oname
Requires: rrd-utils
%py3_requires xml rrdtool

%description -n python3-module-%oname
PyRRD lets you use RRDTool from Python code that takes advantage of
standard object-oriented patterns. The makes the programmatic usage of
RRDTool much easier and reusable.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
PyRRD lets you use RRDTool from Python code that takes advantage of
standard object-oriented patterns. The makes the programmatic usage of
RRDTool much easier and reusable.

This package contains tests for %oname.

%prep
%setup
%patch -p1

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc ChangeLog README TODO docs/* examples
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test*
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/test*
%python_sitelibdir/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc ChangeLog README TODO docs/* examples
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/tests
%endif

%changelog
* Sat Feb 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.git20120117
- Initial build for Sisyphus

