%define oname gevent-loops

%def_with python3

Name: python-module-%oname
Version: 0.0.1
Release: alt1.git20141114
Summary: A collection of improved loop classes to use with gevent
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/gevent-loops/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mattlong/gevent-loops.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-gevent
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-gevent
%endif

%py_provides gevent_loops

%description
This is a collection of custom gevent loop classes meant to override
gevent.core.loop. The original motivation was to prevent a big ugly
stack trace from being printed to stdout whenever a websocket client
disconnects from a Gunicorn server.

%package -n python3-module-%oname
Summary: A collection of improved loop classes to use with gevent
Group: Development/Python3
%py3_provides gevent_loops

%description -n python3-module-%oname
This is a collection of custom gevent loop classes meant to override
gevent.core.loop. The original motivation was to prevent a big ugly
stack trace from being printed to stdout whenever a websocket client
disconnects from a Gunicorn server.

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
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.git20141114
- Initial build for Sisyphus

