%define oname pyte

%def_with python3

Name: python-module-%oname
Version: 0.4.9
Release: alt1.git20141204
Summary: Simple VTXXX-compatible terminal emulator
License: LGPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/pyte/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/selectel/pyte.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname

%description
It's an in memory VTXXX-compatible terminal emulator. XXX stands for a
series of video terminals, developed by DEC between 1970 and 1995. The
first, and probably the most famous one, was VT100 terminal, which is
now a de-facto standard for all virtual terminal emulators. pyte follows
the suit.

%package -n python3-module-%oname
Summary: Simple VTXXX-compatible terminal emulator
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
It's an in memory VTXXX-compatible terminal emulator. XXX stands for a
series of video terminals, developed by DEC between 1970 and 1995. The
first, and probably the most famous one, was VT100 terminal, which is
now a de-facto standard for all virtual terminal emulators. pyte follows
the suit.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
It's an in memory VTXXX-compatible terminal emulator. XXX stands for a
series of video terminals, developed by DEC between 1970 and 1995. The
first, and probably the most famous one, was VT100 terminal, which is
now a de-facto standard for all virtual terminal emulators. pyte follows
the suit.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
It's an in memory VTXXX-compatible terminal emulator. XXX stands for a
series of video terminals, developed by DEC between 1970 and 1995. The
first, and probably the most famous one, was VT100 terminal, which is
now a de-facto standard for all virtual terminal emulators. pyte follows
the suit.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

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

export PYTHONPATH=$PWD
pushd docs
sphinx-build -b pickle -d build/doctrees . build/pickle
sphinx-build -b html -d build/doctrees . build/html
popd

cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc AUTHORS CHANGES README examples
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/build/html/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS CHANGES README examples
%python3_sitelibdir/*
%endif

%changelog
* Sat Jan 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.9-alt1.git20141204
- Initial build for Sisyphus

