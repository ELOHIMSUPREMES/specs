%define oname oct2py

%def_with python3

Name: python-module-%oname
Version: 1.5.0
Release: alt2

Summary: Python to GNU Octave bridge --> run m-files from python
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/oct2py

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

%setup_python_module %oname

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-scipy octave
BuildPreReq: python-module-sphinx-devel python-module-numpydoc
BuildPreReq: python-module-sphinx-bootstrap-theme
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-scipy
%endif

%description
Oct2py is a means to seemlessly call m-files and Octave functions from
python. It manages the Octave session for you, sharing data behind the
scenes using MAT files.

If you want to run legacy m-files, do not have MATLAB(r), and do not
fully trust a code translator, this is your library.

%package -n python3-module-%oname
Summary: Python to GNU Octave bridge --> run m-files from python
Group: Development/Python3

%description -n python3-module-%oname
Oct2py is a means to seemlessly call m-files and Octave functions from
python. It manages the Octave session for you, sharing data behind the
scenes using MAT files.

If you want to run legacy m-files, do not have MATLAB(r), and do not
fully trust a code translator, this is your library.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Oct2py is a means to seemlessly call m-files and Octave functions from
python. It manages the Octave session for you, sharing data behind the
scenes using MAT files.

If you want to run legacy m-files, do not have MATLAB(r), and do not
fully trust a code translator, this is your library.

This package contains tests for %oname.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Oct2py is a means to seemlessly call m-files and Octave functions from
python. It manages the Octave session for you, sharing data behind the
scenes using MAT files.

If you want to run legacy m-files, do not have MATLAB(r), and do not
fully trust a code translator, this is your library.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Oct2py is a means to seemlessly call m-files and Octave functions from
python. It manages the Octave session for you, sharing data behind the
scenes using MAT files.

If you want to run legacy m-files, do not have MATLAB(r), and do not
fully trust a code translator, this is your library.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation

%description docs
Oct2py is a means to seemlessly call m-files and Octave functions from
python. It manages the Octave session for you, sharing data behind the
scenes using MAT files.

If you want to run legacy m-files, do not have MATLAB(r), and do not
fully trust a code translator, this is your library.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

sed -i 's|@VERSION@|%version|' docs/conf.py
%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

pushd docs
sphinx-build -b pickle -d build/doctrees . build/pickle
sphinx-build -b html -d build/doctrees . build/html
popd

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/*/tests
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/build/html/*

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/*/tests
%endif

%changelog
* Tue Jul 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt2
- Moved all tests into tests subpackage

* Mon Jul 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1
- Version 1.5.0
- Added module for Python 3

* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1
- Version 1.1.1

* Fri Nov 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus

