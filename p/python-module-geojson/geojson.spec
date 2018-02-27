%define oname geojson

%def_with python3

Name: python-module-%oname
Version: 1.0.9
Release: alt1.git20141023
Summary: Python bindings and utilities for GeoJSON
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/geojson/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/frewsxcv/python-geojson.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-modules-json
BuildPreReq: python-modules-multiprocessing
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname
%py_requires json

%description
This library contains:

* Functions for encoding and decoding GeoJSON formatted data
* Classes for all GeoJSON Objects
* An implementation of the Python __geo_interface__ Specification

%package examples
Summary: Examples for %oname
Group: Development/Python
Requires: %name = %EVR

%description examples
This library contains:

* Functions for encoding and decoding GeoJSON formatted data
* Classes for all GeoJSON Objects
* An implementation of the Python __geo_interface__ Specification

This package contains examples for %oname.

%package -n python3-module-%oname
Summary: Python bindings and utilities for GeoJSON
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
This library contains:

* Functions for encoding and decoding GeoJSON formatted data
* Classes for all GeoJSON Objects
* An implementation of the Python __geo_interface__ Specification

%package -n python3-module-%oname-examples
Summary: Examples for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-examples
This library contains:

* Functions for encoding and decoding GeoJSON formatted data
* Classes for all GeoJSON Objects
* An implementation of the Python __geo_interface__ Specification

This package contains examples for %oname.

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
export LC_ALL=en_US.UTF-8
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/examples.*

%files examples
%python_sitelibdir/*/examples.*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/examples.*
%exclude %python3_sitelibdir/*/*/examples.*

%files -n python3-module-%oname-examples
%python3_sitelibdir/*/examples.*
%python3_sitelibdir/*/*/examples.*
%endif

%changelog
* Wed Jan 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.9-alt1.git20141023
- Initial build for Sisyphus

