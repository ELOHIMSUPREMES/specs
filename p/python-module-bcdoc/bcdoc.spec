%define oname bcdoc

%def_with python3

Name: python-module-%oname
Version: 0.13.0
Release: alt1.git20150223
Summary: ReST document generation tools for botocore
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/bcdoc/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/boto/bcdoc.git
# branch: develop
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-six python-module-docutils
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-six python3-module-docutils
%endif

%py_provides %oname

%description
Tools to help document botocore-based projects.

%package -n python3-module-%oname
Summary: ReST document generation tools for botocore
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Tools to help document botocore-based projects.

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
py.test
%if_with python3
pushd ../python3
python3 setup.py test
py.test-%_python3_version
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
* Tue Feb 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.0-alt1.git20150223
- Version 0.13.0

* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12.2-alt1.git20140304
- Initial build for Sisyphus

