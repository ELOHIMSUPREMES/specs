%define oname appdirs

%def_with python3

Name: python-module-%oname
Version: 1.4.1
Release: alt1.git20150722
Summary: Determining appropriate platform-specific dirs, e.g. a "user data dir"
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/appdirs/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ActiveState/appdirs.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname

%description
A small Python module for determining appropriate platform-specific
dirs, e.g. a "user data dir".

%package -n python3-module-%oname
Summary: Determining appropriate platform-specific dirs, e.g. a "user data dir"
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
A small Python module for determining appropriate platform-specific
dirs, e.g. a "user data dir".

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
%doc *.rst *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst *.md
%python3_sitelibdir/*
%endif

%changelog
* Mon Aug 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.1-alt1.git20150722
- New snapshot

* Mon Nov 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.1-alt1.git20140820
- Initial build for Sisyphus

