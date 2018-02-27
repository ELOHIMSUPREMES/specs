%define oname openpyxl

%def_with python3

Name: python-module-%oname
Version: 2.1.4
Release: alt1
Summary: A Python library to read/write Excel 2007 xlsx/xlsm files
License: MIT/Expat
Group: Development/Python
Url: https://pypi.python.org/pypi/openpyxl/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-jdcal
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-jdcal
%endif

%py_provides %oname
%py_requires jdcal

%description
openpyxl is a Python library to read/write Excel 2010 xlsx/xlsm files.

It was born from lack of existing library to read/write natively from
Python the Office Open XML format.

%package -n python3-module-%oname
Summary: A Python library to read/write Excel 2007 xlsx/xlsm files
Group: Development/Python3
%py3_provides %oname
%py3_requires jdcal

%description -n python3-module-%oname
openpyxl is a Python library to read/write Excel 2010 xlsx/xlsm files.

It was born from lack of existing library to read/write natively from
Python the Office Open XML format.

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
%if_with python3
pushd ../python3
python3 setup.py test
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
* Wed Feb 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.4-alt1
- Initial build for Sisyphus

