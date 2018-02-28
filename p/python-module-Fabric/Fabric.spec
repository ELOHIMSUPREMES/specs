%define oname Fabric

%def_with python3

Name: python-module-%oname
Version: 1.10.1
Release: alt1.1.1
Summary: A simple, Pythonic tool for remote execution and deployment
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/Fabric/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-paramiko
#BuildPreReq: python-module-setuptools python-module-ecdsa
#BuildPreReq: python-module-sphinx-devel python-module-alabaster
#BuildPreReq: python-module-releases
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires paramiko

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-docutils python-module-ecdsa python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pycrypto python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-tools-2to3 python3 python3-base
BuildRequires: python-module-alabaster python-module-html5lib python-module-objects.inv python-module-paramiko python-module-releases python3-module-setuptools rpm-build-python3 time

%description
Fabric is a Python (2.5-2.7) library and command-line tool for
streamlining the use of SSH for application deployment or systems
administration tasks.

It provides a basic suite of operations for executing local or remote
shell commands (normally or via sudo) and uploading/downloading files,
as well as auxiliary functionality such as prompting the running user
for input, or aborting execution.

%package -n python3-module-%oname
Summary: A simple, Pythonic tool for remote execution and deployment
Group: Development/Python3
%py3_requires paramiko

%description -n python3-module-%oname
Fabric is a Python (2.5-2.7) library and command-line tool for
streamlining the use of SSH for application deployment or systems
administration tasks.

It provides a basic suite of operations for executing local or remote
shell commands (normally or via sudo) and uploading/downloading files,
as well as auxiliary functionality such as prompting the running user
for input, or aborting execution.

%package docs
Summary: Documentationr for Fabric
Group: Development/Documentation

%description docs
Fabric is a Python (2.5-2.7) library and command-line tool for
streamlining the use of SSH for application deployment or systems
administration tasks.

It provides a basic suite of operations for executing local or remote
shell commands (normally or via sudo) and uploading/downloading files,
as well as auxiliary functionality such as prompting the running user
for input, or aborting execution.

This package contains documentationr for Fabric.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx sites
ln -s ../objects.inv sites/docs/
ln -s ../objects.inv sites/www/

%build
%python_build_debug

%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -n -w '{}' +
%python3_build_debug
popd
%endif

pushd sites/docs
sphinx-build -b html -d doctrees . docs
popd
pushd sites/www
sphinx-build -b html -d doctrees . www
popd

%install
%if_with python3
pushd ../python3
%python3_install
popd
mv %buildroot%_bindir/fab %buildroot%_bindir/fab.py3
%endif

%python_install

%files
%doc AUTHORS README.rst
%_bindir/*
%exclude %_bindir/*.py3
%python_sitelibdir/*

%files docs
%doc sites/docs/docs
%doc sites/www/www

%if_with python3
%files -n python3-module-%oname
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.10.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 1.10.1-alt1.1
- NMU: Use buildreq for BR.

* Sun Mar 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.1-alt1
- Version 1.10.1

* Sun Jul 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.0-alt2
- Added module for Python 3

* Fri Jun 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.0-alt1
- Initial build for Sisyphus

