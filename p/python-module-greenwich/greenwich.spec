%define oname greenwich

%def_with python3

Name: python-module-%oname
Version: 0.4.1
Release: alt1.git20150811
Summary: A GDAL wrapper with Python conveniences
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/greenwich
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/bkg/greenwich.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-gdal python-module-numpy
BuildPreReq: python-module-Pillow python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-gdal python3-module-numpy
BuildPreReq: python3-module-Pillow
%endif

%py_provides %oname
%py_requires gdal numpy PIL json

%description
Adding Python conveniences to the wonderful world of GDAL.

Greenwich provides a wrapper for the GDAL SWIG Python bindings. The
focus here is on providing some higher level behavior mainly to the
raster side of the GDAL/OGR fence.

%if_with python3
%package -n python3-module-%oname
Summary: A GDAL wrapper with Python conveniences
Group: Development/Python3
%py3_provides %oname
%py3_requires gdal numpy PIL

%description -n python3-module-%oname
Adding Python conveniences to the wonderful world of GDAL.

Greenwich provides a wrapper for the GDAL SWIG Python bindings. The
focus here is on providing some higher level behavior mainly to the
raster side of the GDAL/OGR fence.
%endif

%prep
%setup

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
python setup.py test -v
#if_with python3
%if 0
pushd ../python3
python3 setup.py test -v
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.git20150811
- Initial build for Sisyphus

