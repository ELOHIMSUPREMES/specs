%define oname pylabs_pyramid_scaffolds

%def_with python3

Name: python-module-%oname
Version: 0.0.5
Release: alt1
Summary: Provides some pyramid scaffold templates with useful default settings
License: Free
Group: Development/Python
Url: https://pypi.python.org/pypi/pylabs_pyramid_scaffolds/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname

%description
This package provides some pyramid scaffold templates with useful
default settings.

%package -n python3-module-%oname
Summary: Provides some pyramid scaffold templates with useful default settings
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
This package provides some pyramid scaffold templates with useful
default settings.

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
%doc *.txt
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%endif

%changelog
* Tue Oct 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.5-alt1
- Initial build for Sisyphus

