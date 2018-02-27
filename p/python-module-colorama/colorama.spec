%define oname colorama

%def_with python3

Name: python-module-%oname
Version: 0.3.3
Release: alt1.git20150709
Summary: Simple cross-platform colored terminal text in Python
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/colorama/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/tartley/colorama.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-mock
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-mock
%endif

%py_provides %oname

%description
Makes ANSI escape character sequences for producing colored terminal
text and cursor positioning work under MS Windows.

ANSI escape character sequences have long been used to produce colored
terminal text and cursor positioning on Unix and Macs. Colorama makes
this work on Windows, too, by wrapping stdout, stripping ANSI sequences
it finds (which otherwise show up as gobbledygook in your output), and
converting them into the appropriate win32 calls to modify the state of
the terminal. On other platforms, Colorama does nothing.

Colorama also provides some shortcuts to help generate ANSI sequences
but works fine in conjunction with any other ANSI sequence generation
library, such as Termcolor.

%package -n python3-module-%oname
Summary: Simple cross-platform colored terminal text in Python
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Makes ANSI escape character sequences for producing colored terminal
text and cursor positioning work under MS Windows.

ANSI escape character sequences have long been used to produce colored
terminal text and cursor positioning on Unix and Macs. Colorama makes
this work on Windows, too, by wrapping stdout, stripping ANSI sequences
it finds (which otherwise show up as gobbledygook in your output), and
converting them into the appropriate win32 calls to modify the state of
the terminal. On other platforms, Colorama does nothing.

Colorama also provides some shortcuts to help generate ANSI sequences
but works fine in conjunction with any other ANSI sequence generation
library, such as Termcolor.

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
%doc *.rst demos
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst demos
%python3_sitelibdir/*
%endif

%changelog
* Thu Jul 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.3-alt1.git20150709
- Version 0.3.3

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.git20141101
- Initial build for Sisyphus

