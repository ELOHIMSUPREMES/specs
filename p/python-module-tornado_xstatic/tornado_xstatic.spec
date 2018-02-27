%define oname tornado_xstatic

%def_with python3

Name: python-module-%oname
Version: 0.1
Release: alt1.git20140929
Summary: Utilities for using XStatic in Tornado applications
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/tornado_xstatic/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/takluyver/tornado_xstatic.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-tornado
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-tornado
%endif

%py_provides %oname
%py_requires tornado

%description
XStatic is a means of packaging static files, especially JS libraries,
for Python applications. Tornado is a Python web framework.

This integration provides two pieces:

* XStaticFileHandler to serve static files from XStatic packages.
* url_maker to build URLs for XStatic files, including the ?v=... tag
  that Tornado uses for cache invalidation.

%package -n python3-module-%oname
Summary: Utilities for using XStatic in Tornado applications
Group: Development/Python3
%py3_provides %oname
%py3_requires tornado

%description -n python3-module-%oname
XStatic is a means of packaging static files, especially JS libraries,
for Python applications. Tornado is a Python web framework.

This integration provides two pieces:

* XStaticFileHandler to serve static files from XStatic packages.
* url_maker to build URLs for XStatic files, including the ?v=... tag
  that Tornado uses for cache invalidation.

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
py.test
%if_with python3
pushd ../python3
py.test-%_python3_version
popd
%endif

%files
%doc *.rst *.html example.py
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst *.html example.py
%python3_sitelibdir/*
%endif

%changelog
* Tue Nov 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20140929
- Initial build for Sisyphus

