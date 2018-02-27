%define oname spec

%def_with python3

Name: python-module-%oname
Version: 0.11.2
Release: alt1.git20141210
Summary: Specification-style output for nose
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/spec/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/bitprophet/spec.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-nose python-module-six
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-nose python3-module-six
%endif

%py_provides %oname

%description
spec is a Python (2.6+ and 3.3+) testing tool.

%package -n python3-module-%oname
Summary: Specification-style output for nose
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
spec is a Python (2.6+ and 3.3+) testing tool.

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
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.mkd
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.mkd
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Thu Dec 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.2-alt1.git20141210
- Version 0.11.2

* Sat Nov 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.1-alt1.git20131231
- Initial build for Sisyphus

