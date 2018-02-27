%define oldname yolk
%define oname yolk3k

%def_with python3

Name: python-module-%oname
Version: 0.8.4
Release: alt1.git20140628
Summary: Command-line tool for querying PyPI and Python packages installed on your system
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/yolk3k/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/myint/yolk.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides %oldname
Conflicts: python-module-%oldname

%description
Yolk is a Python tool for obtaining information about installed Python
packages and querying packages available on PyPI (Python Package Index).
yolk3k is a fork of the original yolk. yolk3k add Python 3 support
(while maintaining Python 2 support). It also adds additional features.

You can see which packages are active, non-active or in development mode
and show you which have newer versions available by querying PyPI.

%package -n python3-module-%oname
Summary: Command-line tool for querying PyPI and Python packages installed on your system
Group: Development/Python3
%py3_provides %oldname
Conflicts: python3-module-%oldname

%description -n python3-module-%oname
Yolk is a Python tool for obtaining information about installed Python
packages and querying packages available on PyPI (Python Package Index).
yolk3k is a fork of the original yolk. yolk3k add Python 3 support
(while maintaining Python 2 support). It also adds additional features.

You can see which packages are active, non-active or in development mode
and show you which have newer versions available by querying PyPI.

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
%doc CREDITS *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc CREDITS *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Tue Sep 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.4-alt1.git20140628
- Initial build for Sisyphus

