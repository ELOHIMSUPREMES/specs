%define oname lingua

%def_with python3

Name: python-module-%oname
Version: 3.3
Release: alt1.git20141003
Summary: Translation toolset
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/lingua/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/wichert/lingua.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname

%description
Lingua is a package with tools to extract translateable texts from your
code, and to check existing translations. It replaces the use of the
xgettext command from gettext, or pybabel from Babel.

%package -n python3-module-%oname
Summary: Translation toolset
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Lingua is a package with tools to extract translateable texts from your
code, and to check existing translations. It replaces the use of the
xgettext command from gettext, or pybabel from Babel.

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

%files
%doc *.rst docs/examples
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/examples
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Thu Oct 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3-alt1.git20141003
- Initial build for Sisyphus

