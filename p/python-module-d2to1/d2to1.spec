%define oname d2to1

%def_with python3

Name: python-module-%oname
Version: 0.2.11
Release: alt1

Summary: Allows using setup.cfg files for a package's metadata with a setuptools setup.py
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/d2to1/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

%setup_python_module %oname

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
d2to1 (the 'd' is for 'distutils') allows using distutils2-like
setup.cfg files for a package's metadata with a distribute/setuptools
setup.py script. It works by providing a distutils2-formatted setup.cfg
file containing all of a package's metadata, and a very minimal setup.py
which will slurp its arguments from the setup.cfg.

Note: distutils2 has been merged into the CPython standard library,
where it is now known as 'packaging'. This project was started before
that change was finalized. So all references to distutils2 should also
be assumed to refer to packaging.

%if_with python3
%package -n python3-module-%oname
Summary: Allows using setup.cfg files for a package's metadata with a setuptools setup.py
Group: Development/Python3

%description -n python3-module-%oname
d2to1 (the 'd' is for 'distutils') allows using distutils2-like
setup.cfg files for a package's metadata with a distribute/setuptools
setup.py script. It works by providing a distutils2-formatted setup.cfg
file containing all of a package's metadata, and a very minimal setup.py
which will slurp its arguments from the setup.cfg.

Note: distutils2 has been merged into the CPython standard library,
where it is now known as 'packaging'. This project was started before
that change was finalized. So all references to distutils2 should also
be assumed to refer to packaging.
%endif

%prep
%setup

%if_with python3
rm -rf ../python3
cp -a . ../python3
pushd ../python3
#find -type f -exec sed -i 's|%_bindir/python|%_bindir/python3|' -- '{}' +
#find -type f -exec sed -i 's|%_bindir/env python|%_bindir/python3|' -- '{}' +
find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +
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

%files
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Wed Nov 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.11-alt1
- Initial build for Sisyphus

