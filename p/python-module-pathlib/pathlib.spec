%define oname pathlib

%def_with python3

Name: python-module-%oname
Version: 1.0.1
Release: alt1
Summary: Object-oriented filesystem paths
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pathlib/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-test
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-test
%endif

%py_provides %oname

%description
pathlib offers a set of classes to handle filesystem paths. It offers
the following advantages over using string objects:

* No more cumbersome use of os and os.path functions. Everything can be
  done easily through operators, attribute accesses, and method calls.
* Embodies the semantics of different path types. For example, comparing
  Windows paths ignores casing.
* Well-defined semantics, eliminating any warts or ambiguities (forward
  vs. backward slashes, etc.).

%package -n python3-module-%oname
Summary: Object-oriented filesystem paths
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
pathlib offers a set of classes to handle filesystem paths. It offers
the following advantages over using string objects:

* No more cumbersome use of os and os.path functions. Everything can be
  done easily through operators, attribute accesses, and method calls.
* Embodies the semantics of different path types. For example, comparing
  Windows paths ignores casing.
* Well-defined semantics, eliminating any warts or ambiguities (forward
  vs. backward slashes, etc.).

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
py.test
%if_with python3
pushd ../python3
py.test-%_python3_version
popd
%endif

%files
%doc *.txt docs/*.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt docs/*.rst
%python3_sitelibdir/*
%endif

%changelog
* Sat Jan 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus

