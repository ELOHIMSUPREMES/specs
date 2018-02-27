%define oname bitmap

%def_without python3

Name: python-module-%oname
Version: 0.0.5
Release: alt2
Summary: BitMap for python
License: Free
Group: Development/Python
Url: https://pypi.python.org/pypi/bitmap/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname

%description
This package provides a `BitMap` class which is an array of bits stored
in compact format.

%if_with python3
%package -n python3-module-%oname
Summary: BitMap for python
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
This package provides a `BitMap` class which is an array of bits stored
in compact format.
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
python setup.py test
export PYTHONPATH=$PWD/src
py.test -vv
%if_with python3
pushd ../python3
python3 setup.py test
export PYTHONPATH=$PWD/src
py.test-%_python3_version -vv
popd
%endif

%files
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Mon Mar 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.5-alt2
- Fixed build

* Wed Feb 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.5-alt1
- Initial build for Sisyphus

